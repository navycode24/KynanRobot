import os

from gtts import gTTS
from gtts import gTTSError
from telethon import *
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *

from KynanRobot import *

from KynanRobot import telethn as tbot
from KynanRobot.events import register


@register(pattern="^/tts (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply(
            "Sintaks\nFormat . Tidak Valid `/tts lang | teks`\n misalnya: `/tts en | halo`"
        )
        return
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld="com", lang=lan)
        tts.save("k.mp3")
    except AssertionError:
        await event.reply(
            "Teksnya kosong.\n"
            "Tidak ada yang tersisa untuk dibicarakan setelah pra-presesi, "
            "tokenizing dan pembersihan."
        )
        return
    except ValueError:
        await event.reply("Bahasa tidak didukung.")
        return
    except RuntimeError:
        await event.reply("Terjadi kesalahan saat memuat kamus bahasa.")
        return
    except gTTSError:
        await event.reply("Kesalahan dalam permintaan API Google Text-to-Speech !")
        return
    with open("k.mp3", "r"):
        await tbot.send_file(
            event.chat_id, "k.mp3", voice_note=True, reply_to=reply_to_id
        )
        os.remove("k.mp3")
