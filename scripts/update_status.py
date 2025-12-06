#!/usr/bin/env python3
"""
Apple Documentation Update Status
Shows current update status (like git status)
"""

import json
from pathlib import Path
from datetime import datetime
import argparse


class UpdateStatus:
    """Shows current documentation status"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.docsync_dir = self.base_dir / '.docsync'
        self.manifest_file = self.docsync_dir / 'manifest.json'

        # State
        self.manifest = {}
        self.latest_check = None
        self.latest_version = None

    def load_manifest(self):
        """Load the current manifest"""
        if not self.manifest_file.exists():
            print("No documentation found.")
            print("Run 02_download_json.py to download the initial documentation.")
            return False

        with open(self.manifest_file, 'r') as f:
            self.manifest = json.load(f)

        return True

    def load_latest_update_check(self):
        """Load the most recent update check"""
        cache_dir = self.docsync_dir / 'cache'

        if not cache_dir.exists() or not list(cache_dir.glob('update_check_*.json')):
            return None

        cache_files = sorted(cache_dir.glob('update_check_*.json'), reverse=True)

        with open(cache_files[0], 'r') as f:
            return json.load(f)

    def load_latest_version(self):
        """Load the most recent version snapshot"""
        versions_dir = self.docsync_dir / 'versions'

        if not versions_dir.exists() or not list(versions_dir.glob('*.json')):
            return None

        version_files = sorted(versions_dir.glob('*.json'), reverse=True)

        with open(version_files[0], 'r') as f:
            return json.load(f)

    def format_timestamp(self, iso_timestamp: str) -> str:
        """Format ISO timestamp to readable string"""
        try:
            dt = datetime.fromisoformat(iso_timestamp)
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return iso_timestamp

    def format_time_ago(self, iso_timestamp: str) -> str:
        """Format ISO timestamp as 'time ago'"""
        try:
            dt = datetime.fromisoformat(iso_timestamp)
            now = datetime.now()
            diff = now - dt

            if diff.days > 365:
                return f"{diff.days // 365} year(s) ago"
            elif diff.days > 30:
                return f"{diff.days // 30} month(s) ago"
            elif diff.days > 0:
                return f"{diff.days} day(s) ago"
            elif diff.seconds > 3600:
                return f"{diff.seconds // 3600} hour(s) ago"
            elif diff.seconds > 60:
                return f"{diff.seconds // 60} minute(s) ago"
            else:
                return "just now"
        except:
            return ""

    def print_status(self):
        """Print current status"""
        print("\n" + "="*70)
        print("Apple Documentation Status")
        print("="*70)

        if not self.load_manifest():
            return

        # Load latest check and version
        self.latest_check = self.load_latest_update_check()
        self.latest_version = self.load_latest_version()

        # Current documentation info
        print(f"\nCurrent Documentation:")
        print(f"  Total pages: {len(self.manifest)}")

        # Count by framework
        by_framework = {}
        for doc_path in self.manifest.keys():
            framework = doc_path.split('/')[0]
            by_framework[framework] = by_framework.get(framework, 0) + 1

        print(f"  Frameworks: {len(by_framework)}")
        for framework, count in sorted(by_framework.items())[:10]:
            print(f"    - {framework}: {count} pages")
        if len(by_framework) > 10:
            print(f"    ... and {len(by_framework) - 10} more")

        # Latest version info
        if self.latest_version:
            print(f"\n Latest Snapshot:")
            timestamp = self.latest_version.get('timestamp', '')
            print(f"  Date: {self.format_timestamp(timestamp)} ({self.format_time_ago(timestamp)})")
            print(f"  Type: {self.latest_version.get('type', 'unknown')}")

            if 'stats' in self.latest_version:
                stats = self.latest_version['stats']
                if 'downloaded' in stats:
                    print(f"  Downloaded: {stats['downloaded']} pages")

        # Latest update check
        if self.latest_check:
            print(f"\n Latest Update Check:")
            timestamp = self.latest_check.get('timestamp', '')
            print(f"  Checked: {self.format_timestamp(timestamp)} ({self.format_time_ago(timestamp)})")

            updates = self.latest_check.get('updates', {})
            modified = updates.get('modified', [])

            if modified:
                print(f"\n  Updates available: {len(modified)} pages")
                print(f"\n  Modified pages (showing first 10):")
                for page in modified[:10]:
                    title = page.get('title', '')
                    path = page.get('path', '')
                    print(f"    - {title or path}")

                if len(modified) > 10:
                    print(f"    ... and {len(modified) - 10} more")

                print(f"\n  To download updates, run:")
                print(f"    python scripts/update_pull.py")
            else:
                print(f"\n  No updates available")
                print(f"  All documentation is up to date!")

        else:
            print(f"\n No update check found")
            print(f"  Run: python scripts/update_check.py")

        # Recent changelogs
        changelog_dir = self.docsync_dir / 'changelog'
        if changelog_dir.exists():
            changelogs = sorted(changelog_dir.glob('*.md'), reverse=True)[:5]
            if changelogs:
                print(f"\n Recent Updates:")
                for changelog in changelogs:
                    print(f"  - {changelog.name}")

        print("\n" + "="*70)
        print("\nAvailable Commands:")
        print("  python scripts/update_check.py    - Check for updates")
        print("  python scripts/update_pull.py     - Download updates")
        print("  python scripts/update_status.py   - Show this status")
        print("="*70)


def main():
    parser = argparse.ArgumentParser(description='Show Apple documentation status')
    parser.add_argument('--base-dir', default='.', help='Base directory (default: project directory)')

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent / args.base_dir if args.base_dir == '.' else Path(args.base_dir)

    status = UpdateStatus(base_dir=base_dir)
    status.print_status()


if __name__ == '__main__':
    main()
