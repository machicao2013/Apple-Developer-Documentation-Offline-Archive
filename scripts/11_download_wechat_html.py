#!/usr/bin/env python3
"""
WeChat Pay Documentation HTML Downloader
Downloads HTML content for all discovered pages
"""

import asyncio
import aiohttp
import json
import time
import hashlib
from pathlib import Path
from typing import Dict, Optional
from tqdm import tqdm
import argparse
from datetime import datetime


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


class WeChatPayDownloader:
    """Downloads HTML content for WeChat Pay documentation"""

    def __init__(self, output_dir: Path, html_dir: Path):
        self.output_dir = Path(output_dir)
        self.html_dir = Path(html_dir)
        self.html_dir.mkdir(parents=True, exist_ok=True)

        # Manifest for tracking downloads
        self.manifest_file = self.output_dir / '.docsync' / 'wechat_manifest.json'
        self.manifest_file.parent.mkdir(parents=True, exist_ok=True)
        self.manifest: Dict[str, dict] = {}

        # Rate limiting
        self.rate_limiter = RateLimiter(requests_per_second=5.0)

        # User agent
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

        # Stats
        self.stats = {
            'downloaded': 0,
            'skipped': 0,
            'failed': 0,
        }

    def load_manifest(self):
        """Load existing manifest"""
        if self.manifest_file.exists():
            with open(self.manifest_file, 'r', encoding='utf-8') as f:
                self.manifest = json.load(f)
            print(f"Loaded manifest with {len(self.manifest)} entries")

    def save_manifest(self):
        """Save manifest"""
        with open(self.manifest_file, 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, indent=2, ensure_ascii=False)

    def url_to_filename(self, url: str) -> str:
        """Convert URL to filename"""
        # Extract the ID from URL
        # Example: https://pay.weixin.qq.com/doc/v3/merchant/4012062524 -> merchant_4012062524.html
        parts = url.split('/')
        if len(parts) >= 6:
            doc_type = parts[-2]  # merchant or partner
            doc_id = parts[-1]
            return f"{doc_type}_{doc_id}.html"
        else:
            # Fallback: use hash
            url_hash = hashlib.md5(url.encode()).hexdigest()[:16]
            return f"doc_{url_hash}.html"

    def get_content_hash(self, content: str) -> str:
        """Calculate content hash"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    async def fetch_page(self, session: aiohttp.ClientSession, url: str) -> Optional[tuple]:
        """Fetch HTML page with rate limiting"""
        await self.rate_limiter.wait()

        headers = {'User-Agent': self.user_agent}

        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    content = await response.text()
                    etag = response.headers.get('ETag', '')
                    return content, etag
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

    def should_download(self, url: str, filepath: Path) -> bool:
        """Check if file should be downloaded"""
        # If file doesn't exist, download
        if not filepath.exists():
            return True

        # If not in manifest, download
        if url not in self.manifest:
            return True

        # File exists and is tracked - skip
        return False

    async def download_page(self, session: aiohttp.ClientSession, url: str, metadata: dict) -> bool:
        """Download a single page"""
        filename = self.url_to_filename(url)
        filepath = self.html_dir / filename

        # Check if we should download
        if not self.should_download(url, filepath):
            self.stats['skipped'] += 1
            return True

        # Fetch page
        result = await self.fetch_page(session, url)
        if not result:
            self.stats['failed'] += 1
            return False

        content, etag = result

        # Calculate content hash
        content_hash = self.get_content_hash(content)

        # Save HTML
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        # Update manifest
        self.manifest[url] = {
            'filename': filename,
            'etag': etag,
            'content_hash': content_hash,
            'downloaded_at': datetime.now().isoformat(),
            'title': metadata.get('title', ''),
            'h1': metadata.get('h1', ''),
            'last_updated': metadata.get('last_updated', ''),
        }

        self.stats['downloaded'] += 1
        return True

    async def download_all(self, index_file: Path):
        """Download all pages from index"""
        # Load index
        if not index_file.exists():
            print(f"Error: Index file not found: {index_file}")
            print("Please run 10_discover_wechat_pay.py first")
            return

        with open(index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)

        pages = index['pages']
        print(f"\nDownloading {len(pages)} pages...")

        async with aiohttp.ClientSession() as session:
            with tqdm(total=len(pages), desc="Downloading HTML") as pbar:
                for page in pages:
                    url = page['url']
                    await self.download_page(session, url, page)
                    pbar.update(1)

                    # Save manifest periodically
                    if (self.stats['downloaded'] + self.stats['skipped']) % 10 == 0:
                        self.save_manifest()

        # Final save
        self.save_manifest()

        # Print stats
        print(f"\n{'='*60}")
        print(f"Download complete!")
        print(f"{'='*60}")
        print(f"Downloaded: {self.stats['downloaded']}")
        print(f"Skipped (already exists): {self.stats['skipped']}")
        print(f"Failed: {self.stats['failed']}")
        print(f"Total: {len(pages)}")
        print(f"\nHTML files saved to: {self.html_dir}")
        print(f"Manifest saved to: {self.manifest_file}")


async def main():
    parser = argparse.ArgumentParser(description='Download WeChat Pay documentation HTML')
    parser.add_argument('--output', default='.', help='Output directory (default: project directory)')
    parser.add_argument('--html-dir', default='raw-html/wechat-pay', help='HTML output directory')

    args = parser.parse_args()

    # Setup paths
    output_dir = Path(__file__).parent.parent / args.output if args.output == '.' else Path(args.output)
    html_dir = output_dir / args.html_dir

    # Check for index file
    index_file = output_dir / 'wechat_pay_index.json'

    # Create downloader
    downloader = WeChatPayDownloader(output_dir=output_dir, html_dir=html_dir)
    downloader.load_manifest()

    # Download all pages
    await downloader.download_all(index_file)

    print("\nNext steps:")
    print("  Run 12_wechat_html_to_markdown.py to convert HTML to Markdown")


if __name__ == '__main__':
    asyncio.run(main())
