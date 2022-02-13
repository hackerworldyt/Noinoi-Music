import os
from os import getenv
from dotenv import load_dotenv
from Noinoi.DREAMS.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ɴᴏɪ ɴᴏɪ ᴍᴜsɪᴄ 🌸")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/88b954d019f1879737575.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/88b954d019f1879737575.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/88b954d019f1879737575.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/88b954d019f1879737575.jpg")
OWNER_NAME = getenv("OWNER_NAME", "iam_your_heart4")
ALIVE_NAME = getenv("ALIVE_NAME", "ᴄғᴄ ᴍᴜsɪᴄ 🔥")
BOT_USERNAME = getenv("BOT_USERNAME", "broken_mr_z_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BROKEN Mr z Music")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "iam_your_heart4")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "iam_your_heart4")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/88b954d019f1879737575.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1800"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Baziibro/NoinoiMusicBot")
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
