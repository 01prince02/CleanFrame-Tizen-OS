# CleanFrame for Samsung Tizen

CleanFrame is a remote-friendly home-screen web app adapted from the open-source CleanFrame project. It provides List and Dock layouts, installed-app discovery, Favorites and Recently Used sections, wallpaper and appearance controls, saved preferences, and a browser preview.

This is experimental community software. It is not affiliated with Samsung or any streaming service. The manifest's Tizen 5.0 minimum is an installation floor, not a promise that every TV model, region, firmware, API or app is compatible. Test on your own target TV before relying on a feature.

## Start here

1. Install Node.js 22.13+ in the 22.x line or Node.js 24+, and Python 3.10+.
2. Clone this repository and open its folder in your editor or AI coding assistant.
3. Read [README-SETUP.md](README-SETUP.md) for first-run setup and [AI-GUIDE.md](AI-GUIDE.md) before asking an AI assistant to edit files.
4. Run `npm ci`, then `npm run dev:public`.
5. Open the generated address printed by the preview server in a browser on the same computer. Use arrow keys, Enter and Escape to preview remote navigation.

The preview server selects an available port and binds to the computer's loopback interface. It is for local UI development and does not communicate with a TV. Keep the loopback binding in place; do not expose the development server to a network.

## What is in the project

- `app/` — Tizen web app source, styles and bundled public assets.
- `scripts/` — local preview, validation, public export, packaging and explicitly invoked device utilities.
- `docs/` — development, interaction, assets, test and compatibility notes.
- `signing.example.json` — safe placeholder template; copy to ignored `.local/signing.json` and configure your own SDK/profile locally.

The app discovers installed consumer apps through supported Tizen APIs where available. It does not install streaming services or assume app IDs from another TV. Settings and app destinations can vary by platform and model.

## Checks

After installing the dependencies, available project checks are:

```sh
npm run check
npm run check:tools
npm run check:browser
npm run check:public
```

For the optional Playwright browser check, install Chromium first with `npx playwright install chromium`. These checks are not physical-TV compatibility tests. See [docs/testing.md](docs/testing.md).

## Build and TV testing

Creating a personal installable widget requires Samsung's official TV SDK and a certificate profile created through Samsung's supported workflow. Follow [docs/development.md](docs/development.md) and [docs/agent-tv-setup-guide.md](docs/agent-tv-setup-guide.md). The packaging runner supports the SDK's Windows batch CLI and POSIX SDK CLI. On Windows, use Samsung SDK-managed certificate password access; password files are intentionally unsupported because Python cannot verify restrictive Windows ACLs portably.

Keep certificates, passwords, DUIDs, device addresses, recovery data and signed WGT files in ignored local storage. Never commit them. A TV install or launch is a separate device operation and must be authorized by the TV owner. The project does not root the TV, bypass security, remove system apps or replace Smart Hub through supported app APIs.

## License and assets

The original CleanFrame source and documentation retain their MIT license and copyright notice. Third-party fonts, photographs and icons have separate notices and terms in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The repository owner-supplied wallpapers have not had their public redistribution rights independently verified; do not redistribute those images unless you have permission. The MIT license does not grant rights to third-party assets.

See [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes and [SECURITY.md](SECURITY.md) to report a security issue.
