# Experimental native Home control

This one-shot development helper is separate from CleanFrame's Tizen web app. It uses undocumented Samsung TV native APIs and a target-specific SDB execution route to query or change Home/startup state. It is not an official Samsung app-installation workflow, does not work as a generic launcher feature, and is not recommended for routine use.

The helper supports read-only query and guarded apply/restore. Apply writes Home/startup-related values and enables autostart; it is not Home-only. A TV setting or firmware update can make an old snapshot unsafe. Query/inspect also stages temporary files on the TV. The apply/restore route depends on the same SDB transport; an independent recovery route is not established.

## Target configuration

Do not put real target data in tracked files. If an owner separately authorizes an investigation, copy `profile.example.json` to ignored `.local/native-home/profile.json` and enter the exact model name, full firmware version and SDK-generated package/application identities. Configure the device address privately in `.local/device.json`. Store compiled output and an exact original-state snapshot only in ignored `.local/native-home/` storage.

The runner checks the configured model before staging. The helper checks the configured firmware, package, application ID, runtime bitness and SDK user, and refuses a mismatched state. These guards reduce mistakes; they do not establish safety or support on another TV. Never remove or weaken them to force a run.

## Local build and use

The compiled helper must already exist in `.local/native-home/out/` with its runtime and dependency files. Review `Control.cs`, all scripts and the recovery plan for the exact target before use. The runner performs device operations even in query mode; only invoke it under a separate explicit owner request.

```sh
python3 scripts/native-home/run.py query
python3 scripts/native-home/run.py apply
python3 scripts/native-home/run.py restore
```

Apply/restore require a private `original.json` captured from the supported original state. Do not overwrite it with the applied state. If it is missing, stale, empty, or does not match the live state, stop. Do not infer a reset value. Confirm actual screen behavior with the TV owner; a return code alone does not prove the visible destination.

The separate [`frame-2020` source](frame-2020/README.md) is a different experimental profile and does not broaden this helper's target guard. For ordinary Tizen app development, installation and supported APIs, see the [portable TV setup guide](../../docs/agent-tv-setup-guide.md).
