#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

# ваши хэндлеры
from handlers.start import start_cmd
from handlers.nomination import nomination_handler
from handlers.soundtrack import soundtrack_handler

load_dotenv()
TOKEN       = os.environ["TELEGRAM_TOKEN"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"]  # например "https://improvisaur-bot.onrender.com"

def error_handler(update, context):
    # просто залогируем любую ошибку
    print(f"Update {update} caused error {context.error}")

def main():
    # 1) Сборка приложения
    app = ApplicationBuilder().token(TOKEN).build()

    # 2) Удаляем старый webhook (если был) и ставим новый
    #    drop_pending_updates=True чтобы не упало кучей старых апдейтов
    app.bot.delete_webhook(drop_pending_updates=True)
    app.bot.set_webhook(f"{WEBHOOK_URL}/{TOKEN}")

    # 3) Регистрируем команды
    app.add_handler(CommandHandler("start",      start_cmd))
    app.add_handler(CommandHandler("nomination", nomination_handler))
    app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

    # 4) Общий обработчик ошибок
    app.add_error_handler(error_handler)

    # 5) Запускаем встроенный webhook-сервер
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", "8443")),
        url_path=TOKEN,
    )

if __name__ == "__main__":
    main()
