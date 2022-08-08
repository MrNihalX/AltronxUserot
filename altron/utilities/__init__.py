from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pyrogram import Client
from config import *
from ..logger import LOGGER


_mongo_async_ = _mongo_client_(MONGO_DB)

mongodb = _mongo_async_.altron

dbb = _mongo_async_["ALTRONDB"]
