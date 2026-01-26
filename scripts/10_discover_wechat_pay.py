#!/usr/bin/env python3
"""
WeChat Pay Documentation Discovery
Crawls navigation to discover all documentation pages
"""

import asyncio
import aiohttp
import json
import time
from pathlib import Path
from typing import Set, Dict
from tqdm import tqdm
import argparse
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re


# Root URLs for WeChat Pay Documentation (seed URLs to discover all pages)
# Start from a few valid pages, and discover all linked pages from their sidebar navigation
ROOT_URLS = [
    # Use a few valid seed URLs from different sections
    # The sidebar navigation (//*[@id="sidebar"]/div) contains ALL links
    'https://pay.weixin.qq.com/doc/v3/merchant/4012062524',  # JSAPI支付 - 产品介绍
    'https://pay.weixin.qq.com/doc/v3/merchant/4012081606',  # 通用规则
    'https://pay.weixin.qq.com/doc/v3/merchant/4012076498',  # SDK&开发工具
]


class RateLimiter:
    """Rate limiter to avoid overwhelming servers"""

    def __init__(self, requests_per_second: float = 5.0):
        self.delay = 1.0 / requests_per_second
        self.last_request = 0.0

    async def wait(self):
        now = time.time()
        time_since_last = now - self.last_request
        if time_since_last < self.delay:
            await asyncio.sleep(self.delay - time_since_last)
        self.last_request = time.time()


