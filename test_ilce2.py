#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    print("Endeksa Ankara ilçeler bulunuyor...")
    
    async with AsyncWebCrawler(
        verbose=True,
        headless=True,
        js_enabled=True
    ) as crawler:
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/ankara/iller',
            wait_for=3,  # JS yüklenmesi için bekle
            timeout=30000
        )
        
        if result.success:
            print("\n=== HTML (ilk 10000 char) ===")
            print(result.html[:10000])
            
            # JSON data var mı kontrol et
            import re
            json_matches = re.findall(r'\{[^{}]*"il"[^{}]*\}', result.html)
            print(f"\n=== JSON parçaları ===")
            for m in json_matches[:5]:
                print(m)

if __name__ == "__main__":
    asyncio.run(main())
