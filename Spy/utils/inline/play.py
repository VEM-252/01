import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy import app
from Spy.utils.formatters import time_to_seconds

# 1. Track Selection (Audio/Video)
def track_markup(_, videoid, user_id, channel, fplay, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ADD TO GROUP",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="🎵 AUDIO", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 VIDEO", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="🗑 CLOSE", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 2. Player with Progress Bar
def stream_markup_timer(_, videoid, chat_id, played, dur, *args, **kwargs):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    # Modern Progress Bar ▬●▬
    bar_length = 10
    filled_length = int(bar_length * umm // 100)
    bar = "▬" * filled_length + "●" + "▬" * (max(0, bar_length - filled_length - 1))
    
    buttons = [
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer")
        ],
        [
            InlineKeyboardButton(text="⏸ PAUSE", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏹ STOP", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="⏭ SKIP", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="▶️ RESUME", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="🔄 REPLAY", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="๏ FEATURES ๏", callback_data=f"MainMarkup {videoid}|{chat_id}"),
        ],
    ]
    return buttons

# 3. Standard Player (Controls)
def stream_markup(_, videoid, chat_id, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text="✚ PLAYLIST", callback_data=f"spy_playlist {videoid}"),
            InlineKeyboardButton(text="CONTROLS ♻", callback_data=f"Pages Back|3|{videoid}|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="📥 VIDEO", callback_data=f"downloadvideo {videoid}"),
            InlineKeyboardButton(text="📥 AUDIO", callback_data=f"downloadaudio {videoid}"),
        ],
        [
            InlineKeyboardButton(text="๏ ADVANCE ๏", callback_data=f"Pages Forw|0|{videoid}|{chat_id}"),
        ],
    ]
    return buttons

# 4. VIP Panel 1 (Shuffle, Loop, Seek)
def panel_markup_1(_, videoid, chat_id, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text="🎧 SHUFFLE", callback_data=f"ADMIN Shuffle|{chat_id}"),
            InlineKeyboardButton(text="↺ LOOP", callback_data=f"ADMIN Loop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="◁ 10 SEC", callback_data=f"ADMIN 1|{chat_id}"),
            InlineKeyboardButton(text="10 SEC ▷", callback_data=f"ADMIN 2|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="๏ HOME ๏", callback_data=f"Pages Back|2|{videoid}|{chat_id}"),
            InlineKeyboardButton(text="๏ NEXT ๏", callback_data=f"Pages Forw|2|{videoid}|{chat_id}"),
        ],
    ]
    return buttons

# 5. VIP Panel 2 (Speed & Volume)
def panel_markup_2(_, videoid, chat_id, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5"),
            InlineKeyboardButton(text="🕓 1.0x", callback_data=f"SpeedUP {chat_id}|1.0"),
            InlineKeyboardButton(text="🕤 2.0x", callback_data=f"SpeedUP {chat_id}|2.0"),
        ],
        [
            InlineKeyboardButton(text="๏ MUTE ๏", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(text="๏ UNMUTE ๏", callback_data=f"ADMIN Unmute|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="๏ BACK ๏", callback_data=f"Pages Back|1|{videoid}|{chat_id}"),
        ],
    ]
    return buttons

# 6. Playlist Selection
def playlist_markup(_, videoid, user_id, ptype, channel, fplay, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 AUDIO", callback_data=f"SpyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 VIDEO", callback_data=f"SpyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="🗑 CLOSE", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 7. Search Slider
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay, *args, **kwargs):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text="🎵 AUDIO", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 VIDEO", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="⬅️ BACK", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text="❌ CLOSE", callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="NEXT ➡️", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]
    return buttons

# 8. Close Markup
def close_markup(_):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text="🗑 CLOSE", callback_data="close")]])

# Compatibility Aliases (Error bachane ke liye)
def track_markupp(*args, **kwargs): return track_markup(*args, **kwargs)
def stream_markup_timerr(*args, **kwargs): return stream_markup_timer(*args, **kwargs)
def stream_markupp(*args, **kwargs): return stream_markup(*args, **kwargs)
def playlist_markupp(*args, **kwargs): return playlist_markup(*args, **kwargs)
