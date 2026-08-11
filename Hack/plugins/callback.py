import asyncio
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message

async def setup(c:Client):
 c.on_callback_query()(cb_handler)

async def cb_handler(c:Client,cb:CallbackQuery):
 data=cb.data
 if data=="ping":
  await cb.answer("Pong!",show_alert=False)
 elif data=="close":
  await cb.message.delete()
 elif data=="help":
  await cb.answer("Use /help for commands",show_alert=True)
 else:
  await cb.answer("Unknown action",show_alert=True)
