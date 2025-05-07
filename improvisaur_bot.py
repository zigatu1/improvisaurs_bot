import os
from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv

# Ваши хендлеры
from handlers import start_cmd, nomination_handler, soundtrack_handler

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")
PORT = int(os.getenv("PORT", 5000))

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN не задан")
if not RENDER_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL не задан")

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

app.add_handler(CommandHandler("start", start_cmd))
app.add_handler(CommandHandler("nomination", nomination_handler))
app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

webhook_url = f"{RENDER_URL}/{TOKEN}"

if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=webhook_url,
        drop_pending_updates=True,  # сбросить старые невыполненные апдейты
    )
