# Session Hack Bot
# Instagram session hijack tool

import os
from pyrogram import Client, filters
from env import API_ID, API_HASH, BOT_TOKEN
from logger import logger
# main bot entry point

app = Client(
    "session_hack_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply("Session Hack Bot is ready!")

async def main():
    await app.start()
    logger.info("Bot started")
    await asyncio.Event().wait()

if __name__ == "__main__":
    import asyncio
    app.run(main())
