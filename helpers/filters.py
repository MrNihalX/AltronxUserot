from pyrogram import filters
from typing import Union, List
from config import *

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
hero_filters = filters.me & filters.user(SUDO_USERS)

