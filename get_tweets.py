#!/usr/bin/env python3
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        executable_path='/usr/bin/chromium',
        args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--disable-dev-shm-usage']
    )
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 720})
    
    try:
        page.goto('https://x.com/mansuryavas06', timeout=30000, wait_until='domcontentloaded')
        page.wait_for_timeout(10000)
        
        # Get all links
        links = page.query_selector_all('a')
        print(f"Found {len(links)} links")
        
        for link in links[:20]:
            try:
                href = link.get_attribute('href')
                text = link.inner_text()[:50]
                if href:
                    print(f"Link: {text} -> {href}")
            except:
                pass
        
        # Check for login button
        login = page.query_selector('text=Log in')
        if login:
            print("\n*** Login button found! ***")
        
        # Get title
        title = page.title()
        print(f"\nPage title: {title}")
                
    except Exception as e:
        print(f"Error: {e}")
    
    browser.close()
