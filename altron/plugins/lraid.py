# Credit » @AdityaHalder

import random
from typing import Tuple
from pyrogram import Client, filters
from traceback import format_exc
from config import *
from helpers.data import *
from pyrogram.errors import *
from pyrogram.types import *
from database import *
from altron.plugins import *



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["loveraid", "lraid", "lr"]))
@Client.on_message(filters.me & filters.command(["loveraid", "lraid", "lr"]))
async def replyramd(client: Client, message: Message):
    await message.delete()
    ff = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await ff.edit("`Reply To User Or Mention To Activate LoveRaid `")
        return
    try:
        userz = await client.get_users(user)
    except:
        await ff.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    if not reason:
        reason = "Private Reason!"
    mee= await client.get_me()
    if userz.id == mee.id:
        await ff.edit("`Jaa Na Tharki Kahe Dimag Kha rha? Khudpe Raid kyu laga rha?`")
        return
    if await loveub_info(userz.id):
        await ff.edit("`Who So Noob? LoveRaid Already Activated on that User:/`")
        return
    if int(userz.id) in SUDO_USERS:
        await ff.edit("Abe Chimkandi that guy part of my X.")
        return
    await ff.edit("`Please, Wait Fectching Using Details!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        ff.edit("`You Have No Chats! So Sad`")
        return
    await ff.edit("`Activating LoveRaid....!`")
    await rlove(userz.id, reason)
    gbanned = f"LoveRaid has Been Activated On {userz.first_name}"
    await ff.edit(gbanned)
    

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dloveraid", "dlraid", "dlr"]))
@Client.on_message(filters.me & filters.command(["dloveraid", "dlraid", "dlr"]))
async def dreplyramd(client: Client, message: Message):
    await message.delete()
    ff = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await ff.edit("`Reply To User Or Mention To Deactivate LoveRaid`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await ff.edit(f"`404 : User Doesn't Exists!`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await ff.edit("`Soja Tharki`")
        return
    if not await loveub_info(userz.id):
        await ff.edit("`When I LoveRaid Activated? On That User?:/`")
        return
    await ff.edit("`Please, Wait Fectching User details!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        ff.edit("`You Have No Chats! So Sad`")
        return
    await ff.edit("`De-Activating LoveRaid Raid....!`")
    await runlove(userz.id)
    ungbanned = f"**De-activated LoveRaid Raid [{userz.first_name}](tg://user?id={userz.id})"
    await ff.edit(ungbanned)


