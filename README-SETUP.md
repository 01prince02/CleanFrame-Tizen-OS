# Beginner setup

This guide gets the existing CleanFrame project open and running locally. It does not install anything on a TV.

## 1. Download the project

Install Git, Node.js 22.13+ in the 22.x line or Node.js 24+, and Python 3.10+. Then open a terminal and run:

```sh
git clone https://github.com/01prince02/CleanFrame-Tizen-OS.git
cd CleanFrame-Tizen-OS
npm ci
```

If you downloaded a ZIP instead, extract it and open a terminal in the extracted project folder before running `npm ci`.

## 2. Preview the app

```sh
npm run dev:public
```

The server prints a generated address when it starts. Open that address in a browser on the same computer. Use arrow keys, Enter and Escape. The preview uses public fonts and does not connect to a TV. It selects an available port automatically.

## 3. Open it in an AI coding assistant

Open the repository folder in Codex, Google Antigravity, Claude Code, ChatGPT, GitHub Copilot or another coding assistant. Start by asking it to read `AGENTS.md`, `AI-GUIDE.md`, `docs/development.md` and `docs/testing.md`, explain the project, and make no changes. Then give one small, specific change at a time. Review the diff before accepting edits.

## 4. Run checks

The commands below are defined in `package.json`; they require dependencies from `npm ci`:

```sh
npm run check
npm run check:tools
npm run check:public
```

The browser suite additionally needs Playwright Chromium:

```sh
npx playwright install chromium
npm run check:browser
```

Some scripts require Python. `npm run check` runs ESLint, `scripts/check.py` and the synthetic-device Node test. `npm run check:tools` runs Python test fixtures. `npm run check:public` scans working files and Git history for known private-file patterns. These checks are bounded; a pass does not prove that every secret is absent or that a TV feature works.

## 5. Optional local TV configuration

To build and test on your own TV, first read [docs/development.md](docs/development.md), [docs/agent-tv-setup-guide.md](docs/agent-tv-setup-guide.md) and [docs/testing.md](docs/testing.md). Install Samsung's official TV SDK, create your own certificate profile through Samsung's supported tools, and configure local ignored files. `signing.example.json` contains placeholders, not working values. Keep your certificate, password, TV DUID, network address, recovery data and signed WGT out of Git and chat.

The package helper uses POSIX APIs and is documented for macOS/Linux. The repository does not provide a tested Windows package runner. TV access can require enabling Developer Mode, configuring the TV's developer host, connecting with SDB, and authorizing installation in Samsung's device manager. Requirements vary by SDK and TV firmware.

Do not install or launch on a TV unless its owner explicitly approved that operation. A browser preview cannot establish actual TV compatibility. Never replace Smart Hub, remove system apps, root the TV or bypass Samsung security.

## Troubleshooting

- **Port is occupied:** use the alternate `--port` command above.
- **`npm` is not found:** install a supported Node.js distribution that includes npm, reopen the terminal and confirm `node --version` and `npm --version`.
- **Python is missing:** install Python 3.10+ and ensure it is available in the terminal. npm scripts check `CLEANFRAME_PYTHON`, then `python3`/`python`, or the Windows `py -3` launcher. Set `CLEANFRAME_PYTHON` to the full Python executable path if detection does not find it.
- **Chromium cannot start:** install Playwright's browser with `npx playwright install chromium`; on Linux, see Playwright's official system dependency instructions.
- **SDK/signing failure:** confirm the official SDK and TV extension are installed, the profile is selected in the official tools, and local config paths are valid. Never paste certificate content or passwords into an issue or assistant chat.
- **TV connection failure:** check the TV's current Developer Mode status, the host computer address configured on the TV, the active local network, SDB's connected-device list and the SDK version. Do not publish those values in logs.
- **A TV API or app is unavailable:** check the installed apps and capabilities on that exact TV. Do not assume a service, app ID, remote key or system settings destination from another model.

For more detail, see [AI-SETUP-GUIDE.md](AI-SETUP-GUIDE.md), [docs/development.md](docs/development.md), [docs/compatibility.md](docs/compatibility.md) and [docs/testing.md](docs/testing.md).
