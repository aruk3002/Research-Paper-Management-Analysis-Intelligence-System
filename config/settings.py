"""
Central configuration loader.
Loads and validates environment variables.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY missing in .env")

settings = Settings()
