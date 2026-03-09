#!/usr/bin/env python3
import asyncio
import re
from crawl4ai import AsyncWebCrawler

async def main():
    print("Endeksa il/ilçe yapısı araştırılıyor...")
    
    async with AsyncWebCrawler(verbose=False, headless=True, js_enabled=True) as crawler:
        # Ana sayfa yerine doğrudan iller sayfası
        result = await crawler.arun(
            url='https://www.endeksa.com/tr/iller',
            wait_for=5,
            timeout=30000
        )
        
        if result.success:
            html = result.html
            
            # Script taglarını bul - API url'leri olabilir
            scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
            
            print("=== Scriptlerde API aranıyor ===")
            for i, s in enumerate(scripts[:5]):
                if 'api' in s.lower() or 'http' in s:
                    print(f"Script {i}: {s[:500]}...")
            
            # JSON-LD veya window.__data varsa
            data_matches = re.findall(r'window\.__[A-Z_]+.*?=.*?(\{.*?\});', html)
            print(f"\n=== Window data ===")
            for m in data_matches[:3]:
                print(m[:500])
                
            # a href linkleri bul
            links = re.findall(r'href="([^"]+)"', html)
            ankara_links = [l for l in links if 'ankara' in l.lower()]
            print(f"\n=== Ankara linkleri ===")
            for l in ankara_links[:15]:
                print(l)

if __name__ == "__main__":
    asyncio.run(main())
