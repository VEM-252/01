from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Spy import app

def first_page(_):
    # 3-Column Grid with Simple Text (Like your screenshot)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="ADMIN", callback_data="help_callback hb1"),
                InlineKeyboardButton(text="AUTH", callback_data="help_callback hb2"),
                InlineKeyboardButton(text="BROADCAST", callback_data="help_callback hb3"),
            ],
            [
                InlineKeyboardButton(text="BL-CHAT", callback_data="help_callback hb4"),
                InlineKeyboardButton(text="BL-USER", callback_data="help_callback hb5"),
                InlineKeyboardButton(text="C-PLAY", callback_data="help_callback hb6"),
            ],
            [
                InlineKeyboardButton(text="G-BAN", callback_data="help_callback hb7"),
                InlineKeyboardButton(text="LOOP", callback_data="help_callback hb8"),
                InlineKeyboardButton(text="MAINTENANCE", callback_data="help_callback hb9"),
            ],
            [
                InlineKeyboardButton(text="PING", callback_data="help_callback hb10"),
                InlineKeyboardButton(text="PLAY", callback_data="help_callback hb11"),
                InlineKeyboardButton(text="SHUFFLE", callback_data="help_callback hb12"),
            ],
            [
                InlineKeyboardButton(text="SEEK", callback_data="help_callback hb13"),
                InlineKeyboardButton(text="SONG", callback_data="help_callback hb14"),
                InlineKeyboardButton(text="SPEED", callback_data="help_callback hb15"),
            ],
            [
                # Full Width Back Button
                InlineKeyboardButton(text="BACK", callback_data="settingsback_helper"),
            ],
        ]
    )
    return upl


def second_page(_):
    # Second page agar zarurat ho (Simple Font)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="STATS", callback_data="help_callback hb16"),
                InlineKeyboardButton(text="VIDEOCHAT", callback_data="help_callback hb17"),
            ],
            [
                InlineKeyboardButton(text="BACK", callback_data="Adisa"),
            ],
        ]
    )
    return upl


def help_back_markup(_):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="BACK", callback_data="settings_back_helper")]]
    )


def private_help_panel(_):
    # Bot PM buttons
    return [
        [
            InlineKeyboardButton(text="HELP MENU", url=f"https://t.me/{app.username}?start=help")
        ]
            ]
