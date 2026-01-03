import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy import app
from Spy.utils.formatters import time_to_seconds

# --- GHOST-NET TERMINAL UI ---

# 1. FILE INTERCEPT (Track Selection)
def track_markup(_, videoid, user_id, channel, fplay, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text="┌─── ᴅᴇᴄʀʏᴘᴛ ᴀᴜᴅɪᴏ ───┐", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="└─── ᴅᴇᴄʀʏᴘᴛ ᴠɪᴅᴇᴏ ───┘", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="[ ᴘᴜʀɢᴇ sᴇssɪᴏɴ ]", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 2. CORE TERMINAL (Main Player with Block-Bar)
def stream_markup_timer(_, videoid, chat_id, played, dur, *args, **kwargs):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    # Unique Block-Loading Bar (Never seen before in bots)
    total_blocks = 12
    filled_blocks = int(total_blocks * umm // 100)
    bar = "█" * filled_blocks + "▒" * (total_blocks - filled_blocks)
    
    buttons = [
        [
            InlineKeyboardButton(text=f"STATUS: DECODING | {umm}%", callback_data="GetTimer")
        ],
        [
            InlineKeyboardButton(text=f"「 {played} {bar} {dur} 」", callback_data="GetTimer")
        ],
        [
            InlineKeyboardButton(text="├─ ᴇxᴇᴄᴜᴛᴇ ─┤", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="├─ sᴜsᴘᴇɴᴅ ─┤", callback_data=f"ADMIN Pause|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="├─ ᴏᴠᴇʀʀɪᴅᴇ ─┤", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="├─ ʀᴇ-sʏɴᴄ ─┤", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="[ ᴛᴇʀᴍɪɴᴀᴛᴇ ᴘʀᴏᴄᴇss ]", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="─── ɢʜᴏsᴛ ᴘᴀɴᴇʟ ───", callback_data=f"MainMarkup {videoid}|{chat_id}"),
        ],
    ]
    return buttons

# 3. ARCHIVE ACCESS (Standard Player)
def stream_markup(_, videoid, chat_id, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text="┌────── ᴅᴀᴛᴀ ʙᴀsᴇ ──────┐", callback_data=f"spy_playlist {videoid}"),
        ],
        [
            InlineKeyboardButton(text="│ ᴄᴏɴᴛʀᴏʟs │", callback_data=f"Pages Back|3|{videoid}|{chat_id}"),
            InlineKeyboardButton(text="│ ᴀᴅᴠᴀɴᴄᴇᴅ │", callback_data=f"Pages Forw|0|{videoid}|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="└────── ᴇxɪᴛ ɴᴇᴛ ──────┘", callback_data="close"),
        ],
    ]
    return buttons

# 4. DATA VAULT (Playlist Selection)
def playlist_markup(_, videoid, user_id, ptype, channel, fplay, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text="[ sᴇᴄᴜʀᴇ-ᴀᴜᴅɪᴏ-ʟɪɴᴋ ]", callback_data=f"SpyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="[ sᴇᴄᴜʀᴇ-ᴠɪᴅᴇᴏ-ʟɪɴᴋ ]", callback_data=f"SpyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="── ᴀʙᴏʀᴛ ᴀᴄᴄᴇss ──", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 5. SCANNER SLIDER
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay, *args, **kwargs):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text=f"sᴄᴀɴɴɪɴɢ: {query}...", callback_data="none"),
        ],
        [
            InlineKeyboardButton(text="[ ᴘʀᴇᴠɪᴏᴜs ]", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text="[ ɴᴇxᴛ ]", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="[ ᴄᴀɴᴄᴇʟ sᴄᴀɴ ]", callback_data=f"forceclose {query}|{user_id}"),
        ],
    ]
    return buttons

# 6. Compatibility Aliases (TypeError Safe)
def close_markup(_):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text="[ ᴅɪsᴄᴏɴɴᴇᴄᴛ ]", callback_data="close")]])

def track_markupp(*args, **kwargs): return track_markup(*args, **kwargs)
def stream_markup_timerr(*args, **kwargs): return stream_markup_timer(*args, **kwargs)
def stream_markupp(*args, **kwargs): return stream_markup(*args, **kwargs)
def playlist_markupp(*args, **kwargs): return playlist_markup(*args, **kwargs)
