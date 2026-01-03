import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy import app
from Spy.utils.formatters import time_to_seconds

# 1. Track Markup (Selection)
def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"
            ),
            InlineKeyboardButton(text="ᴇɴᴅ ▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴍᴏʀᴇ ๏",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
    ]
    return buttons

# 2. Player Timer Markup (The Main Screen)
def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 40:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 50 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="II ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="▢ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(
                text="sᴋɪᴘ ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷ ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ғᴇᴀᴛᴜʀᴇs ๏",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

# 3. Stream Markup (Secondary Screen)
def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✚ ᴘʟᴀʏʟɪsᴛ", callback_data=f"spy_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="ᴄᴏɴᴛʀᴏʟs ♻",
                callback_data=f"Pages Back|3|{videoid}|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📥 ᴠɪᴅᴇᴏ", callback_data=f"downloadvideo {videoid}"
            ),
            InlineKeyboardButton(
                text="📥 ᴀᴜᴅɪᴏ", callback_data=f"downloadaudio {videoid}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴀᴅᴠᴀɴᴄᴇ ๏",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

# 4. Panel Markup 1 (Shuffle & Loop)
def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎧 sᴜғғʟᴇ",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(text="ʟᴏᴏᴘ ↺", callback_data=f"ADMIN Loop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="◁ 10 sᴇᴄ",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="10 sᴇᴄ ▷",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ʜᴏᴍᴇ ๏",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="๏ ɴᴇxᴛ ๏",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

# 5. Panel Markup 2 (Speed Controls)
def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🕒 0.5x",
                callback_data=f"SpeedUP {chat_id}|0.5",
            ),
            InlineKeyboardButton(
                text="🕓 1.0x",
                callback_data=f"SpeedUP {chat_id}|1.0",
            ),
            InlineKeyboardButton(
                text="🕤 2.0x",
                callback_data=f"SpeedUP {chat_id}|2.0",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴍᴜᴛᴇ ๏",
                callback_data=f"ADMIN Mute|{chat_id}",
            ),
            InlineKeyboardButton(
                text="๏ ᴜɴᴍᴜᴛᴇ ๏",
                callback_data=f"ADMIN Unmute|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ʙᴀᴄᴋ ๏",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

# 6. Slider Markup (Search Navigation)
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

# 7. Close Markup
def close_markup(_):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close")]]
    )