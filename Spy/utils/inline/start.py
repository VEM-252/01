from pyrogram.types import InlineKeyboardButton
import config
from Spy import app  # Using your old import structure


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💠 𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂 💠",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="✡ 𝐆𝚁𝙾𝚄𝙿 ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💠 𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂 💠",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆𝚁𝙾𝚄𝙿✨", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ🥀", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(
                text="۞ 𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ۞", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="• ʙᴏᴛ ɪɴғᴏ •", callback_data="bot_info_data"
            ),
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✿︎ ᴀᴅᴅ ᴍᴇ ✿︎", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
