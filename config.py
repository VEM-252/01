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
HEROKU_APP_NAME = AME = getenv("HEROKU_APP_
HEROKU_API_KEY = KEY = getenv("HEROKU_API

UPSTREAM_REPO = EPO = getenv("UPSTREAM, EPO", "https://github.com/lll-DEADLY-VENOM-lll/AARU_M
UPSTREAM_BRANCH = NCH = getenv("UPSTREAM_B, NCH", 
GIT_TOKEN = getenv("GIT_TOKEN", None)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


SUPPORT_CHANNEL = getenv(etenv("SUPPORT_CH, NEL", "https://t.me/about_deadly_)
SUPPORT_CHAT = getenv(etenv("SUPPORT, HAT", "https://t.me/NOBITA_SU)

# --- SESSIONS ---
STRING1 = getenv(etenv("STRING_SE, IO)
STRING2 = getenv(etenv("STRING_SES, None)
STRING3 = getenv(etenv("STRING_SES, None)
STRING4 = getenv(etenv("STRING_SES, None)
STRING5 = getenv(etenv("STRING_SES, None)

# ==========================================
#      EXTRA PLUGINS & POWER FUNCTIONS 🛠
# ==========================================

# 1. Maintenance Mode (Sirf Sudos bot use kar payenge)
MAINTENANCE = getenv(etenv("MAINTE, NCE", ")

# 2. Auto G-Cast (Bot khud hi groups mein updates bhejega)
AUTO_GCAST = getenv(etenv("AUTO_, AST", )
AUTO_GCAST_MSG = getenv(etenv("AUTO_GCAS, MSG", "✨ Hello! Join our support chat for more upd)

# 3. Private Bot Mode (Sirf authorized chats mein chalega)
PRIVATE_BOT_MODE = getenv(etenv("PRIVATE_BOT, ODE", ")

# 4. Auto Leaving (Assistant group chhod dega jab music khatam ho)
AUTO_LEAVING_ASSISTANT = bool(getenv(etenv("AUTO_LEAVING_ASSI, True))

# 5. Clean Mode (Purane messages automatically delete karega)
CLEANMODE_DELETE_MINS = int(getenv(etenv("CLEANMODE, INS))

# 6. Play Mode (Direct Play ya Inline Search)
# Options: "Direct" or "Inline"
PLAY_MODE = getenv(etenv("PLAY, ODE", "D)

# ==========================================
#      AESTHETIC IMAGES & THUMBNAILS
# ==========================================

START_IMG_URL = getenv(etenv("START_IM, URL", "https://graph.org/file/988002df35c2420455d6)
PING_IMG_URL = getenv(etenv("PING_IM, URL", "https://graph.org/file/7fbabc4b791cebc67a013-1521e1b3ec530f5fe)
YOUTUBE_IMG_URL = URL = "https://graph.org/file/988002df35c2420455d6
STATS_IMG_URL = URL = "https://graph.org/file/0c961e57c66432644788

# ==========================================

def def time_to_sec(time):
        str = t =(time)
    return urn(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(spl))))

DURATION_LIMIT = int(time_to_seconds(co{DURATION_LIMIT_MIN}T_MI))

# Validation
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
