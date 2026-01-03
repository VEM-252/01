import math
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy import app
from Spy.utils.formatters import time_to_seconds

# 1. Track Markups (Dono version daal diye hain taaki error na aaye)
def track_markup(_, videoid, user_id, channel, fplay, *args, **kwargs):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data=f"forceclose {videoid}|{user_id}")],
    ]
    return buttons

def track_markupp(_, videoid, user_id, channel, fplay, *args, **kwargs):
    return track_markup(_, videoid, user_id, channel, fplay)

# 2. Player Timer Markups
def stream_markup_timer(_, videoid, chat_id, played, dur, *args, **kwargs):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 40: bar = "◉——————————"
    elif 10 < umm < 20: bar = "—◉—————————"
    elif 20 < umm < 30: bar = "——◉————————"
    elif 30 <= umm < 40: bar = "———◉———————"
    elif 40 <= umm < 50: bar = "————◉——————"
    elif 50 <= umm < 60: bar = "——————◉————"
    elif 60 <= umm < 70: bar = "———————◉———"
    else: bar = "——————————◉"

    buttons = [
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton(text="II ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▢ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="sᴋɪᴘ ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="▷ ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [InlineKeyboardButton(text="๏ ғᴇᴀᴛᴜʀᴇs ๏", callback_data=f"MainMarkup {videoid}|{chat_id}")],
    ]
    return buttons

def stream_markup_timerr(_, videoid, chat_id, played, dur, *args, **kwargs):
    return stream_markup_timer(_, videoid, chat_id, played, dur)

# 3. Standard Stream Markups
def stream_markup(_, videoid, chat_id, *args, **kwargs):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton(text="✚ ᴘʟᴀʏʟɪsᴛ", callback_data=f"spy_playlist {videoid}"),
            InlineKeyboardButton(text="ᴄᴏɴᴛʀᴏʟs ♻", callback_data=f"Pages Back|3|{videoid}|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="📥 ᴠɪᴅᴇᴏ", callback_data=f"downloadvideo {videoid}"),
            InlineKeyboardButton(text="📥 ᴀᴜᴅɪᴏ", callback_data=f"downloadaudio {videoid}"),
        ],
        [InlineKeyboardButton(text="๏ ᴀᴅᴠᴀɴᴄᴇ ๏", callback_data=f"Pages Forw|0|{videoid}|{chat_id}")],
    ]
    return buttons

def stream_markupp(_, videoid, chat_id, *args, **kwargs):
    return stream_markup(_, videoid, chat_id)

# 4. Playlist Markups
def playlist_markup(_, videoid, user_id, ptype, channel, fplay, *args, **kwargs):
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"VIPPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"VIPPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}")],
    ]
    return buttons

def playlist_markupp(_, videoid, user_id, ptype, channel, fplay, *args, **kwargs):
    return playlist_markup(_, videoid, user_id, ptype, channel, fplay)

# 5. Panel Markups (1 se 5 tak saare add kar diye)
def panel_markup_1(_, videoid, chat_id, *args, **kwargs):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton(text="🎧 sᴜғғʟᴇ", callback_data=f"ADMIN Shuffle|{chat_id}"),
            InlineKeyboardButton(text="ʟᴏᴏᴘ ↺", callback_data=f"ADMIN Loop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="◁ 10 sᴇᴄ", callback_data=f"ADMIN 1|{chat_id}"),
            InlineKeyboardButton(text="10 sᴇᴄ ▷", callback_data=f"ADMIN 2|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="๏ ʜᴏᴍᴇ ๏", callback_data=f"Pages Back|2|{videoid}|{chat_id}"),
            InlineKeyboardButton(text="๏ ɴᴇxᴛ ๏", callback_data=f"Pages Forw|2|{videoid}|{chat_id}"),
        ],
    ]
    return buttons

def panel_markup_2(_, videoid, chat_id, *args, **kwargs):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5"),
            InlineKeyboardButton(text="🕓 1.0x", callback_data=f"SpeedUP {chat_id}|1.0"),
            InlineKeyboardButton(text="🕤 2.0x", callback_data=f"SpeedUP {chat_id}|2.0"),
        ],
        [
            InlineKeyboardButton(text="๏ ᴍᴜᴛᴇ ๏", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(text="๏ ᴜɴᴍᴜᴛᴇ ๏", callback_data=f"ADMIN Unmute|{chat_id}"),
        ],
        [InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data=f"Pages Back|1|{videoid}|{chat_id}")],
    ]
    return buttons

# 6. Slider Markups
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay, *args, **kwargs):
    query = f"{query[:20]}"
    buttons = [
        [InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]
    return buttons

def slider_markupp(_, videoid, user_id, query, query_type, channel, fplay, *args, **kwargs):
    return slider_markup(_, videoid, user_id, query, query_type, channel, fplay)

# 7. Close Markup
def close_markup(_):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close")]])

close_keyboard = close_markup
