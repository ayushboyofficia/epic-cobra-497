import asyncio

async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("broadcast",prefixes="/")&filters.me)(h)

async def h(c,m):
 if not m.reply_to_message:await m.edit("Reply to a msg.");return
 await m.edit("Broadcasting...");cnt=0
 async for d in c.get_dialogs():
  try:await m.reply_to_message.copy(d.chat.id);cnt+=1;await asyncio.sleep(0.3)
  except:pass
 await m.edit(f"Done! Sent to {cnt} chats.")
