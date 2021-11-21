import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Royals-Music")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Somyajeet_Mishra")
ALIVE_NAME = getenv("ALIVE_NAME", "Royals")
BOT_USERNAME = getenv("BOT_USERNAME", "RoyalsMusic_Robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Royals_Music_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Royalduniya_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RoyalsDuniya_Update")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/e94e61b2895d7b0c243bc.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/somyajeet100/Royals-Music")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/4931f471167df73b6dc49.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/e876ac3fb7baf46fa4240.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/33702daba37a4d635e734.jpg")
