#!/usr/bin/env python3
"""
App Store Connect Help HTML to Markdown Converter
Converts extracted HTML content to clean Markdown format
"""

import json
import re
from pathlib import Path
from typing import Dict
from tqdm import tqdm
import argparse
from bs4 import BeautifulSoup, NavigableString, Tag
import yaml


class AppStoreHtmlToMarkdown:
    """Converts App Store Connect Help HTML to Markdown"""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.raw_html_dir = self.base_dir / 'raw-html' / 'appstore-connect'
        self.markdown_dir = self.base_dir / 'markdown' / 'appstore-connect'
        self.docsync_dir = self.base_dir / '.docsync'

        # Create markdown directory
        self.markdown_dir.mkdir(parents=True, exist_ok=True)

        # Track used filenames for deduplication
        self.used_filenames: Dict[str, int] = {}

        # Stats
        self.stats = {
            'converted': 0,
            'failed': 0,
            'skipped': 0,
        }

    def load_manifest(self) -> Dict:
        """Load the manifest"""
        manifest_file = self.docsync_dir / 'appstore_manifest.json'
        with open(manifest_file, 'r') as f:
            return json.load(f)

    def sanitize_filename(self, title: str) -> str:
        """Convert title to safe filename"""
        # Remove " - App Store Connect" or similar suffixes
        title = re.sub(r'\s*[-–—]\s*App Store Connect.*$', '', title, flags=re.IGNORECASE)

        # Convert to lowercase
        filename = title.lower()

        # Replace spaces and special chars with hyphens
        filename = re.sub(r'[^\w\s-]', '', filename)
        filename = re.sub(r'[-\s]+', '-', filename)

        # Remove leading/trailing hyphens
        filename = filename.strip('-')

        # Truncate to 100 chars
        if len(filename) > 100:
            filename = filename[:100].rsplit('-', 1)[0]

        # Ensure not empty
        if not filename:
            filename = 'untitled'

        # Handle duplicates
        if filename in self.used_filenames:
            self.used_filenames[filename] += 1
            filename = f"{filename}-{self.used_filenames[filename]}"
        else:
            self.used_filenames[filename] = 1

        return filename + '.md'

    def convert_element_to_markdown(self, element, depth=0) -> str:
        """Convert HTML element to Markdown recursively"""
        if isinstance(element, NavigableString):
            return str(element)

        if not isinstance(element, Tag):
            return ''

        result = []
        tag_name = element.name

        # Headings
        if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag_name[1])
            text = element.get_text().strip()
            result.append(f"\n{'#' * level} {text}\n\n")

        # Paragraphs
        elif tag_name == 'p':
            text = self.convert_children(element)
            result.append(f"{text}\n\n")

        # Lists
        elif tag_name == 'ul':
            for li in element.find_all('li', recursive=False):
                text = self.convert_children(li)
                result.append(f"- {text.strip()}\n")
            result.append('\n')

        elif tag_name == 'ol':
            for i, li in enumerate(element.find_all('li', recursive=False), 1):
                text = self.convert_children(li)
                result.append(f"{i}. {text.strip()}\n")
            result.append('\n')

        # Code blocks
        elif tag_name == 'pre':
            code = element.get_text()
            # Try to detect language
            lang = ''
            code_tag = element.find('code')
            if code_tag and code_tag.get('class'):
                classes = code_tag.get('class')
                for cls in classes:
                    if cls.startswith('language-'):
                        lang = cls.replace('language-', '')
            result.append(f"```{lang}\n{code}\n```\n\n")

        # Inline code
        elif tag_name == 'code' and element.parent.name != 'pre':
            text = element.get_text()
            result.append(f"`{text}`")

        # Bold
        elif tag_name in ['strong', 'b']:
            text = self.convert_children(element)
            result.append(f"**{text}**")

        # Italic
        elif tag_name in ['em', 'i']:
            text = self.convert_children(element)
            result.append(f"*{text}*")

        # Links
        elif tag_name == 'a':
            text = self.convert_children(element)
            href = element.get('href', '')
            if href:
                result.append(f"[{text}]({href})")
            else:
                result.append(text)

        # Images
        elif tag_name == 'img':
            alt = element.get('alt', '')
            src = element.get('src', '')
            result.append(f"![{alt}]({src})\n\n")

        # Blockquotes
        elif tag_name == 'blockquote':
            text = self.convert_children(element)
            lines = text.strip().split('\n')
            quoted = '\n'.join(f"> {line}" for line in lines)
            result.append(f"{quoted}\n\n")

        # Tables
        elif tag_name == 'table':
            result.append(self.convert_table(element))

        # Line breaks
        elif tag_name == 'br':
            result.append('\n')

        # Divs and other containers - process children
        else:
            result.append(self.convert_children(element))

        return ''.join(result)

    def convert_children(self, element) -> str:
        """Convert all children of an element"""
        result = []
        for child in element.children:
            result.append(self.convert_element_to_markdown(child))
        return ''.join(result)

    def convert_table(self, table) -> str:
        """Convert HTML table to Markdown table"""
        rows = []

        # Process header
        thead = table.find('thead')
        if thead:
            header_row = thead.find('tr')
            if header_row:
                cells = [th.get_text().strip() for th in header_row.find_all(['th', 'td'])]
                rows.append('| ' + ' | '.join(cells) + ' |')
                rows.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')

        # Process body
        tbody = table.find('tbody') or table
        for tr in tbody.find_all('tr'):
            cells = [td.get_text().strip() for td in tr.find_all(['td', 'th'])]
            if cells:  # Skip empty rows
                rows.append('| ' + ' | '.join(cells) + ' |')

        return '\n'.join(rows) + '\n\n'

    def convert_html_to_markdown(self, html_path: Path, url: str) -> tuple[str, str]:
        """Convert HTML file to Markdown, return (markdown, title)"""
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'html.parser')

        # Extract title
        title_tag = soup.find('title')
        h1_tag = soup.find('h1')

        if title_tag:
            title = title_tag.get_text().strip()
        elif h1_tag:
            title = h1_tag.get_text().strip()
        else:
            title = 'Untitled'

        # Generate YAML frontmatter
        frontmatter = {
            'title': title,
            'url': url,
            'category': 'App Store Connect Help',
            'downloaded_at': html_path.stat().st_mtime,
        }

        yaml_str = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        markdown = f"---\n{yaml_str}---\n\n"

        # Add title as H1 if not already present
        if not h1_tag:
            markdown += f"# {title}\n\n"

        # Convert body content
        body_content = self.convert_element_to_markdown(soup)
        markdown += body_content

        # Clean up excessive newlines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown, title

    def convert_all(self):
        """Convert all HTML files to Markdown"""
        manifest = self.load_manifest()

        print(f"\nConverting {len(manifest)} pages to Markdown...")

        with tqdm(total=len(manifest), desc="Converting") as pbar:
            for url, metadata in manifest.items():
                try:
                    html_path = self.base_dir / metadata['local_path']

                    if not html_path.exists():
                        print(f"\nWarning: HTML file not found: {html_path}")
                        self.stats['skipped'] += 1
                        pbar.update(1)
                        continue

                    # Convert to Markdown
                    markdown, title = self.convert_html_to_markdown(html_path, url)

                    # Generate filename
                    filename = self.sanitize_filename(title)
                    md_path = self.markdown_dir / filename

                    # Save Markdown file
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(markdown)

                    self.stats['converted'] += 1

                except Exception as e:
                    print(f"\nError converting {url}: {e}")
                    self.stats['failed'] += 1

                pbar.update(1)

        # Print stats
        print("\n" + "="*60)
        print("Conversion Statistics:")
        print(f"  Successfully converted: {self.stats['converted']}")
        print(f"  Failed: {self.stats['failed']}")
        print(f"  Skipped: {self.stats['skipped']}")
        print("="*60)


def main():
    parser = argparse.ArgumentParser(description='Convert App Store Connect Help HTML to Markdown')
    parser.add_argument('--base-dir', default='.', help='Base directory (default: project directory)')

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent / args.base_dir if args.base_dir == '.' else Path(args.base_dir)

    # Check if manifest exists
    manifest_file = base_dir / '.docsync' / 'appstore_manifest.json'
    if not manifest_file.exists():
        print(f"Error: Manifest file not found: {manifest_file}")
        print("Please run 08_download_appstore_html.py first to download the documentation")
        return

    converter = AppStoreHtmlToMarkdown(base_dir=base_dir)
    converter.convert_all()

    print("\nConversion complete!")
    print(f"Markdown files saved to: {converter.markdown_dir}")
    print("\nYou can now:")
    print("  - Browse markdown files in markdown/appstore-connect/")
    print("  - Use them with AI/LLM tools")
    print("  - Run 06_markdown_merge.py to merge into single file")


if __name__ == '__main__':
    main()
