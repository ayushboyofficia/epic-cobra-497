"""Helpers"""
import asyncio,logging
logger=logging.getLogger(__name__)

async def bar(cur,total,msg):
 pct=cur*100/total
 b="█"*int(pct/5)+"░"*(20-int(pct/5))
 await msg.edit(f"[{b}] {pct:.1f}%")

async def safe_del(msg,delay=0):
 if delay:await asyncio.sleep(delay)
 try:await msg.delete()
 except:pass
