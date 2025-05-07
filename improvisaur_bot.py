#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

# Ваши асинхронные хендлеры
from handlers.start import start_cmd
from handlers.nomination import nomination_handler
from handlers.soundtrack import soundtrack_handler

load_dotenv()
TOKEN       = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g. "https://improvisaurs-bot.onrender.com"
PORT        = int(os.getenv("PORT", "8443"))

if not TOKEN or not WEBHOOK_URL:
    raise RuntimeError("TELEGRAM_TOKEN и WEBHOOK_URL должны быть заданы в Environment")

# Собираем приложение
app = ApplicationBuilder().token(TOKEN).build()

# Регистрируем команды
app.add_handler(CommandHandler("start",      start_cmd))
app.add_handler(CommandHandler("nomination", nomination_handler))
app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

# Запускаем встроенный webhook-сервер
if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,                     # Telegram шлёт POST на /<TOKEN>
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}", 
        drop_pending_updates=True,          # сбросить старые апдейты
    )
