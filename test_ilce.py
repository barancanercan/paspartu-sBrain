#!/usr/bin/env python3
import asyncio
import re
from crawl4ai import AsyncWebCrawler

async def main():
    print("Endeksa ilçe/mahalle aranıyor...")
    
    async with AsyncWebCrawler(
        verbose=True,
        headless=True,
        js_enabled=True
    ) as crawler:
        # Farklı URL formatları dene
        urls_to_try = [
            'https://www.endeksa.com/tr/ankara/iller',
            'https://www.endeksa.com/tr/ankara/ilceler',
            'https://www.endeksa.com/tr/ankara/satilik',
            'https://www.endeksa.com/tr/ankara/kiralik',
            'https://www.endeksa.com/tr/analiz/ankara',
        ]
        
        for url in urls_to_try:
            print(f"\n=== Deneniyor: {url} ===")
            result = await crawler.arun(
                url=url,
                wait_for="body",
                timeout=30000
            )
            
            if result.success and "404" not in result.html[:500]:
                print(f"✅ Bulundu! Uzunluk: {len(result.html)}")
                # İlçe linklerini bul
                matches = re.findall(r'href="([^"]*ankara[^"]*)"', result.html)
                print(f"Linkler: {matches[:10]}")
                break
            else:
                print(f"❌ 404 veya hata")

if __name__ == "__main__":
    asyncio.run(main())
