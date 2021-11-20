from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
      f"""✨ **Welcome !! How are uh dear [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
      ‼️ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's VC !! 😎🤘🏻**
      
      
      🤞🏻 **Uh can Find out all commands just click commands button there !!**
     
