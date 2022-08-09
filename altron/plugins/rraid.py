import random
from typing import Tuple
from pyrogram import *
from traceback import format_exc
from altron.utilities.data import *
from altron.modules.helpers.filters import command
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import *
from altron.modules.database.mongo import veerub_info, rveer, runveer
from altron.utilities.misc import SUDOERS


async def iter_chats(client: Client):
    """Iter Your All Chats"""
    chats = []
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ["supergroup", "channel"]:
            chats.append(dialog.chat.id)
    return chats

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 1024:
        await message.edit("`OutPut is Too Large, Sending As File!`")
        file_names = f"{file_name}.text"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

   


@Client.on_message(command(["replyraid", "rraid", "rr"]) & SUDOERS)
async def replyramd(client: Client, message: Message):
    await message.delete()
    veer = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await veer.edit("`Reply To User Or Mention To Activate ReplyRaid `")
        return
    try:
        userz = await client.get_users(user)
    except:
        await veer.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    if not reason:
        reason = "Private Reason!"
    mee= await client.get_me()
    if userz.id == mee.id:
        await veer.edit("`Jaa Na Tharki Kahe Dimag Kha rha? Khudpe Raid kyu laga rha?`")
        return
    if await veerub_info(userz.id):
        await veer.edit("`Who So Noob? ReplyRaid Already Activated on that User:/`")
        return
    await veer.edit("`Please, Wait Fectching Using Details!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        veer.edit("`You Have No Chats! So Sad`")
        return
    await veer.edit("`Activating ReplyRaid....!`")
    await rveer(userz.id, reason)
    gbanned = f"ReplyRaid has Been Activated On {userz.first_name}"
    await veer.edit(gbanned)
    

@Client.on_message(command(["dreplyraid", "drraid", "drr"]) & SUDOERS)
async def dreplyramd(client: Client, message: Message):
    await message.delete()
    veer = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await veer.edit("`Reply To User Or Mention To Deactivate ReplyRaid`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await veer.edit(f"`404 : User Doesn't Exists!`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await veer.edit("`Soja Tharki`")
        return
    if not await veerub_info(userz.id):
        await veer.edit("`When I ReplyRaid Activated? On That User?:/`")
        return
    await veer.edit("`Please, Wait Fectching User details!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        veer.edit("`You Have No Chats! So Sad`")
        return
    await veer.edit("`De-Activating ReplyRaid Raid....!`")
    await runveer(userz.id)
    ungbanned = f"**De-activated ReplyRaid Raid [{userz.first_name}](tg://user?id={userz.id})"
    await veer.edit(ungbanned)

