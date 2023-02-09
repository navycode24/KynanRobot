from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from KynanRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot, OWNER_USERNAME


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"┏━━━━━━━━━━━━━━━━━━━━┓\n"
    TEXT += f"┠➣ **ᴀᴋᴜ {BOT_NAME}.** \n"
    TEXT += f"┠➣ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
    TEXT += f"┠➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
    TEXT += f"┠➣ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n"
    TEXT += "┗━━━━━━━━━━━━━━━━━━━━┛\n\n"
    TEXT += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪsɪɴɪ ❤️**"
    BUTTON = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
        [
            InlineKeyboardButton("ᴍʏ ᴏᴡɴᴇʀ", url=f"t.me/{OWNER_USERNAME}"),
        ]
    ]
    await message.reply_photo(
        photo=START_IMG,
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )
