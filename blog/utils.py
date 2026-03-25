import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")


def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        return requests.get(url).json().get('articles', [])
    except:
        return []


def get_weather(city="Kathmandu"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        return requests.get(url).json()
    except:
        return {}


def get_gifs():
    try:
        url = f"https://api.giphy.com/v1/gifs/trending?api_key={GIPHY_API_KEY}&limit=5"
        return requests.get(url).json().get('data', [])
    except:
        return []