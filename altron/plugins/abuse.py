import asyncio
from pyrogram import *
from pyrogram.types import *
from altron.modules.helpers.basics import edit_or_reply
from altron.modules.helpers.command import commandpro
from altron.utilities.misc import SUDOERS


GALI = "TERII MAAA KI CHUTT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BEHEN KA ROAD PEY RAPE KARUNGA GANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO"


@Client.on_message(commandpro(["matherchod"]) & SUDOERS)
async def mother_chod(client: Client, message: Message):
    veer = await edit_or_reply(message, "🤣 Abe Ruk Ja Bete 😝 ...")
    await asyncio.sleep(2)
    await veer.edit(GALI)
    
    
__MODULE__ = "Aʙᴜsᴇ"
__HELP__ = f"""
**🥀 Hᴇʏ Hᴇʀᴇ Is Aʟʟ Aʙᴜsᴇ ✨**

**Cᴏᴍᴍᴀɴᴅs:**

`motherchod` - **Rᴇᴘʟʏ Tᴏ Aɴʏ Usᴇʀ Tᴏ Gɪᴠᴇ Mᴀxɪᴍᴜᴍ Gᴀʟɪ**
"""
