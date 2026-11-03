# Public release review

Use this checklist for each source or widget release. Results apply only to the exact commit or package reviewed.

## Source and history

- Review the full working-tree diff, staged files, hidden files, ignored local paths and Git history.
- Run `npm run check:public` and inspect its scope and result. It is a bounded scanner, not proof that no secret exists.
- Check commit metadata and all reachable refs. Removing a file from the latest tree does not remove earlier versions.
- Keep certificates, keys, passwords, tokens, device configuration, DUIDs, recovery state, signed WGTs and proprietary fonts private.
- Do not rewrite shared history or force-push without explicit owner approval. GitHub notes that cached references can remain after sensitive-data removal; follow its [sensitive-data removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

The current repository's older commits contain personal author contact metadata. It remains in public history because history has not been rewritten. The current source cleanup cannot remove it. The owner should review GitHub email privacy controls and decide whether further history remediation is appropriate. No credential value should be repeated in a public report.

## Assets and notices

Retain the original CleanFrame MIT license and all third-party notices. Review `THIRD_PARTY_NOTICES.md`, asset source records and each asset's actual redistribution terms. Owner-supplied wallpaper rights have not been independently verified; do not redistribute them until the owner has confirmed permission. A source-code license does not grant rights to third-party assets.

## Build and device evidence

Run the checks listed in `docs/testing.md`, preserve their output privately, and report which commands actually passed. Do not describe a browser check as a TV test. Test a signed widget only with the official Samsung SDK and the owner's certificate profile. Keep signed output private. A device install/launch requires explicit approval for that exact operation.

## Publication

Before publishing, show the owner the exact diff, upload file list, security scan results, license concerns and any history exposure. Do not push until the owner approves the reviewed changes. A new cleanup commit does not make old public history disappear.
