#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.start import start_cmd
from handlers.nomination import nomination_handler
from handlers.soundtrack import soundtrack_handler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def error_handler(update, context):
    # Логируем ошибку в консоль
    print(f"Update {update} caused error {context.error}")

def main():
    # Строим приложение без rate_limiter_options
    app = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем хэндлеры команд
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("nomination", nomination_handler))
    app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

    # Глобальный обработчик ошибок
    app.add_error_handler(error_handler)

    # Запуск long polling
    app.run_polling()

if __name__ == "__main__":
    main()
