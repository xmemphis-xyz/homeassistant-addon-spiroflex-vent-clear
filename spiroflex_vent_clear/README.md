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
