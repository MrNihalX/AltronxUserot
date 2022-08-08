import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "1020199"))
API_HASH = getenv("API_HASH", "3672885f650c19ef18d53548bb641d5f")
BOT_TOKEN = getenv("BOT_TOKEN", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB = getenv("MONGO_DB_URL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1323020756").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1323020756").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheAltronX/AltronUserbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "test")
HEROKU_MODE = getenv("HEROKU_MODE", "ENABLE")

SESSION1 = getenv("SESSION1")
SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")