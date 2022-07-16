from config import db

gmute = db.gmuth


async def is_gmuted(user):
    kk = await gmute.find_one({"user": user})
    if not kk:
        return False
    else:
        return True


async def gmute(user, reason="#GMuted"):
    await gmute.insert_one({"user": user, "reason": reason})


async def ungmute(user):
    await gmute.delete_one({"user": user})
