import os
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv

# Ваши хендлеры
from handlers import start_cmd, nomination_handler, soundtrack_handler

# Загружаем .env
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")
PORT = int(os.getenv("PORT", 5000))

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN не задан")
if not RENDER_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL не задан")

# Строим Application
application = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

# Регистрируем хендлеры
application.add_handler(CommandHandler("start", start_cmd))
application.add_handler(CommandHandler("nomination", nomination_handler))
application.add_handler(CommandHandler("soundtrack", soundtrack_handler))

# Генерим URL для Telegram
webhook_url = f"{RENDER_URL}/{TOKEN}"

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",        # все интерфейсы
        port=PORT,               # порт из Render
        url_path=TOKEN,          # endpoint: POST /<TOKEN>
        webhook_url=webhook_url, # полный URL для регистрации
        drop_pending_updates=True,
    )
