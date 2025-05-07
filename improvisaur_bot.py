#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

# импорт ваших хэндлеров
from handlers.start import start_cmd
from handlers.nomination import nomination_handler
from handlers.soundtrack import soundtrack_handler

load_dotenv()
TOKEN       = os.environ["TELEGRAM_TOKEN"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"]  # например "https://improvisaur-bot.onrender.com"

def error_handler(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    # 1) Создаём приложение с поддержкой вебхуков
    app = ApplicationBuilder() \
        .token(TOKEN) \
        .webhook_url(f"{WEBHOOK_URL}/{TOKEN}") \
        .build()

    # 2) Регистрируем команды
    app.add_handler(CommandHandler("start",      start_cmd))
    app.add_handler(CommandHandler("nomination", nomination_handler))
    app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

    # 3) Общий обработчик ошибок
    app.add_error_handler(error_handler)

    # 4) Поднимаем HTTP-сервер на $PORT и путь /<TOKEN>
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", "8443")),
        url_path=TOKEN,
    )

if __name__ == "__main__":
    main()
