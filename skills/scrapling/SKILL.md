# OpenClaw + Scrapling Entegrasyonu - Headless Sunucu Çözümü

## Problem Özeti

Headless sunucularda (KiloClaw gibi VPS) OpenClaw ile Scrapling kullanırken cookie yönetimi ve browser oturumu sıkıntıları yaşanabilir. Bunun birkaç ana nedeni var:

1. **Headless ortamda GUI yok** - Browser profilleri düzgün oluşturulamıyor
2. **Cookie persistence sorunları** - Oturumlar korunmuyor
3. **Anti-bot korumaları** - Cloudflare vb. sistemler headless tarayıcıları tespit ediyor

---

## Çözüm Yolları

### 1. StealthySession ile Kalıcı Profil Kullanımı

Scrapling'in `user_data_dir` parametresi ile browser profilini kalıcı hale getirin:

```python
from scrapling.fetchers import StealthySession

# Kalıcı profil dizini belirle
PROFILE_DIR = "/root/.openclaw/workspace/chrome-profiles/scraping-profile"

with StealthySession(
    headless=True,
    user_data_dir=PROFILE_DIR,  # Cookie'ler burada saklanır
    solve_cloudflare=True,
    network_idle=True
) as session:
    page = session.fetch('https://hedef-site.com')
    data = page.css('.veri-class').getall()
```

### 2. Cookie Export/Import Yöntemi

Tarayıcıdan export ettiğin cookie'leri Python ile kullan:

```python
import json
from scrapling.fetchers import Fetcher

# Cookie dosyasını yükle (JSON formatında)
with open('/root/.openclaw/workspace/cookies.json', 'r') as f:
    cookies = json.load(f)

# Cookie string oluştur
cookie_header = "; ".join([f"{c['name']}={c['value']}" for c in cookies])

# Fetcher ile kullan
page = Fetcher.get(
    'https://hedef-site.com',
    headers={"Cookie": cookie_header},
    stealthy_headers=True,
    impersonate='chrome'
)
```

### 3. Virtual Display (Xvfb) Kullanımı

Headless sunucuda sanal ekran oluştur:

```bash
# Xvfb kurulumu
apt-get install xvfb

# Sanal ekranı başlat
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99

# Şimdi browser "görünür" modda çalışabilir
```

Python'da:
```python
import os
os.environ['DISPLAY'] = ':99'

from scrapling.fetchers import StealthyFetcher

page = StealthyFetcher.fetch(
    'https://hedef-site.com',
    headless=False,  # Artık çalışır çünkü sanal display var
    solve_cloudflare=True
)
```

### 4. noVNC ile Remote Desktop (Manuel CAPTCHA Çözümü)

OpenClaw'ın `virtual-remote-desktop` skill'ini kullan:

```bash
# noVNC başlat
bash /root/.openclaw/workspace/skills/virtual-remote-desktop/scripts/start_vrd.sh

# URL'yi al, browser'dan bağlan, manuel login yap
# Cookie'ler CHROME_PROFILE_DIR'de saklanır
```

---

## OpenClaw Cron Job Yapılandırması

### Sabah 07:30'da Çalışacak Scraping Job'ı Oluştur

```bash
openclaw cron add \
  --name "Sabah-Scraping-Gorevi" \
  --cron "30 7 * * *" \
  --tz "Europe/Istanbul" \
  --session isolated \
  --message "Scrapling skill'ini çalıştır. Hedef siteleri tara, verileri çek ve raporu /root/.openclaw/workspace/reports/ dizinine kaydet. Rapor adı: scraping_rapor_TARIH.md formatında olsun." \
  --announce \
  --channel telegram \
  --to "CHAT_ID"
```

### Sabah 09:00'da Rapor Gönderme Job'ı

```bash
openclaw cron add \
  --name "Scraping-Rapor-Gonder" \
  --cron "0 9 * * *" \
  --tz "Europe/Istanbul" \
  --session isolated \
  --message "Son scraping raporunu oku ve özet olarak gönder. Rapor dizini: /root/.openclaw/workspace/reports/" \
  --announce \
  --channel telegram \
  --to "CHAT_ID"
```

---

## Kurulum Adımları

### 1. Scrapling Kurulumu (Sunucuda)

```bash
# Python ortamı
cd /root/.openclaw/workspace
python3 -m venv venv
source venv/bin/activate

# Scrapling kurulumu
pip install "scrapling[fetchers]"
scrapling install

# Gerekli dizinleri oluştur
mkdir -p chrome-profiles/daily-scraper
mkdir -p reports
```

### 2. Cookie Export (Manuel - Bir Kere Yapılacak)

1. noVNC veya local browser'dan hedef siteye login ol
2. Developer Tools → Application → Cookies
3. Tüm cookie'leri JSON olarak export et
4. `/root/.openclaw/workspace/cookies.json` olarak kaydet

Cookie JSON formatı:
```json
[
  {"name": "session_id", "value": "abc123", "domain": ".example.com"},
  {"name": "auth_token", "value": "xyz789", "domain": ".example.com"}
]
```

### 3. Cron Job'ları Oluştur

```bash
# Scraping görevi
openclaw cron add \
  --name "Sabah-Scraping-0730" \
  --cron "30 7 * * *" \
  --tz "Europe/Istanbul" \
  --session isolated \
  --message "Python script'i çalıştır: python /root/.openclaw/workspace/skills/scrapling/scraper.py" \
  --announce

# Rapor gönderimi  
openclaw cron add \
  --name "Rapor-Gonder-0900" \
  --cron "0 9 * * *" \
  --tz "Europe/Istanbul" \
  --session isolated \
  --message "En son raporu oku ve özet olarak gönder: cat $(ls -t /root/.openclaw/workspace/reports/*.md | head -1)" \
  --announce
```

### 4. Test Et

```bash
# Manuel test
openclaw cron run "Sabah-Scraping-0730"

# Cron listesini kontrol et
openclaw cron list

# Log'ları izle
tail -f ~/.openclaw/logs/gateway.log
```

---

## Özet

| Saat | Görev | Açıklama |
|------|-------|----------|
| 07:30 | Scraping | Hedef siteleri tara, veri çek, rapor oluştur |
| 09:00 | Rapor | Oluşturulan raporu kullanıcıya gönder |

Bu sistem, headless sunucuda Scrapling ile güvenilir scraping yapmanı sağlar. Cookie yönetimi ve anti-bot bypass özellikleri ile çoğu siteyi başarıyla kazıyabilirsin.
