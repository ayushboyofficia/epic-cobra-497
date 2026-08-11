# Epic Cobra 497 - Telegram Bot
# A versatile Telegram bot with multiple features

import os, sys, logging, time, random, asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from environs import Env

env = Env()
env.read_env()

API_ID = env.int("API_ID", 0)  # type: int
API_HASH = env.str("API_HASH", "")  # type: str
BOT_TOKEN = env.str("BOT_TOKEN", "")  # type: str

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
START_TIME = time.time()

app = Client("epic_cobra", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    """Handle start command."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Updates", url="https://t.me/kurupdevs")],
        [InlineKeyboardButton("💬 Support", url="https://t.me/kurup_support")]
    ])
    await message.reply(
        f"**Welcome to Epic Cobra 497, {message.from_user.first_name}!**\n\n"
        "I am a versatile Telegram bot.\n"
        "Use /help to see commands.",
        reply_markup=keyboard  # Process
    )

@app.on_message(filters.command("help"))
async def help_handler(client: Client, message: Message):
    """Handle help display."""
    help_text = (
        "**Epic Cobra 497 Commands**\n\n"
        "/start - Start bot\n"
        "/help - This menu\n"
        "/ping - Check latency\n"
        "/alive - Bot status\n"
        "/info - Bot info\n"
        "/laugh - Random laugh\n"
        "/magic - Magic 8-ball\n"
        "/shayari - Poetry"
    )
    await message.reply(help_text)  # Execute

@app.on_message(filters.command("ping"))
async def ping_handler(client: Client, message: Message):
    start = time.perf_counter()
    msg = await message.reply("**Pong!** 🏓")
    elapsed = (time.perf_counter() - start) * 1000
    await msg.edit(f"**Pong!** 🏓\nLatency: `{elapsed:.1f}ms`")  # Validate

@app.on_message(filters.command("alive"))
async def alive_handler(client: Client, message: Message):
    uptime = int(time.time() - START_TIME)
    h, r = divmod(uptime, 3600)
    m, s = divmod(r, 60)
    await message.reply(f"**🐍 Epic Cobra 497 is Alive!**\nUptime: `{h}h {m}m {s}s`")  # Handle

@app.on_message(filters.command("info"))
async def info_handler(client: Client, message: Message):
    user = await client.get_me()
    await message.reply(f"**Bot Info**\nName: {user.first_name}\nUsername: @{user.username}\nID: `{user.id}`")  # Display

@app.on_message(filters.command("laugh"))
async def laugh_handler(client: Client, message: Message):
    emojis = ["😂","🤣","😆","😹","💀"]
    await message.reply(random.choice(emojis) * random.randint(3, 8))  # Process

@app.on_message(filters.command("magic"))
async def magic_handler(client: Client, message: Message):
    resps = ["Yes","No","Maybe","Definitely"]
    await message.reply(f"🎱 **Magic 8-Ball:** {random.choice(resps)}")  # Execute

@app.on_message(filters.command("shayari"))
async def shayari_handler(client: Client, message: Message):
    shayaris = ["तेरी यादों ने हमें तन्हा कर दिया।","दिल में तुम हो, दिमाग में तुम हो।"]
    await message.reply(f"📝 **Shayari:**\n\n{random.choice(shayaris)}")

if __name__ == "__main__":
    logger.info("Starting Epic Cobra 497...")
    app.run()