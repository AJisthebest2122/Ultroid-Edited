# Heroku Environment Variables for Ultroid Extended

The following environment variables are required for deploying Ultroid Extended to Heroku:

## Required Variables

| Variable | Description |
| --- | --- |
| `API_ID` | Your Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Your Telegram API Hash from [my.telegram.org](https://my.telegram.org) |
| `SESSION` | Telethon session string (Generate using [Replit](https://replit.com/@TeamUltroid/UltroidStringSession)) |
| `REDIS_URI` | Redis database URL (Use Heroku Redis addon or [RedisLabs](https://redislabs.com)) |
| `REDIS_PASSWORD` | Redis database password (If using RedisLabs) |

## Optional Variables

| Variable | Description |
| --- | --- |
| `BOT_TOKEN` | Telegram bot token from [@BotFather](https://t.me/BotFather) |
| `LOG_CHANNEL` | Channel ID for logging bot events |
| `HEROKU_API` | Heroku API token (for dyno management commands) |
| `HEROKU_APP_NAME` | Your Heroku app name (same as in deployment) |
| `OWNER_ID` | Your Telegram user ID |

## Database Options
You can use either of these for database:

1. **Heroku Redis** (Recommended): Use the Heroku Redis addon
2. **Redis Labs**: Create a free database at [RedisLabs](https://redislabs.com)

## Important Notes for Heroku:

- Free tier Heroku apps restart every 24 hours
- Redis addons have limited storage - optimize your usage accordingly
- Heroku has a 30-minute request timeout - avoid long-running operations
