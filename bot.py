"""SessionHack - Main bot entry point."""
import os
import asyncio
from pyrogram import Client
from Hack import load_plugins
from env import API_ID, API_HASH, BOT_TOKEN
from logger import setup_logging, get_logger

logger = get_logger(__name__)

app = Client(
    "sessionhack",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


async def main():
    """Start the SessionHack bot."""
    setup_logging()
    logger.info("Starting SessionHack...")
    await app.start()
    logger.info("SessionHack is online!")
    await load_plugins(app)
    logger.info("Plugins loaded.")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
