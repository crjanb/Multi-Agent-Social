import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Handles application configuration from environment variables."""
    
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
    
    X_API_KEY = os.getenv("X_API_KEY")
    X_API_SECRET = os.getenv("X_API_SECRET")
    X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
    X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
    X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
    
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls):
        """Validates that essential config is present."""
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing!")
        if not cls.TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY is missing!")
