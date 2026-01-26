#!/usr/bin/env python3
"""
WeChat Pay Documentation Discovery with Browser Automation
Uses Playwright to expand all sidebar sections and extract ALL links
"""

import asyncio
import json
from pathlib import Path
from typing import Set, Dict
import argparse
from datetime import datetime
from playwright.async_api import async_playwright
from urllib.parse import urlparse


# Root URL for WeChat Pay Documentation
ROOT_URL = 'https://pay.weixin.qq.com/doc/v3/merchant/4012062524'


class WeChatPayBrowserCrawler:
    """Crawls WeChat Pay documentation using browser automation"""

    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.root_url = ROOT_URL
        self.discovered_urls: Set[str] = set()
        self.url_metadata: Dict[str, dict] = {}

    def normalize_url(self, url: str) -> str:
        """Normalize and filter URLs"""
        # Handle relative URLs
        if url.startswith('/'):
            url = 'https://pay.weixin.qq.com' + url

        # Parse URL
        parsed = urlparse(url)

        # Only keep WeChat Pay doc URLs
        if not parsed.path.startswith('/doc/v3/'):
            return None

        # Remove fragments
        clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        return clean_url

    def is_valid_doc_url(self, url: str) -> bool:
        """Check if URL is a valid documentation page"""
        if not url:
            return False

        # Must be from WeChat Pay docs
        if not url.startswith('https://pay.weixin.qq.com/doc/v3/'):
            return False

        # Must be merchant or partner docs
        if '/merchant/' not in url and '/partner/' not in url:
            return False

        return True

    async def expand_all_sidebar_groups(self, page):
        """Click to expand all collapsed sidebar groups"""
        print("Expanding all sidebar sections...")

        # Find all collapsed groups (with 'down arrow' class)
        # We need to click multiple times because some groups are nested
        max_iterations = 10
        for iteration in range(max_iterations):
            # Find all collapsed sections
            collapsed_sections = await page.query_selector_all('.sidebar-group.collapsable p.sidebar-heading .arrow.down')

            if not collapsed_sections:
                print(f"All sections expanded after {iteration} iterations")
                break

            print(f"Iteration {iteration + 1}: Found {len(collapsed_sections)} collapsed sections")

            # Click each collapsed section
            for section in collapsed_sections:
                try:
                    # Click the parent heading to expand
                    parent = await section.evaluate_handle('element => element.closest("p.sidebar-heading")')
                    if parent:
                        await parent.as_element().click()
                        await asyncio.sleep(0.1)  # Small delay for animation
                except Exception as e:
                    print(f"Error clicking section: {e}")

            # Wait for DOM updates
            await asyncio.sleep(0.5)

    async def extract_all_links(self, page):
        """Extract all links from the expanded sidebar using XPath"""
        print("Extracting all links from sidebar using XPath //*[@id='sidebar']/div...")

        # Use XPath to get all links in sidebar divs
        # XPath: //*[@id="sidebar"]/div//a
        links = await page.query_selector_all('#sidebar > div a[href]')

        print(f"Found {len(links)} links in sidebar")

        for link in links:
            href = await link.get_attribute('href')
            text = await link.inner_text()

            url = self.normalize_url(href)
            if self.is_valid_doc_url(url):
                self.discovered_urls.add(url)

                # Store title from link text
                if url not in self.url_metadata:
                    self.url_metadata[url] = {'title': text.strip()}

    async def discover(self):
        """Discover all documentation pages using browser automation"""
        print(f"\nDiscovering WeChat Pay documentation with browser automation...")

        async with async_playwright() as p:
            # Launch browser (headless mode)
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            # Navigate to root page
            print(f"Loading {self.root_url}...")
            await page.goto(self.root_url, wait_until='networkidle', timeout=60000)

            # Wait for sidebar to load
            await page.wait_for_selector('.sidebar', timeout=10000)

            # Expand all collapsed sections
            await self.expand_all_sidebar_groups(page)

            # Extract all links
            await self.extract_all_links(page)

            # Close browser
            await browser.close()

        # Save results
        self.save_index()

    def save_index(self):
        """Save complete discovered index"""
        index_file = self.output_dir / 'wechat_pay_index.json'

        index = {
            'root_url': self.root_url,
            'discovered_at': datetime.now().isoformat(),
            'total_pages': len(self.discovered_urls),
            'discovery_method': 'browser_automation',
            'pages': []
        }

        # Build pages list with metadata
        for url in sorted(self.discovered_urls):
            metadata = self.url_metadata.get(url, {})
            index['pages'].append({
                'url': url,
                'title': metadata.get('title', ''),
            })

        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)

        print(f"\nIndex saved to {index_file}")
        print(f"Total pages discovered: {len(self.discovered_urls)}")


async def main():
    parser = argparse.ArgumentParser(description='Discover WeChat Pay documentation pages using browser automation')
    parser.add_argument('--output', default='.', help='Output directory (default: project directory)')

    args = parser.parse_args()

    output_dir = Path(__file__).parent.parent / args.output if args.output == '.' else Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    crawler = WeChatPayBrowserCrawler(output_dir=output_dir)
    await crawler.discover()

    print("\nDiscovery complete!")
    print("\nNext steps:")
    print("  Run 11_download_wechat_html.py to download the HTML content")


if __name__ == '__main__':
    asyncio.run(main())
