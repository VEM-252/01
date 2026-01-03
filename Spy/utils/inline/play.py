import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy.utils.formatters import time_to_seconds

# 1. Selection Markup (Ek hi line mein sab - Sabse Chhota)
def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 ᴀᴜᴅɪᴏ", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 ᴠɪᴅᴇᴏ", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
            InlineKeyboardButton(text="❌ ᴄᴀɴᴄᴇʟ", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 2. Ultra-Compact Player (Sabse zyada compressed layout)
def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    bar_length = 8
    filled_length = int(bar_length * umm // 100)
    bar = "━" * filled_length + "🔘" + "━" * (bar_length - filled_length - 1)
    
    buttons = [
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer")
        ],
        [
            # Line 1: Main Controls (4 Buttons)
            InlineKeyboardButton(text="⏮", callback_data=f"ADMIN Prev|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            # Line 2: All Extra Controls (5 Buttons together = Tiny Size)
            # Yahan Loop, Replay, Shuffle, Stop aur Close sab merge hain
            InlineKeyboardButton(text="🔄", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="🔁", callback_data=f"ADMIN Loop|{chat_id}"),
            InlineKeyboardButton(text="🔀", callback_data=f"ADMIN Shuffle|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="🗑", callback_data="close"),
        ],
    ]
    return buttons

# 3. Mini Standard Player (No Timer)
def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="🔄", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="⏹ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return buttons

# 4. Search Slider (Navigation merge kar di)
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text="🎵 ᴀᴜᴅɪᴏ", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 ᴠɪᴅᴇᴏ", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            # Navigation aur Cancel ek hi row mein
            InlineKeyboardButton(text="⬅️", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text="❌ ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="➡️", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]
    return buttons

# 5. Playlist Markup (Compact)
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 ᴀᴜᴅɪᴏ", callback_data=f"SagarPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 ᴠɪᴅᴇᴏ", callback_data=f"SagarPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
            InlineKeyboardButton(text="🗑", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons
