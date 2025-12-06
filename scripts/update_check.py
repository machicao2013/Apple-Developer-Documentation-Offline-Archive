#!/usr/bin/env python3
"""
Apple Documentation Update Checker
Checks for new and updated documentation (like git fetch)
"""

import asyncio
import aiohttp
import json
import hashlib
from pathlib import Path
from typing import Dict, Set
from tqdm import tqdm
import argparse
from datetime import datetime


class RateLimiter:
    """Rate limiter to avoid overwhelming Apple's servers"""

    def __init__(self, requests_per_second: float = 10.0):
        import time
        self.delay = 1.0 / requests_per_second
        self.last_request = 0.0
        self.time = time

    async def wait(self):
        now = self.time.time()
        time_since_last = now - self.last_request
        if time_since_last < self.delay:
            await asyncio.sleep(self.delay - time_since_last)
        self.last_request = self.time.time()


class UpdateChecker:
    """Checks for documentation updates"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.docsync_dir = self.base_dir / '.docsync'
        self.manifest_file = self.docsync_dir / 'manifest.json'

        # State
        self.manifest: Dict = {}
        self.updates = {
            'new': [],
            'modified': [],
            'unchanged': [],
        }

        # Rate limiting
        self.rate_limiter = RateLimiter(requests_per_second=10.0)

        # User agent
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

    def load_manifest(self):
        """Load the current manifest"""
        if not self.manifest_file.exists():
            print(f"Error: Manifest file not found: {self.manifest_file}")
            print("Please run 02_download_json.py first to download the initial documentation")
            exit(1)

        with open(self.manifest_file, 'r') as f:
            self.manifest = json.load(f)

    async def check_page_etag(self, session: aiohttp.ClientSession, doc_path: str, current_etag: str) -> str:
        """Check if a page has been updated using ETag"""
        await self.rate_limiter.wait()

        url = f'https://developer.apple.com/tutorials/data/documentation/{doc_path}.json'
        headers = {'User-Agent': self.user_agent}

        try:
            async with session.head(url, headers=headers) as response:
                if response.status == 200:
                    new_etag = response.headers.get('ETag', '')
                    if new_etag and new_etag != current_etag:
                        return 'modified'
                    else:
                        return 'unchanged'
                elif response.status == 404:
                    return 'deleted'
                else:
                    return 'unknown'

        except Exception as e:
            print(f"\nError checking {doc_path}: {e}")
            return 'error'

    async def check_all_pages(self, frameworks: list = None):
        """Check all pages for updates"""
        self.load_manifest()

        # Filter by frameworks if specified
        if frameworks:
            pages_to_check = {
                k: v for k, v in self.manifest.items()
                if any(k.startswith(f'{fw}/') for fw in frameworks)
            }
        else:
            pages_to_check = self.manifest

        print(f"\nChecking {len(pages_to_check)} pages for updates...")

        async with aiohttp.ClientSession() as session:
            with tqdm(total=len(pages_to_check), desc="Checking") as pbar:
                for doc_path, metadata in pages_to_check.items():
                    current_etag = metadata.get('etag', '')

                    status = await self.check_page_etag(session, doc_path, current_etag)

                    if status == 'modified':
                        self.updates['modified'].append({
                            'path': doc_path,
                            'title': metadata.get('title', ''),
                            'url': metadata.get('url', ''),
                        })
                    elif status == 'unchanged':
                        self.updates['unchanged'].append(doc_path)

                    pbar.update(1)

    def discover_new_pages(self):
        """Discover new pages by checking framework roots"""
        # This would require re-running the discovery crawler
        # For now, we'll note this as a TODO
        print("\nNote: Discovery of completely new pages requires running 01_discover_docs.py")
        print("      This check only detects changes to existing pages")

    def save_update_cache(self):
        """Save update check results"""
        cache_file = self.docsync_dir / 'cache' / f'update_check_{datetime.now().strftime("%Y-%m-%d_%H-%M")}.json'
        cache_file.parent.mkdir(parents=True, exist_ok=True)

        cache_data = {
            'timestamp': datetime.now().isoformat(),
            'updates': self.updates,
            'total_checked': len(self.manifest),
            'modified_count': len(self.updates['modified']),
            'unchanged_count': len(self.updates['unchanged']),
        }

        with open(cache_file, 'w') as f:
            json.dump(cache_data, f, indent=2)

        return cache_file

    def print_summary(self):
        """Print update summary"""
        print("\n" + "="*70)
        print("Update Check Summary")
        print("="*70)

        if self.updates['modified']:
            print(f"\n Updates available: {len(self.updates['modified'])} pages\n")

            print("Modified pages:")
            for update in self.updates['modified'][:20]:  # Show first 20
                print(f"  [CHANGED] {update['path']}")
                if update['title']:
                    print(f"            {update['title']}")

            if len(self.updates['modified']) > 20:
                print(f"\n  ... and {len(self.updates['modified']) - 20} more")

            print(f"\nTotal: {len(self.updates['modified'])} modified pages")
            print(f"\nTo download updates, run:")
            print(f"  python scripts/update_pull.py")

        else:
            print("\n All documentation is up to date!")

        print(f"\nChecked: {len(self.manifest)} pages")
        print(f"Modified: {len(self.updates['modified'])}")
        print(f"Unchanged: {len(self.updates['unchanged'])}")
        print("="*70)


async def main():
    parser = argparse.ArgumentParser(description='Check for Apple documentation updates')
    parser.add_argument('--frameworks', nargs='+', help='Frameworks to check (default: all)')
    parser.add_argument('--base-dir', default='.', help='Base directory (default: project directory)')

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent / args.base_dir if args.base_dir == '.' else Path(args.base_dir)

    checker = UpdateChecker(base_dir=base_dir)
    await checker.check_all_pages(frameworks=args.frameworks)

    # Save results
    cache_file = checker.save_update_cache()
    print(f"\nUpdate check results cached to: {cache_file}")

    # Print summary
    checker.print_summary()


if __name__ == '__main__':
    asyncio.run(main())
