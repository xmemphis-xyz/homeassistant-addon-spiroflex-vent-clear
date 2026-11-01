# Changelog

## 0.1.8

- Only the Spiroflex / ecoNET mobile app **username and password** are required.
- Backend identifiers are now built in: region, Cognito pools, app client, API Gateway and IoT endpoint. They are optional overrides in the app configuration.
- The installation is discovered automatically after login. If the account has several installations, set `installation.name` or `installation.id`. The app log lists the available installations.
- Existing configurations keep working unchanged. Leftover placeholder values from older versions (`region: eu-west-3` with empty identifiers) are replaced with the built-in defaults.
- Backend source pinned to commit 0ca9075f15bdb43ecfa50f3df08aaf8029fdf88c.

## 0.1.6

- Added per-mode BOOST cancellation endpoints: POST /api/vent/boost/1/off and /api/vent/boost/2/off.
- Stop clears only the selected BOOST bit and verifies its flag and timer without switching ventilation power off.
- Serialize BOOST commands in the backend. Repeating ON does not reset an active timer.
- Use the same validation for the legacy diagnostic write route.
- Pin backend source to commit 301c5539c87e34f274c8c9aed92a089e21f4a801 and run tests before publishing the image.
- Intended for the new ON/OFF switches in HACS integration 0.1.5; existing start endpoints remain compatible with 0.1.4.

The cancellation command must still be verified on the physical ecoVENT controller. A successful build confirms compilation and software tests, not hardware behavior. If cancellation is not confirmed by the flag and timer, the API reports an error. Do not uninstall the app or erase its configuration.
