import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)
from dotenv import load_dotenv

# Подхватываем .env при локальной разработке или переменные окружения на Render
load_dotenv()

# Импорт ваших хендлеров
from handlers import start_cmd, nomination_handler, soundtrack_handler

# Читаем обязательные переменные
TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")
PORT = int(os.getenv("PORT", 5000))

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN не задан")
if not RENDER_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL не задан")

# Создаём Telegram-приложение
app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

# Регистрируем хендлеры
app.add_handler(CommandHandler("start", start_cmd))
app.add_handler(CommandHandler("nomination", nomination_handler))
app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

# URL для webhook
webhook_url = f"{RENDER_URL}/{TOKEN}"

# Удаляем старый webhook и устанавливаем новый
asyncio.run(app.bot.delete_webhook(drop_pending_updates=True))
asyncio.run(app.bot.set_webhook(webhook_url))

# Запуск встроенного webhook-сервера PTB
if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",     # слушать все интерфейсы
        port=PORT,            # порт, который даёт Render
        url_path=TOKEN,       # endpoint: POST /<TOKEN>
        webhook_url=webhook_url,  # полный URL для Telegram
    )
