import os
import logging

from environs import Env

env = Env()
env.read_env()

# Core environment configuration for SESSIONHACK
API_ID = env.int("API_ID", 0)
API_HASH = env.str("API_HASH", "")
BOT_TOKEN = env.str("BOT_TOKEN", "")

# Server configuration
PORT = env.int("PORT", 8080)
DEBUG = env.bool("DEBUG", False)

# Logging
LOG_LEVEL = env.str("LOG_LEVEL", "INFO")

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

logger.info("Environment configuration loaded successfully")
