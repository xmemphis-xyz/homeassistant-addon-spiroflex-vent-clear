undefined
## Timed modes (0.1.7)

The Go REST bridge supports BOOST 1, BOOST 2, and Kominek (fireplace)
with individually controllable ON/OFF endpoints and controller-confirmed
state and countdown values. Update the app to **0.1.7** before updating
the HACS integration to **0.1.7**. Existing Home Assistant entities
remain in place; the Kominek switch and sensors are added.

Kominek ON/OFF has been verified on a real device (2026-11-02).

## Releasing

The app builds the backend from the commit pinned in
`spiroflex_vent_clear/backend.json`.

1. Publish a backend release in
   [spiroflex-vent-clear](https://github.com/xmemphis-xyz/spiroflex-vent-clear)
   by bumping `manifest.json` and `CHANGELOG.md` there.
2. Within an hour, the **Sync backend release** workflow opens a PR here. You
   can also start it by hand under Actions. The PR pins the release commit,
   bumps the app version and adds the backend release notes to the changelog.
3. Merge the PR. **Build and publish Home Assistant app** tests the backend
   and publishes the image.

To let the workflow open PRs, enable *Settings → Actions → General →
Workflow permissions → Allow GitHub Actions to create and approve pull
requests*. Without it, the workflow only pushes the branch and links to it in
the run summary.
