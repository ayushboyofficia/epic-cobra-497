"""SessionHack bot."""
import asyncio
from pyrogram import Client
from env import API_ID,API_HASH,BOT_TOKEN
from logger import setup_logging,get_logger
from Hack import load_plugins

logger=get_logger(__name__)
app=Client("hack",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

async def main():
 setup_logging()
 logger.info("Starting SessionHack...")
 await app.start()
 await load_plugins(app)
 logger.info("SessionHack running!")
 await asyncio.Event().wait()

if __name__=="__main__":asyncio.run(main())
