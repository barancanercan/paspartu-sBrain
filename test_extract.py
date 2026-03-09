#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncCrawlerStrategy, AsyncWebCrawler, CrawlerRunConfig

async def main():
    print("Endeksa - extraction_strategy ile...")
    
    # Enhanced extraction ile dene
    config = CrawlerRunConfig(
        wait_for=10,
        js_enabled=True,
        # Page interaction
        simulate_user=True,  # Mouse hareketi simüle et
        ad_block=True,
    )
    
    async with AsyncWebCrawler(verbose=True, headless=True) as crawler:
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            config=config
        )
        
        if result.success:
            print(f"\nHTML uzunluk: {len(result.html)}")
            
            # Markdown'a bak
            if result.markdown:
                print(f"\n=== Markdown (ilk 3000) ===")
                print(result.markdown[:3000])
                
            # Text'e bak
            if result.text:
                print(f"\n=== Text (ilk 3000) ===")
                print(result.text[:3000])

if __name__ == "__main__":
    asyncio.run(main())
