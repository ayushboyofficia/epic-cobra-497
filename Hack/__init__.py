"""SessionHack - Session Hijacker Bot"""
import logging,os
from pyrogram import Client

logger=logging.getLogger(__name__)
PLUGIN_DIR="Hack/plugins"

async def load_plugins(c:Client):
 if not os.path.exists(PLUGIN_DIR):return
 for f in os.listdir(PLUGIN_DIR):
  if f.endswith(".py")and not f.startswith("__"):
   m=f"Hack.plugins.{f[:-3]}"
   try:
    mod=__import__(m,fromlist=["setup"])
    if hasattr(mod,"setup"):await mod.setup(c)
    logger.info(f"Loaded: {f}")
   except Exception as e:logger.error(f"Failed {f}: {e}")
