# App Store Connect Help Documentation Scraper - Design Document

**Date:** 2026-01-21
**Author:** AI Assistant
**Status:** Approved for Implementation

## Overview

Design for scraping Apple's App Store Connect Help documentation from https://developer.apple.com/help/app-store-connect/ and converting it to Markdown format. This extends the existing Apple Developer Documentation offline archive project with support for HTML-based help documentation.

## Requirements

- Scrape all documentation pages from App Store Connect Help site
- Extract content from `<div class="main-content">` sections
- Convert HTML to clean Markdown format
- Use page titles as filenames
- Follow existing project patterns (3-script modular approach)
- Support resume/recovery for interrupted operations
- Include rate limiting to be respectful of Apple's servers

## Architecture

### Three-Script Modular Design

Following the existing pattern (discover → download → convert), we'll implement:

1. **07_discover_appstore_help.py** - Navigation crawler
2. **08_download_appstore_html.py** - HTML downloader
3. **09_html_to_markdown.py** - Markdown converter

### Why This Approach?

- **Consistency:** Matches existing scripts 01-06
- **Modularity:** Each step can be run independently
- **Resume Support:** Can restart from any stage
- **Debugging:** Easier to troubleshoot individual stages
- **Flexibility:** Can re-convert markdown without re-downloading

## Component Details

### 1. Navigation Discovery (07_discover_appstore_help.py)

**Purpose:** Crawl the site navigation and discover all documentation URLs

**Input:**
- Root URL: `https://developer.apple.com/help/app-store-connect/`

**Process:**
1. Fetch the main page HTML
2. Parse left sidebar navigation structure (nested `<nav>` or `<ul>` elements)
3. Extract all documentation links recursively
4. Handle hierarchical categories (nested navigation)
5. Normalize URLs (resolve relative paths, remove fragments)
6. Deduplicate URLs
7. Save periodically for resume support

**Output:**
- `appstore_help_index.json` containing:
  ```json
  {
    "root_url": "https://developer.apple.com/help/app-store-connect/",
    "discovered_at": "2026-01-21T19:20:00Z",
    "total_pages": 250,
    "pages": [
      {
        "url": "https://developer.apple.com/help/app-store-connect/get-started",
        "category": "Getting Started",
        "depth": 1
      }
    ]
  }
  ```

**Features:**
- Resume support via `discovery_state_appstore.json`
- Progress bar showing discovery progress
- Rate limiting (5 req/sec)
- Filters external links and non-documentation URLs
- Command-line arguments: `--resume`, `--output`

**Key Classes/Functions:**
- `AppStoreHelpCrawler` class
- `parse_navigation()` - Extract nav links
- `normalize_url()` - Clean and deduplicate URLs
- `save_state()` / `load_state()` - Resume support

### 2. HTML Download (08_download_appstore_html.py)

**Purpose:** Download all discovered pages and extract main content

**Input:**
- `appstore_help_index.json` from script 07

**Process:**
1. Read URL list from index
2. Download each page asynchronously (aiohttp)
3. Parse HTML with BeautifulSoup
4. Extract `<div class="main-content">` section
5. Save extracted HTML to `raw-html/appstore-connect/`
6. Track downloads in manifest with ETags
7. Handle errors with retry logic

**Output:**
- `raw-html/appstore-connect/*.html` - Extracted content files
- `.docsync/appstore_manifest.json` - Download metadata:
  ```json
  {
    "version": "1.0",
    "last_updated": "2026-01-21T19:30:00Z",
    "pages": {
      "https://developer.apple.com/help/app-store-connect/get-started": {
        "etag": "abc123",
        "downloaded_at": "2026-01-21T19:25:00Z",
        "file_path": "raw-html/appstore-connect/page-001.html",
        "content_hash": "sha256:..."
      }
    }
  }
  ```

**Features:**
- Async downloads with aiohttp (5 req/sec rate limiting)
- Exponential backoff for failed requests (3 retries)
- Skip existing files (check manifest)
- Progress tracking with tqdm
- Graceful handling of 404s
- Auto-save progress every 50 pages
- Command-line arguments: `--output-dir`, `--rate-limit`

