#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.start import start_cmd
from handlers.nomination import nomination_handler
from handlers.soundtrack import soundtrack_handler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
# Render прокидывает порт в переменную PORT
PORT = int(os.getenv("PORT", "8443"))

async def error_handler(update, context):
    # Просто логируем ошибку в stdout
    print(f"Update {update} caused error {context.error}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Удаляем возможный старый webhook, чтобы не было конфликтов
    app.bot.delete_webhook(drop_pending_updates=True)

    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("nomination", nomination_handler))
    app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

    # Глобальный обработчик ошибок
    app.add_error_handler(error_handler)

    # Запускаем long polling + health-endpoint на нужном порту
    app.run_polling(
        health_server=True,
        health_server_port=PORT,
        health_server_bind_address="0.0.0.0",
    )

if __name__ == "__main__":
    main()
