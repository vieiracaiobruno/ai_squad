"""
Configuration module for AI Squad application.
Handles environment variables and settings.
"""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for managing application settings."""
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # GitHub Configuration
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    GITHUB_REPOSITORY: Optional[str] = os.getenv("GITHUB_REPOSITORY")
    
    @classmethod
    def validate(cls) -> None:
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in .env file.")
        
        if not cls.GITHUB_TOKEN:
            raise ValueError("GITHUB_TOKEN is required. Please set it in .env file.")
    
    @classmethod
    def is_configured(cls) -> bool:
        """Check if required configuration is present."""
        return bool(cls.OPENAI_API_KEY and cls.GITHUB_TOKEN)
