#!/usr/bin/env python3
from scrapling.fetchers import Fetcher

print("Endeksa Ankara çekiliyor...")
try:
    page = Fetcher.get(
        'https://www.endeksa.com/ankara',
        impersonate='chrome',
        stealthy_headers=True
    )
    
    print("\n=== Status ===")
    print(page.status)
    
    print("\n=== İçerik (ilk 5000 char) ===")
    print(page.text[:5000])
    
    print("\n=== Linkler ===")
    links = page.css('a').getall()
    print(f"Toplam link: {len(links)}")
    for l in links[:20]:
        print(l)
    
except Exception as e:
    print(f"Hata: {e}")
    import traceback
    traceback.print_exc()
