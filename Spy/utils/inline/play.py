import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy.utils.formatters import time_to_seconds

# 1. Aesthetic Track Selection (Glass-Style)
def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="✨ Choose Audio", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎬 Choose Video", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="⊹ ᴄʟᴏsᴇ ⊹", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 2. Premium Player Markup (Progress Bar + Full Controls)
def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    # Unique Progress Bar Design (Custom Symbols)
    bar_length = 12
    filled_length = int(bar_length * umm // 100)
    # ━ is filled, ╌ is empty, 🔘 is slider
    bar = "━" * filled_length + "🔘" + "╌" * (bar_length - filled_length - 1)
    
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="⏮ ʙᴀᴄᴋ", callback_data=f"ADMIN Prev|{chat_id}"),
            InlineKeyboardButton(text="⏸ ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️ ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭ sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🔁 ʟᴏᴏᴘ", callback_data=f"ADMIN Loop|{chat_id}"),
            InlineKeyboardButton(text="⏹ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="🔀 sʜᴜғғʟᴇ", callback_data=f"ADMIN Shuffle|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="⚡ ᴜᴘᴅᴀᴛᴇs", url="https://t.me/YourChannel"), # Change this
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return buttons

# 3. Minimalist Player (No Timer)
def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🛠 ᴍᴇɴᴜ", callback_data=f"ADMIN Menu|{chat_id}"),
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return buttons

# 4. Playlist Selection (Grid Style)
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 ᴀᴜᴅɪᴏ ᴘʟᴀʏʟɪsᴛ", callback_data=f"SagarPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="🎥 ᴠɪᴅᴇᴏ ᴘʟᴀʏʟɪsᴛ", callback_data=f"SagarPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="🔙 ʙᴀᴄᴋ", callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons

# 5. Advanced Slider (Search Results)
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text="🎧 ᴘʟᴀʏ ᴀᴜᴅɪᴏ", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎬 ᴘʟᴀʏ ᴠɪᴅᴇᴏ", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text="🚀 ǫᴜɪᴄᴋ sᴇᴀʀᴄʜ", callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"),
        ],
    ]
    return buttons
