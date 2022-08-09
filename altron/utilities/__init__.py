from altron.modules.database import cli
from pymongo import MongoClient
from pyrogram import Client
from config import *
from ..logger import LOGGER


_mongo_sync_ = MongoClient(MONGO_DB)

mongodb = cli.altron
pymongodb = _mongo_sync_.altron

dbb = cli["ALTRONDB"]
