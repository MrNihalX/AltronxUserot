from pyrogram import filters, Client
from typing import Tuple
import asyncio
import random
from pyrogram.types import Message
from database import *
from helpers.data import *
from config import *


@Client.on_message( ~filters.me & filters.incoming)
async def watch(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user = message.from_user.id
    ff = random.choice(RAID)
    love = random.choice(MRAID)
    if int(user) in VERIFIED_USERS:
        return
    elif int(user) in SUDO_USERS:
        return
    if await ffub_info(user):
        try:
            await message.reply_text(ff)
        except:
            return
    if await loveub_info(user):
        try:
            await message.reply_text(love)
        except:
            return
        await client.send_message(
            message.chat.id,
            f"**ᴡᴀᴛᴄʜ** \n__ᴄʜᴀᴛ ɪᴅ :__ `{message.chat.id}` \n__ᴜsᴇʀ :__ `{user}` \n__ʀᴇᴀsᴏɴ :__ `{await ffub_info(user)}`",
        )

