import asyncio, logging
from pyrogram import Client
from pyrogram.types import Message

logger=logging.getLogger(__name__)

async def send_log(c:Client,text:str,chat_id:int=None):
 try:
  if chat_id:await c.send_message(chat_id,text)
 except Exception as e:logger.error(f"Log failed: {e}")

async def fetch_user(c:Client,uid:int):
 try:return await c.get_users(uid)
 except:return None

async def get_chat_info(c:Client,cid:int):
 try:return await c.get_chat(cid)
 except:return None
