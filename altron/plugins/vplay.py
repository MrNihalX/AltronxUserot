import asyncio
from altron.modules.helpers.command import commandpro
from altron.modules.helpers.decorators import errors, sudo_users_only
from altron.modules.client import client1 as client, call_py1 as call_py
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio, 
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch
from config import HEROKU_MODE
from altron.modules.helpers.queues import QUEUE, add_to_queue, get_queue


__MODULE__ = "PʟᴀʏFʀᴏᴍ"
__HELP__ = f"""
**🖤 PʟᴀʏFʀᴏᴍ Mᴏᴅᴜʟᴇ 🖤**

`!pf` - __Tᴏ Pʟᴀʏ Aᴜᴅɪᴏ Fɪʟᴇs Oғ Aɴᴏᴛʜᴇʀ Gʀᴏᴜᴘ Iɴ Yᴏᴜʀ Vᴏɪᴄᴇ Cʜᴀᴛ__

`!pl` - __Tᴏ Cʜᴇᴄᴋ PʟᴀʏLɪsᴛ__

"""

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:35] + "..."
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        # CHANGE THIS BASED ON WHAT YOU WANT
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@client.on_message(commandpro(["$vplay", "V", "!v", "/v", "!vplay", "/vplay", "Vplay"]))
@errors
@sudo_users_only
async def vplay(client, m: Message):
    if HEROKU_MODE == "ENABLE":
        await m.reply_text("__ᴄᴜʀʀᴇɴᴛʟʏ ʜᴇʀᴏᴋᴜ ᴍᴏᴅᴇ ɪs ᴇɴᴀʙʟᴇᴅ, so ʏᴏᴜ ᴄᴀɴ'ᴛ sᴛʀᴇᴀᴍ ᴠɪᴅᴇᴏ ʙᴇᴄᴀᴜsᴇ ᴠɪᴅᴇᴏ sᴛʀᴇᴀᴍɪɴɢ ᴄᴀᴜsᴇ ᴏғ ʙᴀɴɴɪɴɢ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ__.")
        return
    replied = m.reply_to_message
    chat_id = m.chat.id
    m.chat.title
    if replied:
        if replied.video or replied.document:
            await m.delete()
            huehue = await replied.reply("**🔄 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈...**")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await huehue.edit(
                        "**𝑶𝒏𝒍𝒚 720P, 480P, 360P 𝒂𝒍𝒍𝒐𝒘𝒆𝒅** \n**𝑵𝒐𝒘 𝒔𝒕𝒓𝒆𝒂𝒎𝒊𝒏𝒈 𝒊𝒏 720𝒑**"
                    )

            if replied.video:
                songname = replied.video.file_name[:35] + "..."
            elif replied.document:
                songname = replied.document.file_name[:35] + "..."

            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_text(f"""
**⃣ 𝑽𝒊𝒅𝒆𝒐 𝒊𝒏 𝒒𝒖𝒆𝒖𝒆 𝒕𝒐 {pos}
🎵 𝑶𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕 {m.from_user.mention}**
""",
                )
            else:
                if Q == 720:
                    hmmm = HighQualityVideo()
                elif Q == 480:
                    hmmm = MediumQualityVideo()
                elif Q == 360:
                    hmmm = LowQualityVideo()
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_text(f"""
**▶️ 𝑺𝒕𝒂𝒓𝒕𝒆𝒅 𝒑𝒍𝒂𝒚𝒊𝒏𝒈 𝒗𝒊𝒅𝒆𝒐
🎵 𝑶𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕 {m.from_user.mention}**
""",
                )

    else:
        if len(m.command) < 2:
            await m.reply("💫 𝑹𝒆𝒑𝒍𝒚 𝒕𝒐 𝒂𝒏 𝒗𝒊𝒅𝒆𝒐 𝒇𝒊𝒍𝒆 𝒐𝒓 𝒑𝒓𝒐𝒗𝒊𝒅𝒆 𝒔𝒐𝒎𝒆𝒕𝒉𝒊𝒏𝒈 𝒇𝒐𝒓 𝒔𝒆𝒂𝒓𝒄𝒉")
        else:
            await m.delete()
            huehue = await m.reply("🔎 𝑺𝒆𝒂𝒓𝒄𝒉𝒊𝒏𝒈...")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            hmmm = HighQualityVideo()
            if search == 0:
                await huehue.edit("`❌ 𝑭𝒐𝒖𝒏𝒅 𝒏𝒐𝒕𝒉𝒊𝒏𝒈 `")
            else:
                songname = search[0]
                url = search[1]
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await huehue.edit(f"**𝒀𝑻𝑫𝑳 𝑬𝒓𝒓𝒐𝒓... ⚠️** \n\n`{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await huehue.delete()
                        # await m.reply_to_message.delete()
                        await m.reply_text(f"""
**⃣ 𝑽𝒊𝒅𝒆𝒐𝒔 𝒂𝒅𝒅𝒆𝒅 𝒊𝒏 𝒒𝒖𝒆𝒖𝒆 𝒂𝒕 {pos}
🎵 𝑶𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕 {m.from_user.mention}**
""",
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await huehue.delete()
                            # await m.reply_to_message.delete()
                            await m.reply_text(f"""
**▶️ 𝑺𝒕𝒂𝒓𝒕𝒆𝒅 𝒑𝒍𝒂𝒚𝒊𝒏𝒈 𝒗𝒊𝒅𝒆𝒐
🎵 𝑶𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕 {m.from_user.mention}**
""",
                            )
                        except Exception as ep:
                            await huehue.edit(f"`{ep}`")

