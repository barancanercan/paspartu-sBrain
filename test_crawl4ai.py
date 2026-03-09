#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    print("Endeksa Ankara çekiliyor...")
    
    async with AsyncWebCrawler(
        verbose=True,
        headless=True,
        js_enabled=True
    ) as crawler:
        # Türkçe versiyonunu dene
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/ankara',
            wait_for="body",
            timeout=30000
        )
        
        print("\n=== Status ===")
        print(f"Success: {result.success}")
        print(f"URL: {result.url}")
        
        if result.success:
            print("\n=== Markdown (ilk 5000 char) ===")
            print(result.markdown[:5000] if result.markdown else "Boş")
            
            print("\n=== HTML uzunluğu ===")
            print(len(result.html) if result.html else 0)
        else:
            print(f"Hata: {result.error}")

if __name__ == "__main__":
    asyncio.run(main())
