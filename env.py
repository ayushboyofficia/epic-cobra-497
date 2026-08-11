"""Environment configuration loader."""
import os
from typing import Optional


def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get environment variable with fallback."""
    return os.getenv(key, default)


def get_int_env(key: str, default: int = 0) -> int:
    """Get integer environment variable."""
    try:
        return int(os.getenv(key, str(default)))
    except (ValueError, TypeError):
        return default


# Core config
API_ID = get_int_env("API_ID")
API_HASH = get_env("API_HASH", "")
BOT_TOKEN = get_env("BOT_TOKEN", "")
MONGO_URI = get_env("MONGO_URI", "")
OWNER_ID = get_int_env("OWNER_ID")
LOG_CHANNEL = get_int_env("LOG_CHANNEL")
