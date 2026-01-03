from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def stats_buttons(_, status):
    # Agar user sudo nahi hai
    not_sudo = [
        InlineKeyboardButton(
            text="GLOBAL SPY ANALYTICS",
            callback_data="TopOverall",
        )
    ]
    # Agar user sudo/admin hai
    sudo = [
        InlineKeyboardButton(
            text="SECRET HQ STATS",
            callback_data="bot_stats_sudo",
        ),
        InlineKeyboardButton(
            text="GLOBAL ANALYTICS",
            callback_data="TopOverall",
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                InlineKeyboardButton(
                    text="ABORT MISSION",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def back_stats_buttons(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="BACK TO BASE",
                    callback_data="stats_back",
                ),
                InlineKeyboardButton(
                    text="TERMINATE",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl
