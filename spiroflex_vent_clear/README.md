## Configuration

Enter only the **username** and **password** you use in the Spiroflex /
ecoNET mobile app under `cognito`, then start the app.

Everything else is optional:

- Backend identifiers (`region`, `cognito.user_pool_id`, `cognito.client_id`,
  `cognito.identity_pool_id`, `gateway.name`, `iot.name`) are built in.
  Fill them in only if the vendor changes its backend.
- The installation is discovered automatically after login. If your account
  has more than one, set `installation.name` or `installation.id`. The app
  log lists the available installations.
- After startup, the log shows `Using installation "<name>" (id ...)`.

The REST API listens on port 8088. In the HACS integration, enter the Home
Assistant host and port 8088.

undefined
## Kominek timed mode (version 0.1.7)

Version 0.1.7 includes the `/api/vent/fireplace/on` and `/off` endpoints
and returns `fireplace_active` and `fireplace_remaining` in
`/api/vent/status`.

Update this app to 0.1.7 before installing the matching HACS integration
0.1.7. In Home Assistant, the device then includes **Kominek** after the two
BOOST switches, plus its activity and remaining-time sensors.

The user verified that the third timed mode sets u6639 to 256, u7429 to
10 minutes, and fan speed from 40/40% to 100/10%. The new writable API
requires a separate live test on the controller: test ON/OFF manually
before enabling any hood-driven automation. Timed writes are serialized,
masked to the selected mode bit, and read back before being confirmed.
