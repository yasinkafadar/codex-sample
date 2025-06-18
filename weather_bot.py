import os
import logging
import time

import requests
import tweepy
from dotenv import load_dotenv
import schedule


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

CITY = "Istanbul"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def load_config():
    """Load environment variables from .env file."""
    load_dotenv()
    required_vars = [
        "TWITTER_CONSUMER_KEY",
        "TWITTER_CONSUMER_SECRET",
        "TWITTER_ACCESS_TOKEN",
        "TWITTER_ACCESS_TOKEN_SECRET",
        "OPENWEATHER_API_KEY",
    ]
    missing = [var for var in required_vars if var not in os.environ]
    if missing:
        raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")


def get_weather():
    """Fetch current weather data for Istanbul."""
    api_key = os.environ["OPENWEATHER_API_KEY"]
    params = {"q": CITY, "appid": api_key, "units": "metric"}
    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def format_tweet(data):
    """Format weather data into a tweet."""
    main = data.get("weather", [{}])[0].get("main", "Unknown")
    desc = data.get("weather", [{}])[0].get("description", "").title()
    temp = data.get("main", {}).get("temp")
    wind = data.get("wind", {}).get("speed")
    humidity = data.get("main", {}).get("humidity")
    return (
        f"\U0001F326\uFE0F Istanbul Weather Update \U0001F326\uFE0F\n"
        f"Temperature: {temp}°C, Condition: {desc or main}\n"
        f"Wind: {wind} km/h, Humidity: {humidity}%"
    )


def send_tweet(text):
    """Send a tweet using Tweepy."""
    auth = tweepy.OAuth1UserHandler(
        os.environ["TWITTER_CONSUMER_KEY"],
        os.environ["TWITTER_CONSUMER_SECRET"],
        os.environ["TWITTER_ACCESS_TOKEN"],
        os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )
    api = tweepy.API(auth)
    api.update_status(text)
    logger.info("Tweet sent successfully")


def job():
    try:
        weather = get_weather()
        tweet = format_tweet(weather)
        send_tweet(tweet)
    except Exception as exc:
        logger.error("Failed to post tweet: %s", exc)


def schedule_jobs():
    schedule.every().day.at("08:00").do(job)
    schedule.every().day.at("12:00").do(job)
    schedule.every().day.at("16:00").do(job)
    schedule.every().day.at("20:00").do(job)
    logger.info("Scheduler started")
    while True:
        schedule.run_pending()
        time.sleep(30)


def main():
    load_config()
    schedule_jobs()


if __name__ == "__main__":
    main()
