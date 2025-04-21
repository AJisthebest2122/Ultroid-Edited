# Ultroid Extended - Heroku Edition

![Ultroid Extended](https://graph.org/file/031957757a4f6a5191040.jpg)

A special fork of the [Ultroid UserBot](https://github.com/TeamUltroid/Ultroid) optimized specifically for seamless Heroku deployment.

## Features

- **Heroku Optimized**: Specially modified to work within Heroku's limitations
- **Web Interface**: Includes a web server to prevent Heroku dynos from idling
- **Easy Deployment**: One-click deploy button for quick setup
- **Resource Efficient**: Carefully selected dependencies to stay within Heroku free tier limits

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ThePrateekBhatia/Ultroid)

## Quick Setup Guide

1. Click the Deploy to Heroku button above
2. Enter your Telegram API credentials and other required information
3. Deploy the application
4. Ensure both dynos (web and worker) are enabled in the Heroku dashboard
5. Check your Telegram for the bot startup confirmation

## Requirements

- Telegram API ID and Hash (get from [my.telegram.org](https://my.telegram.org))
- Telethon Session String (generate using the [Session Generator](https://replit.com/@TeamUltroid/UltroidStringSession))
- Redis Database (the Heroku Redis add-on will be automatically installed)

## Important Environment Variables

| Variable | Description |
| --- | --- |
| `SESSION` | Telethon session string |
| `API_ID` | Telegram API ID from my.telegram.org |
| `API_HASH` | Telegram API Hash from my.telegram.org |
| `REDIS_URI` | Redis endpoint URL (auto-configured with Heroku Redis addon) |
| `REDIS_PASSWORD` | Redis endpoint password (auto-configured with Heroku Redis addon) |
| `HEROKU_APP_NAME` | Your Heroku app name (same as in deployment) |

See [HEROKU.md](HEROKU.md) for the complete list of environment variables.

## Notes on Heroku Deployment

- This fork is specifically optimized for Heroku's environment
- Both web and worker dynos are required for optimal operation
- Resource-intensive features have been optimized or removed to work within Heroku's limits
- The web server component prevents Heroku from idling your application
- Free tier Heroku apps will restart every 24 hours (this is normal)

## Troubleshooting

- If the bot doesn't start properly, check the Heroku logs for errors
- Ensure both web and worker dynos are enabled in the Heroku dashboard
- Verify that your session string is valid and correctly entered
- Check that the Heroku Redis addon was properly installed

## Support

For support related to this Heroku-specific version, please open an issue in this repository.

---

## Credits
- [TeamUltroid](https://github.com/TeamUltroid) for the original Ultroid UserBot
- [ThePrateekBhatia](https://github.com/ThePrateekBhatia) for the Heroku-optimized fork
