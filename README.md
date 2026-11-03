# CleanFrame Tizen

A personal, remote-friendly home screen for Samsung Tizen TVs, adapted from the open-source CleanFrame project.

CleanFrame brings a focused app dock, customizable home layout, photographic wallpapers and settings into a lightweight Tizen web application. Its glass surfaces use bundled, pre-rendered artwork so the TV does not have to calculate large blur effects during remote navigation.

This project is independent and is not affiliated with Samsung or any streaming service. It is experimental software. The manifest targets Tizen 5.0 and later, but that minimum does not guarantee every feature works on every model, region or firmware. Verify compatibility on your own TV.

## Features in the source

- List and dock home layouts with remote-friendly focus navigation.
- Installed-app discovery and app launching through Tizen APIs.
- Editable apps on Home, Favorites and Recently Used sections.
- Wallpaper selection, appearance controls, and persistent app preferences.
- Settings for layout, typography, focus materials, animation, date/time, screensaver and Samsung actions where supported.
- An in-app idle screen; it does not replace Samsung's system screensaver or Smart Hub.
- Browser preview and offline source checks.

The browser preview cannot verify installed TV apps, Samsung system destinations, remote key delivery, the TV compositor, or physical-TV performance. Device-specific behavior is documented separately and must not be inferred from a browser result.

## Preview the interface

Development prerequisites are Node.js 22.13 or later in the 22.x line, or Node.js 24 or later, and Python 3.10 or later. Install dependencies, then run:

    npm ci
    npm run dev:public

Open the local preview address printed by `npm run dev` in a browser. Use the keyboard arrows, Enter and Escape, or click the preview controls. Actions requiring a TV report that limitation rather than simulating a successful launch.

The public preview uses the fonts bundled under their respective open font licenses. Proprietary font binaries and machine-specific configuration are excluded.

## Checks

The project documents these offline checks:

    npm run check
    npm run check:tools
    npm run check:browser
    npm run check:public

The source and browser checks do not contact a TV. See docs/testing.md for coverage and limits. A passing browser check is not evidence of physical-TV compatibility.

## Samsung TV setup

Building a personal installable widget requires the official Samsung TV SDK, a Samsung TV certificate profile generated through Samsung's supported certificate tools, and a package identity selected locally in .local/signing.json. The distributor certificate must be valid for the target TV. Never commit certificates, passwords, DUIDs, device addresses or signed WGT packages.

Read docs/development.md and docs/agent-tv-setup-guide.md before using device tools. The documented tv:info, tv:install and tv:launch commands contact a connected TV. Verify SDB connectivity and device state first, review the exact package identity and signatures, and obtain the owner's approval for any install or launch. Do not use this application to replace Smart Hub, change Home/startup assignments, remove system apps, root the TV or modify firmware.

The app manifest declares a Tizen 5.0 installation floor. The exact model, firmware, region, installed streaming app IDs, supported remote keys and Samsung Settings destinations must be checked on each target TV.

## Wallpapers, attribution and license

The original CleanFrame source and documentation are distributed under the MIT License; see LICENSE. Preserve its copyright and permission notice when sharing this derivative. Third-party fonts, photographs and icons retain their separate terms in THIRD_PARTY_NOTICES.md and the asset source records.

Some wallpapers in this personal project were supplied by the project owner. Their original authorship and public redistribution permissions have not been independently established. Confirm rights before publishing or redistributing those image files. The repository's MIT license does not grant rights to third-party assets.

This project contains no ready-to-install signed package. Generate and sign your own package locally with your own certificate profile.

## Contributing

Read CONTRIBUTING.md and AI-GUIDE.md before making changes. Keep device-specific observations separate from assumptions, preserve remote navigation and preference migrations, and do not include private device or signing data in issues or pull requests.
