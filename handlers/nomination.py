# handlers/nomination.py
from telegram import Update
from telegram.ext import ContextTypes

async def nomination_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Номинации...")
