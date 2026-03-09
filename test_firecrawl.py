#!/usr/bin/env python3
from firecrawl import FirecrawlApp

app = FirecrawlApp()

# Ankara'yı scrape et - JS render ile
print("Endeksa Ankara sayfası çekiliyor...")
result = app.scrape_url(
    'https://www.endeksa.com/ankara',
    formats=['markdown', 'html'],
    wait_for=None,
    timeout=60000
)

print("\n=== MARKDOWN ===")
print(result.markdown[:5000] if result.markdown else "Boş")

print("\n=== HTML (ilk 2000 char) ===")
print(result.html[:2000] if result.html else "Boş")
