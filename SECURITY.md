# Security policy

## Supported versions

Security fixes are made on the current `main` branch. Older copies may not receive updates; upgrade from the current repository and review each change before using it on a TV.

## Report a vulnerability privately

Do not publish exploitable details, credentials, device identifiers or personal logs in a public issue. Use GitHub's private vulnerability reporting for this repository when it is enabled. Otherwise contact the repository maintainer through an established private channel. Include the affected file or version, impact and a minimal reproduction that contains no real credentials or device data.

## Protect local credentials and devices

- Keep Samsung author/distributor certificates, private keys, profile files, passwords, tokens and signed WGT packages out of Git.
- Keep `.local/`, `dist/`, signing configuration, device configuration and recovery snapshots private. `.gitignore` excludes the standard local paths, but always inspect staged files before committing.
- Do not post TV DUIDs, IP addresses, serial numbers, account information, Wi-Fi details, SDB logs or screenshots containing them.
- Use your own Samsung account and certificate profile. Never send passwords or verification codes to an AI assistant.
- Do not run experimental native-Home tools as routine app setup. They are firmware-specific and use undocumented native behavior.
- Do not root a TV, bypass Samsung security, replace protected system components or remove system apps.

## Checks and limitations

`npm run check:public` and the packaging/public-export checks detect a bounded set of private paths and credential patterns in their defined inputs. They do not detect every possible secret or determine whether a value is private. Inspect the full diff, staged file list, screenshots, images and Git history before publishing. A later deletion does not erase information from earlier commits.

If a credential was committed, revoke or rotate it first. Then contact the repository owner to plan history remediation. Do not rewrite or force-push shared history without explicit authorization; cached copies may remain accessible even after a rewrite.
