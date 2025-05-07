#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

# Импортируйте именно те функции, которые реально есть в ваших файлах
from handlers.start import start_cmd
from handlers.nomination import nomination_handler
from handlers.soundtrack import soundtrack_handler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def error_handler(update, context):
    # простой лог ошибок
    print(f"Update {update} caused error {context.error}")

def main():
    # создаём приложение
    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .rate_limiter_options(None)
        .build()
    )

    # регистрируем команды
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("nomination", nomination_handler))
    app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

    # ловим все ошибки
    app.add_error_handler(error_handler)

    # запускаем long polling
    app.run_polling()

if __name__ == "__main__":
    main()
