# Istanbul Weather Bot

This project posts regular weather updates for Istanbul to Twitter.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies (requests, tweepy, python-dotenv, schedule):
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

You can deploy this project to a server or run it automatically with **GitHub Actions**.

1. Add the secrets from `.env.example` to your repository under **Settings → Secrets and variables → Actions**.
2. The included workflow file `.github/workflows/bot.yml` installs dependencies and executes `weather_bot.py` at **08:00**, **12:00**, **16:00**, and **20:00** UTC daily.
3. Commit and push the workflow file, then enable GitHub Actions on your repository.

## Development Tasks
Follow these tasks to build and deploy the bot:
1. **Project Setup** – create a GitHub repository and initialize a Python virtual environment.
2. **Obtain API Keys** – register for Twitter and OpenWeatherMap developer accounts.
3. **Configure API Access** – store the credentials in a `.env` file and load them in the script.
4. **Fetch Weather Data** – write a function to retrieve Istanbul weather from the API and test it.
5. **Format Tweets** – convert the weather data into a human‑readable tweet.
6. **Twitter Integration** – use Tweepy to authenticate and send tweets.
7. **Automation** – schedule the script to run four times daily locally or with GitHub Actions.
8. **Deployment** – run the bot on a cloud host or via the included GitHub Actions workflow.
9. **Monitoring and Maintenance** – add logging and monitor tweets for consistency.
