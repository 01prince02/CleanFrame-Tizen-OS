import { spawnSync } from 'node:child_process';

export function resolvePython() {
  const candidates = process.env.CLEANFRAME_PYTHON
    ? [[process.env.CLEANFRAME_PYTHON, []]]
    : process.platform === 'win32'
      ? [['python', []], ['py', ['-3']]]
      : [['python3', []], ['python', []]];
  for (const [command, prefix] of candidates) {
    const result = spawnSync(command, [...prefix, '--version'], { encoding: 'utf8', windowsHide: true });
    if (result.status === 0 && /^Python 3\./.test((result.stdout || '') + (result.stderr || ''))) {
      return { command, prefix };
    }
  }
  throw new Error('Python 3 was not found. Install Python 3.10+ or set CLEANFRAME_PYTHON to its executable.');
}

if (process.argv[1] && import.meta.url === new URL(`file://${process.argv[1].replaceAll('\\', '/')}`).href) {
  try {
    const { command, prefix } = resolvePython();
    const result = spawnSync(command, [...prefix, ...process.argv.slice(2)], {
      stdio: 'inherit', windowsHide: true
    });
    if (result.error) throw result.error;
    process.exitCode = result.status ?? 1;
  } catch (error) {
    process.stderr.write(error.message + '\n');
    process.exitCode = 1;
  }
}
