import os
from dotenv import load_dotenv

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
MODEL = os.getenv("GOOGLE_MODEL")

if not GEMINI_API_KEY or not AVIATIONSTACK_API_KEY or not WEATHER_API_KEY:
    raise RuntimeError("⚠️ Missing API keys in environment variables")
