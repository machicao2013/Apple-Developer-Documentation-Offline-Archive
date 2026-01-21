#!/usr/bin/env python3
"""
App Store Connect Help HTML Downloader
Downloads all discovered pages and extracts main content
"""

import asyncio
import aiohttp
import json
import hashlib
import time
from pathlib import Path
from typing import Dict, Set
from tqdm import tqdm
import argparse
from datetime import datetime
from bs4 import BeautifulSoup


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


class AppStoreHelpDownloader:
    """Downloads App Store Connect Help pages"""

    def __init__(self, base_dir: Path, index_file: Path):
        self.base_dir = Path(base_dir)
        self.index_file = Path(index_file)

        # Directories
        self.raw_html_dir = self.base_dir / 'raw-html' / 'appstore-connect'
        self.docsync_dir = self.base_dir / '.docsync'

        # Create directories
        self.raw_html_dir.mkdir(parents=True, exist_ok=True)
        self.docsync_dir.mkdir(parents=True, exist_ok=True)

        # State
        self.manifest: Dict[str, dict] = {}
        self.downloaded: Set[str] = set()

        # Stats
        self.stats = {
            'total': 0,
            'downloaded': 0,
            'failed': 0,
            'skipped': 0,
        }

        # Rate limiting
        self.rate_limiter = RateLimiter(requests_per_second=5.0)

        # User agent
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

    def load_index(self) -> Dict:
        """Load the discovery index"""
        with open(self.index_file, 'r') as f:
            return json.load(f)

    def load_manifest(self):
        """Load existing manifest if it exists"""
        manifest_file = self.docsync_dir / 'appstore_manifest.json'
        if manifest_file.exists():
            with open(manifest_file, 'r') as f:
                self.manifest = json.load(f)
            print(f"Loaded existing manifest with {len(self.manifest)} entries")

    def save_manifest(self):
        """Save manifest to disk"""
        manifest_file = self.docsync_dir / 'appstore_manifest.json'
        with open(manifest_file, 'w') as f:
            json.dump(self.manifest, f, indent=2)

    def calculate_sha256(self, content: str) -> str:
        """Calculate SHA256 hash of content"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def extract_main_content(self, html: str) -> str:
        """Extract main content from HTML page"""
        soup = BeautifulSoup(html, 'html.parser')

        # Try multiple selectors for main content
        content_selectors = [
            '.main-content',
            'div.main-content',
            '#main-content',
            'main',
            'article',
            '[role="main"]',
            '.content',
            '#content',
        ]

        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break

        # Fallback to body if no main content found
        if not main_content:
            print(f"Warning: No main content found, using body")
            main_content = soup.find('body')

        return str(main_content) if main_content else html

    async def download_page(self, session: aiohttp.ClientSession, url: str, page_num: int) -> bool:
        """Download a single page and extract content"""
        await self.rate_limiter.wait()

        headers = {'User-Agent': self.user_agent}

        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    html = await response.text()

                    # Extract main content
                    content = self.extract_main_content(html)

                    # Save HTML file
                    filename = f'page-{page_num:04d}.html'
                    output_file = self.raw_html_dir / filename

                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(content)

                    # Update manifest
                    self.manifest[url] = {
                        'local_path': str(output_file.relative_to(self.base_dir)),
                        'filename': filename,
                        'last_modified': response.headers.get('Last-Modified', ''),
                        'etag': response.headers.get('ETag', ''),
                        'sha256': self.calculate_sha256(content),
                        'downloaded_at': datetime.now().isoformat(),
                    }

                    self.downloaded.add(url)
                    self.stats['downloaded'] += 1
                    return True

                elif response.status == 404:
                    print(f"\n404 Not Found: {url}")
                    self.stats['failed'] += 1
                    return False

                elif response.status == 429:
                    print(f"\nRate limited. Waiting 30 seconds...")
                    await asyncio.sleep(30)
                    return await self.download_page(session, url, page_num)

                else:
                    print(f"\nError {response.status}: {url}")
                    self.stats['failed'] += 1
                    return False

        except Exception as e:
            print(f"\nException downloading {url}: {e}")
            self.stats['failed'] += 1
            return False

    async def download_all(self):
        """Download all pages from index"""
        # Load index
        index = self.load_index()

        # Load existing manifest
        self.load_manifest()

        # Get list of pages to download
        pages = index.get('pages', [])

        # Filter out already downloaded
        if self.manifest:
            pages = [p for p in pages if p['url'] not in self.manifest]
            self.stats['skipped'] = len(self.manifest)

        self.stats['total'] = len(pages)

        print(f"\nDownloading {self.stats['total']} pages...")
        if self.stats['skipped'] > 0:
            print(f"Skipping {self.stats['skipped']} already downloaded pages")

        # Download pages
        async with aiohttp.ClientSession() as session:
            with tqdm(total=len(pages), desc="Downloading") as pbar:
                for i, page in enumerate(pages):
                    url = page['url']
                    page_num = len(self.manifest) + i + 1

                    await self.download_page(session, url, page_num)
                    pbar.update(1)

                    # Save manifest periodically
                    if i % 50 == 0:
                        self.save_manifest()

        # Final save
        self.save_manifest()

        # Print stats
        print("\n" + "="*60)
        print("Download Statistics:")
        print(f"  Total to download: {self.stats['total']}")
        print(f"  Successfully downloaded: {self.stats['downloaded']}")
        print(f"  Failed: {self.stats['failed']}")
        print(f"  Skipped (already downloaded): {self.stats['skipped']}")
        print(f"  Total in manifest: {len(self.manifest)}")
        print("="*60)

        print(f"\nManifest saved to: {self.docsync_dir / 'appstore_manifest.json'}")


async def main():
    parser = argparse.ArgumentParser(description='Download App Store Connect Help pages')
    parser.add_argument('--base-dir', default='.', help='Base directory (default: project directory)')
    parser.add_argument('--index', default='./appstore_help_index.json', help='Index file from discovery step')

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent / args.base_dir if args.base_dir == '.' else Path(args.base_dir)
    index_file = Path(__file__).parent.parent / args.index if args.index.startswith('./') else Path(args.index)

    if not index_file.exists():
        print(f"Error: Index file not found: {index_file}")
        print("Please run 07_discover_appstore_help.py first to create the index")
        return

    downloader = AppStoreHelpDownloader(base_dir=base_dir, index_file=index_file)
    await downloader.download_all()

    print("\nDownload complete!")
    print("\nNext steps:")
    print("  Run 09_html_to_markdown.py to convert HTML to Markdown")


if __name__ == '__main__':
    asyncio.run(main())
