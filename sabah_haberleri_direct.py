#!/usr/bin/env python3
"""Sabah haberleri - doğrudan Telegram API ile gönderir."""

import subprocess
import os
from datetime import datetime
import urllib.request
import urllib.parse
import json

# Config
TELEGRAM_BOT_TOKEN = "8225539420:AAEZixR4CQuP3nq9zh6VcizG6IQKNAWN47A"
TELEGRAM_CHAT_ID = "1145527793"
VENV_PY = "/root/.openclaw/workspace/news-intelligence-agent/.venv/bin/python"
AGENT_DIR = "/root/.openclaw/workspace/news-intelligence-agent"

def send_telegram(msg):
    """Telegram'a mesaj gönder."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    data_encoded = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data_encoded, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result.get('ok', False)
    except Exception as e:
        print(f"Telegram error: {e}")
        return False

# 1. Haberleri çek
print("Haberler çekiliyor...")
subprocess.run([VENV_PY, "collector/fetch.py"], cwd=AGENT_DIR, capture_output=True)
subprocess.run([VENV_PY, "scripts/export_to_csv.py"], cwd=AGENT_DIR, capture_output=True)

# 2. Oku
csv_path = os.path.join(AGENT_DIR, "news_report_categorized.csv")
if not os.path.exists(csv_path):
    msg = "Haberler çekilemedi!"
    send_telegram(msg)
    print(msg)
    exit(1)

with open(csv_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()[:20]

# 3. Mesaj oluştur
tarih = datetime.now().strftime("%d %B %Y")
mesaj = f"📰 *Sabah Haberleri - {tarih}*\n\n"

for line in lines[1:]:
    parts = line.strip().split(',')
    if len(parts) >= 2:
        baslik = parts[0][:100]
        mesaj += f"• {baslik}\n"

mesaj += "\n_Veritabaninda daha fazla haber var_"

# 4. Gonder
if send_telegram(mesaj):
    print("Gonderildi!")
else:
    print("Gonderilemedi")
