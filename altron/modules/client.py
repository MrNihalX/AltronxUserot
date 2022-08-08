from config import *
from pyrogram import Client
from pytgcalls import PyTgCalls


#-------------------------BOT-----------------------------

bot = Client(":memory:", API_ID, API_HASH, bot_token=BOT_TOKEN)


#-------------------------CLIENTS-----------------------------

if SESSION1:
    client1 = Client(SESSION1, API_ID, API_HASH, plugins=dict(root="altron.plugins"))
    call_py1 = PyTgCalls(client, overload_quiet_mode=False)
else:
    client1 = None
    call_py1 = None

if SESSION2:
    client2 = Client(SESSION2, API_ID, API_HASH, plugins=dict(root="altron.plugins"))
    call_py2 = PyTgCalls(client2, overload_quiet_mode=False)
else:
    client2 = None
    call_py2 = None

if SESSION3:
    client3 = Client(SESSION3, API_ID, API_HASH, plugins=dict(root="altron.plugins"))
    call_py3 = PyTgCalls(client3, overload_quiet_mode=False)
else:
    client3 = None
    call_py3 = None

if SESSION4:
    client4 = Client(SESSION4, API_ID, API_HASH, plugins=dict(root="altron.plugins"))
    call_py4 = PyTgCalls(client4, overload_quiet_mode=False)
else:
    client4 = None
    call_py4 = None

if SESSION5:
    client5 = Client(SESSION5, API_ID, API_HASH, plugins=dict(root="altron.plugins"))
    call_py5 = PyTgCalls(client5, overload_quiet_mode=False)
else:
    client5 = None
    call_py5 = None


