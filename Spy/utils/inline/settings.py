from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Spy Music Settings Markup
def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text="AUDIO SETTINGS", callback_data="AQ"),
            InlineKeyboardButton(text="VIDEO SETTINGS", callback_data="VQ"),
        ],
        [
            InlineKeyboardButton(text="AUTH AGENTS", callback_data="AU"),
            InlineKeyboardButton(text="LANGUAGE", callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text="PLAY MODE", callback_data="PM"),
            InlineKeyboardButton(text="CLEAN MODE", callback_data="CM"),
        ],
        [
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ]
    return buttons


def audio_quality_markup(
    _,
    LOW: Union[bool, str] = None,
    MEDIUM: Union[bool, str] = None,
    HIGH: Union[bool, str] = None,
    STUDIO: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="LOW [SELECTED]" if LOW == True else "LOW",
                callback_data="LOW",
            ),
            InlineKeyboardButton(
                text="MEDIUM [SELECTED]" if MEDIUM == True else "MEDIUM",
                callback_data="MEDIUM",
            ),
        ],
        [
            InlineKeyboardButton(
                text="HIGH [SELECTED]" if HIGH == True else "HIGH",
                callback_data="HIGH",
            ),
            InlineKeyboardButton(
                text="STUDIO [SELECTED]" if STUDIO == True else "STUDIO",
                callback_data="STUDIO",
            ),
        ],
        [
            InlineKeyboardButton(
                text="BACK",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ]
    return buttons


def video_quality_markup(
    _,
    SD_360p: Union[bool, str] = None,
    SD_480p: Union[bool, str] = None,
    HD_720p: Union[bool, str] = None,
    FHD_1080p: Union[bool, str] = None,
    QHD_2K: Union[bool, str] = None,
    UHD_4K: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="360p [SELECTED]" if SD_360p == True else "360p",
                callback_data="SD_360p",
            ),
            InlineKeyboardButton(
                text="480p [SELECTED]" if SD_480p == True else "480p",
                callback_data="SD_480p",
            ),
        ],
        [
            InlineKeyboardButton(
                text="720p [SELECTED]" if HD_720p == True else "720p",
                callback_data="HD_720p",
            ),
            InlineKeyboardButton(
                text="1080p [SELECTED]" if FHD_1080p == True else "1080p",
                callback_data="FHD_1080p",
            ),
        ],
        [
            InlineKeyboardButton(
                text="2K [SELECTED]" if QHD_2K == True else "2K",
                callback_data="QHD_2K",
            ),
            InlineKeyboardButton(
                text="4K [SELECTED]" if UHD_4K == True else "4K",
                callback_data="UHD_4K",
            ),
        ],
        [
            InlineKeyboardButton(
                text="BACK",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ]
    return buttons


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(text="CLEAN MODE INFO", callback_data="CMANSWER"),
            InlineKeyboardButton(
                text="ENABLED" if status == True else "DISABLED",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text="COMMAND DELETE", callback_data="COMMANDANSWER"),
            InlineKeyboardButton(
                text="ENABLED" if dels == True else "DISABLED",
                callback_data="COMMANDELMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="BACK",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="AUTH INFO", callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text="ENABLED" if status == True else "DISABLED",
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(text="AUTHORIZED AGENTS LIST", callback_data="AUTHLIST"),
        ],
        [
            InlineKeyboardButton(
                text="BACK",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(text="SEARCH MODE", callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text="DIRECT" if Direct == True else "INLINE",
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="CHANNEL PLAY", callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text="ENABLED" if Group == True else "DISABLED",
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="PLAY TYPE", callback_data="PLAYTYPEANSWER"),
            InlineKeyboardButton(
                text="ADMINS ONLY" if Playtype == True else "EVERYONE",
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="BACK",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ]
    return buttons

# Yeh function aapka error theek karega (Missing Function)
def vote_mode_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="VOTING INFO", callback_data="VOTEANSWER"),
            InlineKeyboardButton(
                text="ENABLED" if status == True else "DISABLED",
                callback_data="VOTEMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="BACK",
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)
