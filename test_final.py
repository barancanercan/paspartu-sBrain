#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from playwright.async_api import TimeoutError as PlaywrightTimeout

async def main():
    print("Endeksa - Son deneme...")
    
    # JS ile etkileşim
    js_code = """
    async () => {
        // Sayfa yüklenene kadar bekle
        await new Promise(r => setTimeout(r, 5000));
        
        // Body içeriğini döndür
        return document.body.innerHTML;
    }
    """
    
    run_config = CrawlerRunConfig(
        js_code=js_code,
        js_only=True,
        page_timeout=30000,
    )
    
    async with AsyncWebCrawler(verbose=True, headless=True) as crawler:
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            config=run_config
        )
        
        print(f"\n=== Sonuç ===")
        print(f"Success: {result.success}")
        
        if result.success:
            print(f"HTML uzunluk: {len(result.html)}")
            print(f"\n=== HTML ===")
            print(result.html[:2000])

if __name__ == "__main__":
    asyncio.run(main())
