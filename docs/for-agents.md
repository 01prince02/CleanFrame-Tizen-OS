# Working with a coding agent

Choose the task scope before starting: browser-only development, a locally signed app, or an experimental native Home investigation. Each requires a different toolchain and level of device access. Read `AGENTS.md`, `AI-GUIDE.md` and `docs/testing.md`; inspect the current Git status before editing.

## Browser-only work

Use the public-font preview described in `README.md`. The source and synthetic-device checks are offline; Playwright uses an isolated local browser. Ask for one bounded UI or behavior change at a time, preserve preference migrations and remote focus behavior, run the requested checks, and state which TV behaviors still need physical verification.

## Install your own app

Follow `docs/agent-tv-setup-guide.md` and current Samsung documentation. Use your own SDK, account, certificate profile, application identity and TV configuration. Store private values under ignored `.local/` files. The packaging runner supports POSIX SDK commands and the Windows batch CLI. On Windows, use Samsung SDK-managed certificate password access rather than a password file. A cloud-only assistant generally cannot access a TV on your local network.

Example prompt:

```text
Read AGENTS.md and docs/agent-tv-setup-guide.md. Help me prepare a local,
officially signed CleanFrame build for my Samsung Tizen TV. First inspect the
current source and the scripts' OS assumptions. Use only my own Samsung account,
certificate profile, application identity and target TV details. Keep credentials
and device values private and out of Git. Let me complete sign-in and verification
myself. Before any TV connection, install, launch, restart or settings action,
show me the exact proposed operation and wait for my authorization. Stop on errors.
Do not change Home/startup assignments, remove system apps, root the TV or bypass
Samsung security. Report what was tested and what still needs my physical review.
```

## Experimental native Home work

The tools under `scripts/native-home/` have fixed firmware, identity, runtime and recovery assumptions. They use undocumented behavior and are not portable installation steps. Querying may itself stage files on a TV. Do not run them or remove their guards as part of ordinary app work. Any such investigation needs a separate explicit owner request, exact-target review and recovery plan.

Keep account credentials, certificates, TV addresses, DUIDs, app identities and recovery snapshots private. A successful browser preview or package build does not establish physical TV compatibility.
