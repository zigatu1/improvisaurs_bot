import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
from dotenv import load_dotenv

load_dotenv()  # подхватывает .env локально или в Render

from handlers import start_cmd, nomination_handler, soundtrack_handler

app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN is not set")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, None, workers=int(os.getenv("WORKERS", 4)))

# Регистрируем хендлеры
dp.add_handler(CommandHandler("start", start_cmd))
dp.add_handler(CommandHandler("nomination", nomination_handler))
dp.add_handler(CommandHandler("soundtrack", soundtrack_handler))

# Точка входа webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook_handler():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    render_url = os.getenv("RENDER_EXTERNAL_URL")
    if not render_url:
        raise RuntimeError("RENDER_EXTERNAL_URL is not set")
    bot.set_webhook(f"{render_url}/{TOKEN}")
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
