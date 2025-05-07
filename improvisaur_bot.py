import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)
from dotenv import load_dotenv

load_dotenv()
from handlers import start_cmd, nomination_handler, soundtrack_handler

TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")
PORT = int(os.getenv("PORT", 5000))

if not TOKEN or not RENDER_URL:
    raise RuntimeError("TELEGRAM_TOKEN or RENDER_EXTERNAL_URL not set")

# Строим приложение
app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

app.add_handler(CommandHandler("start", start_cmd))
app.add_handler(CommandHandler("nomination", nomination_handler))
app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

# Регистрируем webhook
webhook_url = f"{RENDER_URL}/{TOKEN}"
# Сбрасываем старый webhook, если нужно
app.bot.delete_webhook(drop_pending_updates=True)
# Устанавливаем новый
import asyncio
asyncio.run(app.bot.set_webhook(webhook_url))

# Запускаем встроенный веб-сервер PTB для webhook
if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url_path=TOKEN,
        webhook_url=webhook_url,
    )
