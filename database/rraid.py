from config import db

Rbun = db.rraid


async def rff(user, reason="#CHUMTLESSS"):
    await Rbun.insert_one({"user": user, "reason": reason})


async def runff(user):
    await Rbun.delete_one({"user": user})


async def rban_list():
    return [lo async for lo in Rbun.find({})]


async def ffub_info(user):
    kk = await Rbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
