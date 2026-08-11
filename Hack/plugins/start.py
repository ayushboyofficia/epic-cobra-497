from pyrogram import Client,filters

async def setup(c):
 c.on_message(filters.command("start",prefixes="/")&filters.private)(h)

async def h(c,m):
 await m.reply("**Welcome to SessionHack!**\nUse /help for commands.")
