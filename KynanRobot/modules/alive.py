from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver
import os
import re
from KynanRobot.events import register
from KynanRobot import telethn as tbot
from KynanRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot


PHOTO = "https://telegra.ph//file/b5fa050775543872ae0ec.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴀᴋᴜ ˹ҡʏɴλɴ ꭙ ꝛᴏʙᴏᴛ˼༗.** \n\n"
  TEXT += "๏ **ᴀᴋᴜ ʜɪᴅᴜᴘ** \n\n"
  TEXT += f"๏ **ᴍʏ ᴏᴡɴᴇʀ : [↻˹ҡʏɴλɴ˼༗](https://t.me/Riizzvbss)** \n\n"
  TEXT += f"๏ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"๏ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"๏ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪsɪɴɪ ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/KynanUserbot?start=help"), Button.url("ᴅᴏɴᴀsɪ ​❤️", "https://graph.org/file/2982a27fe0e1500bf5b17.jpg")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
