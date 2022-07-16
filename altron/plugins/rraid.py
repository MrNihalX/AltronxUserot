# Credit » @Timeisnotwaiting

import random
from typing import Tuple
from pyrogram import Client, filters
from traceback import format_exc
from config import SUDO_USERS
from helpers.data import *
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from database import ffub_info, rff, runff
from altron.plugins import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["replyraid", "rraid", "rr"], [".", "/", "!"]))
@Client.on_message(filters.me & filters.command(["replyraid", "rraid", "rr"], ["/", ".", "!"]))
async def replyramd(client: Client, message: Message):
    ff = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await ff.edit("`Reply To User Or Mention To Activate Replyraid `")
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
        await ff.edit("`Jaa Na Lawde Kahe Dimag Kha rha? Khudpe Raid kyu laga rha?`")
        return
    if await ffub_info(userz.id):
        await ff.edit("`Who So Noob? Reply Raid Already Activated on that User:/`")
        return
    if int(userz.id) in SUDO_USERS:
        await ff.edit("Abe Lawde that guy part of my devs.")
        return
    await ff.edit("`Please, Wait Fectching Using Details!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        ff.edit("`You Have No Chats! So Sad`")
        return
    await ff.edit("`Activating Replyraid....!`")
    await rff(userz.id, reason)
    gbanned = f"Reply Raid has Been Activated On {userz.first_name}"
    await ff.edit(gbanned)
    

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dreplyraid", "drraid", "drr"], ["/", "!", "."]))
@Client.on_message(filters.me & filters.command(["dreplyraid", "drraid", "drr"], ["/", "!", "."]))
async def dreplyramd(client: Client, message: Message):
    ff = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await ff.edit("`Reply To User Or Mention To Deactivate Replyraid`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await ff.edit(f"`404 : User Doesn't Exists!`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await ff.edit("`Soja Lomde`")
        return
    if not await ffub_info(userz.id):
        await ff.edit("`When I Replyraid Activated? On That User?:/`")
        return
    await ff.edit("`Please, Wait Fectching User details!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        ff.edit("`You Have No Chats! So Sad`")
        return
    await ff.edit("`De-Activating Replyraid Raid....!`")
    await runff(userz.id)
    ungbanned = f"**De-activated Replyraid Raid [{userz.first_name}](tg://user?id={userz.id})"
    await ff.edit(ungbanned)


