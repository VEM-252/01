import asyncio
import re
import requests
from typing import Union
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message

# List of working Invidious instances
INSTANCES = [
    "https://yewtu.be",
    "https://inv.riverside.rocks",
    "https://invidious.snopyta.org",
    "https://vid.puffyan.us",
    "https://invidious.kavin.rocks"
]

def get_instance():
    # Aap isme random logic bhi daal sakte hain, filhal pehla use kar rahe hain
    return INSTANCES[0]

async def time_to_seconds(time):
    # Agar aapka utils formatters load nahi ho raha toh ye backup hai
    try:
        parts = list(map(int, time.split(':')))
        return sum(x * 60**i for i, x in enumerate(reversed(parts)))
    except:
        return 0

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"

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

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            vidid = link
        else:
            # Link se Video ID nikaalna
            vidid = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link).group(1)

        instance = get_instance()
        try:
            # Invidious API call for details
            api_url = f"{instance}/api/v1/videos/{vidid}"
            res = requests.get(api_url, timeout=10).json()
            
            title = res.get("title", "Unknown")
            duration_sec = res.get("lengthSeconds", 0)
            duration_min = f"{duration_sec // 60:02d}:{duration_sec % 60:02d}"
            thumbnail = f"{instance}/vi/{vidid}/maxresdefault.jpg"
            
            # Streaming link nikaalna (audio only)
            audio_url = ""
            for fmt in res.get("adaptiveFormats", []):
                if "audio/" in fmt.get("type", ""):
                    audio_url = fmt["url"]
                    break
            
            return title, duration_min, duration_sec, thumbnail, vidid, audio_url
        except Exception as e:
            print(f"Error in details: {e}")
            return None

    async def track(self, query: str, videoid: Union[bool, str] = None):
        instance = get_instance()
        try:
            # Search logic if query is not a link
            if not await self.exists(query):
                search_url = f"{instance}/api/v1/search?q={query}&type=video"
                search_res = requests.get(search_url, timeout=10).json()
                if not search_res:
                    return None, None
                vidid = search_res[0]["videoId"]
            else:
                vidid = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", query).group(1)

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
                "stream_link": audio_url # Direct play ke liye
            }
            return track_details, vidid
        except Exception as e:
            print(f"Error in track: {e}")
            return None, None

    async def video(self, link: str, videoid: Union[bool, str] = None):
        # Voice Chat mein play karne ke liye direct link deta hai
        res = await self.details(link, videoid)
        if res:
            return 1, res[5] # audio_url returns here
        return 0, "Error fetching stream"

    async def download(self, link: str, mystic, video=None, videoid=None, songaudio=None, songvideo=None, title=None):
        # Invidious se direct link mil raha hai toh download ki zarurat nahi padti 
        # Lekin agar file chahiye toh hum stream URL return kar denge
        res = await self.details(link, videoid)
        if res:
            return res[5], True # Directly streaming the URL
        return None, False
