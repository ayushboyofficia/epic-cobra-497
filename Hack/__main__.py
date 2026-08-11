import asyncio
from env import API_ID,API_HASH,BOT_TOKEN
from pyrogram import Client
from Hack import load_plugins
from logger import setup_logging

async def main():
 setup_logging()
 c=Client("hack",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)
 await c.start();await load_plugins(c)
 print("SessionHack running!")
 await asyncio.Event().wait()

if __name__=="__main__":asyncio.run(main())
