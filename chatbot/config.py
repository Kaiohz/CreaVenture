import os
from dotenv import load_dotenv

load_dotenv()


class SerpConfig:
    API_KEY = os.getenv("SERP_API_KEY")


class GoogleNewsConfig:
    BASE_URL = os.getenv("GOOGLE_NEWS_BASE_URL")
    API_KEY = os.getenv("GOOGLE_NEWS_API_KEY")


class GeminiConfig:
    API_KEY = os.getenv("GOOGLE_API_KEY")
