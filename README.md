<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
</p>

<h1 align="center">
  ✨ ꜱᴩy x ᴍᴜꜱɪᴄ ✨
</h1>

<p align="center">
  <img src="https://graph.org/file/988002df35c2420455d64.jpg" width="300" alt="Logo">
</p>

<p align="center">
  <b>🚀 A powerful Telegram Music Bot with No YouTube API & No Cookies dependency!</b>
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python"></a>
  <a href="https://github.com/pyrogram/pyrogram"><img src="https://img.shields.io/badge/Framework-Pyrogram-red?style=for-the-badge" alt="Pyrogram"></a>
  <a href="https://t.me/NOBITA_SUPPORT"><img src="https://img.shields.io/badge/Join-Support-green?style=for-the-badge&logo=telegram" alt="Support"></a>
</p>

<hr>

## 🌟 Key Features

*   🛡️ **No YouTube API Required:** Uses Invidious instances to fetch music.
*   🍪 **No Cookies Needed:** Goodbye to "403 Forbidden" errors.
*   ⚡ **Ultra-Fast Streaming:** Lag-free audio/video playback.
*   🎨 **Aesthetic UI:** Beautifully designed inline buttons and stylish fonts.
*   🎼 **Multi-Platform:** Supports YouTube, Spotify, Apple Music, and Telegram Files.
*   📊 **Real-time Stats:** Monitor CPU, RAM, and Network usage live.
*   🔄 **Smart Queue:** Advanced queue management with progress bars.

<hr>

## 🛠 Deployment Methods

<details>
<summary><b>🚀 Deploy on Heroku (Fast)</b></summary>
<br>
1. Fork this Repository.
2. Click the button below to start deployment.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/)
</details>

<details>
<summary><b>🖥️ Host on VPS (Manual)</b></summary>
<br>

```bash
# Update System
sudo apt-get update && sudo apt-get upgrade -y

# Install Dependencies
sudo apt-get install python3-pip ffmpeg -y
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash -
sudo apt-get install nodejs -y

# Clone Repo
git clone https://github.com/NEO-O-P/AUNU_MUSIC
cd AUNU_MUSIC

# Install Requirements
pip3 install -r requirements.txt

# Start Bot
bash start
