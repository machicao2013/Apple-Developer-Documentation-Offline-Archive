#!/usr/bin/env python3
"""
Apple Documentation JSON Downloader
Downloads all discovered documentation pages as JSON files and creates manifest
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


class DocumentationDownloader:
    """Downloads all documentation JSON files"""

    def __init__(self, base_dir: Path, index_file: Path):
        self.base_dir = Path(base_dir)
        self.index_file = Path(index_file)

        # Directories
        self.raw_json_dir = self.base_dir / 'raw-json'
        self.docsync_dir = self.base_dir / '.docsync'

        # Create directories
        self.raw_json_dir.mkdir(parents=True, exist_ok=True)
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
        manifest_file = self.docsync_dir / 'manifest.json'
        if manifest_file.exists():
            with open(manifest_file, 'r') as f:
                self.manifest = json.load(f)
            print(f"Loaded existing manifest with {len(self.manifest)} entries")

    def save_manifest(self):
        """Save manifest to disk"""
        manifest_file = self.docsync_dir / 'manifest.json'
        with open(manifest_file, 'w') as f:
            json.dump(self.manifest, f, indent=2)

    def calculate_sha256(self, content: str) -> str:
        """Calculate SHA256 hash of content"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    async def download_page(self, session: aiohttp.ClientSession, doc_path: str) -> bool:
        """Download a single documentation page"""
        await self.rate_limiter.wait()

        url = f'https://developer.apple.com/tutorials/data/documentation/{doc_path}.json'
        headers = {'User-Agent': self.user_agent}

        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    content = await response.text()
                    data = json.loads(content)

                    # Save JSON file
                    output_file = self.raw_json_dir / f'{doc_path}.json'
                    output_file.parent.mkdir(parents=True, exist_ok=True)

                    with open(output_file, 'w') as f:
                        json.dump(data, f, indent=2)

                    # Update manifest
                    self.manifest[doc_path] = {
                        'url': url,
                        'local_path': str(output_file.relative_to(self.base_dir)),
                        'last_modified': response.headers.get('Last-Modified', ''),
                        'etag': response.headers.get('ETag', ''),
                        'sha256': self.calculate_sha256(content),
                        'downloaded_at': datetime.now().isoformat(),
                        'title': data.get('metadata', {}).get('title', ''),
                        'role': data.get('metadata', {}).get('role', ''),
                    }

                    self.downloaded.add(doc_path)
                    self.stats['downloaded'] += 1
                    return True

                elif response.status == 404:
                    print(f"\n404 Not Found: {url}")
                    self.stats['failed'] += 1
                    return False

                elif response.status == 429:
                    # Rate limited
                    print(f"\nRate limited. Waiting 30 seconds...")
                    await asyncio.sleep(30)
                    return await self.download_page(session, doc_path)

                else:
                    print(f"\nError {response.status}: {url}")
                    self.stats['failed'] += 1
                    return False

        except Exception as e:
            print(f"\nException downloading {doc_path}: {e}")
            self.stats['failed'] += 1
            return False

    async def download_all(self, frameworks: list = None):
        """Download all pages from index"""
        # Load index
        index = self.load_index()

        # Load existing manifest
        self.load_manifest()

        # Get list of pages to download
        pages_to_download = []

        if frameworks:
            for framework in frameworks:
                if framework in index['frameworks']:
                    pages_to_download.extend(index['frameworks'][framework])
        else:
            # Download all frameworks
            for framework_pages in index['frameworks'].values():
                pages_to_download.extend(framework_pages)

        # Filter out already downloaded (if resuming)
        if self.manifest:
            pages_to_download = [p for p in pages_to_download if p not in self.manifest]
            self.stats['skipped'] = len(self.manifest)

        self.stats['total'] = len(pages_to_download)

        print(f"\nDownloading {self.stats['total']} pages...")
        if self.stats['skipped'] > 0:
            print(f"Skipping {self.stats['skipped']} already downloaded pages")

        # Download in batches
        batch_size = 10

        async with aiohttp.ClientSession() as session:
            with tqdm(total=len(pages_to_download), desc="Downloading") as pbar:
                for i in range(0, len(pages_to_download), batch_size):
                    batch = pages_to_download[i:i+batch_size]

                    # Download batch concurrently
                    tasks = [self.download_page(session, doc_path) for doc_path in batch]
                    await asyncio.gather(*tasks)

                    pbar.update(len(batch))

                    # Save manifest periodically
                    if i % 100 == 0:
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

        print(f"\nManifest saved to: {self.docsync_dir / 'manifest.json'}")

    def create_initial_version_snapshot(self):
        """Create initial version snapshot"""
        version_file = self.docsync_dir / 'versions' / f'{datetime.now().strftime("%Y-%m-%d_%H-%M")}.json'
        version_file.parent.mkdir(parents=True, exist_ok=True)

        snapshot = {
            'timestamp': datetime.now().isoformat(),
            'type': 'initial_download',
            'stats': self.stats,
            'total_pages': len(self.manifest),
            'frameworks': {},
        }

        # Count pages per framework
        for doc_path in self.manifest.keys():
            framework = doc_path.split('/')[0]
            snapshot['frameworks'][framework] = snapshot['frameworks'].get(framework, 0) + 1

        with open(version_file, 'w') as f:
            json.dump(snapshot, f, indent=2)

        print(f"Version snapshot saved to: {version_file}")


async def main():
    parser = argparse.ArgumentParser(description='Download Apple documentation JSON files')
    parser.add_argument('--frameworks', nargs='+', help='Frameworks to download (default: all)')
    parser.add_argument('--base-dir', default='.', help='Base directory (default: project directory)')
    parser.add_argument('--index', default='./index.json', help='Index file from discovery step')

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent / args.base_dir if args.base_dir == '.' else Path(args.base_dir)
    index_file = Path(__file__).parent.parent / args.index if args.index.startswith('./') else Path(args.index)

    if not index_file.exists():
        print(f"Error: Index file not found: {index_file}")
        print("Please run 01_discover_docs.py first to create the index")
        return

    downloader = DocumentationDownloader(base_dir=base_dir, index_file=index_file)
    await downloader.download_all(frameworks=args.frameworks)

    # Create initial version snapshot
    downloader.create_initial_version_snapshot()

    print("\nDownload complete!")
    print("\nNext steps:")
    print("  1. Run 03_json_to_markdown.py to convert JSON to Markdown")
    print("  2. Use update_check.py in the future to check for documentation updates")


if __name__ == '__main__':
    asyncio.run(main())
