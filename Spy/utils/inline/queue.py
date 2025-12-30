import config
from typing import Union
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1. Queue Markup (Jab user queue check kare)
def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    # Progress Bar UI (Timer ke liye)
    # Agar duration Unknown hai toh simple buttons
    not_dur = [
        [
            InlineKeyboardButton(text="📜 Full Queue", callback_data=f"GetQueued {CPLAY}|{videoid}"),
            InlineKeyboardButton(text="❌ Close", callback_data="close"),
        ]
    ]
    
    # Agar duration pata hai toh progress bar ke sath
    dur_markup = [
        [
            InlineKeyboardButton(
                text=f"⏱ {played} ▬●▬ {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="📜 Full Queue", callback_data=f"GetQueued {CPLAY}|{videoid}"),
            InlineKeyboardButton(text="❌ Close", callback_data="close"),
        ],
    ]
    
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur_markup)
    return upl

# 2. Queue Back Button
def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="🔙 Back", callback_data=f"queue_back_timer {CPLAY}"),
                InlineKeyboardButton(text="❌ Close", callback_data="close"),
            ]
        ]
    )
    return upl

# 3. Active Queue Markup (Buttons for all users)
def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="👤 Developer", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="🗑 Close", callback_data="close"),
        ],
    ]
    return buttons
