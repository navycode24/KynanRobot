import requests
from telegram import Update
from telegram.ext import CallbackContext

from KynanRobot import dispatcher
from KynanRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    truth = requests.get(f"https://api.truthordarebot.xyz/v1/truth").json()["question"]
    update.effective_message.reply_text(truth)


def dare(update: Update, context: CallbackContext):
    dare = requests.get(f"https://api.truthordarebot.xyz/v1/dare").json()["question"]
    update.effective_message.reply_text(dare)


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)


__help__ = """
*Truth & Dare*

 ᐉ /truth *:* Sends a random truth string.
 ᐉ /dare *:* Sends a random dare string.
"""

__mod_name__ = "T&D"
