import os
import asyncio
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated
from logging import getLogger
from Spy import app
from Spy.core.mongo import mongodb # 'db' ki jagah 'mongodb' import kiya

LOGGER = getLogger(__name__)

# Database collection define karein
wlcm = mongodb.welcome

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

def welcome_pic_create(pic, user_name, user_id, uname):
    bg_path = "Spy/assets/welcome.png" 
    font_path = "Spy/assets/font.ttf"
    
    if not os.path.exists(bg_path):
        return None

    try:
        background = Image.open(bg_path)
        pfp = Image.open(pic).convert("RGBA")
        pfp = circle(pfp)
        pfp = pfp.resize((450, 450)) 
        
        draw = ImageDraw.Draw(background)
        try:
            font = ImageFont.truetype(font_path, size=45)
        except:
            font = ImageFont.load_default()

        # Text settings
        name_text = unidecode(user_name)[:15]
        draw.text((65, 250), f'NAME : {name_text}', fill="white", font=font)
        draw.text((65, 340), f'ID : {user_id}', fill="white", font=font)
        draw.text((65, 430), f"USERNAME : @{uname}", fill="white", font=font)
        
        background.paste(pfp, (767, 133), pfp)  
        
        out_path = f"downloads/welcome_{user_id}.png"
        background.save(out_path)
        return out_path
    except Exception as e:
        LOGGER.error(f"Image creation error: {e}")
        return None

@app.on_message(filters.command("welcome") & filters.group)
async def welcome_cmd(_, message):
    # Admin check logic
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        return await message.reply_text("❌ Sirf Admins use kar sakte hain.")
    
    if len(message.command) < 2:
        return await message.reply_text("Usage: /welcome [on|off]")
    
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "on":
        await wlcm.update_one({"chat_id": message.chat.id}, {"$set": {"disabled": False}}, upsert=True)
        await message.reply_text("✅ Welcome Enabled")
    elif state == "off":
        await wlcm.update_one({"chat_id": message.chat.id}, {"$set": {"disabled": True}}, upsert=True)
        await message.reply_text("❌ Welcome Disabled")

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    if not member.new_chat_member or member.old_chat_member:
        return
    
    user = member.new_chat_member.user
    if user.is_bot: return

    chat_id = member.chat.id
    
    # Check if disabled in DB
    A = await wlcm.find_one({"chat_id": chat_id})
    if A and A.get("disabled"):
        return

    # Download PFP
    try:
        if user.photo:
            pic = await app.download_media(user.photo.big_file_id, file_name=f"pp{user.id}.png")
        else:
            pic = "Spy/assets/upic.png"
    except:
        pic = "Spy/assets/upic.png"

    loop = asyncio.get_running_loop()
    welcomeimg = await loop.run_in_executor(None, welcome_pic_create, pic, user.first_name, user.id, user.username or "N/A")

    if welcomeimg:
        try:
            await app.send_photo(
                chat_id,
                photo=welcomeimg,
                caption=f"🌟 <b>ᴡᴇʟᴄᴏᴍᴇ {user.mention}!</b>\n\n🆔 <b>ɪᴅ:</b> <code>{user.id}</code>\n👤 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{user.username or 'N/A'}",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎵 ᴀᴅᴅ ᴍᴇ 🎵", url=f"https://t.me/{app.username}?startgroup=True")]])
            )
        except Exception as e:
            LOGGER.error(f"Send photo error: {e}")
        
        # Cleanup
        try:
            if os.path.exists(welcomeimg): os.remove(welcomeimg)
            if "pp" in pic and os.path.exists(pic): os.remove(pic)
        except: pass
