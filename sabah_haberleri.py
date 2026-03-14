#!/usr/bin/env python3
"""Sabah haberleri - hem çeker hem de Telegram'a gönderilecek mesaj üretir."""

import subprocess
import sys
import os
from datetime import datetime

# News agent venv
VENV_PY = "/root/.openclaw/workspace/news-intelligence-agent/.venv/bin/python"
AGENT_DIR = "/root/.openclaw/workspace/news-intelligence-agent"

print("📰 Sabah haberleri çekiliyor...")

# 1. Haberleri çek
result = subprocess.run(
    [VENV_PY, "collector/fetch.py"],
    cwd=AGENT_DIR,
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print(f"Hata: {result.stderr}")

# 2. CSV'ye aktar
subprocess.run(
    [VENV_PY, "scripts/export_to_csv.py"],
    cwd=AGENT_DIR,
    capture_output=True
)

# 3. Sonuçları oku
csv_path = os.path.join(AGENT_DIR, "news_report_categorized.csv")

if not os.path.exists(csv_path):
    print("CSV bulunamadı!")
    sys.exit(1)

with open(csv_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()[:15]  # header + 14 haber

# Türkiye haberlerini filtrele
turkiye_haberler = []
for line in lines[1:]:
    if 'Turkey' in line or 'Turkiye' in line:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            turkiye_haberler.append(parts[0][:120])

# Mesaj oluştur
tarih = datetime.now().strftime("%d %B %Y")
mesaj = f"📰 *Sabah Haberleri - {tarih}*\n\n"

for i, h in enumerate(turkiye_haberler[:8], 1):
    mesaj += f"• {h}\n"

mesaj += "\n_Veritabanında daha fazla haber var_"

print("MESAJ:")
print(mesaj)
