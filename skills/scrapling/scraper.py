#!/usr/bin/env python3
"""
Günlük Scrapling Scraper
OpenClaw Cron Job tarafından çalıştırılır
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Scrapling imports
from scrapling.fetchers import StealthySession, Fetcher

# Yapılandırma
PROFILE_DIR = "/root/.openclaw/workspace/chrome-profiles/daily-scraper"
COOKIES_FILE = "/root/.openclaw/workspace/cookies.json"
REPORTS_DIR = Path("/root/.openclaw/workspace/reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Hedef siteler (örnek)
TARGETS = [
    {
        "name": "Örnek Site 1",
        "url": "https://example1.com",
        "selectors": {
            "title": "h1::text",
            "items": ".item-class",
            "prices": ".price::text"
        }
    },
    {
        "name": "Örnek Site 2", 
        "url": "https://example2.com",
        "selectors": {
            "headlines": ".headline::text",
            "dates": ".date::text"
        }
    }
]

def load_cookies():
    """Cookie dosyasını yükle"""
    if os.path.exists(COOKIES_FILE):
        with open(COOKIES_FILE, 'r') as f:
            return json.load(f)
    return []

def scrape_with_stealthy_session(targets):
    """StealthySession ile scraping yap"""
    results = {}
    
    with StealthySession(
        headless=True,
        user_data_dir=PROFILE_DIR,
        network_idle=True,
        timeout=60000
    ) as session:
        for target in targets:
            try:
                page = session.fetch(target['url'])
                
                if page.status == 200:
                    data = {}
                    for key, selector in target['selectors'].items():
                        elements = page.css(selector).getall()
                        data[key] = elements
                    
                    results[target['name']] = {
                        'status': 'success',
                        'url': target['url'],
                        'data': data,
                        'timestamp': datetime.now().isoformat()
                    }
                else:
                    results[target['name']] = {
                        'status': 'error',
                        'url': target['url'],
                        'error': f'HTTP {page.status}',
                        'timestamp': datetime.now().isoformat()
                    }
                    
            except Exception as e:
                results[target['name']] = {
                    'status': 'error',
                    'url': target['url'],
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                }
    
    return results

def scrape_with_fetcher_cookies(targets, cookies):
    """Fetcher + Cookie ile scraping yap"""
    results = {}
    cookie_header = "; ".join([f"{c['name']}={c['value']}" for c in cookies])
    
    for target in targets:
        try:
            page = Fetcher.get(
                target['url'],
                headers={"Cookie": cookie_header},
                stealthy_headers=True,
                impersonate='chrome'
            )
            
            if page.status == 200:
                data = {}
                for key, selector in target['selectors'].items():
                    elements = page.css(selector).getall()
                    data[key] = elements
                
                results[target['name']] = {
                    'status': 'success',
                    'url': target['url'],
                    'data': data,
                    'timestamp': datetime.now().isoformat()
                }
            else:
                results[target['name']] = {
                    'status': 'error',
                    'url': target['url'],
                    'error': f'HTTP {page.status}',
                    'timestamp': datetime.now().isoformat()
                }
                
        except Exception as e:
            results[target['name']] = {
                'status': 'error',
                'url': target['url'],
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    return results

def generate_report(results):
    """Markdown raporu oluştur"""
    now = datetime.now()
    report_name = f"scraping_rapor_{now.strftime('%Y%m%d_%H%M')}.md"
    report_path = REPORTS_DIR / report_name
    
    report = f"""# 🕷️ Günlük Scraping Raporu

**Tarih:** {now.strftime('%d.%m.%Y %H:%M')}  
**Toplam Hedef:** {len(results)}  
**Başarılı:** {sum(1 for r in results.values() if r['status'] == 'success')}  
**Başarısız:** {sum(1 for r in results.values() if r['status'] == 'error')}

---

## 📊 Site Bazlı Sonuçlar

"""
    
    for site_name, result in results.items():
        if result['status'] == 'success':
            report += f"""### ✅ {site_name}

**URL:** {result['url']}  
**Zaman:** {result['timestamp']}

**Çekilen Veriler:**

"""
            for key, values in result['data'].items():
                report += f"- **{key}:** {len(values)} öğe bulundu\n"
                if values and len(values) <= 5:
                    for v in values:
                        report += f"  - `{v[:100]}{'...' if len(str(v)) > 100 else ''}`\n"
                elif values:
                    report += f"  - İlk 3 öğe: {values[:3]}\n"
            
            report += "\n"
        else:
            report += f"""### ❌ {site_name}

**URL:** {result['url']}  
**Hata:** {result['error']}  
**Zaman:** {result['timestamp']}

"""
    
    report += f"""---

## 📁 Rapor Bilgileri

- **Rapor Dosyası:** `{report_path}`
- **Oluşturulma:** {now.isoformat()}
- **Motor:** Scrapling v0.4.x

---

*Bu rapor OpenClaw cron job tarafından otomatik oluşturulmuştur.*
"""
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    return report_path, report

def main():
    """Ana fonksiyon"""
    print(f"[{datetime.now()}] Scraping başlıyor...")
    
    # Önce cookie ile dene
    cookies = load_cookies()
    
    if cookies:
        print("Cookie dosyası bulundu, Fetcher kullanılıyor...")
        results = scrape_with_fetcher_cookies(TARGETS, cookies)
    else:
        print("Cookie yok, StealthySession kullanılıyor...")
        results = scrape_with_stealthy_session(TARGETS)
    
    # Rapor oluştur
    report_path, report_content = generate_report(results)
    print(f"Rapor oluşturuldu: {report_path}")
    
    # Özet yazdır (OpenClaw bu çıktıyı okuyabilir)
    success_count = sum(1 for r in results.values() if r['status'] == 'success')
    error_count = sum(1 for r in results.values() if r['status'] == 'error')
    
    print(f"""
=== SCRAPING ÖZETİ ===
Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}
Toplam: {len(results)} site
Başarılı: {success_count}
Başarısız: {error_count}
Rapor: {report_path}
====================
""")
    
    return report_path

if __name__ == "__main__":
    main()
