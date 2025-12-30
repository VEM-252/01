# ──「 sᴘʏ ✘ ᴍᴜsɪᴄ 」──

"""
Telegram Music Bot
A bot to play music in Telegram video chats.
"""

# 🍁 About This Bot
about_bot = "This repository helps you deploy a Telegram Music Bot that streams songs directly into video chats."

# ♢ How to make your own
def deploy_on_heroku():
    steps = [
        "Fork this repository",
        "Click the Deploy button and follow the steps",
        "Set up environment variables after deployment"
    ]
    return steps

def host_locally_vps():
    commands = [
        "sudo apt-get install python3-pip ffmpeg -y",
        "sudo pip3 install -U pip",
        "curl -fssL https://deb.nodesource.com/setup_19.x | sudo -E bash -",
        "sudo apt-get install nodejs -y && npm i -g npm",
        "git clone https://github.com/stkeditz/SpyMusic && cd SpyMusic",
        "pip3 install -U -r requirements.txt",
        "bash setup",
        "sudo apt install tmux",
        "tmux kill-session",
        "tmux",
        "bash start",
        "# Detach with Ctrl+b then d"
    ]
    return commands

# 🔑 Vars and Details
mandatory_vars = {
    "API_ID": "Get from my.telegram.org",
    "API_HASH": "Get from my.telegram.org",
    "BOT_TOKEN": "Obtain from @BotFather",
    "OWNER_ID": "Your Telegram User ID",
    "LOGGER_ID": "Chat ID for logs (bot must be admin)",
    "STRING_SESSION": "String session for assistant account",
    "MONGO_DB_URI": "MongoDB URI for database"
}

optional_vars = {
    "UPDATES_CHANNEL": "Public channel username (bot must be admin there)"
}

# ⚡ Features
features = [
    "Superfast download & streaming",
    "No ads while playing songs",
    "User-friendly interface",
    "MongoDB database support for broadcasting",
    "Real-time CPU, RAM, and internet usage stats",
    "Ping check",
    "Kickme & Video Chat notifier",
    "Channel support",
    "Clean, optimized codebase"
]

# 🎮 Commands
commands = {
    "/start": "Check if bot is alive",
    "/play or /vplay or /cplay": "Play requested track in video chat",
    "/playforce": "Force play (stop current stream and start new one)",
    "/channelplay [username|id]": "Connect channel to group for streaming",
    "/seek": "Seek stream to given duration",
    "/seekback": "Seek backward",
    "/pause": "Pause current stream",
    "/resume": "Resume paused stream",
    "/skip": "Skip current track and play next in queue",
    "/end or /stop": "End stream and clear queue",
    "/reboot": "Restart bot instantly (in logger chat)"
}

# 📡 Channel Support
channel_support = "Add both the bot and assistant as Admins in your channel to enable channel streaming."

# 🙌 Credits
credits = [
    "stkeditz (https://github.com/stkeditz)",
    "Telegram Contact (https://t.me/dil_sagar_121)",
    "Everyone who contributed to this journey 🚀"
]

if __name__ == "__main__":
    print("──「 sᴘʏ ✘ ᴍᴜsɪᴄ 」──")
    print("\nAbout:", about_bot)
    print("\nFeatures:")
    for f in features:
        print("-", f)
    print("\nCommands:")
    for cmd, desc in commands.items():
        print(f"{cmd}: {desc}")
    print("\nCredits:")
    for c in credits:
        print("-", c)
