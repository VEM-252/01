from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy import app

# 1. First Page Menu (Modern & Clean)
def first_page(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="🛠 Admin", callback_data="help_callback hb1"),
                InlineKeyboardButton(text="👤 Auth", callback_data="help_callback hb2"),
            ],
            [
                InlineKeyboardButton(text="📣 Broadcast", callback_data="help_callback hb3"),
                InlineKeyboardButton(text="🚫 G-Ban", callback_data="help_callback hb4"),
            ],
            [
                InlineKeyboardButton(text="🎵 Music", callback_data="help_callback hb5"),
                InlineKeyboardButton(text="📽 VideoChat", callback_data="help_callback hb6"),
            ],
            [
                InlineKeyboardButton(text="📜 Playlist", callback_data="help_callback hb7"),
                InlineKeyboardButton(text="⚙️ Extra", callback_data="help_callback hb8"),
            ],
            [
                InlineKeyboardButton(text="🏠 Home", callback_data="settingsback_helper"),
                InlineKeyboardButton(text="Next ➔", callback_data="dilXaditi"),
            ],
        ]
    )
    return upl

# 2. Second Page Menu
def second_page(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="📝 Lyrics", callback_data="help_callback hb9"),
                InlineKeyboardButton(text="🎤 Ping", callback_data="help_callback hb10"),
            ],
            [
                InlineKeyboardButton(text="🤖 Start", callback_data="help_callback hb11"),
                InlineKeyboardButton(text="🛠 Sudos", callback_data="help_callback hb12"),
            ],
            [
                InlineKeyboardButton(text="🔄 Backup", callback_data="help_callback hb13"),
                InlineKeyboardButton(text="📊 Stats", callback_data="help_callback hb14"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Back", callback_data="Adisa"),
                InlineKeyboardButton(text="Close ✖️", callback_data="close"),
            ],
        ]
    )
    return upl

# 3. Help Back Button (Clean)
def help_back_markup(_):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="🔙 Go Back", callback_data="help_back")]]
    )

# 4. Private Help Panel (Bot PM)
def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(text="📖 Open Help Menu", url=f"https://t.me/{app.username}?start=help")
        ],
        [
            InlineKeyboardButton(text="✨ Support", url="https://t.me/YourSupportGroup"),
            InlineKeyboardButton(text="📢 Updates", url="https://t.me/YourChannel"),
        ]
            ]
