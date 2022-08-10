from altron.modules.client import *
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.types import Message as m
from pyrogram import *


@client1.on_message(filters.command(["startvc"]))
async def _(client, m:Message):
    try:
        await client.CreateGroupCall(m.chat_id))
        await m.reply_text("**🔊 Voice Chat Started Successfully**")
    except
        pass

