from pyrogram import filters, Client
from traceback import format_exc
from typing import Tuple
import asyncio
import random
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message)
from config import *
from altron.utilities.data import *
from altron.modules.database.mongo import * 


@Client.on_message( ~filters.me & filters.incoming)
async def watch_raids(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user = message.from_user.id
    veer = random.choice(RAID)
    love = random.choice(MRAID)
    if int(user) in VERIFIED_USERS:
        return
    elif int(user) in SUDO_USERS:
        return
    if int(message.chat.id) in GROUP:
        return
    if await veerub_info(user):
        try:
            await message.reply_text(veer)
        except:
            return
    if await loveub_info(user):
        try:
            await message.reply_text(love)
        except:
            return




__MODULE__ = "Rᴀɪᴅ"
__HELP__ = f"""
**🥀 Lᴏᴠᴇ Rᴀɪᴅ & Rᴇᴘʟʏ Rᴀɪᴅ ✨**

**ᴜsᴀɢᴇ:**
`.lraid` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Aᴄᴛɪᴠᴀᴛᴇ Lᴏᴠᴇ Rᴀɪᴅ.**

`.dlraid` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇ-Aᴄᴛɪᴠᴀᴛᴇ Lᴏᴠᴇ Rᴀɪᴅ.**

`.rraid` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Aᴄᴛɪᴠᴀᴛᴇ Rᴇᴘʟʏ Rᴀɪᴅ.**

`.drraid` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇ-Aᴄᴛɪᴠᴀᴛᴇ Rᴇᴘʟʏ Rᴀɪᴅ.**
"""
