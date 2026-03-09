#!/usr/bin/env python3
import asyncio
import re
from crawl4ai import AsyncWebCrawler

async def main():
    print("Endeksa - Element bekleme yöntemi...")
    
    async with AsyncWebCrawler(verbose=True, headless=True) as crawler:
        # JS ile yüklenen içerik için
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            wait_for="div",  # Herhangi bir div yüklenene kadar bekle
            css_selector="body",
            timeout=30000
        )
        
        if result.success:
            print(f"\nHTML uzunluk: {len(result.html)}")
            
            # İl linklerini bul
            links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', result.html)
            print(f"\n=== Tüm linkler ({len(links)}) ===")
            for href, text in links[:20]:
                if text.strip():
                    print(f"{text.strip()}: {href}")

if __name__ == "__main__":
    asyncio.run(main())
