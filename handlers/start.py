from telegram import Update
from telegram.ext import ContextTypes

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Теперь await!
    await update.message.reply_text("Привет! Я бот Импровизавры.")
