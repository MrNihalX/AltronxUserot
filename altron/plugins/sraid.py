from pyrogram.types import *
import asyncio
from random import choice
from pyrogram import Client, filters
from altron.utilities.data import *
from altron.config import *

__MODULE__ = "Jᴏɪɴ/Lᴇᴀᴠᴇ"
__HELP__ = f"""
**🖤 Jᴏɪɴ Lᴇᴀᴠᴇ Mᴏᴅᴜʟᴇ 🖤**

`!join` - __Tᴏ Jᴏɪɴ A Cʜᴀɴɴᴇʟ Oʀ Gʀᴏᴜᴘ__

`!leave` - __Tᴏ Lᴇᴀᴠᴇ A Cʜᴀɴɴᴇʟ Oʀ Gʀᴏᴜᴘ__

"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["sraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      hero = await e.reply_text("» ᴜsᴀɢᴇ:\n !sraid 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")   
      TheAltronX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(TheAltronX) == 2:
          ok = await xspam.get_users(TheAltronX[1])
          id = ok.id
          counts = int(TheAltronX[0])
          omp = await hero.edit_text("`sʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
          await omp.delete()
          for _ in range(counts):
                reply = choice(SRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.001)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = e.chat.id
          counts = int(TheAltronX[0])
          omp = await hero.edit_text("`sʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
          await omp.delete()
          for _ in range(counts):
                reply = choice(SRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.001)

