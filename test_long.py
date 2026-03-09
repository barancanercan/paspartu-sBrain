#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    print("Endeksa - Uzun bekleme...")
    
    async with AsyncWebCrawler(verbose=True, headless=True) as crawler:
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            wait_for=15,  # 15 saniye JS yüklenmesi için bekle
            timeout=60000
        )
        
        if result.success:
            print(f"\nHTML uzunluk: {len(result.html)}")
            
            # Angular ng-repeat veya benzeri yapıları bul
            import re
            # İl isimlerini ara
            turkce_sehirler = ['Ankara', 'İstanbul', 'İzmir', 'Adana', 'Antalya']
            for sehir in turkce_sehirler:
                if sehir in result.html:
                    print(f"✅ {sehir} bulundu!")
                    
            # a taglarını bul
            atags = re.findall(r'<a[^>]*>([^<]+)</a>', result.html)
            print(f"\n=== Link metinleri ({len(atags)}) ===")
            for t in atags[:30]:
                if t.strip():
                    print(t.strip())

if __name__ == "__main__":
    asyncio.run(main())
