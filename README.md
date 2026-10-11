undefined
## Timed modes (0.1.7)

The Go REST bridge supports BOOST 1, BOOST 2, and Kominek (fireplace)
with individually controllable ON/OFF endpoints and controller-confirmed
state and countdown values. Update the app to **0.1.7** before updating
the HACS integration to **0.1.7**. Existing Home Assistant entities
remain in place; the Kominek switch and sensors are added.

Kominek ON/OFF still requires a real-device verification after installing
0.1.7. Do not enable automatic cooker-hood control before this test.
