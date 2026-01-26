#!/usr/bin/env python3
"""
App Store Connect Help Documentation Discovery
Crawls navigation to discover all documentation pages
"""

import asyncio
import aiohttp
import json
import time
from pathlib import Path
from typing import Set, Dict, List
from tqdm import tqdm
import argparse
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


# Root URL for App Store Connect Help
ROOT_URL = 'https://developer.apple.com/help/app-store-connect/'


class RateLimiter:
    """Rate limiter to avoid overwhelming Apple's servers"""

    def __init__(self, requests_per_second: float = 5.0):
        self.delay = 1.0 / requests_per_second
        self.last_request = 0.0

    async def wait(self):
        now = time.time()
        time_since_last = now - self.last_request
        if time_since_last < self.delay:
            await asyncio.sleep(self.delay - time_since_last)
        self.last_request = time.time()


class AppStoreHelpCrawler:
    """Crawls App Store Connect Help navigation to discover all pages"""

    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.root_url = ROOT_URL

        # State tracking
        self.discovered_urls: Set[str] = set()
        self.processed_urls: Set[str] = set()
        self.url_metadata: Dict[str, dict] = {}

        # Rate limiting
        self.rate_limiter = RateLimiter(requests_per_second=5.0)

        # User agent
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

    def save_state(self):
        """Save current discovery state"""
        state_file = self.output_dir / 'discovery_state_appstore.json'
        state = {
            'discovered_urls': list(self.discovered_urls),
            'processed_urls': list(self.processed_urls),
            'url_metadata': self.url_metadata,
        }
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def load_state(self):
        """Load previous discovery state for resume"""
        state_file = self.output_dir / 'discovery_state_appstore.json'
        if state_file.exists():
            with open(state_file, 'r') as f:
                state = json.load(f)
            self.discovered_urls = set(state['discovered_urls'])
            self.processed_urls = set(state['processed_urls'])
            self.url_metadata = state['url_metadata']
            print(f"Resumed: {len(self.processed_urls)} processed, {len(self.discovered_urls) - len(self.processed_urls)} remaining")

    def normalize_url(self, url: str, base_url: str) -> str:
        """Normalize and filter URLs"""
        # Join with base URL to handle relative paths
        full_url = urljoin(base_url, url)

        # Parse URL
        parsed = urlparse(full_url)

        # Only keep URLs from the help site
        if not parsed.path.startswith('/help/app-store-connect/'):
            return None

        # Remove fragments and query params
        clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        # Remove trailing slash
        if clean_url.endswith('/') and clean_url != self.root_url:
            clean_url = clean_url[:-1]

        return clean_url

    def is_valid_doc_url(self, url: str) -> bool:
        """Check if URL is a valid documentation page"""
        if not url:
            return False

        # Skip if already processed
        if url in self.discovered_urls:
            return False

        # Must be from help site
        if not url.startswith('https://developer.apple.com/help/app-store-connect/'):
            return False

        # Skip if it's the root (we handle that separately)
        if url == self.root_url:
            return False

        return True

    def parse_navigation(self, html: str, base_url: str) -> Set[str]:
        """Parse HTML and extract documentation links from navigation"""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()

        # Try multiple navigation selectors
        nav_selectors = [
            # 'nav',  # Generic nav element
            # '.nav',  # Nav with class
            # '#nav',  # Nav with ID
            # 'aside',  # Sidebar
            # '.sidebar',  # Sidebar with class
            # '[role="navigation"]',  # ARIA navigation
            '.sidenav-list',
        ]

        nav_element = None
        for selector in nav_selectors:
            nav_element = soup.select_one(selector)
            if nav_element:
                break

        # If no nav found, search entire body
        if not nav_element:
            nav_element = soup.find('body')

        # Extract all links
        if nav_element:
            for a_tag in nav_element.find_all('a', href=True):
                url = self.normalize_url(a_tag['href'], base_url)
                if self.is_valid_doc_url(url):
                    links.add(url)

        return links

    async def fetch_page(self, session: aiohttp.ClientSession, url: str) -> str:
        """Fetch HTML page with rate limiting"""
        await self.rate_limiter.wait()

        headers = {'User-Agent': self.user_agent}

        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.text()
                elif response.status == 404:
                    print(f"\nWarning: 404 Not Found: {url}")
                    return None
                elif response.status == 429:
                    print(f"\nRate limited. Waiting 10 seconds...")
                    await asyncio.sleep(10)
                    return await self.fetch_page(session, url)
                else:
                    print(f"\nError {response.status} fetching {url}")
                    return None
        except Exception as e:
            print(f"\nException fetching {url}: {e}")
            return None

    async def crawl(self):
        """Crawl all documentation pages"""
        print(f"\nDiscovering App Store Connect Help documentation...")

        # Start with root URL
        self.discovered_urls.add(self.root_url)

        async with aiohttp.ClientSession() as session:
            with tqdm(desc="Discovering pages") as pbar:
                while True:
                    # Find unprocessed URLs
                    to_process = self.discovered_urls - self.processed_urls

                    if not to_process:
                        break

                    # Get next URL
                    url = to_process.pop()

                    # Fetch page
                    html = await self.fetch_page(session, url)
                    if not html:
                        self.processed_urls.add(url)
                        continue

                    # Parse navigation and extract links
                    new_links = self.parse_navigation(html, url)

                    # Add new links
                    for link in new_links:
                        if link not in self.discovered_urls:
                            self.discovered_urls.add(link)

                    # Mark as processed
                    self.processed_urls.add(url)

                    # Store metadata
                    soup = BeautifulSoup(html, 'html.parser')
                    title_tag = soup.find('title')
                    h1_tag = soup.find('h1')

                    self.url_metadata[url] = {
                        'title': title_tag.get_text().strip() if title_tag else '',
                        'h1': h1_tag.get_text().strip() if h1_tag else '',
                    }

                    # Update progress
                    pbar.total = len(self.discovered_urls)
                    pbar.n = len(self.processed_urls)
                    pbar.refresh()

                    # Save state periodically
                    if len(self.processed_urls) % 10 == 0:
                        self.save_state()

        # Final save
        self.save_state()
        self.save_index()

    def save_index(self):
        """Save complete discovered index"""
        index_file = self.output_dir / 'appstore_help_index.json'

        index = {
            'root_url': self.root_url,
            'discovered_at': datetime.now().isoformat(),
            'total_pages': len(self.discovered_urls),
            'pages': []
        }

        # Build pages list with metadata
        for url in sorted(self.discovered_urls):
            metadata = self.url_metadata.get(url, {})
            index['pages'].append({
                'url': url,
                'title': metadata.get('title', ''),
                'h1': metadata.get('h1', ''),
            })

        with open(index_file, 'w') as f:
            json.dump(index, f, indent=2)

        print(f"\nIndex saved to {index_file}")
        print(f"Total pages discovered: {len(self.discovered_urls)}")


async def main():
    parser = argparse.ArgumentParser(description='Discover App Store Connect Help pages')
    parser.add_argument('--output', default='.', help='Output directory (default: project directory)')
    parser.add_argument('--resume', action='store_true', help='Resume from previous state')

    args = parser.parse_args()

    output_dir = Path(__file__).parent.parent / args.output if args.output == '.' else Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    crawler = AppStoreHelpCrawler(output_dir=output_dir)

    if args.resume:
        crawler.load_state()

    await crawler.crawl()

    print("\nDiscovery complete!")
    print("\nNext steps:")
    print("  Run 08_download_appstore_html.py to download the pages")


if __name__ == '__main__':
    asyncio.run(main())
