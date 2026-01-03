import asyncio, httpx, yt_dlp, os
import glob, re, random, json, requests

from typing import Union
from pyrogram.types import Message
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from pyrogram.enums import MessageEntityType
from concurrent.futures import ThreadPoolExecutor
from youtubesearchpython.__future__ import VideosSearch, CustomSearch

from Spy.utils.database import is_on_off
from Spy.utils.formatters import time_to_seconds


# -------------------- COOKIES --------------------
def cookie_txt_file():
    try:
        folder_path = f"{os.getcwd()}/cookies"
        filename = f"{os.getcwd()}/cookies/logs.csv"
        txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
        if not txt_files:
            return None
        cookie_txt_file = random.choice(txt_files)
        with open(filename, "a") as file:
            file.write(f"Choosen File : {cookie_txt_file}\n")
        return f"cookies/{os.path.basename(cookie_txt_file)}"
    except Exception:
        return None


# -------------------- SHELL --------------------
async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in errorz.decode().lower():
            return out.decode()
        return errorz.decode()
    return out.decode()


# -------------------- API STREAM --------------------
async def get_stream_url(query, video=False):
    apis = [
        {
            "url": "http://194.182.77.199:1470/youtube",
            "key": "VNI0X_oY6oVn7svGENco2",
        }
    ]

    async with httpx.AsyncClient(timeout=60) as client:
        for api in apis:
            try:
                params = {
                    "query": query,
                    "video": video,
                    "api_key": api["key"],
                }
                r = await client.get(api["url"], params=params)
                if r.status_code == 200:
                    data = r.json()
                    if data.get("stream_url"):
                        return data["stream_url"]
            except Exception:
                continue
    return ""


# -------------------- YOUTUBE CLASS --------------------
class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.listbase = "https://youtube.com/playlist?list="

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def url(self, message: Message) -> Union[str, None]:
        messages = [message]
        if message.reply_to_message:
            messages.append(message.reply_to_message)

        for msg in messages:
            if msg.entities:
                for ent in msg.entities:
                    if ent.type == MessageEntityType.URL:
                        return msg.text[ent.offset : ent.offset + ent.length]
            if msg.caption_entities:
                for ent in msg.caption_entities:
                    if ent.type == MessageEntityType.TEXT_LINK:
                        return ent.url
        return None

    async def details(self, link: str, videoid=False):
        if videoid:
            link = self.base + link
        link = link.split("&")[0]
        r = VideosSearch(link, limit=1)
        data = (await r.next())["result"][0]
        dur = data["duration"]
        return (
            data["title"],
            dur,
            int(time_to_seconds(dur)) if dur else 0,
            data["thumbnails"][0]["url"].split("?")[0],
            data["id"],
        )

    async def video(self, link: str, videoid=False):
        if videoid:
            link = self.base + link
        return await get_stream_url(link, True)

    async def playlist(self, link, limit, user_id, videoid=False):
        if videoid:
            link = self.listbase + link
        link = link.split("&")[0]
        cmd = (
            f'yt-dlp --js-runtime deno -i --get-id '
            f'--flat-playlist --playlist-end {limit} {link}'
        )
        data = await shell_cmd(cmd)
        return [x for x in data.split("\n") if x]

    async def formats(self, link: str, videoid=False):
        if videoid:
            link = self.base + link
        link = link.split("&")[0]

        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
            "js_runtimes": ["deno"],  # ✅ FIX
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=False)
            out = []
            for f in info.get("formats", []):
                if "dash" not in str(f.get("format", "")).lower():
                    out.append(
                        {
                            "format": f.get("format"),
                            "filesize": f.get("filesize"),
                            "format_id": f.get("format_id"),
                            "ext": f.get("ext"),
                            "format_note": f.get("format_note"),
                            "yturl": link,
                        }
                    )
        return out, link

    async def download(self, link: str, mystic, video=False):
        loop = asyncio.get_running_loop()

        ydl_opts = {
            "format": "bestaudio/best" if not video else "bestvideo+bestaudio",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "geo_bypass": True,
            "skip_download": False,
            "js_runtimes": ["deno"],  # ✅ FIX
        }

        def _dl():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=True)
                return os.path.join("downloads", f"{info['id']}.{info['ext']}")

        return await loop.run_in_executor(None, _dl)

