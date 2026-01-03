import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# --- BASIC CONFIGS ---
API_ID = int(getenv("API_ID", "25610347"))
API_HASH = getenv("API_HASH", "c421be09ee9b9af3d13dbf9abb03483c")
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# --- DURATION & LIMITS ---
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))

# --- OWNER & LOGS ---
LOGGER_ID = int(getenv("LOGGER_ID", "-1003034048678"))
OWNER_ID = int(getenv("OWNER_ID", "7967418569"))
# Extra: Sudo users list (Management ke liye)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7967418569").split())) 

# --- BOT DETAILS ---
BOT_USERNAME = getenv("BOT_USERNAME" , "aaru_music_rbot")
COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# --- REPO & SUPPORT ---
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lll-DEADLY-VENOM-lll/SPY_MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "SPY")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_deadly_venom")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NOBITA_SUPPORT")

# --- EXTRA PLUGINS CONFIG (Naye Features) ---
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "500"))
# Maintenance Mode (Bot ko temporary off karne ke liye)
MAINTENANCE = getenv("MAINTENANCE", None) 
# Private Bot Mode (Sirf allow kiye gaye groups mein chalega)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# --- EXTERNAL API KEYS ---
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# --- CLEANMODE ---
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

# --- MULTI-ASSISTANT SESSIONS ---
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# --- FILTERS & DATA ---
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

# --- IMAGES & UI ---
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/7fbabc4b791cebc67a013-1521e1b3ec530f5fe1.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/df9f00159effce45fa2e2-f1c40978b063a5462a.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/75d4a43a76f4272d117d1-a3b25f8c9777d7de2a.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4a7c28726502e24ea0fe0.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/810f874873e1565cf5732.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/16d7dd76f4ce8b8b01fdf.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/53f1a295e172d39eaa39d.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = URL = "https://graph.org/file/f8ca1d42d835ac41ad57a-b14ce33d2ae40d299c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"

# --- UTILS ---
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

# --- VALIDATION ---
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - SUPPORT_CHANNEL url is wrong.")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - SUPPORT_CHAT url is wrong.")
