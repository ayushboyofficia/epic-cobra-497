from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("start", prefixes="/") & filters.private)(start_handler)


async def start_handler(client: Client, message: Message):
    await message.reply(
        "**Welcome to SessionHack!**\n\n"
        "Use /help to see available commands."
    )
