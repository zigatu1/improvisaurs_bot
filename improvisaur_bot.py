import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)
from dotenv import load_dotenv

# Загружаем .env-переменные локально и из Render
load_dotenv()

# Импорт ваших хендлеров
from handlers import start_cmd, nomination_handler, soundtrack_handler

# Обязательные переменные
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN is not set")

RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")
if not RENDER_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL is not set")

PORT = int(os.getenv("PORT", 5000))

# Создаём Flask-приложение
app = Flask(__name__)

# Точка входа webhook: Telegram пришлёт POST-запросы сюда
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook_handler():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot=None)
    await application.process_update(update)
    return "OK", 200


if __name__ == "__main__":
    # 1) Собираем Telegram Application и регистрируем хендлеры
    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )
    application.add_handler(CommandHandler("start", start_cmd))
    application.add_handler(CommandHandler("nomination", nomination_handler))
    application.add_handler(CommandHandler("soundtrack", soundtrack_handler))

    # 2) Устанавливаем webhook в Telegram (await через asyncio.run)
    webhook_url = f"{RENDER_URL}/{TOKEN}"
    asyncio.run(application.bot.set_webhook(webhook_url))

    # 3) Запускаем Flask (в продакшене его заменит Gunicorn)
    app.run(host="0.0.0.0", port=PORT)
