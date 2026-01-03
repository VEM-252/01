import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy.utils.formatters import time_to_seconds

# 1. Selection Markup (With Separate Download Rows)
def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 Play Audio", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 Play Video", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="📥 Download Audio", callback_data=f"dw {videoid}|a|{user_id}"),
        ],
        [
            InlineKeyboardButton(text="📥 Download Video", callback_data=f"dw {videoid}|v|{user_id}"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 2. Player Markup with Download Option (Compact)
def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    bar_length = 10
    filled_length = int(bar_length * umm // 100)
    bar = "━" * filled_length + "🔘" + "━" * (bar_length - filled_length - 1)
    
    buttons = [
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer")
        ],
        [
            InlineKeyboardButton(text="⏮", callback_data=f"ADMIN Prev|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="📥 Audio", callback_data=f"dw {chat_id}|a"),
            InlineKeyboardButton(text="📥 Video", callback_data=f"dw {chat_id}|v"),
            InlineKeyboardButton(text="🔄 Replay", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close Player", callback_data="close"),
        ],
    ]
    return buttons

# 3. Standard Player (Compact)
def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="⏸ Pause", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️ Resume", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭ Skip", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="📥 Get Audio", callback_data=f"dw {chat_id}|a"),
            InlineKeyboardButton(text="📥 Get Video", callback_data=f"dw {chat_id}|v"),
        ],
        [
            InlineKeyboardButton(text="⏹ Stop", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="🗑 Close", callback_data="close"),
        ],
    ]
    return buttons

# 4. Search Slider with Download (Unique)
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text="🎵 Play Audio", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎥 Play Video", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="📥 Audio", callback_data=f"dw {videoid}|a|{user_id}"),
            InlineKeyboardButton(text="📥 Video", callback_data=f"dw {videoid}|v|{user_id}"),
        ],
        [
            InlineKeyboardButton(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text="🗑 Close", callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]
    return buttons
