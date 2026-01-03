import asyncio
import os
import re
from typing import Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from ytmusicapi import YTMusic

from Spy.utils.formatters import time_to_seconds

# Global instance
yt_music = YTMusic()

# Cookies file check
cookies_file = "Spy/cookies.txt"
if not os.path.exists(cookies_file):
    cookies_file = None

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.listbase = "https://youtube.com/playlist?list="

    # --- Metadata Details (No Change) ---
    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        
        search = await asyncio.to_thread(yt_music.search, link, filter="songs", limit=1)
        if not search:
            return None
        
        result = search[0]
        title = result["title"]
        duration_min = result.get("duration", "04:00")
        thumbnail = result["thumbnails"][-1]["url"].split("?")[0]
        vidid = result["videoId"]
        duration_sec = int(time_to_seconds(duration_min))
        
        return title, duration_min, duration_sec, thumbnail, vidid

    # --- Direct Stream Link Generator (No Downloading) ---
    async def get_link(self, link: str, is_video=False):
        loop = asyncio.get_running_loop()
        
        # Audio ke liye m4a aur Video ke liye 720p/best link filter
        if is_video:
            fmt = "best[height<=?720][width<=?1280]/best"
        else:
            fmt = "bestaudio[ext=m4a]/bestaudio/best"

        ydl_opts = {
            "format": fmt,
            "quiet": True,
            "no_warnings": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
        }
        if cookies_file:
            ydl_opts["cookiefile"] = cookies_file

        def extract():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                return info["url"]

        return await loop.run_in_executor(None, extract)

    # --- Replaced Download Method with Streaming Logic ---
    async def download(
        self, link: str, mystic, video=None, videoid=None, **kwargs
    ) -> str:
        if videoid:
            link = self.base + link
        
        # Terminal pe download karne ki jagah direct link bhej raha hai
        try:
            direct_link = await self.get_link(link, is_video=bool(video))
            return direct_link, True # True means it's a direct stream link
        except Exception as e:
            print(f"Streaming Error: {e}")
            return None, False

    # --- Other Helper Methods ---
    async def title(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        return res[0] if res else "Unknown"

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        return res[1] if res else "00:00"

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        return res[3] if res else None

    async def track(self, link: str, videoid: Union[bool, str] = None):
        res = await self.details(link, videoid)
        if not res: return None, None
        title, dur_min, dur_sec, thumb, vidid = res
        track_details = {
            "title": title,
            "link": self.base + vidid,
            "vidid": vidid,
            "duration_min": dur_min,
            "thumb": thumb,
        }
        return track_details, vidid

    async def slider(self, link: str, query_type: int, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        search = await asyncio.to_thread(yt_music.search, link, filter="songs", limit=10)
        result = search[query_type]
        return result["title"], result.get("duration", "00:00"), result["thumbnails"][-1]["url"].split("?")[0], result["videoId"]
