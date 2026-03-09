#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig

async def main():
    print("Endeksa - BrowserConfig ile...")
    
    browser_config = BrowserConfig(
        headless=True,
        verbose=True,
    )
    
    run_config = CrawlerRunConfig(
        wait_for=10,
        js_enabled=True,
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            config=run_config
        )
        
        if result.success:
            print(f"\nHTML uzunluk: {len(result.html)}")
            
            if result.markdown:
                print(f"\n=== Markdown (ilk 3000) ===")
                print(result.markdown[:3000])

if __name__ == "__main__":
    asyncio.run(main())
