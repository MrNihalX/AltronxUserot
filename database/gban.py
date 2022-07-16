from config import db


gban = db.gbam

async def gban_user(user, reason="#GBanned"):
    await gban.insert_one({"user": user, "reason": reason})


async def ungban_user(user):
    await gban.delete_one({"user": user})


async def gban_list():
    return [lo async for lo in gban.find({})]


async def gban_info(user):
    kk = await gban.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
