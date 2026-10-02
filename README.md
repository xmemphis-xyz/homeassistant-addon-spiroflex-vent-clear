# Spiroflex ecoVENT Simple Home Assistant App

Home Assistant App that runs the Go REST bridge for Spiroflex Vent Clear / ecoVENT Simple.

The app replaces the standalone `ventclear` process previously running on another server.

## Installation

In Home Assistant:

1. Go to **Settings → Apps → App repositories**.
2. Add:

```
https://github.com/xmemphis-xyz/homeassistant-addon-spiroflex-vent-clear
```

3. Open the **Apps** section.
4. Install **Spiroflex ecoVENT Simple**.

## Configuration

Configure the ecoNET connection in the app configuration:

- Region
- Cognito username and password
- Cognito User Pool ID
- Cognito Client ID
- Cognito Identity Pool ID
- API Gateway name
- AWS IoT name
- Installation name and ID

The REST API listens on port **8088**.

The configuration is stored by Home Assistant and is not committed to Git.

## Home Assistant integration

After starting the app, configure the **Spiroflex ecoVENT Simple** HACS integration to connect to the Home Assistant host on port 8088.

Keep the existing service on the old server running until the new app has been tested successfully.
