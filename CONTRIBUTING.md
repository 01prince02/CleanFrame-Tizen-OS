# Contributing to CleanFrame

CleanFrame began as an experiment on one Samsung TV, and portability is still limited. Treat it as a starting point and verify behavior on your own target. Contributions are welcome when they preserve remote usability and describe exactly what was tested. New contributors can follow [README-SETUP.md](README-SETUP.md) and [AI-SETUP-GUIDE.md](AI-SETUP-GUIDE.md) first.

## Start in the browser

Use the README's public-font setup. Keep changes in `app/` and the maintained tools in `scripts/`. Use your browser to develop interface changes.

```sh
npm ci
npm run dev:public
npm run check
npm run check:tools
npx playwright install chromium
CLEANFRAME_PUBLIC_FONTS=1 npm run check:browser
npm run check:public
```

Keep runtime JavaScript ES5-compatible. Use existing focus, panel and preference logic. A new CSS/DOM API needs target-device evidence before it becomes a compatibility claim. Keep new dependencies in development tooling unless the runtime need is clear.

The signing/package helper supports the SDK's Windows batch CLI and POSIX SDK CLI. On Windows, use Samsung SDK-managed certificate password access; password files are unsupported because restrictive Windows ACLs are not verified portably. npm scripts select Python 3 from `CLEANFRAME_PYTHON`, `python3`, `python` or the Windows `py -3` launcher. Set `CLEANFRAME_PYTHON` when automatic detection does not find your Python 3 installation.

## Propose a change

For a bug, describe the trigger, expected result and actual result. Include browser/viewport or TV model and full firmware version. For a new feature, explain the task it helps someone complete from the sofa. Open an issue before changing the app model or introducing a new service dependency.

A pull request should explain the resulting behaviour, the checks run and any untested device result. Include a public-font screenshot for visual changes. Check both List and Dock, single focus, panel Back behaviour and saved-preference recovery when relevant. The TV remote remains the final check for remote feel; browser throttling is only a comparison.

## Device work and privacy

Use your own Samsung account, app identity, author certificate and distributor certificate. Follow the staged setup guide and keep native Home/startup experiments separate from UI work. Each TV owner decides whether and when to permit interruptions or settings changes.

Keep passwords, tokens, signing keys, serial numbers, DUIDs, addresses and original native settings out of issues, screenshots and PRs. Keep a private setup/recovery record. Report security issues through GitHub's private vulnerability reporting if enabled, or an established private channel with the maintainer; do not attach credentials to a public issue.

Before publishing, review both the current diff and earlier Git history. Removing a secret in a later commit does not erase it from older commits. See [SECURITY.md](SECURITY.md) for reporting and response guidance.

## Assets and licences

CleanFrame's original code is MIT. Contributions to that code use the same licence. Keep upstream asset licences and source records intact. Add only assets you have permission to redistribute, and explain any required attribution or separate terms. Personal paid fonts stay under `.local/`; the public app must work without them. Review `THIRD_PARTY_NOTICES.md` before adding or replacing a logo, photograph or font.
