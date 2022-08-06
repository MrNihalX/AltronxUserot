from datetime import datetime
from pyrogram import filters, Client
import requests
from config import *

__MODULE__ = "Pɪɴɢ"
__HELP__ = f"""
**🖤 Pɪɴɢ Mᴏᴅᴜʟᴇ 🖤**

`!ping` - __Tᴏ Cʜᴇᴄᴋ Pɪɴɢ Oғ UsᴇʀBᴏᴛ__

"""

@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("» __ᴀʟᴛʀᴏɴ__")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"__🤖 ᴘɪɴɢ__\n» `{mp} ms`")

