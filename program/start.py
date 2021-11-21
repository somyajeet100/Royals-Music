from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
      f"""🔥 **Welcome !! How are uh dear [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
      ‼️ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's VC !! 😎🤘🏻**
      
      
      🤞🏻 **Uh can Find out all commands just click commands button there !!**
     🔊 **Developed By [Dev](t.me/somyajeet_mishra) 😎🤘 Thanks!!**
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Group par Add karo ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("🔺 Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("🔺 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("🔺 Owner", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "🔺 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🔺 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "📀 Source Code", url="https://github.com/somyajeet100/Royals-Music"
                    )
                ],
            ]
        ),
            disable_web_page_preview=True,
    )

