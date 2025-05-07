import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv

from handlers import start_cmd, nomination_handler, soundtrack_handler

logging.basicConfig(
    format="%(asctime)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN не задан")

PORT = int(os.getenv("PORT", 5000))

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_http_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    logging.info(f"Health HTTP server on 0.0.0.0:{PORT}")
    server.serve_forever()

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)
app.add_handler(CommandHandler("start", start_cmd))
app.add_handler(CommandHandler("nomination", nomination_handler))
app.add_handler(CommandHandler("soundtrack", soundtrack_handler))

if __name__ == "__main__":
    threading.Thread(target=run_http_server, daemon=True).start()
    logging.info("Starting long polling")
    app.run_polling(drop_pending_updates=True)
