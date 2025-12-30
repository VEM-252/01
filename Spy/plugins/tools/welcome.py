import os
import asyncio
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated
from logging import getLogger
from Spy import app  # Aapne screenshot mein 'Spy' folder dikhaya hai
from Spy.utils.database import db

LOGGER = getLogger(__name__)
wlcm = db.welcome

class Temp:
    MELCOW = {}

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcome_pic_create(pic, user_name, chat_title, user_id, uname):
    # PATHS - Inhe check karein ki ye files folder mein hain
    bg_path = "Spy/assets/welcome.png" 
    font_path = "Spy/assets/font.ttf"
    
    if not os.path.exists(bg_path):
        return None

    background = Image.open(bg_path)
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((450, 450)) 
    
    draw = ImageDraw.Draw(background)
    try:
        font = ImageFont.truetype(font_path, size=45)
    except:
        font = ImageFont.load_default()

    # Text Drawing
    draw.text((65, 250), f'NAME : {unidecode(user_name)[:15]}', fill="white", font=font)
    draw.text((65, 340), f'ID : {user_id}', fill="white", font=font)
    draw.text((65, 430), f"USERNAME : @{uname}", fill="white", font=font)
    
    background.paste(pfp, (767, 133), pfp)  
    
    out_path = f"downloads/welcome_{user_id}.png"
    background.save(out_path)
    return out_path

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    if not member.new_chat_member or member.old_chat_member:
        return
    
    chat_id = member.chat.id
    # Database check
    A = await wlcm.find_one({"chat_id": chat_id})
    if A and A.get("disabled"):
        return

    user = member.new_chat_member.user
    if user.is_bot: return

    try:
        if user.photo:
            pic = await app.download_media(user.photo.big_file_id, file_name=f"pp{user.id}.png")
        else:
            pic = "Spy/assets/upic.png"
    except:
        pic = "Spy/assets/upic.png"

    loop = asyncio.get_running_loop()
    welcomeimg = await loop.run_in_executor(None, welcome_pic_create, pic, user.first_name, member.chat.title, user.id, user.username or "N/A")

    if welcomeimg:
        try:
            await app.send_photo(
                chat_id,
                photo=welcomeimg,
                caption=f"🌟 <b>Welcome {user.mention}!</b>\n\n🆔 <b>ID:</b> <code>{user.id}</code>\n👤 <b>User:</b> @{user.username}",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎵 Add Me 🎵", url=f"https://t.me/{app.username}?startgroup=True")]])
            )
            os.remove(welcomeimg)
        except Exception as e:
            LOGGER.error(e)
