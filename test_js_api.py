#!/usr/bin/env python3
import asyncio
from crawl4ai import AsyncWebCrawler
import re

async def main():
    print("Endeksa JS'lerde API aranıyor...")
    
    async with AsyncWebCrawler(verbose=False, headless=True) as crawler:
        result = await crawler.arun(url='https://www.endeksa.com/tr', timeout=15000)
        
        if result.success:
            # Script taglarını bul
            scripts = re.findall(r'<script[^>]*src="([^"]*\.js[^"]*)"', result.html)
            
            print("=== JS Dosyaları ===")
            for s in scripts[:20]:
                print(s)
            
            # API URL'lerini JS içinde ara
            js_urls = []
            for script_url in scripts:
                if 'appv3' in script_url or 'api.endeksa' in script_url:
                    js_urls.append(script_url)
                    
            print("\n=== Olası API JS ===")
            for u in js_urls:
                print(u)

if __name__ == "__main__":
    asyncio.run(main())
