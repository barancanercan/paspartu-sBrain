#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    print("API endpoint deneniyor...")
    
    # Endeksa API'sini dene
    api_urls = [
        'https://api.endeksa.com/tr/ankara/iller',
        'https://api.endeksa.com/tr/cities/ankara',
        'https://www.endeksa.com/api/iller',
    ]
    
    async with AsyncWebCrawler(verbose=False, headless=True) as crawler:
        for url in api_urls:
            print(f"\n{url}")
            result = await crawler.arun(url=url, timeout=15000)
            print(f"Status: {result.success}")
            if result.success:
                print(result.html[:1000])

if __name__ == "__main__":
    asyncio.run(main())
