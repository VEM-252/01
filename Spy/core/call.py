import asyncio
from typing import Union

from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
)
from pytgcalls.types import (
    MediaStream,
    AudioQuality,
    VideoQuality,
    Update,
    StreamEnded,
)

from Spy import LOGGER, app
from Spy.utils.database import (
    add_active_chat,
    add_active_video_chat,
    remove_active_chat,
    remove_active_video_chat,
)

# =========================
# CALL CLASS
# =========================
class Call(PyTgCalls):
    def __init__(self):
        super().__init__(app)

    async def start_audio(
        self,
        chat_id: int,
        stream_url: str,
    ):
        try:
            await self.join_group_call(
                chat_id,
                MediaStream(
                    stream_url,
                    audio_quality=AudioQuality.HIGH,
                ),
            )
            await add_active_chat(chat_id)
        except AlreadyJoinedError:
            pass
        except NoActiveGroupCall:
            raise
        except Exception as e:
            LOGGER.error(f"VC AUDIO ERROR: {e}")
            raise

    async def start_video(
        self,
        chat_id: int,
        stream_url: str,
    ):
        try:
            await self.join_group_call(
                chat_id,
                MediaStream(
                    stream_url,
                    audio_quality=AudioQuality.HIGH,
                    video_quality=VideoQuality.HD_720P,
                ),
            )
            await add_active_video_chat(chat_id)
        except AlreadyJoinedError:
            pass
        except NoActiveGroupCall:
            raise
        except Exception as e:
            LOGGER.error(f"VC VIDEO ERROR: {e}")
            raise

    async def stop(self, chat_id: int):
        try:
            await self.leave_group_call(chat_id)
        except Exception:
            pass
        await remove_active_chat(chat_id)
        await remove_active_video_chat(chat_id)


# =========================
# CALLBACKS
# =========================
@Call.on_stream_end()
async def on_stream_end_handler(client: Call, update: StreamEnded):
    chat_id = update.chat_id
    await remove_active_chat(chat_id)
    await remove_active_video_chat(chat_id)


# =========================
# INIT
# =========================
Sagar = Call()

