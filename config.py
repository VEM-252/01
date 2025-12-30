import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# --- BASIC CONFIG ---
API_ID = int(getenv("API_ID", "25610347"))
API_HASH = getenv("API_HASH", "c421be09ee9b9af3d13dbf9abb03483c")
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# --- LIMITS & LOGGER ---
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1003034048678"))
OWNER_ID = int(getenv("OWNER_ID", "7967418569"))
BOT_USERNAME = getenv("BOT_USERNAME" , "aaru_music_rbot")

# --- EXTRA SUDO USERS (Jo bot ko control kar sakein) ---
# Yahan un logo ki ID dalein jo admin wale buttons use kar sakein
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7967418569").split()))

# --- CUSTOMIZATION ---
COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lll-DEADLY-VENOM-lll/AARU_MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "SPY")
GIT_TOKEN = getenv("GIT_TOKEN", None)


SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_deadly_venom")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NOBITA_SUPPORT")

# --- SESSIONS ---
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)

# ==========================================
#      EXTRA PLUGINS & POWER FUNCTIONS 🛠
# ==========================================

# 1. Maintenance Mode (Sirf Sudos bot use kar payenge)
MAINTENANCE = getenv("MAINTENANCE", "False")

# 2. Auto G-Cast (Bot khud hi groups mein updates bhejega)
AUTO_GCAST = getenv("AUTO_GCAST", "True")
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "✨ Hello! Join our support chat for more updates.")

# 3. Private Bot Mode (Sirf authorized chats mein chalega)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")

# 4. Auto Leaving (Assistant group chhod dega jab music khatam ho)
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

# 5. Clean Mode (Purane messages automatically delete karega)
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

# 6. Play Mode (Direct Play ya Inline Search)
# Options: "Direct" or "Inline"
PLAY_MODE = getenv("PLAY_MODE", "Direct")

# ==========================================
#      AESTHETIC IMAGES & THUMBNAILS
# ==========================================

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/988002df35c2420455d64.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/7fbabc4b791cebc67a013-1521e1b3ec530f5fe1.jpg")
YOUTUBE_IMG_URL = "https://graph.org/file/988002df35c2420455d64.jpg"
STATS_IMG_URL = "https://graph.org/file/0c961e57c66432644788c.jpg"

# ==========================================

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validation
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
