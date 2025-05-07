#!/usr/bin/env python3
# coding: utf-8

import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Импортируем ваши асинхронные хэндлеры
from handlers.start import start_cmd
from handlers.nomination import nomination_handler
from handlers.soundtrack import soundtrack_handler

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)

async def health_check(_: Update, __: ContextTypes.DEFAULT_TYPE):
    return  # просто “здоровый” хэндлер, если нужно

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        logging.error("Не задана переменная TELEGRAM_TOKEN")
        return

    # Собираем приложение
    app = (
        ApplicationBuilder()
        .token(token)
        .concurrent_updates(True)
        .build()
    )

    # Регистрируем хэндлеры
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("nomination", nomination_handler))
    app.add_handler(CommandHandler("soundtrack", soundtrack_handler))
    # (добавьте остальные)

    # Запускаем long polling
    logging.info("Запускаем long polling…")
    app.run_polling()

if __name__ == "__main__":
    main()
