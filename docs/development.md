# Development

## Browser preview

Use Node.js 22.13+ in the 22.x line or Node.js 24+, Python 3.10+, and npm dependencies installed with `npm ci`. Chromium is needed only for the optional Playwright browser checks; install it with `npx playwright install chromium`.

`npm run dev` starts `scripts/preview.py` on the development computer's loopback interface, chooses an available port and prints the generated browser address. Use `npm run dev:public` to exclude any local proprietary font overlay. Open the printed address on the same computer. The preview does not communicate with a TV.

Arrow keys, Enter and Escape mirror remote navigation. Device controls report that they require a TV; the preview does not simulate successful TV launches. A port can be supplied with the `--port` option when needed. Keep the loopback binding; do not expose the preview server to a network.

## Runtime map and compatibility

- `app/index.html` loads the device adapter, catalogues, icon metrics and `main.js`, with `style.css`.
- `main.js` owns List and Dock layouts, panels, focus, preferences and wallpaper timers. `device.js` owns installed-app discovery and Tizen calls. Keep device-specific behavior in that adapter.
- The logical stage is 1920 x 1080 and scales uniformly to the viewport. Check 1920 x 1080 and 1280 x 720 in a browser. Geometry checks do not establish TV compositor support.
- Preferences use localStorage key `cleanframe.home.v1`, with a fallback read from `cleanframe.shore.v1`. Preserve the documented 0.6 migration and test saved state when changing this format.
- Runtime JavaScript is checked with ESLint's ES5 grammar. This does not prove DOM, CSS or Tizen API availability on a TV. Verify new APIs on target hardware before claiming support.
- The manifest declares `required_version="5.0"`. This is an installation floor, not a compatibility guarantee. The target TV model, firmware, region, installed app IDs, remote events and Samsung Settings destinations require separate verification.

See [compatibility](compatibility.md), [interaction behavior](interaction-behaviour.md) and [testing](testing.md).

## Local signing configuration

Personal configuration belongs outside tracked source. Copy `signing.example.json` to `.local/signing.json` and replace its placeholders using the official Samsung TV SDK and the identity created by its project tools. The configuration supports an SDK path, profile, package/application IDs and an optional password file; inspect `scripts/local_config.py` for exact validation and path rules. `.local/` is ignored by Git. The example file contains no usable SDK path, profile, app identity or credential.

The password file is optional; the runner can use SDK-managed password access. On macOS/Linux, a configured file must satisfy the owner-only file checks in `scripts/local_config.py`. Windows password files are intentionally rejected because the tool cannot verify restrictive Windows ACLs portably; use the SDK-managed profile access instead. Never put certificates, keys or passwords in project source, screenshots, issues, prompts or commits.

`npm run package` uses `scripts/package.py` and an existing official Samsung SDK certificate profile. It supports the SDK's Windows batch CLI and POSIX SDK CLI, and writes generated packages to ignored `dist/`. On Windows, use Samsung SDK-managed certificate password access; password files are unsupported because restrictive Windows ACLs are not verified portably. Review the source and current SDK guidance before using a different environment. Do not treat an unsigned public export as installable.

`npm run export:public` creates an unsigned public-font WGT and contacts no TV. `npm run tv:info`, `npm run tv:install` and `npm run tv:launch` are device operations. They require local device configuration and an explicitly authorized target. Verify SDB connectivity and the target status before installation; inspect the exact package identity/signatures and obtain the TV owner's approval. No TV operation is implied by running offline checks.

## Official Samsung workflow

Use Samsung's [TV SDK installation](https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/installing-tv-sdk.html), [certificate creation](https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/creating-certificates.html), [TV connection](https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html) and [CLI documentation](https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/command-line-interface.html). Certificate setup uses an author certificate and a distributor certificate authorized for a target TV. Complete account sign-in and password entry yourself in Samsung's official UI. Keep the TV's DUID private and enter it only into Samsung's certificate tools when needed.

For a different computer, install the official SDK locally, make a new certificate profile for your own Samsung account and TV, create your own app identity, and configure ignored local files. Do not copy another developer's certificates, app identity, device address or recovery baseline.

## Device installation and launch

Before a device operation, use the official SDK/SDB workflow to confirm the intended TV appears in `sdb devices` and reports state `device`. Check the TV's actual model, firmware and developer authorization locally. Samsung's Device Manager may also require its documented install permission for the selected target. Build/sign with the official packager, inspect the generated widget's identity and signatures, then install using the SDK's documented Samsung TV install workflow. Verify its explicit success result and installed-app list before launching by the actual application ID. Stop on errors; do not retry with undocumented or security-bypassing methods.

Do not infer the physical Home, Back, shortcut, volume, power or voice button behavior from browser tests. Tizen apps receive only supported key events; some Samsung remote controls are system-reserved. Do not override them or change Smart Hub/startup settings under routine app testing.

## Experimental native Home tools

The `scripts/native-home/` tree contains firmware-specific research tools that use undocumented behavior. They can change Home/startup assignments and depend on a device-specific recovery baseline. They are not supported portable setup steps and are not part of normal app packaging, installation or testing. Do not run, generalize or disable their guards as part of routine development. Read their local instructions and `docs/tv-status.md`; any TV use requires an explicit request and separate target-specific recovery review.