**Content Extraction Strategy:**
- Primary: Find `<div class="main-content">`
- Fallback 1: Try `<main>` or `<article>` tags
- Fallback 2: Try `<div id="content">` or similar
- Last resort: Extract `<body>` and log warning

**Error Handling:**
- 429 (Rate Limit): Exponential backoff up to 60 seconds
- 404 (Not Found): Log and skip
- 5xx (Server Error): Retry with backoff
- Network errors: Retry 3 times then skip

### 3. Markdown Conversion (09_html_to_markdown.py)

**Purpose:** Convert extracted HTML to clean, AI-readable Markdown

**Input:**
- `raw-html/appstore-connect/*.html` files
- `appstore_help_index.json` (for metadata)

**Process:**
1. Read each HTML file
2. Extract page title from `<title>` or `<h1>`
3. Convert HTML elements to Markdown
4. Generate sanitized filename from title
5. Add YAML frontmatter with metadata
6. Save to `markdown/appstore-connect/`
7. Handle duplicate filenames

**Output:**
- `markdown/appstore-connect/*.md` files with structure:
  ```markdown
  ---
  title: "Getting Started with App Store Connect"
  url: "https://developer.apple.com/help/app-store-connect/get-started"
  category: "Getting Started"
  downloaded_at: "2026-01-21"
  ---

  # Getting Started with App Store Connect

  Content here...
  ```

**HTML to Markdown Conversion Rules:**

| HTML Element | Markdown Output |
|--------------|-----------------|
| `<h1>` - `<h6>` | `#` - `######` |
| `<p>` | Plain text + blank line |
| `<strong>`, `<b>` | `**bold**` |
| `<em>`, `<i>` | `*italic*` |
| `<code>` | `` `code` `` |
| `<pre><code>` | ` ```\ncode\n``` ` |
| `<a href="...">` | `[text](url)` |
| `<img src="...">` | `![alt](src)` |
| `<ul><li>` | `- item` |
| `<ol><li>` | `1. item` |
| `<blockquote>` | `> quote` |
| `<table>` | Markdown table |
| `<br>` | Double newline |

**Filename Generation:**
1. Extract title from `<title>` tag (remove " - App Store Connect" suffix)
2. Fallback to `<h1>` text if no title
3. Sanitize:
   - Convert to lowercase
   - Replace spaces with hyphens
   - Remove special characters (keep alphanumeric and `-`)
   - Truncate to 100 characters
4. Handle duplicates: append `-2`, `-3`, etc.
5. Add `.md` extension

**Examples:**
- "Getting Started with App Store Connect" → `getting-started-with-app-store-connect.md`
- "Manage Users & Roles" → `manage-users-roles.md`
- "TestFlight Beta Testing" → `testflight-beta-testing.md`

**Link Handling:**
- Internal links to other help pages: Convert to relative markdown links
- External links: Keep absolute URLs
- Anchor links: Preserve as `#section`
- Missing links: Keep text, remove href

**Features:**
- Progress bar showing conversion progress
- Detailed logging of skipped/problematic content
- Statistics report (pages converted, errors, warnings)
- Command-line arguments: `--input-dir`, `--output-dir`

## Directory Structure

After running all three scripts:

```
Apple-Developer-Documentation-Offline-Archive/
├── scripts/
│   ├── 07_discover_appstore_help.py     # NEW
│   ├── 08_download_appstore_html.py     # NEW
│   ├── 09_html_to_markdown.py           # NEW
│   └── requirements.txt                 # (beautifulsoup4 already included)
│
├── raw-html/                            # NEW
│   └── appstore-connect/
│       ├── page-001.html
│       ├── page-002.html
│       └── ...
│
├── markdown/
│   └── appstore-connect/                # NEW
│       ├── getting-started.md
│       ├── manage-users.md
│       └── ...
│
├── .docsync/
│   ├── appstore_manifest.json           # NEW
│   └── ...
│
├── appstore_help_index.json             # NEW
├── discovery_state_appstore.json        # NEW (temporary)
└── ...
```

## Technical Specifications

### Dependencies

All dependencies already in `requirements.txt`:
- `aiohttp` - Async HTTP requests
- `beautifulsoup4` - HTML parsing
- `tqdm` - Progress bars
- `pyyaml` - YAML frontmatter

