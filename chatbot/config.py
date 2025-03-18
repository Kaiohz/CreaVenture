import os
from dotenv import load_dotenv

load_dotenv()

class GoogleNewsConfig:
    BASE_URL = os.getenv("GOOGLE_NEWS_BASE_URL")
    API_KEY = os.getenv("GOOGLE_NEWS_API_KEY")
