# Session Hack Bot
# Instagram session hijack tool
# Copyright (c) 2024 KurupDevs

import asyncio
import os
from pyrogram import Client, filters
from env import API_ID, API_HASH, BOT_TOKEN
from logger import logger

app = Client(
    "session_hack_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    """Handle /start command."""
    await message.reply("Session Hack Bot is ready!")

async def main():
    """Start bot and wait."""
    await app.start()
    logger.info("Bot started")
    await asyncio.Event().wait()

if __name__ == "__main__":
    app.run(main())