class WeChatPayCrawler:
    """Crawls WeChat Pay documentation navigation to discover all pages"""

    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.root_urls = ROOT_URLS

        # State tracking
        self.discovered_urls: Set[str] = set()
        self.url_metadata: Dict[str, dict] = {}
        self.skipped_404_count: int = 0  # Track how many 404 pages we skip

        # Rate limiting
        self.rate_limiter = RateLimiter(requests_per_second=5.0)

        # User agent
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

    def save_state(self):
        """Save current discovery state"""
        state_file = self.output_dir / 'discovery_state_wechat.json'
        state = {
            'discovered_urls': list(self.discovered_urls),
            'url_metadata': self.url_metadata,
        }
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

    def load_state(self):
        """Load previous discovery state for resume"""
        state_file = self.output_dir / 'discovery_state_wechat.json'
        if state_file.exists():
            with open(state_file, 'r', encoding='utf-8') as f:
                state = json.load(f)
            self.discovered_urls = set(state['discovered_urls'])
            self.url_metadata = state['url_metadata']
            print(f"Resumed: {len(self.discovered_urls)} URLs already discovered")

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

        # Remove fragments and query params
        clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        return clean_url

    def is_valid_doc_url(self, url: str) -> bool:
        """Check if URL is a valid documentation page"""
        if not url:
            return False

        # Skip if already discovered
        if url in self.discovered_urls:
            return False

        # Must be from WeChat Pay docs
        if not url.startswith('https://pay.weixin.qq.com/doc/v3/'):
            return False

        # Must be merchant or partner docs
        if '/merchant/' not in url and '/partner/' not in url:
            return False

        return True

    def parse_navigation(self, html: str) -> Set[str]:
        """Parse HTML and extract documentation links from navigation sidebar

        The WeChat Pay docs embed navigation data in a JSON structure (menuData)
        rather than rendering static HTML links. We extract this JSON and parse it.
        """
        links = set()

        # Extract the menuData JSON from the page source
        # Look for pattern: window.menuData = [...] or similar
        menu_data = self.extract_menu_data(html)

        if menu_data:
            # Recursively extract all URLs from the nested JSON structure
            self.extract_urls_from_menu(menu_data, links)
        else:
            # Fallback: try parsing HTML <a> tags if JSON extraction fails
            soup = BeautifulSoup(html, 'html.parser')
            sidebar = soup.find(id='sidebar')

            if sidebar:
                for a_tag in sidebar.find_all('a', href=True):
                    href = a_tag['href']
                    url = self.normalize_url(href)
                    if self.is_valid_doc_url(url):
                        links.add(url)
                        title = a_tag.get_text().strip()
                        if title and url not in self.url_metadata:
                            self.url_metadata[url] = {'title': title}

        return links

    def extract_menu_data(self, html: str) -> list:
        """Extract the menuData JSON structure from page source"""
        try:
            # Look for menuData JSON in the HTML
            # The pattern is: "menuData":[...]
            # We need to extract the complete JSON array

            # First, try to find the start of menuData
            menu_start = html.find('"menuData":')
            if menu_start == -1:
                return None

            # Find the start of the JSON array
            array_start = html.find('[', menu_start)
            if array_start == -1:
                return None

            # Now we need to find the matching closing bracket
            # Count brackets to find the proper end
            bracket_count = 0
            array_end = array_start
            in_string = False
            escape_next = False

            for i in range(array_start, len(html)):
                char = html[i]

                # Handle string escaping
                if escape_next:
                    escape_next = False
                    continue

                if char == '\\':
                    escape_next = True
                    continue

                # Handle strings (don't count brackets inside strings)
                if char == '"':
                    in_string = not in_string
                    continue

                if in_string:
                    continue

                # Count brackets
                if char == '[' or char == '{':
                    bracket_count += 1
                elif char == ']' or char == '}':
                    bracket_count -= 1

                # When we reach bracket_count == 0, we found the end
                if bracket_count == 0 and i > array_start:
                    array_end = i + 1
                    break

            # Extract the JSON string
            json_str = html[array_start:array_end]

            # Parse it
            try:
                return json.loads(json_str)
            except json.JSONDecodeError as e:
                print(f"\nWarning: Failed to parse menuData JSON: {e}")
                # Save the problematic JSON for debugging
                debug_file = self.output_dir / 'debug_menudata.json'
                with open(debug_file, 'w', encoding='utf-8') as f:
                    f.write(json_str[:10000])  # Save first 10KB for debugging
                return None

        except Exception as e:
            print(f"\nWarning: Failed to extract menuData JSON: {e}")

        return None

    def extract_urls_from_menu(self, menu_items: list, links: set, parent_title: str = ""):
        """Recursively extract all URLs from menuData JSON structure

        Args:
            menu_items: List of menu item objects with docId, title, url, childrenList
            links: Set to add discovered URLs to
            parent_title: Parent category for context
        """
        if not isinstance(menu_items, list):
            return

        for item in menu_items:
            if not isinstance(item, dict):
                continue

            # Extract URL if present
            url_path = item.get('url')
            title = item.get('title', '')
            doc_id = item.get('docId', '')

            if url_path:
                # Normalize and validate URL
                url = self.normalize_url(url_path)
                if self.is_valid_doc_url(url):
                    links.add(url)

                    # Store metadata
                    if url not in self.url_metadata:
                        self.url_metadata[url] = {}

                    if title:
                        self.url_metadata[url]['title'] = title
                    if parent_title:
                        self.url_metadata[url]['category'] = parent_title
                    if doc_id:
                        self.url_metadata[url]['doc_id'] = doc_id

            # Recursively process children
            children = item.get('childrenList', [])
            if children:
                # Use current item title as parent for children
                child_parent = title if title else parent_title
                self.extract_urls_from_menu(children, links, child_parent)

    def extract_page_metadata(self, html: str, url: str) -> dict:
        """Extract metadata from page content"""
        soup = BeautifulSoup(html, 'html.parser')
        metadata = {}

        # Extract title from <title> tag
        title_tag = soup.find('title')
        if title_tag:
            metadata['page_title'] = title_tag.get_text().strip()

        # Extract h1 heading
        h1_tag = soup.find('h1', class_='content-title')
        if h1_tag:
            metadata['h1'] = h1_tag.get_text().strip()

        # Extract update date
        update_date = soup.find('span', class_='last-updated-date')
        if update_date:
            metadata['last_updated'] = update_date.get_text().strip()

        return metadata

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

    async def discover(self):
        """Discover all documentation pages by recursively crawling"""
        print(f"\nDiscovering WeChat Pay documentation...")

        # Start with root URLs
        to_process = set(self.root_urls)
        processed = set()

        async with aiohttp.ClientSession() as session:
            with tqdm(desc="Discovering pages") as pbar:
                while to_process:
                    # Get next URL to process
                    url = to_process.pop()

                    if url in processed:
                        continue

                    # Fetch page
                    html = await self.fetch_page(session, url)
                    if not html:
                        processed.add(url)
                        continue

                    # Add to discovered
                    self.discovered_urls.add(url)

                    # Extract metadata
                    metadata = self.extract_page_metadata(html, url)
                    if url in self.url_metadata:
                        self.url_metadata[url].update(metadata)
                    else:
                        self.url_metadata[url] = metadata

                    # Check if this is a 404 page (category/navigation pages without content)
                    page_title = metadata.get('page_title', '')
                    if page_title == '公益404':
                        self.skipped_404_count += 1
                        print(f"\n⚠️  Skipping 404 page: {url} (title: {self.url_metadata[url].get('title', 'Unknown')})")
                        # Remove from discovered URLs
                        self.discovered_urls.discard(url)
                        # Still mark as processed to avoid re-fetching
                        processed.add(url)
                        continue

                    # Parse navigation and find new links
                    new_links = self.parse_navigation(html)
                    for new_url in new_links:
                        if new_url not in processed and new_url not in to_process:
                            to_process.add(new_url)
                            self.discovered_urls.add(new_url)

                    # Mark as processed
                    processed.add(url)

                    # Update progress
                    pbar.total = len(self.discovered_urls)
                    pbar.n = len(processed)
                    pbar.set_postfix({'queued': len(to_process)})
                    pbar.refresh()

                    # Save state periodically
                    if len(processed) % 10 == 0:
                        self.save_state()

        # Final save
        self.save_state()
        self.save_index()

    def save_index(self):
        """Save complete discovered index"""
        index_file = self.output_dir / 'wechat_pay_index.json'

        index = {
            'root_urls': self.root_urls,
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
                'category': metadata.get('category', ''),
                'doc_id': metadata.get('doc_id', ''),
                'page_title': metadata.get('page_title', ''),
                'h1': metadata.get('h1', ''),
                'last_updated': metadata.get('last_updated', ''),
            })

        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)

        print(f"\nIndex saved to {index_file}")
        print(f"Total pages discovered: {len(self.discovered_urls)}")
        if self.skipped_404_count > 0:
            print(f"⚠️  Skipped {self.skipped_404_count} 404 pages (category/navigation nodes without content)")


async def main():
    parser = argparse.ArgumentParser(description='Discover WeChat Pay documentation pages')
    parser.add_argument('--output', default='.', help='Output directory (default: project directory)')
    parser.add_argument('--resume', action='store_true', help='Resume from previous state')

    args = parser.parse_args()

    output_dir = Path(__file__).parent.parent / args.output if args.output == '.' else Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    crawler = WeChatPayCrawler(output_dir=output_dir)

    if args.resume:
        crawler.load_state()

    await crawler.discover()

    print("\nDiscovery complete!")
    print("\nNext steps:")
    print("  Run 11_download_wechat_html.py to download the HTML content")


if __name__ == '__main__':
    asyncio.run(main())
