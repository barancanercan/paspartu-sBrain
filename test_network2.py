#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
import json

async def main():
    print("Endeksa - Network izleme ile...")
    
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
    )
    
    # Network isteklerini yakala
    run_config = CrawlerRunConfig(
        wait_for=5,
        wait_until="networkidle",
        capture_network_requests=True,
        capture_console_messages=True,
        verbose=True,
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            config=run_config
        )
        
        print(f"\n=== Sonuç ===")
        print(f"Success: {result.success}")
        
        # Network requests
        if hasattr(result, 'network_requests') and result.network_requests:
            print(f"\n=== Network İstekleri ({len(result.network_requests)}) ===")
            for req in result.network_requests[:20]:
                url = req.get('url', '')
                if 'api' in url.lower() or 'json' in url.lower() or 'ankara' in url.lower():
                    print(f"📡 {req.get('method')} {url}")
        
        # Console messages
        if hasattr(result, 'console_messages') and result.console_messages:
            print(f"\n=== Console Messages ===")
            for msg in result.console_messages[:10]:
                print(f"📜 {msg}")

if __name__ == "__main__":
    asyncio.run(main())
