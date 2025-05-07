#!/usr/bin/env bash
set -e

pip install -r requirements.txt
exec gunicorn --workers 4 --bind 0.0.0.0:$PORT improvisaur_bot:app
