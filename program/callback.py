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
         f"""β¨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**
π‘ **Find out all the Bot's commands and how they work by clicking on the Β» π Commands button!**
π **Developed By [Dev](t.me/somyajeet_mishra) ππ€ Thanks!!**
π€ **To know how to use this bot, please click on the Β» β Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Group par Add karo β",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("πΊ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("πΊCommands", callback_data="cbcmds"),
                    InlineKeyboardButton("πΊOwner", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "πΊ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "πΊ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "π  Source Code", url="https://github.com/somyajeet100/Royals-Music"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **Basic Guide for using this bot:**
1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**
π **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**
π‘ **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**
β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
Β» **press the button below to read the explanation and see the list of available commands !**
β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π·π» Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("π§π» Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("π Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("π Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? here is the basic commands:
Β» /mplay (song name/link) - play music on video chat
Β» /stream (query/link) - stream the yt live/radio live music
Β» /vplay (video name/link) - play video on video chat
Β» /vstream - play live video from yt live/m3u8
Β» /playlist - show you the playlist
Β» /video (query) - download video from youtube
Β» /song (query) - download song from youtube
Β» /lyric (query) - scrap the song lyric
Β» /search (query) - search a youtube video link
Β» /ping - show the bot ping status
Β» /uptime - show the bot uptime status
Β» /alive - show the bot alive info (in group)
β‘οΈ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? here is the admin commands:
Β» /pause - pause the stream
Β» /resume - resume the stream
Β» /skip - switch to next stream
Β» /stop - stop the streaming
Β» /vmute - mute the userbot on voice chat
Β» /vunmute - unmute the userbot on voice chat
Β» /volume `1-200` - adjust the volume of music (userbot must be admin)
Β» /reload - reload bot and refresh the admin data
Β» /userbotjoin - invite the userbot to join group
Β» /userbotleave - order userbot to leave from group
β‘οΈ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? here is the sudo commands:
Β» /rmw - clean all raw files
Β» /rmd - clean all downloaded files
Β» /sysinfo - show the system information
Β» /update - update your bot to latest version
Β» /restart - restart your bot
Β» /leaveall - order userbot to leave from all group
β‘ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nΒ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"βοΈ **settings of** {query.message.chat.title}\n\nβΈ : pause stream\nβΆοΈ : resume stream\nπ : mute userbot\nπ : unmute userbot\nβΉ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("βΉ", callback_data="cbstop"),
                      InlineKeyboardButton("βΈ", callback_data="cbpause"),
                      InlineKeyboardButton("βΆοΈ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("π", callback_data="cbmute"),
                      InlineKeyboardButton("π", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("π Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("β nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
