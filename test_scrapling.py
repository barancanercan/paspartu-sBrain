#!/usr/bin/env python3
from scrapling.fetchers import StealthyFetcher

print("Endeksa Ankara çekiliyor...")
try:
    page = StealthyFetcher.fetch(
        'https://www.endeksa.com/ankara',
        solve_cloudflare=True,
        wait_for=5
    )
    
    print("\n=== Title ===")
    print(page.html[:500])
    
    print("\n=== İlçe/Mahalle aranıyor ===")
    # İlçeleri bul
    ilceler = page.css('a[href*="/ankara/"]').getall()
    print(f"Bulunan linkler: {ilceler[:10]}")
    
except Exception as e:
    print(f"Hata: {e}")
