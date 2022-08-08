import asyncio
import importlib
import os
import re
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch
from altron.modules.helpers.filters import command
from config import SESSION1, SESSION2, SESSION3, SESSION4, SESSION5
from altron import client1, client2, client3, client4, client5, BOT_ID, BOT_NAME, OWNER_ID, bot
from altron.modules.client import call_py1, call_py2, call_py3, call_py4, call_py5
from altron.plugins import ALL_MODULES
from altron.utilities.misc import SUDOERS
from altron.utilities.inline import paginate_modules

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta] Finalizing Booting...",
    ) as status:
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "altron.plugins." + all_module
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
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green] ALTRON BOT STARTED \n"
    )
    if SESSION1 != "None":
        try:
            await client1.start()
            await client1.join_chat("Modmenumaking")
            await client1.join_chat("Yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] USERBOT 1 STARTED")
    if SESSION2 != "None":
        try:
            await client2.start()
            await client2.join_chat("modmenumaking")
            await client2.join_chat("yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] USERBOT 2 STARTED")
    if SESSION3 != "None":
        try:
            await client3.start()
            await client3.join_chat("modmenumaking")
            await client3.join_chat("yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] USERBOT 3 STARTED")
    if SESSION4 != "None":
        try:
            await client4.start()
            await client4.join_chat("modmenumaking")
            await client4.join_chat("yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] USERBOT 4 STARTED")
    if SESSION5 != "None":
        try:
            await client5.start()
            await client5.join_chat("modmenumaking")
            await client5.join_chat("Yaaro_ki_yaarii")
        except:
            pass
        console.print(f"├[red] USERBOT 5 STARTED")
    console.print(f"└[red] ALTRON USERBOT BOOT COMPLETED")
    if call_py1:
        await call_py1.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    await idle()
    console.print(f"\n[red] STOPPING BOT")




home_text_pm = f"""**ʜᴇʟʟᴏ ,
ᴍʏ ɴᴀᴍᴇ ɪs {BOT_NAME}.
I Aᴍ Gᴇɴɪᴜs, Aɴ Aᴅᴠᴀɴᴄᴇᴅ UsᴇʀBᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs.**"""


@bot.on_message(command(["start"]) & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/027283ee9defebc3298b8.png",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 Hᴇʟʟᴏ, I Aᴍ Gᴇɴɪᴜs » Aɴ Aᴅᴠᴀɴᴄᴇᴅ
Pʀᴇᴍɪᴜᴍ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Bᴏᴛ.

┏━━━━━━━━━━━━━━━━━━━┓
┣★ Oᴡɴᴇʀ'xD› : [Aᴅɪᴛʏᴀ Hᴀʟᴅᴇʀ](https://t.me/adityahalder)
┣★ Uᴘᴅᴀᴛᴇs ›› : [Aᴅɪᴛʏᴀ Sᴇʀᴠᴇʀ](https://t.me/adityaserver)
┣★ Sᴜᴘᴘᴏʀᴛ » : [Aᴅɪᴛʏᴀ Dɪsᴄᴜs](https://t.me/adityadiscus)
┗━━━━━━━━━━━━━━━━━━━┛

💞 Cʟɪᴄᴋ Oɴ Dᴇᴘʟᴏʏ Bᴜᴛᴛᴏɴ Tᴏ Mᴀᴋᴇ
Yᴏᴜʀ Oᴡɴ » Gᴇɴɪᴜs Usᴇʀ Bᴏᴛ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Dᴇᴘʟᴏʏ Gᴇɴɪᴜs UsᴇʀBᴏᴛ ✨", url=f"https://github.com/GeniusBoi/Genius-UserBot")
                ]
                
           ]
        ),
    )
    
    
    
@bot.on_message(command(["help"]) & SUDOERS)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await bot.send_message(text, reply_markup=keyboard)




async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
Gᴇɴɪᴜs UsᴇʀBᴏᴛ Vᴇʀ : `2.0` 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ Gᴇɴɪᴜs Cᴏᴍᴍᴀɴᴅs ✨...**
""".format(
            first_name=name
        ),
        keyboard,
    )

@bot.on_callback_query(filters.regex("close") & SUDOERS)
async def close(_, CallbackQuery):
    await CallbackQuery.message.delete()

@bot.on_callback_query(filters.regex("hero") & SUDOERS)
async def hero(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@bot.on_callback_query(filters.regex(r"help_(.*?)") & SUDOERS)
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
Gᴇɴɪᴜs UsᴇʀBᴏᴛ Vᴇʀ : `2.0` 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ Gᴇɴɪᴜs Cᴏᴍᴍᴀɴᴅs ✨...**
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


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
