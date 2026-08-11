import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("broadcast", prefixes="/") & filters.me)(broadcast_handler)


async def broadcast_handler(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Reply to a message to broadcast.")
        return
    await message.edit("**Broadcasting...**")
    count = 0
    async for dialog in client.get_dialogs():
        try:
            await message.reply_to_message.copy(dialog.chat.id)
            count += 1
            await asyncio.sleep(0.3)
        except Exception:
            pass
    await message.edit(f"**Broadcast complete!** Sent to {count} chats.")
