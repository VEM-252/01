import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    TelegramServerError,
)
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded

import config
from Spy import LOGGER, YouTube, app
from Spy.misc import db
from Spy.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_lang,
    get_loop,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
    set_loop,
)
from Spy.utils.exceptions import AssistantErr
from Spy.utils.formatters import check_duration, seconds_to_min, speed_converter
from Spy.utils.inline.play import stream_markup
from Spy.utils.stream.autoclear import auto_clean
from Spy.utils.thumbnails import get_thumb
from strings import get_string

autoend = {}
counter = {}

# Speed Optimization: FFmpeg fast probing flags
FFMPEG_OPTS = "-probesize 32 -analyzeduration 0 -hide_banner -loglevel panic"

async def _clear_(chat_id):
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)


class Call(PyTgCalls):
    def __init__(self):
        self.userbot1 = Client(
            name="DilXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
        )
        self.one = PyTgCalls(self.userbot1, cache_duration=100)
        
        self.userbot2 = Client(
            name="DilXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
        )
        self.two = PyTgCalls(self.userbot2, cache_duration=100)
        
        self.userbot3 = Client(
            name="DilXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
        )
        self.three = PyTgCalls(self.userbot3, cache_duration=100)
        
        self.userbot4 = Client(
            name="DilXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
        )
        self.four = PyTgCalls(self.userbot4, cache_duration=100)
        
        self.userbot5 = Client(
            name="DilXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
        )
        self.five = PyTgCalls(self.userbot5, cache_duration=100)

    async def pause_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.pause_stream(chat_id)

    async def resume_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.resume_stream(chat_id)

    async def stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            await _clear_(chat_id)
            await assistant.leave_group_call(chat_id)
        except:
            pass

    async def stop_stream_force(self, chat_id: int):
        try:
            if config.STRING1: await self.one.leave_group_call(chat_id)
        except: pass
        try:
            if config.STRING2: await self.two.leave_group_call(chat_id)
        except: pass
        try:
            if config.STRING3: await self.three.leave_group_call(chat_id)
        except: pass
        try:
            if config.STRING4: await self.four.leave_group_call(chat_id)
        except: pass
        try:
            if config.STRING5: await self.five.leave_group_call(chat_id)
        except: pass
        try:
            await _clear_(chat_id)
        except: pass

    async def speedup_stream(self, chat_id: int, file_path, speed, playing):
        assistant = await group_assistant(self, chat_id)
        if str(speed) != str("1.0"):
            base = os.path.basename(file_path)
            chatdir = os.path.join(os.getcwd(), "playback", str(speed))
            if not os.path.isdir(chatdir):
                os.makedirs(chatdir)
            out = os.path.join(chatdir, base)
            if not os.path.isfile(out):
                vs = 1.0
                if str(speed) == str("0.5"): vs = 2.0
                if str(speed) == str("0.75"): vs = 1.35
                if str(speed) == str("1.5"): vs = 0.68
                if str(speed) == str("2.0"): vs = 0.5
                proc = await asyncio.create_subprocess_shell(
                    cmd=(f"ffmpeg -i {file_path} -filter:v setpts={vs}*PTS -filter:a atempo={speed} {out} {FFMPEG_OPTS}"),
                    stdin=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
                )
                await proc.communicate()
        else:
            out = file_path
        
        dur = await asyncio.get_event_loop().run_in_executor(None, check_duration, out)
        dur = int(dur)
        played, con_seconds = speed_converter(playing[0]["played"], speed)
        duration = seconds_to_min(dur)
        
        params = f"-ss {played} -to {duration} {FFMPEG_OPTS}"
        stream = (
            AudioVideoPiped(out, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo(), additional_ffmpeg_parameters=params)
            if playing[0]["streamtype"] == "video"
            else AudioPiped(out, audio_parameters=HighQualityAudio(), additional_ffmpeg_parameters=params)
        )
        if str(db[chat_id][0]["file"]) == str(file_path):
            await assistant.change_stream(chat_id, stream)
            db[chat_id][0]["played"] = con_seconds
            db[chat_id][0]["dur"] = duration
            db[chat_id][0]["seconds"] = dur
            db[chat_id][0]["speed"] = speed

    async def force_stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            db.get(chat_id).pop(0)
        except: pass
        await remove_active_video_chat(chat_id)
        await remove_active_chat(chat_id)
        try:
            await assistant.leave_group_call(chat_id)
        except: pass

    async def skip_stream(self, chat_id: int, link: str, video: Union[bool, str] = None, image: Union[bool, str] = None):
        assistant = await group_assistant(self, chat_id)
        if video:
            stream = AudioVideoPiped(link, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo(), additional_ffmpeg_parameters=FFMPEG_OPTS)
        else:
            stream = AudioPiped(link, audio_parameters=HighQualityAudio(), additional_ffmpeg_parameters=FFMPEG_OPTS)
        await assistant.change_stream(chat_id, stream)

    async def seek_stream(self, chat_id, file_path, to_seek, duration, mode):
        assistant = await group_assistant(self, chat_id)
        params = f"-ss {to_seek} -to {duration} {FFMPEG_OPTS}"
        stream = (
            AudioVideoPiped(file_path, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo(), additional_ffmpeg_parameters=params)
            if mode == "video"
            else AudioPiped(file_path, audio_parameters=HighQualityAudio(), additional_ffmpeg_parameters=params)
        )
        await assistant.change_stream(chat_id, stream)

    async def join_call(self, chat_id: int, original_chat_id: int, link, video: Union[bool, str] = None, image: Union[bool, str] = None):
        assistant = await group_assistant(self, chat_id)
        language = await get_lang(chat_id)
        _ = get_string(language)
        
        stream = (
            AudioVideoPiped(link, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo(), additional_ffmpeg_parameters=FFMPEG_OPTS)
            if video else AudioPiped(link, audio_parameters=HighQualityAudio(), additional_ffmpeg_parameters=FFMPEG_OPTS)
        )
            
        try:
            await assistant.join_group_call(chat_id, stream, stream_type=StreamType().pulse_stream)
        except NoActiveGroupCall: raise AssistantErr(_["call_8"])
        except AlreadyJoinedError: raise AssistantErr(_["call_9"])
        except TelegramServerError: raise AssistantErr(_["call_10"])
        
        await add_active_chat(chat_id)
        await music_on(chat_id)
        if video: await add_active_video_chat(chat_id)

    async def change_stream(self, client, chat_id):
        check = db.get(chat_id)
        loop = await get_loop(chat_id)
        try:
            if loop == 0: popped = check.pop(0)
            else:
                loop -= 1
                await set_loop(chat_id, loop)
            await auto_clean(popped)
            if not check:
                await _clear_(chat_id)
                return await client.leave_group_call(chat_id)
        except:
            await _clear_(chat_id)
            try: return await client.leave_group_call(chat_id)
            except: return
        
        queued = check[0]["file"]
        language = await get_lang(chat_id)
        _ = get_string(language)
        title, user, videoid = (check[0]["title"]).title(), check[0]["by"], check[0]["vidid"]
        original_chat_id, streamtype = check[0]["chat_id"], check[0]["streamtype"]
        video = True if str(streamtype) == "video" else False

        if "live_" in queued:
            n, link = await YouTube.video(videoid, True)
            if n == 0: return await app.send_message(original_chat_id, text=_["call_6"])
            stream = AudioVideoPiped(link, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo(), additional_ffmpeg_parameters=FFMPEG_OPTS) if video else AudioPiped(link, audio_parameters=HighQualityAudio(), additional_ffmpeg_parameters=FFMPEG_OPTS)
            await client.change_stream(chat_id, stream)
        
        elif "vid_" in queued:
            mystic = await app.send_message(original_chat_id, _["call_7"])
            file_path, direct = await YouTube.download(videoid, mystic, videoid=True, video=video)
            stream = AudioVideoPiped(file_path, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo(), additional_ffmpeg_parameters=FFMPEG_OPTS) if video else AudioPiped(file_path, audio_parameters=HighQualityAudio(), additional_ffmpeg_parameters=FFMPEG_OPTS)
            await client.change_stream(chat_id, stream)
            await mystic.delete()
        
        else:
            stream = AudioVideoPiped(queued, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo(), additional_ffmpeg_parameters=FFMPEG_OPTS) if video else AudioPiped(queued, audio_parameters=HighQualityAudio(), additional_ffmpeg_parameters=FFMPEG_OPTS)
            await client.change_stream(chat_id, stream)

    async def ping(self):
        pings = []
        clients = [self.one, self.two, self.three, self.four, self.five]
        for c in clients:
            try: pings.append(await c.ping)
            except: pass
        return str(round(sum(pings) / len(pings), 3)) if pings else "0"

    async def start(self):
        LOGGER(__name__).info("Starting PyTgCalls Clients...\n")
        if config.STRING1: await self.one.start()
        if config.STRING2: await self.two.start()
        if config.STRING3: await self.three.start()
        if config.STRING4: await self.four.start()
        if config.STRING5: await self.five.start()

    async def decorators(self):
        clients = [self.one, self.two, self.three, self.four, self.five]
        for c in clients:
            @c.on_kicked()
            @c.on_closed_voice_chat()
            @c.on_left()
            async def stream_services_handler(_, chat_id: int):
                await self.stop_stream(chat_id)

            @c.on_stream_end()
            async def stream_end_handler(client, update: Update):
                if not isinstance(update, StreamAudioEnded): return
                await self.change_stream(client, update.chat_id)

Sagar = Call()