#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    print("Endeksa API'leri test ediliyor...")
    
    # Bulunan API endpointleri
    api_urls = [
        'https://appv3.endeksa.com/currency',
        'https://appv3.endeksa.com/iller',
        'https://appv3.endeksa.com/iller/ankara',
        'https://appv3.endeksa.com/iller/ankara/ilceler',
        'https://api.endeksa.com/iller',
        'https://api.endeksa.com/iller/ankara',
    ]
    
    async with AsyncWebCrawler(verbose=False, headless=True) as crawler:
        for url in api_urls:
            print(f"\n=== {url} ===")
            result = await crawler.arun(url=url, timeout=15000)
            
            if result.success:
                content_type = result.html[:200]
                print(f"İçerik tipi: {content_type[:100]}")
                
                # JSON mı?
                if '{' in result.html or '[' in result.html:
                    print(f"JSON olabilir! İlk 500: {result.html[:500]}")
            else:
                print(f"Hata: {result.error}")

if __name__ == "__main__":
    asyncio.run(main())
