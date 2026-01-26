#!/usr/bin/env python3
"""
WeChat Pay HTML to Markdown Converter
Converts downloaded HTML to clean, AI-readable Markdown
"""

import json
import re
from pathlib import Path
from typing import Dict, Optional
from tqdm import tqdm
import argparse
from bs4 import BeautifulSoup, Tag, NavigableString
from datetime import datetime


class WeChatPayMarkdownConverter:
    """Converts WeChat Pay HTML documentation to Markdown"""

    def __init__(self, html_dir: Path, markdown_dir: Path, manifest_file: Path):
        self.html_dir = Path(html_dir)
        self.markdown_dir = Path(markdown_dir)
        self.markdown_dir.mkdir(parents=True, exist_ok=True)

        self.manifest_file = Path(manifest_file)
        self.manifest: Dict[str, dict] = {}

        # Stats
        self.stats = {
            'converted': 0,
            'skipped': 0,
            'failed': 0,
        }

    def load_manifest(self):
        """Load manifest with file metadata"""
        if self.manifest_file.exists():
            with open(self.manifest_file, 'r', encoding='utf-8') as f:
                self.manifest = json.load(f)
            print(f"Loaded manifest with {len(self.manifest)} entries")
        else:
            print("Warning: Manifest not found. Please run 11_download_wechat_html.py first")

    def sanitize_filename(self, text: str) -> str:
        """Convert text to safe filename"""
        # Remove or replace invalid characters
        text = re.sub(r'[<>:"/\\|?*]', '', text)
        text = re.sub(r'\s+', '_', text)
        text = text.strip('._')

        # Limit length
        if len(text) > 100:
            text = text[:100]

        return text or 'untitled'

    def extract_main_content(self, soup: BeautifulSoup) -> Optional[Tag]:
        """Extract main content from HTML"""
        # Try to find main content area
        main_content = soup.find('div', id='main-content')
        if main_content:
            return main_content

        # Fallback: try other selectors
        main_content = soup.find('div', class_='page-content')
        if main_content:
            return main_content

        return None

    def convert_element_to_markdown(self, element, depth=0) -> str:
        """Recursively convert HTML element to Markdown"""
        if isinstance(element, NavigableString):
            text = str(element).strip()
            return text if text else ''

        if not isinstance(element, Tag):
            return ''

        markdown = ''
        tag_name = element.name

        # Headings
        if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag_name[1])
            text = element.get_text().strip()
            markdown = f"\n\n{'#' * level} {text}\n\n"

        # Paragraphs
        elif tag_name == 'p':
            text = self.convert_children(element)
            if text.strip():
                markdown = f"{text}\n\n"

        # Lists
        elif tag_name == 'ul':
            for li in element.find_all('li', recursive=False):
                text = self.convert_children(li)
                markdown += f"- {text}\n"
            markdown += '\n'

        elif tag_name == 'ol':
            for i, li in enumerate(element.find_all('li', recursive=False), 1):
                text = self.convert_children(li)
                markdown += f"{i}. {text}\n"
            markdown += '\n'

        # Code blocks
        elif tag_name == 'pre':
            code = element.get_text()
            # Try to detect language from class
            code_tag = element.find('code')
            lang = ''
            if code_tag and code_tag.get('class'):
                classes = code_tag.get('class')
                for cls in classes:
                    if cls.startswith('language-'):
                        lang = cls.replace('language-', '')
                        break
            markdown = f"\n```{lang}\n{code}\n```\n\n"

        elif tag_name == 'code' and element.parent.name != 'pre':
            text = element.get_text()
            markdown = f"`{text}`"

        # Tables
        elif tag_name == 'table':
            markdown = self.convert_table(element)

        # Links
        elif tag_name == 'a':
            text = self.convert_children(element)
            href = element.get('href', '')
            if href and text:
                markdown = f"[{text}]({href})"
            else:
                markdown = text

        # Images
        elif tag_name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '') or element.get('name', '')
            if src:
                markdown = f"\n![{alt}]({src})\n\n"

        # Bold
        elif tag_name in ['strong', 'b']:
            text = self.convert_children(element)
            markdown = f"**{text}**"

        # Italic
        elif tag_name in ['em', 'i']:
            text = self.convert_children(element)
            markdown = f"*{text}*"

        # Span with special styling
        elif tag_name == 'span':
            style = element.get('style', '')
            text = self.convert_children(element)

            # Check for bold
            if 'font-weight: bold' in style or 'font-weight:bold' in style:
                markdown = f"**{text}**"
            else:
                markdown = text

        # Divs - recurse into children
        elif tag_name == 'div':
            markdown = self.convert_children(element)

        # Default: recurse into children
        else:
            markdown = self.convert_children(element)

        return markdown

    def convert_children(self, element) -> str:
        """Convert all children of an element"""
        result = ''
        for child in element.children:
            result += self.convert_element_to_markdown(child)
        return result

    def convert_table(self, table: Tag) -> str:
        """Convert HTML table to Markdown table"""
        markdown = '\n'

        rows = table.find_all('tr')
        if not rows:
            return ''

        # Extract headers
        headers = []
        first_row = rows[0]
        header_cells = first_row.find_all(['th', 'td'])

        for cell in header_cells:
            text = cell.get_text().strip()
            headers.append(text)

        # Create header row
        markdown += '| ' + ' | '.join(headers) + ' |\n'
        markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'

        # Process data rows
        for row in rows[1:]:
            cells = row.find_all(['td', 'th'])
            if cells:
                cell_texts = []
                for cell in cells:
                    text = cell.get_text().strip()
                    # Escape pipes in cell content
                    text = text.replace('|', '\\|')
                    # Replace newlines with spaces
                    text = text.replace('\n', ' ')
                    cell_texts.append(text)

                markdown += '| ' + ' | '.join(cell_texts) + ' |\n'

        markdown += '\n'
        return markdown

    def extract_metadata(self, soup: BeautifulSoup, url: str) -> dict:
        """Extract metadata from HTML"""
        metadata = {
            'url': url,
            'converted_at': datetime.now().isoformat(),
        }

        # Title
        title_tag = soup.find('h1', class_='content-title')
        if title_tag:
            metadata['title'] = title_tag.get_text().strip()
        else:
            title_tag = soup.find('title')
            if title_tag:
                metadata['title'] = title_tag.get_text().strip()

        # Last updated
        update_date = soup.find('span', class_='last-updated-date')
        if update_date:
            metadata['last_updated'] = update_date.get_text().strip()

        return metadata

    def html_to_markdown(self, html_file: Path, url: str) -> Optional[str]:
        """Convert HTML file to Markdown"""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                html = f.read()

            soup = BeautifulSoup(html, 'html.parser')

            # Extract metadata
            metadata = self.extract_metadata(soup, url)

            # Extract main content
            main_content = self.extract_main_content(soup)
            if not main_content:
                print(f"Warning: Could not find main content in {html_file}")
                return None

            # Convert to Markdown
            markdown_content = self.convert_element_to_markdown(main_content)

            # Clean up extra whitespace
            markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
            markdown_content = markdown_content.strip()

            # Build final markdown with frontmatter
            markdown = '---\n'
            for key, value in metadata.items():
                markdown += f"{key}: {value}\n"
            markdown += '---\n\n'
            markdown += markdown_content

            return markdown

        except Exception as e:
            print(f"Error converting {html_file}: {e}")
            return None

    def convert_all(self):
        """Convert all HTML files to Markdown"""
        if not self.manifest:
            print("Error: No manifest loaded")
            return

        print(f"\nConverting {len(self.manifest)} HTML files to Markdown...")

        with tqdm(total=len(self.manifest), desc="Converting to Markdown") as pbar:
            for url, info in self.manifest.items():
                filename = info['filename']
                html_file = self.html_dir / filename

                if not html_file.exists():
                    print(f"\nWarning: HTML file not found: {html_file}")
                    self.stats['failed'] += 1
                    pbar.update(1)
                    continue

                # Convert to markdown
                markdown = self.html_to_markdown(html_file, url)

                if not markdown:
                    self.stats['failed'] += 1
                    pbar.update(1)
                    continue

                # Generate markdown filename
                title = info.get('h1') or info.get('title') or 'untitled'
                md_filename = self.sanitize_filename(title) + '.md'
                md_file = self.markdown_dir / md_filename

                # Save markdown
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(markdown)

                self.stats['converted'] += 1
                pbar.update(1)

        # Print stats
        print(f"\n{'='*60}")
        print(f"Conversion complete!")
        print(f"{'='*60}")
        print(f"Converted: {self.stats['converted']}")
        print(f"Failed: {self.stats['failed']}")
        print(f"Total: {len(self.manifest)}")
        print(f"\nMarkdown files saved to: {self.markdown_dir}")


def main():
    parser = argparse.ArgumentParser(description='Convert WeChat Pay HTML to Markdown')
    parser.add_argument('--output', default='.', help='Output directory (default: project directory)')
    parser.add_argument('--html-dir', default='raw-html/wechat-pay', help='HTML input directory')
    parser.add_argument('--markdown-dir', default='markdown/wechat-pay', help='Markdown output directory')

    args = parser.parse_args()

    # Setup paths
    output_dir = Path(__file__).parent.parent / args.output if args.output == '.' else Path(args.output)
    html_dir = output_dir / args.html_dir
    markdown_dir = output_dir / args.markdown_dir
    manifest_file = output_dir / '.docsync' / 'wechat_manifest.json'

    # Create converter
    converter = WeChatPayMarkdownConverter(
        html_dir=html_dir,
        markdown_dir=markdown_dir,
        manifest_file=manifest_file
    )

    converter.load_manifest()
    converter.convert_all()

    print("\nAll done! You can now use the Markdown files for AI/LLM processing.")


if __name__ == '__main__':
    main()
