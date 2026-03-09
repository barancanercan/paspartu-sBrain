#!/usr/bin/env python3
import requests

# Firecrawl API
API_KEY = "fc-7f45c3d059174af88afc0a51b7e715cd"

url = "https://api.firecrawl.dev/v1/scrape"

payload = {
    "url": "https://www.endeksa.com/tr/ankara",
    "formats": ["markdown", "html"],
    "waitFor": 5
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("Firecrawl ile Endeksa çekiliyor...")
response = requests.post(url, json=payload, headers=headers)

print(f"Status: {response.status_code}")
print(f"\n=== JSON ===")
print(response.text[:3000])
