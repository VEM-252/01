import asyncio
import os
import re
import requests
from typing import Union

# Invidious Instances list (for No-API/No-Cookie)
INSTANCES = [
    "https://yewtu.be",
    "https://inv.riverside.rocks",
    "https://invidious.snopyta.org",
    "https://vid.puffyan.us"
]

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message

# Agar aapko utils se functions import karne hain toh:
# from Spy.utils.database import is_on_off
# from Spy.utils.formatters import time_to_seconds

def get_instance():
    return INSTANCES[0]

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if re.search(self.regex, link):
            return True
        return False

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[entity.offset : entity.offset + entity.length]
        return None

    # --- INVIDIOUS POWERED DETAILS (No API/Cookies) ---
    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            vidid = link
        else:
            search = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link)
            vidid = search.group(1) if search else link

        instance = get_instance()
        try:
            # Fetch from Invidious instead of YTMusic API
            api_url = f"{instance}/api/v1/videos/{vidid}"
            res = requests.get(api_url, timeout=10).json()
            
            title = res.get("title", "Unknown")
            duration_sec = res.get("lengthSeconds", 0)
            duration_min = f"{duration_sec // 60:02d}:{duration_sec % 60:02d}"
            thumbnail = f"https://img.youtube.com/vi/{vidid}/maxresdefault.jpg"
            
            # Streaming Link Extraction
            audio_url = None
            for fmt in res.get("adaptiveFormats", []):
                if "audio/" in fmt.get("type", ""):
                    audio_url = fmt["url"]
                    break
            
            return title, duration_min, duration_sec, thumbnail, vidid, audio_url
        except Exception as e:
            print(f"Invidious Error: {e}")
            return None

    async def title(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        return res[0] if res else "Unknown"

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        return res[1] if res else "00:00"

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        return res[3] if res else None

    # --- VOICE CHAT PLAYING LINK ---
    async def video(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        if res and res[5]: # stream_url
            return 1, res[5]
        return 0, "No Stream Found"

    # --- SEARCH & TRACK LOGIC ---
    async def track(self, query: str, videoid: Union[bool, str] = None):
        instance = get_instance()
        try:
            if not await self.exists(query):
                search_url = f"{instance}/api/v1/search?q={query}&type=video"
                search_res = requests.get(search_url, timeout=10).json()
                if not search_res:
                    return None, None
                vidid = search_res[0]["videoId"]
            else:
                search = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", query)
                vidid = search.group(1) if search else query

            res = await self.details(vidid, videoid=True)
            if not res:
                return None, None
            
            title, duration_min, duration_sec, thumbnail, vidid, audio_url = res
            track_details = {
                "title": title,
                "link": self.base + vidid,
                "vidid": vidid,
                "duration_min": duration_min,
                "thumb": thumbnail,
                "stream_link": audio_url
            }
            return track_details, vidid
        except Exception as e:
            print(f"Track Error: {e}")
            return None, None

    # --- SEARCH SLIDER (Top 10 Results) ---
    async def slider(self, query: str, query_type: int, videoid: Union[bool, str] = None):
        instance = get_instance()
        try:
            search_url = f"{instance}/api/v1/search?q={query}&type=video"
            res = requests.get(search_url, timeout=10).json()
            result = res[query_type]
            
            title = result["title"]
            duration_sec = result.get("lengthSeconds", 0)
            duration_min = f"{duration_sec // 60:02d}:{duration_sec % 60:02d}"
            vidid = result["videoId"]
            thumbnail = f"https://img.youtube.com/vi/{vidid}/maxresdefault.jpg"
            return title, duration_min, thumbnail, vidid
        except:
            return None

    # --- DOWNLOAD LOGIC (Using yt-dlp from your requirements) ---
    async def download(self, link: str, mystic, video=None, videoid=None, songaudio=None, songvideo=None, format_id=None, title=None):
        if videoid:
            link = self.base + link
        loop = asyncio.get_running_loop()

        # yt-dlp setup (no cookies needed for most songs)
        ydl_opts = {
            "format": "bestaudio/best" if not video else "best",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
        }

        def dl():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=True)
                return ydl.prepare_filename(info)

        # Download path return
        try:
            file_path = await loop.run_in_executor(None, dl)
            return file_path, True
        except Exception as e:
            # If download fails, return the Invidious stream URL as fallback
            res = await self.details(link)
            if res:
                return res[5], True
            return None, False