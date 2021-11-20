import asyncio
from pytgcalls import idle
from Royalscall.Royals import call_py, bot

async def mulai_bot():
    print("[ROYALS]: STARTING BOT CLIENT")
    await bot.start()
    print("[ROYALS]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[ROYALS]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
