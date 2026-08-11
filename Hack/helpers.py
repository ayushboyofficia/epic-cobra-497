"""Helper utilities for SessionHack."""
import asyncio
import logging
from typing import Optional
from pyrogram import Client
from pyrogram.types import Message

logger = logging.getLogger(__name__)


async def progress_bar(current: int, total: int, message: Message):
    """Display upload/download progress."""
    percent = current * 100 / total
    bar = "█" * int(percent / 5) + "░" * (20 - int(percent / 5))
    await message.edit(f"[{bar}] {percent:.1f}%")


async def safe_delete(message: Message, delay: int = 0):
    """Safely delete a message."""
    if delay:
        await asyncio.sleep(delay)
    try:
        await message.delete()
    except Exception:
        pass


async def get_user_mention(user) -> str:
    """Get user mention string."""
    if user.username:
        return f"@{user.username}"
    return user.mention


def parse_duration(duration_str: str) -> Optional[int]:
    """Parse duration string to seconds."""
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    if duration_str[-1] in units:
        try:
            return int(duration_str[:-1]) * units[duration_str[-1]]
        except ValueError:
            return None
    try:
        return int(duration_str)
    except ValueError:
        return None
