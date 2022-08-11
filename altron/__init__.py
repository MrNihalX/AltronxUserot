import asyncio
import os
import time
from os import listdir, mkdir
import heroku3
from aiohttp import ClientSession
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from rich.console import Console
from rich.table import Table
from altron.config import OWNER_ID, SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, UPSTREAM_BRANCH, UPSTREAM_REPO
from altron.modules.client import client1, client2, client3, client4, client5, bot
from altron.utilities.tasks import install_requirements

loop = asyncio.get_event_loop()
console = Console()

UPSTREAM_BRANCH = UPSTREAM_BRANCH
UPSTREAM_REPO = UPSTREAM_REPO

MOD_LOAD = []
MOD_NOLOAD = []

boottime = time.time()

aiohttpsession = ClientSession()

OWNER_ID = OWNER_ID

bot = bot
client1 = client1
client2 = client2
client3 = client3
client4 = client4
client5 = client5

BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""


async def initiate_bot():
    global OWNER_ID
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global Heroku_cli, Heroku_app
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "ALTRON..."
    )
    console.print(header)
    with console.status(
        "[magenta] Hero Music Bot Booting...",
    ) as status:
        console.print("┌ [red]Booting Up The Clients...\n")
        await bot.start()
        console.print("└ [green]Booted Bot Client")
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "cache" not in listdir():
            mkdir("cache")
        if "search" not in listdir():
            mkdir("search")
        console.print("\n┌ [red]Loading Clients Information...")
        getme = await bot.get_me()
        BOT_ID = getme.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        console.print("└ [green]Loaded Clients Information!")
        try:
            repo = Repo()
        except GitCommandError:
            console.print("┌ [red] Checking Git Updates!")
            console.print("└ [red]Git Command Error\n")
            return
        except InvalidGitRepositoryError:
            console.print("┌ [red] Checking Git Updates!")
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            repo.create_head(UPSTREAM_BRANCH, origin.refs[UPSTREAM_BRANCH])
            repo.heads[UPSTREAM_BRANCH].set_tracking_branch(
                origin.refs[UPSTREAM_BRANCH]
            )
            repo.heads[UPSTREAM_BRANCH].checkout(True)
            try:
                repo.create_remote("origin", UPSTREAM_REPO)
            except BaseException:
                pass
            nrs = repo.remote("origin")
            nrs.fetch(UPSTREAM_BRANCH)
            try:
                nrs.pull(UPSTREAM_BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
            await install_requirements(
                "pip3 install --no-cache-dir -r requirements.txt"
            )
            console.print("└ [red]ɢɪᴛ ᴄʟɪᴇɴᴛ ᴜᴘᴅᴀᴛᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ\n")


loop.run_until_complete(initiate_bot())