### Rate Limiting

- **Discovery:** 5 requests/second
- **Download:** 5 requests/second with exponential backoff
- **Conversion:** No rate limiting (local file processing)

### Error Recovery

All scripts support graceful interruption:
1. Save state periodically (every 50 operations)
2. Resume flag: `--resume` to continue interrupted operations
3. Skip existing files automatically
4. Log all errors to console and continue

### Performance Estimates

Assuming ~250 pages in App Store Connect Help:

| Script | Duration | Bottleneck |
|--------|----------|------------|
| 07_discover | 2-5 minutes | Navigation parsing |
| 08_download | 10-15 minutes | Rate limiting (5 req/sec) |
| 09_html_to_markdown | 2-3 minutes | CPU (parsing) |
| **Total** | **~15-25 minutes** | Network I/O |

## Usage Examples

### Initial Download

```bash
# Step 1: Discover all documentation pages
python scripts/07_discover_appstore_help.py

# Step 2: Download HTML content
python scripts/08_download_appstore_html.py

# Step 3: Convert to Markdown
python scripts/09_html_to_markdown.py
```

### Resume Interrupted Download

```bash
# Resume discovery if interrupted
python scripts/07_discover_appstore_help.py --resume

# Download automatically skips existing files
python scripts/08_download_appstore_html.py

# Re-convert specific files
python scripts/09_html_to_markdown.py --force
```

### Output Example

**File:** `markdown/appstore-connect/getting-started-with-app-store-connect.md`

```markdown
---
title: "Getting Started with App Store Connect"
url: "https://developer.apple.com/help/app-store-connect/get-started"
category: "Getting Started"
downloaded_at: "2026-01-21"
---

# Getting Started with App Store Connect

App Store Connect is your home base for managing your apps...

## Key Features

- Manage app metadata and pricing
- Monitor sales and trends
- Respond to customer reviews

## Next Steps

Learn how to [create your first app](create-first-app.md).
```

## Future Enhancements

After initial implementation, consider:

1. **Update Detection:** Track page changes with ETags (like scripts 01-06)
2. **Image Download:** Download and save images locally
3. **Search Index:** Generate searchable index for offline use
4. **PDF Generation:** Extend `04_markdown_to_pdf.py` to support App Store Connect docs
5. **HTML Output:** Extend `05_markdown_to_html.py` for browsable site
6. **Merge Support:** Add to `06_markdown_merge.py` for single-file output

## Testing Strategy

1. **Test with single page first:** Manually specify one URL to verify parsing
2. **Test small subset:** Limit to one category (~10-20 pages)
3. **Validate output:** Check markdown formatting, links, code blocks
4. **Full run:** Execute complete download
5. **Resume test:** Interrupt and resume to verify state management

## Success Criteria

- ✅ All documentation pages discovered
- ✅ Main content extracted correctly (no navigation/footer clutter)
- ✅ Clean Markdown output (proper headings, lists, code blocks)
- ✅ Unique, readable filenames based on page titles
- ✅ Resume support for all three scripts
- ✅ Rate limiting respected (no 429 errors)
- ✅ Integration with existing project structure

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Navigation structure changes | High | Flexible parsing with multiple fallbacks |
| Rate limiting / blocking | Medium | Respectful delays, user-agent, exponential backoff |
| Malformed HTML | Low | BeautifulSoup handles most cases gracefully |
| Duplicate filenames | Low | Automatic suffix numbering |
| Large pages (memory) | Low | Stream processing, chunk handling |

## Implementation Notes

- Start with script 07 (discovery) first to understand actual site structure
- May need to inspect actual HTML to verify `main-content` class name
- Consider adding `--dry-run` flag for testing without downloading
- Log verbose output for debugging navigation parsing
- Add `--max-pages` flag for testing with limited set

## Conclusion

This design provides a robust, maintainable solution for scraping App Store Connect Help documentation that:
- Follows existing project patterns for consistency
- Handles errors and interruptions gracefully
- Produces clean, AI-readable Markdown output
- Respects Apple's servers with appropriate rate limiting
- Can be easily extended with future enhancements

Ready for implementation following the superpowers:writing-plans workflow.
