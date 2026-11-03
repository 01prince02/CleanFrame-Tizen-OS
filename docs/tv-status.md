# TV verification status

## Public-project boundary

Owner-specific TV model/firmware combinations, network addresses, device identifiers, package identities, installed-app IDs, signing details and recovery state are intentionally not published here. A private device test report is not a compatibility guarantee for other TVs.

The source has been exercised on Samsung Tizen TV hardware in a Tizen 9 generation environment. The exact model and owner-specific evidence are kept private. Current rendering and feature behavior must be rechecked against the exact TV, firmware, region and installed apps before release. The manifest's Tizen 5.0 floor means only that the app declares that installation floor; it does not prove the app works on every later device.

## What source checks can establish

Browser and synthetic-device tests can check source behavior, saved preference logic, assets, simulated navigation and package contents. They cannot establish installed-app IDs, Samsung Settings destinations, physical remote key delivery, TV compositor behavior, Art Mode behavior or real-device performance. Record device checks privately and publish only the least identifying compatibility evidence needed, with the device owner's consent.

## App and native Home boundaries

The application can discover and launch apps through supported Tizen APIs where available. Installed apps, IDs and platform destinations vary. It does not install services or replace Smart Hub through the supported web-app interface.

Experimental scripts under `scripts/native-home/` are separate, undocumented, firmware- and identity-guarded research tools. They are not part of app installation or routine testing. Do not run them against a TV unless the owner requests that specific experiment, the exact firmware and recovery path have been reviewed, and the owner has approved each device operation. Their source may contain fixed assumptions for the original test environment; a clone must not remove guards or treat the scripts as portable.

See [compatibility evidence](compatibility.md), [development](development.md), [testing](testing.md) and the [staged TV setup guide](agent-tv-setup-guide.md).
