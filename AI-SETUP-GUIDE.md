# Set up CleanFrame with an AI coding assistant

This beginner guide applies to the existing project. AI tools can help explain and edit the code, but they cannot establish that a feature works on a physical Samsung TV without a real device test.

## 1. Download and prepare the project

Install Git, Node.js 22.13+ (22.x) or Node.js 24+, and Python 3.10+. Then run:

```sh
git clone https://github.com/01prince02/CleanFrame-Tizen-OS.git
cd CleanFrame-Tizen-OS
npm ci
```

For a ZIP download, extract it and open a terminal in the extracted folder. `npm ci` installs the development dependencies recorded in `package-lock.json`.

## 2. Ask the assistant to understand the code first

Open this folder in Codex, Google Antigravity, Claude Code, ChatGPT, GitHub Copilot or another coding assistant. Ask it to read:

- `AGENTS.md` for project-specific rules.
- `AI-GUIDE.md` for safe AI-assisted work.
- `docs/development.md` for architecture and local configuration.
- `docs/interaction-behaviour.md` for remote navigation and focus behavior.
- `docs/testing.md` for what checks do and do not establish.

Start with this prompt:

> Read AGENTS.md, AI-GUIDE.md, README.md, docs/development.md and docs/testing.md. Explain the app structure, the main runtime files, the supported development commands, and the known TV-specific limits. Do not edit files, connect to a TV or make compatibility claims beyond the documented evidence. Separate confirmed facts from assumptions.

## 3. Preview on your computer

After `npm ci`, run:

```sh
npm run dev:public
```

The server prints a generated address when it starts. Open it in a browser on the same computer and use the keyboard arrows, Enter and Escape to exercise remote-like navigation. The development server binds to loopback, chooses an available port and does not communicate with a TV.

## 4. Make a small change with AI

Give the assistant a bounded task, for example:

> In the existing app, improve the spacing of the Favorites row. First inspect the relevant layout, its focus behavior and current tests. Preserve stored settings and both home layouts. Make only this change, run the checks I requested, and show me the diff and any unverified TV assumptions. Do not access a TV.

Ask for one feature at a time. Review each proposed diff. Keep runtime JavaScript ES5-compatible and use existing focus, panel and preference code. Do not let the assistant invent supported apps, remote keys, system destinations or physical-TV results.

## 5. Run checks

The available scripts are listed in `package.json`. Typical checks are:

```sh
npm run check
npm run check:tools
npm run check:public
npx playwright install chromium
npm run check:browser
```

Python is needed by several commands. The browser check requires Playwright Chromium. On Linux, Playwright may need system packages as described in its documentation. Review `docs/testing.md` for coverage and limits. The repository's package script uses POSIX APIs and is not a tested Windows build path.

## 6. Configure your own computer and TV (optional)

Browser development does not need SDK configuration. To build and install your own widget:

1. Install Samsung's official TV SDK compatible with your target TV.
2. Create your own Samsung TV author/distributor certificate profile with Samsung's official tools. Complete login yourself in the official sign-in UI.
3. Copy `signing.example.json` to `.local/signing.json` and replace the placeholders with your own SDK path, profile and SDK-generated package/application IDs. `.local/` is ignored by Git.
4. Configure your own TV address privately in `.local/device.json` only if using the device scripts.
5. Connect only to a TV you are authorized to test. Check the SDB device state and target details before preparing any install.
6. Use Samsung's official packaging/install workflow and review the package identity and signatures. Ask the TV owner to approve installation before installing or launching.

The repository does not include private certificates. The packaging runner supports the SDK's Windows batch CLI and POSIX SDK CLI. On Windows, use Samsung SDK-managed certificate password access; private password files are intentionally unsupported because restrictive Windows ACLs are not verified portably. Do not copy another person's signing profile, app identity, device configuration or recovery file. Keep secrets, DUIDs, addresses, signed packages and diagnostic logs out of Git and AI chats.

## 7. Contribute the change

Create a fork or feature branch, make and review the diff, run relevant checks, and open a pull request describing behavior and the exact checks performed. Keep test evidence honest: browser results are not TV results. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and the license terms for every asset.

For questions about security, see [SECURITY.md](SECURITY.md). For first-time local setup, see [README-SETUP.md](README-SETUP.md).
