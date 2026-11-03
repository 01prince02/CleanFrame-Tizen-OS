# AI Coding Guide for CleanFrame Tizen

This guide helps an AI coding assistant work safely in this existing CleanFrame Tizen project. It does not grant permission to contact, install on, or modify a TV.

## Start with the project

1. Read AGENTS.md.
2. Read docs/development.md and docs/interaction-behaviour.md before changing app behavior.
3. Read docs/assets.md before changing images, glass materials, logos or icon sizing.
4. Read docs/tv-status.md and docs/compatibility.md before making device-compatibility claims.
5. Read docs/testing.md to distinguish source tests, browser preview results and physical TV evidence.
6. Inspect git status and the existing diff. Preserve unrelated user edits; never reset, clean or overwrite them.

The app source is in app/. It is a Samsung Tizen web app built with HTML, CSS and ES5-compatible JavaScript. scripts/ contains preview, validation, packaging, device and experimental native-Home tools. docs/ describes current behavior and the limits of recorded TV tests.

## Work in small, reviewable steps

- Ask the owner for missing product decisions. Do not invent features, supported apps, remote key behavior or TV settings destinations.
- Make the smallest change that satisfies the request and preserve app identity, stored preference migrations and remote focus behavior.
- Keep feature behavior honest. Do not simulate a successful TV app launch or present unsupported Samsung settings as working.
- Keep glass blur and image analysis off the TV animation path. Use the bundled material images and lightweight transforms/opacity for focus effects.
- Keep credentials and machine-specific values in ignored local configuration. Never print or commit certificates, passwords, account details, DUIDs, local addresses, private logs or signed WGTs.
- Preserve LICENSE, THIRD_PARTY_NOTICES.md, image credits and each asset's separate license. The owner-supplied wallpaper files currently have no independently verified public redistribution terms; do not redistribute them without confirming rights.
- Do not remove Samsung system apps, root or exploit the TV, bypass security, alter firmware, or replace Smart Hub.

## Browser-only tasks

For UI or source work that does not require a TV, ask for a bounded change and keep all device commands out of scope. Useful commands documented by the project include:

    npm run check
    npm run check:tools
    npm run check:browser
    npm run check:public

Read docs/testing.md before interpreting results. The check and browser commands use synthetic device behavior or an isolated local browser; they do not validate a physical TV. Do not run checks unless the owner or task requests verification.

Example prompt:

> Read AGENTS.md and the relevant development/interaction docs. Make this one browser-only change: [describe it]. Preserve existing edits, remote navigation, app identity and saved preference migrations. Do not contact or change a TV, sign a package or change Home/startup settings. Show the diff and report any unverified assumptions.

## TV tasks require separate authorization

A task involving device information, installation or launching must explicitly request that operation. Before any install:

1. Confirm SDB can start, connect to the intended TV, list it, and report device state.
2. Verify target model/firmware, certificate profile and distributor authorization locally.
3. Inspect the exact WGT hash, app/package identity and signature with official Samsung/Tizen tools.
4. Show the owner the exact package and proposed action. Do not install unless the owner has authorized that package and action.
5. Stop on errors and report the exact result; do not try risky workarounds.

Use only official Samsung/Tizen SDK tooling. Do not download DLLs from third-party sites or replace Windows system files. Let the owner perform Samsung account sign-in and enter passwords/verification codes directly; never ask for them in chat.

Samsung Tizen apps can receive only the remote events the platform delivers and permits the app to register. Shortcut, volume, mute, power and voice controls may be reserved by Samsung. Do not override them or claim support without testing on the target remote.

The native-Home helper scripts are experimental, firmware/identity guarded utilities derived from a different reference TV. They are not part of routine app installation. Do not run them or change Home/startup assignments without a separate, explicit owner request, a target-specific review and a recovery plan.

## Package and publishing boundaries

- npm run package signs a personal package using local SDK/profile configuration; inspect its effects before using it.
- npm run tv:install and npm run tv:launch contact a TV.
- npm run export:public creates an unsigned public-font WGT; it is not ready to install.
- Review git status, staged file names, diffs, licenses and secret scans before committing or publishing.
- Publishing a commit or release requires the repository owner's explicit approval.

## Useful prompts

**Explain only**

> Read the project docs and explain how [component] works. Do not edit files or access a TV. Separate confirmed behavior from assumptions.

**Review a change**

> Review the current diff for Tizen compatibility, remote navigation, saved preferences, accessibility/readability and license/privacy issues. Do not modify files or access a TV.

**Implement a bounded change**

> Implement [one specific change] in the existing project. Preserve uncommitted edits, IDs, migrations and remote behavior. Do not connect to or modify a TV. Run only the checks I requested, then show the diff and limitations.
