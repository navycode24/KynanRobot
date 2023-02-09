import os
import random
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterVideo, InputMessagesFilterVoice
from KynanRobot.events import register
from KynanRobot import telethn                 


@register(pattern="^/asupan ?(.*)")
async def _(event):
    memeks = await event.reply("`Mencari Video Asupan...🔍`") 
    try:
        asupannya = [
            asupan
            async for asupan in telethn.iter_messages(
            "punyakenkan", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await telethn.download_media(kontols)
        await telethn.send_file(
            event.chat.id, 
            caption="**Nih Asupan nya Kak**", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("**Asupan nya kosong kesian..**")  


@register(pattern="^/ppanime ?(.*)")
async def _(event):
    memeks = await event.reply("`Mencari PP Anime...🔍`") 
    try:
        asupannya = [
            asupan
            async for asupan in telethn.iter_messages(
            "animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await telethn.download_media(kontols)
        await telethn.send_file(
            event.chat.id, 
            caption="**Nih pp animenya**", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("**PP animenya ga ada**")  


@register(pattern="^/wallanime ?(.*)")
async def _(event):
    memeks = await event.reply("`Mencari Wallpaper Anime...`") 
    try:
        asupannya = [
            asupan
            async for asupan in telethn.iter_messages(
            "Anime_WallpapersHD", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await telethn.download_media(kontols)
        await telethn.send_file(
            event.chat.id, 
            caption="**Nih Wallpaper Animenya**", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("**Wallpaper Animenya Kosong**")  


@register(pattern="^/ayang ?(.*)")
async def _(event):
    memeks = await event.reply("`Mencari ayang...💕`") 
    try:
        asupannya = [
            asupan
            async for asupan in telethn.iter_messages(
            "CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await telethn.download_media(kontols)
        await telethn.send_file(
            event.chat.id, 
            caption="**Nih kak ayang nya....**", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("**Kasian Jomblo...**")  
        
        
@register(pattern="^/ppcp ?(.*)")
async def _(event):
    memeks = await event.reply("`Mencari Foto Couple ...`") 
    try:
        asupannya = [
            asupan
            async for asupan in telethn.iter_messages(
            "mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await telethn.download_media(kontols)
        await telethn.send_file(
            event.chat.id, 
            caption="**Nih PP Couple Nya..**", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("**Banyakan Dosa...**")  
        
@register(pattern="^/bokep?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Bokep....**") 
    try:
        asupannya = [
            asupan
            async for asupan in telethn.iter_messages(
            "bahaninimah", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await telethn.download_media(kontols)
        await telethn.send_file(
            event.chat.id, 
            caption="`Astaghfirullah..`", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("**Coli Mulu...**")  
        
@register(pattern="^/bugil ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Foto Bugil...**") 
    try:
        asupannya = [
            asupan
            async for asupan in telethn.iter_messages(
            "durovbgst", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await telethn.download_media(kontols)
        await telethn.send_file(
            event.chat.id, 
            caption="`Insyaf lah wahai anak mude`", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("**Disuruh insyaf lu..**")  


__mod_name__ = "Asupan"

__help__ = """
ᐉ /asupan - Video Tiktok random.
ᐉ /ayang - Untuk mendapatkan ayang mu (sering digunakan oleh jomblo)
ᐉ /bugil - Coba sendiri (tobat anj)
ᐉ /bokep - Coli mulu anj
ᐉ /ppcp - Untuk Mendapatkan Mentahan PP couple Secara Random

"""
















  




