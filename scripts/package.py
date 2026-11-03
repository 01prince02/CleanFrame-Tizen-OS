"""Build and sign through an existing official Tizen SDK profile."""
import os
from pathlib import Path
import queue
import subprocess
import tempfile
import threading
import time
import zipfile

if os.name != 'nt':
    import pty
    import select
    import signal
    import termios

from font_assets import write_widget_archive
from local_config import ROOT, load_settings, read_password
from private_files import check_signed_widget


def sign(command, password=None, timeout=60):
    # SDK output can include profile credentials. Never copy it to diagnostics.
    if os.name == 'nt':
        return _sign_windows(command, password, timeout)
    pid, terminal = pty.fork()
    if pid == 0:
        try:
            os.execv(command[0], command)
        except BaseException:
            os._exit(127)
    output = b''
    passwords = saves = 0
    status = None
    deadline = time.monotonic() + timeout
    try:
        while time.monotonic() < deadline:
            ready, _, _ = select.select([terminal], [], [], 1)
            if not ready:
                continue
            try:
                chunk = os.read(terminal, 8192)
            except OSError:
                break
            if not chunk:
                break
            output += chunk
            if len(output) > 1024 * 1024:
                raise ValueError('SDK produced excessive signing output.')
            count = output.lower().count(b'password:')
            if count > passwords:
                if password is None:
                    raise ValueError('SDK requested a password. Configure saved profile access or select a protected password file.')
                if count > 2:
                    raise ValueError('SDK requested too many passwords. Check both certificate passwords in the selected profile.')
                attributes = termios.tcgetattr(terminal)
                attributes[3] &= ~termios.ECHO
                termios.tcsetattr(terminal, termios.TCSANOW, attributes)
                os.write(terminal, password + b'\n')
                passwords = count
            count = output.count(b'No: (N) ?')
            if count > saves:
                os.write(terminal, b'n\n')
                saves = count
        else:
            raise ValueError('SDK signing timed out.')
        while time.monotonic() < deadline:
            finished, status = os.waitpid(pid, os.WNOHANG)
            if finished:
                break
            status = None
            time.sleep(0.01)
        if status is None:
            raise ValueError('SDK signing timed out.')
    finally:
        if status is None:
            finished, status = os.waitpid(pid, os.WNOHANG)
            if not finished:
                try:
                    try:
                        os.killpg(pid, signal.SIGKILL)
                    except PermissionError:
                        os.kill(pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                _, status = os.waitpid(pid, 0)
        os.close(terminal)
    return os.waitstatus_to_exitcode(status)


def _sign_windows(command, password=None, timeout=60):
    """Answer SDK prompts over a private stdin pipe without echoing passwords."""
    command = list(command)
    executable = Path(command[0])
    if executable.suffix.lower() not in {'.bat', '.cmd', '.exe'}:
        # Synthetic Python SDKs used by the offline tests have no Windows
        # executable wrapper. Real Tizen Studio installs provide tizen.bat.
        import sys
        if not executable.is_file():
            return 127
        command.insert(0, sys.executable)
        shell = False
    else:
        shell = executable.suffix.lower() in {'.bat', '.cmd'}
    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, shell=shell,
                                   creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    except OSError:
        return 127
    chunks = queue.Queue()

    def read_output():
        try:
            while True:
                chunk = process.stdout.read(1)
                if not chunk:
                    break
                chunks.put(chunk)
        finally:
            chunks.put(None)

    reader = threading.Thread(target=read_output, daemon=True)
    reader.start()
    output = bytearray()
    passwords = saves = 0
    deadline = time.monotonic() + timeout
    ended = False
    try:
        while not ended:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ValueError('SDK signing timed out.')
            try:
                chunk = chunks.get(timeout=min(0.25, remaining))
            except queue.Empty:
                if process.poll() is not None:
                    break
                continue
            if chunk is None:
                ended = True
                break
            output.extend(chunk)
            if len(output) > 1024 * 1024:
                raise ValueError('SDK produced excessive signing output.')
            count = output.lower().count(b'password:')
            if count > passwords:
                if password is None:
                    raise ValueError('SDK requested a password. Configure saved profile access or select a protected password file.')
                if count > 2:
                    raise ValueError('SDK requested too many passwords. Check both certificate passwords in the selected profile.')
                process.stdin.write(password + b'\n')
                process.stdin.flush()
                passwords = count
            count = output.count(b'No: (N) ?')
            if count > saves:
                process.stdin.write(b'n\n')
                process.stdin.flush()
                saves = count
        remaining = max(0, deadline - time.monotonic())
        try:
            return process.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            raise ValueError('SDK signing timed out.') from None
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        if process.stdin:
            process.stdin.close()
        if process.stdout:
            process.stdout.close()


def main(root=ROOT):
    settings = load_settings(root)
    cli = settings['sdk_path'] / 'tools/ide/bin/tizen'
    if os.name == 'nt' and not cli.is_file():
        cli = cli.with_suffix('.bat')
    if not cli.is_file() or (os.name != 'nt' and not os.access(cli, os.X_OK)):
        raise ValueError('Tizen CLI missing. Set sdk_path in .local/signing.json; see docs/development.md.')
    password = read_password(settings['password_file'], root=root) if settings['password_file'] else None
    dist = root / 'dist'
    dist.mkdir(exist_ok=True)
    unsigned = dist / 'CleanFrame-unsigned.wgt'
    write_widget_archive(unsigned, root=root, identity=settings['identity'])
    # A fresh folder prevents a previous signed widget masking a failed build.
    signed_dir = Path(tempfile.mkdtemp(prefix='signed-', dir=dist))
    command = [str(cli), 'package', '-t', 'wgt', '-s', settings['profile'], '-o', str(signed_dir), '--', str(unsigned)]
    if sign(command, password):
        raise ValueError('SDK signing failed. Check the selected profile and password access in Certificate Manager.')
    signed = signed_dir / unsigned.name
    check_signed_widget(signed, settings['identity'])
    target = dist / 'CleanFrame.wgt'
    # Promote on the same filesystem so a failed copy preserves the last build.
    ready = signed_dir / 'validated.wgt'
    ready.write_bytes(signed.read_bytes())
    ready.replace(target)
    print('Signed widget created: ' + str(target))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, zipfile.BadZipFile) + ((termios.error,) if os.name != 'nt' else ()) as error:
        # Known validation messages contain no credentials. Suppress SDK/OS payloads.
        message = str(error) if isinstance(error, ValueError) else 'Cannot complete packaging. Check SDK/profile setup and local file permissions.'
        raise SystemExit(message) from None
