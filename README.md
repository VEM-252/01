# 🎵 SPY Music Bot

A fast and reliable **Telegram Music Bot** that streams audio/video in **group & channel video chats** using Pyrogram and PyTgCalls.

---

## 🚀 Features

* ⚡ Ultra‑fast streaming (audio & video)
* 🚫 No ads while playing music
* 🎛 Simple & user‑friendly commands
* 📢 Updates channel support
* 🗄 MongoDB support for broadcasting
* 🧑‍💻 Real‑time CPU, RAM & network stats
* ⏯ Pause / Resume / Skip / Seek
* 🔔 VC notifier & kick‑me protection
* 🧹 Cleaned & optimized codebase

---

## 🧩 Requirements

* Python **3.9+**
* FFmpeg
* Node.js **18 LTS** (recommended)
* MongoDB (optional but recommended)

---

## ☁️ Deploy on Heroku

### Steps

1. **Fork** this repository
2. Click the button below
3. Fill required environment variables

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

> ⚠️ Make sure all mandatory variables are added, otherwise the bot will not start.

---

## 🖥 Deploy on VPS / Local Server

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip ffmpeg git tmux -y
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs -y

# Clone repo
git clone https://github.com/lll-DEADLY-VENOM-lll/SPY_MUSIC
cd SPY_MUSIC

# Install requirements
pip3 install -U pip
pip3 install -r requirements.txt

# Setup environment
cp sample.env .env
nano .env

# Start bot
tmux new -s spymusic
bash start
# Press CTRL+B then D to detach
```

To stop the bot:

```bash
CTRL + C
```

---

## 🔐 Environment Variables

Create a `.env` file (or add on Heroku):

```env
API_ID=
API_HASH=
BOT_TOKEN=
OWNER_ID=
LOGGER_ID=
STRING_SESSION=
MONGO_DB_URI=
```

### Variable Info

* **API_ID / API_HASH** → Get from my.telegram.org
* **BOT_TOKEN** → @BotFather
* **OWNER_ID** → Your Telegram user ID
* **LOGGER_ID** → Private log group/chat ID (bot + assistant must be admin)
* **STRING_SESSION** → Pyrogram string session (assistant account)
* **MONGO_DB_URI** → MongoDB connection string

### Optional

* **UPDATES_CHANNEL** → Force users to join a channel

---

## 🎮 Bot Commands

| Command          | Description               |
| ---------------- | ------------------------- |
| `/start`         | Check bot status          |
| `/play`          | Play audio                |
| `/vplay`         | Play video                |
| `/playforce`     | Force play & stop current |
| `/pause`         | Pause stream              |
| `/resume`        | Resume stream             |
| `/skip`          | Skip track                |
| `/seek`          | Seek forward              |
| `/seekback`      | Seek backward             |
| `/stop` / `/end` | Stop streaming            |
| `/channelplay`   | Play via channel          |

---

## 📢 Channel Support

Add **bot + assistant** as **admin** in channel to stream music directly in channel video chats.

---

## 🧪 Tips

* Always add the bot to **LOGGER_ID** as admin
* Use **Node.js 18 LTS** (Node 19 is EOL)
* Use **private log group** for safety

---

## ❤️ Credits

* Developer: **Spy Music Team**
* Frameworks: Pyrogram, PyTgCalls
* Thanks to Telegram open‑source community

---

### ⭐ If you like this project, don’t forget to star the repo!#### ⭐ If you like this project, don’t forget to star the repo!
