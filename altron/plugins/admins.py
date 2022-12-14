from pyrogram import Client
from pyrogram.types import Message
from helpers.command import commandpro
from config import call_py
from helpers.decorators import errors, sudo_users_only
from helpers.handlers import skip_current_song, skip_item
from helpers.queues import QUEUE, clear_queue


@Client.on_message(commandpro(["!skip", ".skip", "/skip", "/s", "S", "Skip"]))
@errors
@sudo_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**β π»ππππ'π πππππππ ππ πππ πππππ ππ ππππ**")
        elif op == 1:
            await m.reply("**π¬ππππ πππππ πππππππ πππππ ππππ**")
        else:
            await m.reply(
                f"**β© πΊππππππ ππππππππ** \n**πΆ π΅ππ πππππππ** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**ποΈ πΉππππππ πππ πππππππππ πππππ ππππ πππ πΈππππ: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#β£{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(commandpro(["!end", ".end", "/end", "!stop", ".stop", "/stop", "E", "End", "/e", "Stop"]))
@errors
@sudo_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**β π¬ππππ ππππππππ**")
        except Exception as e:
            await m.reply(f"**π¬ππππ....** \n`{e}`")
    else:
        await m.reply("**β π΅ππππππ ππ πππππππ**")


@Client.on_message(commandpro(["!pause", ".pause", "/pause", "pause"]))
@errors
@sudo_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**βΈ π·πππππππ ππππππ**\n\nπ»π ππππππ ππππππππ, πππ πππ πππππππ Β» `!resume`"
            )
        except Exception as e:
            await m.reply(f"**π¬ππππ.....** \n`{e}`")
    else:
        await m.reply("**β π΅ππππππ ππ πππππππ**")


@Client.on_message(commandpro(["!resume", ".resume", "/resume", "resume"]))
@errors
@sudo_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**βΆοΈ π·πππππππ πππππππ**\n\nπ»π πππππ ππππππππ, πππ πππ πππππππ Β» `!pause`"
            )
        except Exception as e:
            await m.reply(f"**π¬ππππ....** \n`{e}`")
    else:
        await m.reply("**β π΅ππππππ ππ πππππππ**")
