#!/usr/bin/env python3
"""
Markdown Merger for Apple Documentation
Merges markdown files within each framework directory to reduce file count
"""

import hashlib
import os
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import argparse
from tqdm import tqdm


class MarkdownMerger:
    """Merges markdown files with deduplication and hierarchical structure"""

    def __init__(self, markdown_dir: Path, output_dir: Path):
        self.markdown_dir = Path(markdown_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Statistics
        self.stats = {
            'total_files': 0,
            'duplicates_removed': 0,
            'case_conflicts_resolved': 0,
            'frameworks_processed': 0,
            'merged_files_created': 0
        }

    def calculate_md5(self, file_path: Path) -> str:
        """Calculate MD5 hash of a file"""
        md5_hash = hashlib.md5()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    md5_hash.update(chunk)
            return md5_hash.hexdigest()
        except Exception as e:
            print(f"Warning: Failed to calculate MD5 for {file_path}: {e}")
            return ""

    def has_uppercase(self, filename: str) -> bool:
        """Check if filename contains uppercase letters"""
        # Remove extension for checking
        name_without_ext = filename.rsplit('.', 1)[0]
        return any(c.isupper() for c in name_without_ext)

    def deduplicate_files(self, files: List[Path]) -> List[Path]:
        """
        Deduplicate files based on:
        1. MD5 hash (exact duplicates)
        2. Filename case conflicts (prefer files with uppercase)
        """
        # First pass: Remove MD5 duplicates
        md5_map: Dict[str, Path] = {}
        for file_path in files:
            md5_hash = self.calculate_md5(file_path)
            if not md5_hash:
                continue

            if md5_hash not in md5_map:
                md5_map[md5_hash] = file_path
            else:
                self.stats['duplicates_removed'] += 1

        unique_files = list(md5_map.values())

        # Second pass: Resolve filename case conflicts
        # Group by lowercase filename
        filename_groups: Dict[str, List[Path]] = defaultdict(list)
        for file_path in unique_files:
            lower_name = file_path.name.lower()
            filename_groups[lower_name].append(file_path)

        final_files: List[Path] = []
        for lower_name, file_group in filename_groups.items():
            if len(file_group) == 1:
                final_files.append(file_group[0])
            else:
                # Prefer files with uppercase letters
                files_with_upper = [f for f in file_group if self.has_uppercase(f.name)]
                if files_with_upper:
                    final_files.append(files_with_upper[0])
                    self.stats['case_conflicts_resolved'] += len(file_group) - 1
                else:
                    # If no uppercase, just take the first one
                    final_files.append(file_group[0])
                    self.stats['case_conflicts_resolved'] += len(file_group) - 1

        return final_files

    def get_relative_path(self, file_path: Path, base_dir: Path) -> str:
        """Get relative path from base directory"""
        try:
            return str(file_path.relative_to(base_dir))
        except ValueError:
            return str(file_path)

    def build_file_tree(self, files: List[Path], base_dir: Path) -> Dict:
        """Build a hierarchical tree structure from file paths"""
        tree = {}

        for file_path in files:
            rel_path = self.get_relative_path(file_path, base_dir)
            parts = Path(rel_path).parts

            current = tree
            for i, part in enumerate(parts[:-1]):  # Navigate through directories
                if part not in current:
                    current[part] = {}
                current = current[part]

            # Add the file
            filename = parts[-1]
            current[filename] = file_path

        return tree

    def read_markdown_content(self, file_path: Path) -> str:
        """Read markdown file and return its content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Warning: Failed to read {file_path}: {e}")
            return f"<!-- Error reading file: {e} -->\n"

    def generate_markdown_tree(self, tree: Dict, level: int = 1, current_path: str = "") -> str:
        """Generate markdown content from the tree structure"""
        markdown_parts = []

        # Sort keys: directories first, then files
        directories = sorted([k for k in tree.keys() if isinstance(tree[k], dict)])
        files = sorted([k for k in tree.keys() if isinstance(tree[k], Path)])

        # Process directories
        for dirname in directories:
            dir_path = os.path.join(current_path, dirname) if current_path else dirname
            markdown_parts.append(f"\n{'#' * (level + 1)} {dirname}\n\n")
            markdown_parts.append(self.generate_markdown_tree(tree[dirname], level + 1, dir_path))

        # Process files
        for filename in files:
            file_path = tree[filename]

            # Add file header
            file_display_name = filename.replace('.md', '')
            markdown_parts.append(f"\n{'#' * (level + 1)} {file_display_name}\n\n")

            # Add file content
            content = self.read_markdown_content(file_path)

            # Remove YAML frontmatter if exists
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].strip()

            # Remove the first # heading if it duplicates the section heading
            lines = content.split('\n')
            if lines and lines[0].strip().startswith('# '):
                content = '\n'.join(lines[1:]).strip()

            markdown_parts.append(content)
            markdown_parts.append('\n\n---\n\n')

        return ''.join(markdown_parts)

    def merge_framework(self, framework_name: str):
        """Merge all markdown files for a specific framework"""
        framework_dir = self.markdown_dir / framework_name
        top_level_file = self.markdown_dir / f"{framework_name}.md"

        # Collect all markdown files
        all_files = []

        # Add top-level file if exists
        if top_level_file.exists():
            all_files.append(top_level_file)

        # Add all files from the framework directory
        if framework_dir.exists() and framework_dir.is_dir():
            for md_file in framework_dir.rglob('*.md'):
                all_files.append(md_file)

        if not all_files:
            print(f"Warning: No markdown files found for framework '{framework_name}'")
            return

        self.stats['total_files'] += len(all_files)

        # Deduplicate files
        unique_files = self.deduplicate_files(all_files)

        # Separate top-level file and directory files
        top_level_files = [f for f in unique_files if f.parent == self.markdown_dir]
        directory_files = [f for f in unique_files if f.parent != self.markdown_dir]

        # Build merged markdown content
        merged_content = []

        # Add title
        merged_content.append(f"# {framework_name}\n\n")
        merged_content.append(f"*Merged documentation for {framework_name}*\n\n")
        merged_content.append("---\n\n")

        # Add top-level file content
        if top_level_files:
            for top_file in top_level_files:
                content = self.read_markdown_content(top_file)

                # Remove YAML frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        content = parts[2].strip()

                merged_content.append(content)
                merged_content.append('\n\n---\n\n')

        # Build hierarchical structure for directory files
        if directory_files:
            merged_content.append(f"\n# Detailed Documentation\n\n")
            tree = self.build_file_tree(directory_files, framework_dir)
            merged_content.append(self.generate_markdown_tree(tree))

        # Write merged file
        output_file = self.output_dir / f"{framework_name}_merged.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(''.join(merged_content))

        self.stats['merged_files_created'] += 1
        self.stats['frameworks_processed'] += 1

        print(f"  Created: {output_file}")
        print(f"  Files merged: {len(unique_files)} (from {len(all_files)} total)")

    def merge_all_frameworks(self):
        """Merge all frameworks found in the markdown directory"""
        # Find all top-level framework directories
        frameworks = set()

        # Add frameworks that have directories
        for item in self.markdown_dir.iterdir():
            if item.is_dir():
                frameworks.add(item.name)

        # Add frameworks that have top-level .md files
        for item in self.markdown_dir.glob('*.md'):
            framework_name = item.stem
            frameworks.add(framework_name)

        if not frameworks:
            print("No frameworks found in the markdown directory")
            return

        print(f"\nFound {len(frameworks)} frameworks to merge")
        print("="*60)

        for framework in tqdm(sorted(frameworks), desc="Merging frameworks"):
            print(f"\nProcessing: {framework}")
            try:
                self.merge_framework(framework)
            except Exception as e:
                print(f"Error merging {framework}: {e}")

        # Print statistics
        print("\n" + "="*60)
        print("Merge Statistics:")
        print(f"  Frameworks processed: {self.stats['frameworks_processed']}")
        print(f"  Total files scanned: {self.stats['total_files']}")
        print(f"  MD5 duplicates removed: {self.stats['duplicates_removed']}")
        print(f"  Case conflicts resolved: {self.stats['case_conflicts_resolved']}")
        print(f"  Merged files created: {self.stats['merged_files_created']}")
        print("="*60)


def main():
    parser = argparse.ArgumentParser(
        description='Merge markdown files for each framework to reduce file count'
    )
    parser.add_argument(
        '--markdown-dir',
        default='markdown',
        help='Directory containing markdown files (default: markdown)'
    )
    parser.add_argument(
        '--output-dir',
        default='markdown-merged',
        help='Output directory for merged files (default: markdown-merged)'
    )
    parser.add_argument(
        '--frameworks',
        nargs='+',
        help='Specific frameworks to merge (default: all)'
    )

    args = parser.parse_args()

    # Resolve paths
    base_dir = Path(__file__).parent.parent
    markdown_dir = base_dir / args.markdown_dir
    output_dir = base_dir / args.output_dir

    if not markdown_dir.exists():
        print(f"Error: Markdown directory not found: {markdown_dir}")
        print("Please run 03_json_to_markdown.py first")
        return

    # Create merger
    merger = MarkdownMerger(markdown_dir, output_dir)

    # Merge frameworks
    if args.frameworks:
        print(f"Merging specific frameworks: {', '.join(args.frameworks)}")
        for framework in args.frameworks:
            print(f"\nProcessing: {framework}")
            try:
                merger.merge_framework(framework)
            except Exception as e:
                print(f"Error merging {framework}: {e}")
    else:
        merger.merge_all_frameworks()

    print(f"\nMerge complete!")
    print(f"Merged files saved to: {output_dir}")
    print(f"\nNext steps:")
    print(f"  1. Review merged files in '{args.output_dir}/' directory")
    print(f"  2. Each framework is now in a single large markdown file")
    print(f"  3. Use these merged files for storage systems with file count limits")


if __name__ == '__main__':
    main()
