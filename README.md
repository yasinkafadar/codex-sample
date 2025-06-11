# Istanbul Weather Bot

This project posts regular weather updates for Istanbul to Twitter.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your Twitter and OpenWeatherMap API keys.

## Usage

Run the bot locally with:
```bash
python weather_bot.py
```
The script schedules tweets at **08:00**, **12:00**, **16:00**, and **20:00** each day.

## Deployment

You can deploy this project to a server or use a GitHub Actions workflow with a cron
schedule to run the script automatically.

## Development Tasks

The repository was prepared following these steps:
1. Project setup with a Python environment and required libraries.
2. API credentials are loaded from a `.env` file for security.
3. Weather data is fetched from OpenWeatherMap and formatted into a tweet.
4. Tweets are sent using Tweepy and scheduled four times daily.
5. Basic logging assists with monitoring and troubleshooting.
