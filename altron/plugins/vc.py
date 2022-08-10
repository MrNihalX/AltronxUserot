from altron.modules.client import *
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.types import Message
from pyrogram import *


@client1.on_message(filters.command(["startvc"]))
async def _(c:client1, m:Message):
    try:
        await c(CreateGroupCall(m.chat_id)) 
        await m.reply_text("**🔊 Voice Chat Started Successfully**")
    except:
        pass

