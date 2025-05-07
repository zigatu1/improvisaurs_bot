import os
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)
from dotenv import load_dotenv

load_dotenv()

# Ваши хендлеры
from handlers import start_cmd, nomination_handler, soundtrack_handler

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN is not set")

# Создаём Flask-приложение
app = Flask(__name__)

# Точка входа webhook — прокидываем Update в Telegram Application
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook_handler():
    update = Update.de_json(request.get_json(force=True), bot=None)
    # обрабатываем через приложение, не блокируя поток
    await application.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    # Строим Telegram Application
    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    # Регистрируем хендлеры
    application.add_handler(CommandHandler("start", start_cmd))
    application.add_handler(CommandHandler("nomination", nomination_handler))
    application.add_handler(CommandHandler("soundtrack", soundtrack_handler))

    # Устанавливаем webhook на Render URL
    render_url = os.getenv("RENDER_EXTERNAL_URL")
    if not render_url:
        raise RuntimeError("RENDER_EXTERNAL_URL is not set")
    webhook_url = f"{render_url}/{TOKEN}"
    application.bot.set_webhook(webhook_url)

    # Запускаем Flask на порту
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
