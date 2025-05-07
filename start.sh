#!/usr/bin/env bash
set -e

pip install -r requirements.txt

# Запускаем telegram-бот на webhook-подключении через встроенный сервер
exec python improvisaur_bot.py
