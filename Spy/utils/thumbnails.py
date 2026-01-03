import os
import re
import textwrap
import random
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageOps, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch
from Spy import app
from config import YOUTUBE_IMG_URL

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight), Image.Resampling.LANCZOS)

def clear(text):
    list = text.split(" ")
    title = ""
    for i in list:
        if len(title) + len(i) < 30: # Limit for better look
            title += " " + i
    return title.strip()

async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            title = re.sub("\W+", " ", title).title()
            duration = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            views = result["viewCount"]["short"]
            channel = result["channel"]["name"]

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        # 1. Background Setup
        youtube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"Spy/assets/dil.png").convert("RGBA") # User's custom asset
        
        # Heavy Blur Background
        background = changeImageSize(1280, 720, youtube)
        background = background.filter(filter=ImageFilter.GaussianBlur(radius=25))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.4) # Darken background

        # 2. Circular Artwork Creation
        logo_size = (450, 450)
        logo = youtube.convert("RGBA")
        logo = ImageOps.fit(logo, logo_size, centering=(0.5, 0.5))
        
        # Create Circle Mask
        mask = Image.new("L", logo_size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0) + logo_size, fill=255)
        
        # Apply mask and Neon Border
        circular_logo = Image.new("RGBA", logo_size, (0, 0, 0, 0))
        circular_logo.paste(logo, (0, 0), mask=mask)
        
        # Draw Neon Ring
        neon_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), 255)
        draw_ring = ImageDraw.Draw(background)
        ring_pos = [750, 135, 750+450, 135+450] # Position on right side
        draw_ring.ellipse([ring_pos[0]-10, ring_pos[1]-10, ring_pos[2]+10, ring_pos[3]+10], outline=neon_color, width=15)

        # 3. Combine Images
        background.paste(circular_logo, (750, 135), circular_logo)
        background.paste(changeImageSize(1280, 720, bg), (0, 0), mask=bg)

        # 4. Drawing Text and UI
        draw = ImageDraw.Draw(background)
        title_font = ImageFont.truetype("Spy/assets/font2.ttf", 60)
        info_font = ImageFont.truetype("Spy/assets/font2.ttf", 35)
        tag_font = ImageFont.truetype("Spy/assets/font.ttf", 30)

        # Draw Tag (SpyXDil)
        draw.text((40, 40), "S P Y  M U S I C", fill="white", font=tag_font)

        # Title wrapping
        lines = textwrap.wrap(title, width=20)
        y_text = 220
        for line in lines[:2]: # Only 2 lines for title
            draw.text((60, y_text), line, fill="white", font=title_font)
            y_text += 80

        # Channel Info
        draw.text((60, 420), f"👤 {channel[:20]}", fill="#E0E0E0", font=info_font)
        draw.text((60, 470), f"👀 {views} Views", fill="#E0E0E0", font=info_font)

        # 5. Stylized Progress Bar (Unique Feature)
        bar_x1, bar_y, bar_x2 = 60, 580, 600
        draw.line([(bar_x1, bar_y), (bar_x2, bar_y)], fill="grey", width=8) # Base bar
        draw.line([(bar_x1, bar_y), (bar_x1 + 250, bar_y)], fill=neon_color, width=8) # Progress
        draw.ellipse([bar_x1 + 245, bar_y - 10, bar_x1 + 265, bar_y + 10], fill="white") # Slider dot

        # Duration Text
        draw.text((60, 600), "00:00", fill="white", font=info_font)
        draw.text((510, 600), f"{duration}", fill="white", font=info_font)

        # Final cleanup and save
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
            
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"

    except Exception as e:
        print(f"Thumbnail Error: {e}")
        return YOUTUBE_IMG_URL
