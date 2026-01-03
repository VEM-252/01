import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy.utils.formatters import time_to_seconds

# 1. Audio/Video Selection Markup (Clean & Simple)
def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 Audio", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 Video", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 2. Player Markup with Progress Bar (Modern Look)
def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    # Professional Progress Bar (▬ and ●)
    bar_length = 10
    filled_length = int(bar_length * umm // 100)
    bar = "▬" * filled_length + "●" + "▬" * (bar_length - filled_length - 1)
    
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🔄 Replay", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="❌ Close", callback_data="close"),
        ],
    ]
    return buttons

# 3. Standard Player Markup (No Timer)
def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🔄 Replay", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="⏹ Stop", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close", callback_data="close"),
        ],
    ]
    return buttons

# 4. Playlist Markup
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 Audio", callback_data=f"SagarPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 Video", callback_data=f"SagarPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 5. Search Slider Markup (Modern Navigation)
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text="🎵 Audio", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 Video", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="⬅️", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text="❌", callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="➡️", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]
    return buttonsi
