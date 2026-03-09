#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.browser import BrowserConfig

async def main():
    print("Endeksa - Network izleme...")
    
    # Network izleme ile
    config = BrowserConfig(
        headless=True,
        verbose=True,
    )
    
    async with AsyncWebCrawler(config=config) as crawler:
        # Session ile
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            wait_for=10,  # 10 saniye bekle
            timeout=60000
        )
        
        if result.success:
            print(f"\nHTML uzunluk: {len(result.html)}")
            print("\n=== Son 5000 char ===")
            print(result.html[-5000:])

if __name__ == "__main__":
    asyncio.run(main())
