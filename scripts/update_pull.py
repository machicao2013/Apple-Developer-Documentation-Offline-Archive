#!/usr/bin/env python3
"""
Apple Documentation Update Puller
Downloads changed documentation pages (like git pull)
"""

import asyncio
import aiohttp
import json
import hashlib
import time
from pathlib import Path
from typing import Dict, List
from tqdm import tqdm
import argparse
from datetime import datetime
import subprocess
import sys


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


class UpdatePuller:
    """Pulls documentation updates"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.docsync_dir = self.base_dir / '.docsync'
        self.raw_json_dir = self.base_dir / 'raw-json'
        self.markdown_dir = self.base_dir / 'markdown'
        self.manifest_file = self.docsync_dir / 'manifest.json'

        # State
        self.manifest: Dict = {}
        self.pages_to_update: List[Dict] = []

        # Stats
        self.stats = {
            'downloaded': 0,
            'failed': 0,
            'converted': 0,
        }

        # Rate limiting
        self.rate_limiter = RateLimiter(requests_per_second=5.0)

        # User agent
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

    def load_manifest(self):
        """Load the current manifest"""
        if not self.manifest_file.exists():
            print(f"Error: Manifest file not found: {self.manifest_file}")
            exit(1)

        with open(self.manifest_file, 'r') as f:
            self.manifest = json.load(f)

    def save_manifest(self):
        """Save updated manifest"""
        with open(self.manifest_file, 'w') as f:
            json.dump(self.manifest, f, indent=2)

    def load_latest_update_check(self) -> Dict:
        """Load the most recent update check results"""
        cache_dir = self.docsync_dir / 'cache'

        if not cache_dir.exists():
            print("No update check found. Please run update_check.py first.")
            exit(1)

        # Find most recent cache file
        cache_files = sorted(cache_dir.glob('update_check_*.json'), reverse=True)

        if not cache_files:
            print("No update check found. Please run update_check.py first.")
            exit(1)

        with open(cache_files[0], 'r') as f:
            return json.load(f)

    def calculate_sha256(self, content: str) -> str:
        """Calculate SHA256 hash of content"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    async def download_page(self, session: aiohttp.ClientSession, page_info: Dict) -> bool:
        """Download a single updated page"""
        await self.rate_limiter.wait()

        doc_path = page_info['path']
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
                    self.manifest[doc_path]['last_modified'] = response.headers.get('Last-Modified', '')
                    self.manifest[doc_path]['etag'] = response.headers.get('ETag', '')
                    self.manifest[doc_path]['sha256'] = self.calculate_sha256(content)
                    self.manifest[doc_path]['updated_at'] = datetime.now().isoformat()

                    self.stats['downloaded'] += 1
                    return True

                elif response.status == 429:
                    print(f"\nRate limited. Waiting 30 seconds...")
                    await asyncio.sleep(30)
                    return await self.download_page(session, page_info)

                else:
                    print(f"\nError {response.status}: {url}")
                    self.stats['failed'] += 1
                    return False

        except Exception as e:
            print(f"\nException downloading {doc_path}: {e}")
            self.stats['failed'] += 1
            return False

    async def pull_updates(self, frameworks: list = None):
        """Pull all available updates"""
        self.load_manifest()

        # Load latest update check
        update_check = self.load_latest_update_check()
        self.pages_to_update = update_check['updates']['modified']

        # Filter by frameworks if specified
        if frameworks:
            self.pages_to_update = [
                p for p in self.pages_to_update
                if any(p['path'].startswith(f'{fw}/') for fw in frameworks)
            ]

        if not self.pages_to_update:
            print("\nNo updates to download!")
            print("Run update_check.py to check for new updates.")
            return

        print(f"\nDownloading {len(self.pages_to_update)} updated pages...")

        async with aiohttp.ClientSession() as session:
            with tqdm(total=len(self.pages_to_update), desc="Downloading") as pbar:
                for page_info in self.pages_to_update:
                    await self.download_page(session, page_info)
                    pbar.update(1)

                    # Save manifest periodically
                    if self.stats['downloaded'] % 20 == 0:
                        self.save_manifest()

        # Final save
        self.save_manifest()

        print(f"\n Downloaded {self.stats['downloaded']} pages")
        if self.stats['failed'] > 0:
            print(f" Failed: {self.stats['failed']} pages")

    def convert_to_markdown(self):
        """Convert updated pages to Markdown"""
        if self.stats['downloaded'] == 0:
            return

        print(f"\nConverting {self.stats['downloaded']} updated pages to Markdown...")

        # Get the converter script path
        converter_script = Path(__file__).parent / '03_json_to_markdown.py'

        if not converter_script.exists():
            print("Warning: Markdown converter not found. Skipping conversion.")
            return

        # Run converter for each updated page
        # For simplicity, we'll just run the full converter
        # In a production system, you'd want to convert only updated pages
        try:
            result = subprocess.run(
                [sys.executable, str(converter_script), '--base-dir', str(self.base_dir)],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print(" Markdown conversion completed")
                self.stats['converted'] = self.stats['downloaded']
            else:
                print(f"Warning: Markdown conversion had issues:\n{result.stderr}")

        except Exception as e:
            print(f"Error running markdown converter: {e}")

    def create_changelog(self):
        """Create changelog for this update"""
        if self.stats['downloaded'] == 0:
            return

        changelog_file = self.docsync_dir / 'changelog' / f'{datetime.now().strftime("%Y-%m-%d_%H-%M")}.md'
        changelog_file.parent.mkdir(parents=True, exist_ok=True)

        # Group by framework
        by_framework = {}
        for page in self.pages_to_update:
            framework = page['path'].split('/')[0]
            if framework not in by_framework:
                by_framework[framework] = []
            by_framework[framework].append(page)

        # Generate changelog
        lines = [
            f"# Update from {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n",
            f"## Changed Pages ({len(self.pages_to_update)})\n\n"
        ]

        for framework, pages in sorted(by_framework.items()):
            lines.append(f"### {framework.capitalize()} ({len(pages)} changes)\n\n")
            for page in sorted(pages, key=lambda p: p['path']):
                title = page.get('title', '')
                path = page['path']
                lines.append(f"- [{title or path}](../../markdown/{path}.md)\n")
            lines.append('\n')

        lines.append(f"## Statistics\n\n")
        lines.append(f"- Downloaded: {self.stats['downloaded']}\n")
        lines.append(f"- Failed: {self.stats['failed']}\n")
        lines.append(f"- Converted to Markdown: {self.stats['converted']}\n")
        lines.append(f"- Frameworks affected: {len(by_framework)}\n")

        with open(changelog_file, 'w') as f:
            f.writelines(lines)

        print(f"\nChangelog saved to: {changelog_file}")

    def create_version_snapshot(self):
        """Create version snapshot"""
        version_file = self.docsync_dir / 'versions' / f'{datetime.now().strftime("%Y-%m-%d_%H-%M")}.json'
        version_file.parent.mkdir(parents=True, exist_ok=True)

        # Count by framework
        by_framework = {}
        for page in self.pages_to_update:
            framework = page['path'].split('/')[0]
            by_framework[framework] = by_framework.get(framework, 0) + 1

        snapshot = {
            'timestamp': datetime.now().isoformat(),
            'type': 'update',
            'stats': self.stats,
            'pages_updated': len(self.pages_to_update),
            'frameworks_affected': by_framework,
        }

        with open(version_file, 'w') as f:
            json.dump(snapshot, f, indent=2)

        print(f"Version snapshot saved to: {version_file}")


async def main():
    parser = argparse.ArgumentParser(description='Pull Apple documentation updates')
    parser.add_argument('--frameworks', nargs='+', help='Frameworks to update (default: all)')
    parser.add_argument('--base-dir', default='.', help='Base directory (default: project directory)')
    parser.add_argument('--no-convert', action='store_true', help='Skip Markdown conversion')

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent / args.base_dir if args.base_dir == '.' else Path(args.base_dir)

    puller = UpdatePuller(base_dir=base_dir)

    # Pull updates
    await puller.pull_updates(frameworks=args.frameworks)

    # Convert to Markdown
    if not args.no_convert and puller.stats['downloaded'] > 0:
        puller.convert_to_markdown()

    # Create changelog
    puller.create_changelog()

    # Create version snapshot
    if puller.stats['downloaded'] > 0:
        puller.create_version_snapshot()

    print("\n" + "="*60)
    print("Update Complete!")
    print("="*60)
    if puller.stats['downloaded'] > 0:
        print(f"\n {puller.stats['downloaded']} pages updated successfully")
        print(f"\nView changelog at: .docsync/changelog/")


if __name__ == '__main__':
    asyncio.run(main())
