"""Functions"""
import asyncio,logging
logger=logging.getLogger(__name__)

async def log(c,text,chat_id=None):
 try:
  if chat_id:await c.send_message(chat_id,text)
 except Exception as e:logger.error(e)

async def get_user(c,uid):
 try:return await c.get_users(uid)
 except:return None
