import asyncio
import importlib
from altron import ALL_MODULES
from pyrogram import idle
from config import client, client2, client3, client4, client5, client6, client7, client8, client9, client10, bot, call_py, call_py2, call_py3, call_py4, call_py5, call_py6, call_py7, call_py8, call_py9, call_py10
from config import *
import re
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from helpers.inline import paginate_modules


HELPABLE = {}

async def main():
    if client:
        try:
            await client.start()
            await client.join_chat("TheAltron")
            await client.join_chat("Altron_X")
            await client.join_chat("Yaaro_Ki_Yaarii")
            await client.join_chat("AboutShailendra")
            await client.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client2:
        try:
            await client2.start()
            await client2.join_chat("TheAltron")
            await client2.join_chat("Altron_X")
            await client2.join_chat("Yaaro_Ki_Yaarii")
            await client2.join_chat("AboutShailendra")
            await client2.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client3:
        try:
            await client3.start()
            await client3.join_chat("TheAltron")
            await client3.join_chat("Altron_X")
            await client3.join_chat("Yaaro_Ki_Yaarii")
            await client3.join_chat("AboutShailendra")
            await client3.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client4:
        try:
            await client4.start()
            await client4.join_chat("TheAltron")
            await client4.join_chat("Altron_X")
            await client4.join_chat("Yaaro_Ki_Yaarii")
            await client4.join_chat("AboutShailendra")
            await client4.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client5:
        try:
            await client5.start()
            await client5.join_chat("TheAltron")
            await client5.join_chat("Altron_X")
            await client5.join_chat("Yaaro_Ki_Yaarii")
            await client5.join_chat("AboutShailendra")
            await client5.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client6:
        try:
            await client6.start()
            await client6.join_chat("TheAltron")
            await client6.join_chat("Altron_X")
            await client6.join_chat("Yaaro_Ki_Yaarii")
            await client6.join_chat("AboutShailendra")
            await client6.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client7:
        try:
            await client7.start()
            await client7.join_chat("TheAltron")
            await client7.join_chat("Altron_X")
            await client7.join_chat("Yaaro_Ki_Yaarii")
            await client7.join_chat("AboutShailendra")
            await client7.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client8:
        try:
            await client8.start()
            await client8.join_chat("TheAltron")
            await client8.join_chat("Altron_X")
            await client8.join_chat("Yaaro_Ki_Yaarii")
            await client8.join_chat("AboutShailendra")
            await client8.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client9:
        try:
            await client9.start()
            await client9.join_chat("TheAltron")
            await client9.join_chat("Altron_X")
            await client9.join_chat("Yaaro_Ki_Yaarii")
            await client9.join_chat("AboutShailendra")
            await client9.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))

    if client10:
        try:
            await client10.start()
            await client10.join_chat("TheAltron")
            await client10.join_chat("Altron_X")
            await client10.join_chat("Yaaro_Ki_Yaarii")
            await client10.join_chat("AboutShailendra")
            await client10.join_chat("HeroOfficialBots")
        except Exception as e:
            print(str(e))
    await bot.start()
    print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(
            "altron" + all_module
        )
        if (
            hasattr(imported_module, "__MODULE__")
            and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                hasattr(imported_module, "__HELP__")
                and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.lower()
                ] = imported_module


home_text_pm = f"""**ʜᴇʟʟᴏ ,
✘ ɪ'ᴍ ᴀɴ ᴜsᴇʀʙᴏᴛ ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ. ɪ ᴄᴀɴ sᴘᴀᴍ ᴍsɢ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ . ɪ ʜᴀᴠᴇ ʟᴏᴛꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ʟɪᴋᴇꜱ ᴛʜᴀᴛ.**"""

    
@bot.on_message(filters.command(["start", "help"]) & filters.user(SUDO_USERS))
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await bot.send_message(text, reply_markup=keyboard)


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ Aʟᴛʀᴏɴ UsᴇʀBᴏᴛ Vᴇʀsɪᴏɴ : `2.1` 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs Tᴏ Gᴇᴛ Aʟᴛʀᴏɴ Cᴏᴍᴍᴀɴᴅs ✨...**
""".format(
            first_name=name
        ),
        keyboard,
    )

@bot.on_callback_query(filters.regex("close") & filters.user(SUDO_USERS))
async def close(_, CallbackQuery):
    await CallbackQuery.message.delete()

@bot.on_callback_query(filters.regex("veer") & filters.user(SUDO_USERS))
async def veer(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@bot.on_callback_query(filters.regex(r"help_(.*?)") & filters.user(SUDO_USERS))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ Aʟᴛʀᴏɴ UsᴇʀBᴏᴛ Vᴇʀsɪᴏɴ : `2.1` 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs Tᴏ Gᴇᴛ Aʟᴛʀᴏɴ Cᴏᴍᴍᴀɴᴅs ✨...**
 """
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :** ", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ ʙᴀᴄᴋ", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="🔄 ᴄʟᴏsᴇ", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await bot.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)

    if call_py:
        await call_py.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    if call_py6:
        await call_py6.start()
    if call_py7:
        await call_py7.start()
    if call_py8:
        await call_py8.start()
    if call_py9:
        await call_py9.start()
    if call_py10:
        await call_py10.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
