#!/usr/bin/env python3
"""
Zotero SQLite Direct Importer + PDF Downloader
Parses .bib file and inserts items directly into Zotero's zotero.sqlite database,
with automatic PDF download and attachment.
Run when Zotero is NOT running (database must be unlocked).

Usage: python3 zotero_import.py <bib_file> [--dry-run] [--no-pdf]
"""
import sys
import os
import json
import sqlite3
import hashlib
import uuid
import re
import urllib.request
import urllib.error
from datetime import datetime, timezone

# --- Config ---
ZOTERO_DB = "/Users/mondyzy/Zotero/zotero.sqlite"
ZOTERO_STORAGE = "/Users/mondyzy/Zotero/storage"
LIBRARY_ID = 1
ITEM_TYPE_JOURNAL = 22  # journalArticle
ITEM_TYPE_ATTACHMENT = 3  # attachment

# Field name → fieldID mapping (for journalArticle, itemTypeID=22)
FIELD_IDS = {
    'title': 1, 'abstractNote': 2, 'publicationTitle': 3,
    'publisher': 4, 'place': 5, 'date': 6, 'volume': 7,
    'issue': 8, 'pages': 9, 'series': 10, 'seriesTitle': 11,
    'seriesText': 12, 'journalAbbreviation': 13, 'DOI': 14,
    'citationKey': 15, 'url': 16, 'accessDate': 17, 'PMID': 18,
    'PMCID': 19, 'ISSN': 20, 'archive': 21, 'archiveLocation': 22,
    'shortTitle': 23, 'language': 24, 'libraryCatalog': 25,
    'callNumber': 26, 'rights': 27, 'extra': 28,
}

AUTHOR_TYPE_ID = 1  # author creatorTypeID for journalArticle

# Direction → collectionID mapping
DIRECTION_COLLECTIONS = {
    'A': 50, 'B': 51, 'C': 52, 'D': 53, 'E': 54, 'F': 55, 'X': 56,
    'Direction-A': 50, 'Direction-B': 51, 'Direction-C': 52,
    'Direction-D': 53, 'Direction-E': 54, 'Direction-F': 55, 'Direction-X': 56,
}


def bibtex_parse_authors(author_str):
    """Parse BibTeX author string into list of (firstName, lastName) tuples."""
    if not author_str:
        return []
    authors = []
    for part in author_str.split(' and '):
        part = part.strip().strip('{}').strip()
        if ',' in part:
            last, first = part.split(',', 1)
            authors.append((first.strip(), last.strip()))
        else:
            parts = part.rsplit(None, 1)
            if len(parts) == 2:
                authors.append((parts[0], parts[1]))
            else:
                authors.append(('', parts[0]))
    return authors


def bibtex_parse_keywords(keyword_str):
    """Parse BibTeX keywords string into list of tags."""
    if not keyword_str:
        return []
    kw = keyword_str.strip().strip('{}').strip()
    return [t.strip() for t in re.split(r'[,\s;]+', kw) if t.strip()]


def parse_bib_file(filepath):
    """Manually parse a BibTeX file (lightweight, no bibtexparser dependency needed)."""
    entries = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'(?m)^\s*%.*$', '', content)
    blocks = re.split(r'(?=@\w+\s*\{)', content)

    for block in blocks:
        block = block.strip()
        if not block or not block.startswith('@'):
            continue

        m = re.match(r'@(\w+)\s*\{\s*([^,]+)\s*,', block)
        if not m:
            continue
        entry_type = m.group(1)
        entry_key = m.group(2).strip()

        entry = {'type': entry_type, 'key': entry_key}
        rest = block[block.index(',', m.end()-1)+1:]
        
        pos = 0
        while pos < len(rest):
            while pos < len(rest) and rest[pos] in ' \t\n\r,':
                pos += 1
            if pos >= len(rest):
                break
            
            fm = re.match(r'(\w+)\s*=\s*', rest[pos:])
            if not fm:
                pos += 1
                continue
            field_name = fm.group(1).lower()
            pos += fm.end()

            val_start = pos
            brace_depth = 0
            in_quotes = False
            while pos < len(rest):
                ch = rest[pos]
                if ch == '{' and not in_quotes:
                    brace_depth += 1
                elif ch == '}' and not in_quotes:
                    if brace_depth == 0:
                        break
                    brace_depth -= 1
                elif ch == '"':
                    in_quotes = not in_quotes
                elif ch == ',' and brace_depth == 0 and not in_quotes:
                    break
                pos += 1

            value = rest[val_start:pos].strip()
            if value.startswith('{') and value.endswith('}'):
                value = value[1:-1]
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            if field_name in ('title', 'author', 'journal', 'year', 'doi', 'url',
                            'eprint', 'archiveprefix', 'note', 'keywords', 'abstract',
                            'volume', 'pages', 'publisher', 'number', 'month'):
                entry[field_name] = value

            while pos < len(rest) and rest[pos] in ',\s':
                pos += 1

        entries.append(entry)

    return entries


def download_pdf(url, dest_path, timeout=30):
    """Download a PDF file from URL to dest_path. Returns True on success."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                          'ZoteroImport/1.0'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status != 200:
                return False
            content_type = resp.headers.get('Content-Type', '')
            # Verify it's actually a PDF
            data = resp.read()
            if len(data) < 1000:
                return False
            # Check if it starts with PDF magic bytes
            if not data.startswith(b'%PDF'):
                # Might still be a PDF from some servers
                if b'%PDF' not in data[:1024]:
                    return False
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, 'wb') as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"    PDF download failed: {e}")
        return False


def attach_pdf_to_item(conn, parent_item_id, parent_key, entry, pdf_path):
    """Create an attachment item for a downloaded PDF."""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    att_key = str(uuid.uuid4())[:8].upper()
    
    # Create attachment item
    conn.execute(
        "INSERT INTO items (itemTypeID, dateAdded, dateModified, "
        "clientDateModified, libraryID, key, version, synced) "
        "VALUES (?, ?, ?, ?, ?, ?, 1, 0)",
        (ITEM_TYPE_ATTACHMENT, now, now, now, LIBRARY_ID, att_key))
    att_item_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    # Get filename
    filename = os.path.basename(pdf_path)
    # Move/rename to storage path
    storage_dir = os.path.join(ZOTERO_STORAGE, att_key)
    os.makedirs(storage_dir, exist_ok=True)
    final_path = os.path.join(storage_dir, filename)
    
    if os.path.abspath(pdf_path) != os.path.abspath(final_path):
        import shutil
        shutil.move(pdf_path, final_path)
    
    # Get file modification time
    mod_time = int(os.path.getmtime(final_path) * 1000)
    
    # Insert attachment info
    conn.execute(
        "INSERT INTO itemAttachments (itemID, parentItemID, linkMode, "
        "contentType, path, storageModTime) "
        "VALUES (?, ?, 0, 'application/pdf', ?, ?)",
        (att_item_id, parent_item_id, f'storage:{filename}', mod_time))

    # Add title for attachment item
    title = entry.get('title', 'Full Text PDF')
    conn.execute(
        "INSERT OR IGNORE INTO itemDataValues (value) VALUES (?)", (title,))
    cur = conn.execute(
        "SELECT valueID FROM itemDataValues WHERE value = ?", (title,))
    title_value_id = cur.fetchone()[0]
    conn.execute(
        "INSERT INTO itemData (itemID, fieldID, valueID) VALUES (?, 1, ?)",
        (att_item_id, title_value_id))

    return True


def find_pdf_url(entry):
    """Determine the best PDF URL for an entry. Returns (url, suggested_filename)."""
    # arXiv papers: direct PDF link
    eprint = entry.get('eprint', '')
    archive_prefix = entry.get('archiveprefix', '').lower()
    if eprint and archive_prefix == 'arxiv':
        pdf_url = f"https://arxiv.org/pdf/{eprint}.pdf"
        safe_title = re.sub(r'[^a-zA-Z0-9\s-]', '', entry.get('title', 'paper'))[:80].strip()
        safe_title = re.sub(r'\s+', '_', safe_title)
        filename = f"{safe_title}.pdf"
        return pdf_url, filename

    # DOI: try unpaywall / direct DOI resolution
    doi = entry.get('doi', '')
    if doi:
        # Try direct DOI PDF resolution
        pdf_url = f"https://doi.org/{doi}"
        safe_title = re.sub(r'[^a-zA-Z0-9\s-]', '', entry.get('title', 'paper'))[:80].strip()
        safe_title = re.sub(r'\s+', '_', safe_title)
        filename = f"{safe_title}.pdf"
        return pdf_url, filename

    # URL fallback
    url = entry.get('url', '')
    if url and url.endswith('.pdf'):
        filename = url.split('/')[-1]
        return url, filename

    return None, None


def check_item_exists(conn, entry):
    """Check if an item already exists by DOI or title."""
    doi = entry.get('doi', '')
    if doi:
        cur = conn.execute(
            "SELECT id.itemID FROM itemData id "
            "JOIN itemDataValues idv ON id.valueID = idv.valueID "
            "JOIN fields f ON id.fieldID = f.fieldID "
            "WHERE f.fieldName = 'DOI' AND idv.value = ?", (doi,))
        existing = cur.fetchone()
        if existing:
            return existing[0]

    title = entry.get('title', '')
    if title:
        cur = conn.execute(
            "SELECT id.itemID FROM itemData id "
            "JOIN itemDataValues idv ON id.valueID = idv.valueID "
            "JOIN fields f ON id.fieldID = f.fieldID "
            "WHERE f.fieldName = 'title' AND idv.value = ?", (title,))
        existing = cur.fetchone()
        if existing:
            return existing[0]

    return None


def insert_item(conn, entry, dry_run=False, skip_pdf=False):
    """Insert a single item into Zotero database. Returns (item_id, item_key)."""
    
    item_key = str(uuid.uuid4())[:8].upper()
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    # Check duplicates
    existing = check_item_exists(conn, entry)
    if existing:
        doi = entry.get('doi', '')
        title = entry.get('title', '')
        if doi:
            print(f"  SKIP (DOI exists): {doi}")
        else:
            print(f"  SKIP (title exists): {title[:60]}...")
        return None, None

    title = entry.get('title', '')

    if dry_run:
        print(f"  DRY-RUN: Would insert: {title[:80]}")
        return -1, 'DRYRUN'

    # Insert into items
    conn.execute(
        "INSERT INTO items (itemTypeID, dateAdded, dateModified, "
        "clientDateModified, libraryID, key, version, synced) "
        "VALUES (?, ?, ?, ?, ?, ?, 1, 0)",
        (ITEM_TYPE_JOURNAL, now, now, now, LIBRARY_ID, item_key))
    item_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    # Insert data values
    data_map = {
        'title': entry.get('title', ''),
        'url': entry.get('url', ''),
        'DOI': entry.get('doi', ''),
        'date': entry.get('year', ''),
        'volume': entry.get('volume', ''),
        'pages': entry.get('pages', ''),
        'publicationTitle': entry.get('journal', ''),
        'publisher': entry.get('publisher', ''),
        'accessDate': now,
        'libraryCatalog': 'arXiv.org' if entry.get('archiveprefix', '').lower() == 'arxiv' else 'CrossRef',
    }

    if entry.get('eprint'):
        data_map['archive'] = 'arXiv'
        data_map['archiveLocation'] = entry['eprint']
        if not data_map['url']:
            data_map['url'] = f"https://arxiv.org/abs/{entry['eprint']}"

    if entry.get('note'):
        data_map['extra'] = entry['note']

    for field_name, value in data_map.items():
        if not value:
            continue
        field_id = FIELD_IDS.get(field_name)
        if field_id is None:
            continue
        conn.execute(
            "INSERT OR IGNORE INTO itemDataValues (value) VALUES (?)", (value,))
        cur = conn.execute(
            "SELECT valueID FROM itemDataValues WHERE value = ?", (value,))
        value_id = cur.fetchone()[0]
        conn.execute(
            "INSERT INTO itemData (itemID, fieldID, valueID) VALUES (?, ?, ?)",
            (item_id, field_id, value_id))

    # Insert authors
    authors = bibtex_parse_authors(entry.get('author', ''))
    for order_idx, (first, last) in enumerate(authors):
        cur = conn.execute(
            "SELECT creatorID FROM creators WHERE firstName = ? AND lastName = ?",
            (first, last))
        c = cur.fetchone()
        if c:
            creator_id = c[0]
        else:
            conn.execute(
                "INSERT INTO creators (firstName, lastName) VALUES (?, ?)",
                (first, last))
            creator_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        conn.execute(
            "INSERT INTO itemCreators (itemID, creatorID, creatorTypeID, orderIndex) "
            "VALUES (?, ?, ?, ?)",
            (item_id, creator_id, AUTHOR_TYPE_ID, order_idx))

    # Insert tags
    keywords = bibtex_parse_keywords(entry.get('keywords', ''))
    for tag_name in keywords:
        cur = conn.execute("SELECT tagID FROM tags WHERE name = ?", (tag_name,))
        t = cur.fetchone()
        if t:
            tag_id = t[0]
        else:
            conn.execute("INSERT INTO tags (name) VALUES (?)", (tag_name,))
            tag_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        conn.execute(
            "INSERT OR IGNORE INTO itemTags (itemID, tagID, type) VALUES (?, ?, 0)",
            (item_id, tag_id))

    # Add to collections
    for kw in keywords:
        if kw in DIRECTION_COLLECTIONS:
            coll_id = DIRECTION_COLLECTIONS[kw]
            conn.execute(
                "INSERT OR IGNORE INTO collectionItems (collectionID, itemID) "
                "VALUES (?, ?)", (coll_id, item_id))

    # Download and attach PDF
    pdf_ok = False
    if not skip_pdf:
        pdf_url, filename = find_pdf_url(entry)
        if pdf_url:
            pdf_path = os.path.join('/tmp/zotero_pdf_import', filename)
            print(f"    Downloading PDF: {pdf_url[:80]}...")
            if download_pdf(pdf_url, pdf_path):
                attach_pdf_to_item(conn, item_id, item_key, entry, pdf_path)
                pdf_ok = True
                print(f"    PDF attached ✓")
            else:
                print(f"    ⚠ PDF not available (will try Find Available PDF in Zotero)")
        else:
            print(f"    ⚠ No PDF URL found")

    status = "📄+📎" if pdf_ok else "📄"
    short_title = title[:60] + "..." if len(title) > 60 else title
    print(f"  {status} INSERTED [{item_key}]: {short_title}")
    return item_id, item_key


def delete_items_by_date(conn, date_str):
    """Delete items added on a specific date. Use with caution!"""
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute(
        "DELETE FROM items WHERE dateAdded LIKE ?", (f'{date_str}%',))
    deleted = conn.total_changes
    print(f"Deleted {deleted} items from {date_str}")
    return deleted


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <bib_file> [--dry-run] [--no-pdf] [--clean-date YYYY-MM-DD]")
        sys.exit(1)

    bib_file = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    skip_pdf = '--no-pdf' in sys.argv
    clean_date = None
    if '--clean-date' in sys.argv:
        idx = sys.argv.index('--clean-date')
        if idx + 1 < len(sys.argv):
            clean_date = sys.argv[idx + 1]

    if not os.path.exists(bib_file):
        print(f"Error: file not found: {bib_file}")
        sys.exit(1)

    # Check Zotero
    zotero_running = os.popen('pgrep -x zotero 2>/dev/null').read().strip()
    if zotero_running:
        print("ERROR: Zotero is running. Please close Zotero first.")
        print("  pkill -x zotero")
        sys.exit(1)

    if not os.path.exists(ZOTERO_DB):
        print(f"ERROR: Zotero database not found: {ZOTERO_DB}")
        sys.exit(1)

    # Clean up temp dir
    os.makedirs('/tmp/zotero_pdf_import', exist_ok=True)

    conn = sqlite3.connect(ZOTERO_DB)
    conn.execute("PRAGMA foreign_keys = ON")

    # Clean previous imports if requested
    if clean_date:
        print(f"Cleaning items from {clean_date}...")
        delete_items_by_date(conn, clean_date)

    print(f"Parsing: {bib_file}")
    entries = parse_bib_file(bib_file)
    print(f"Found {len(entries)} entries\n")

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    inserted = 0
    skipped = 0
    pdf_count = 0
    for entry in entries:
        result = insert_item(conn, entry, dry_run=dry_run, skip_pdf=skip_pdf)
        if result[0] is not None:
            inserted += 1
        else:
            skipped += 1

    if not dry_run:
        conn.commit()
    conn.close()

    print(f"\n{'='*50}")
    print(f"Results: {inserted} inserted, {skipped} skipped (duplicates)")
    
    if not dry_run and not skip_pdf:
        print(f"\nDone! Restart Zotero: open -a Zotero")
        print(f"Papers are now in your library WITH PDFs attached.")
        print(f"If some PDFs failed, right-click → Find Available PDF in Zotero.")


if __name__ == '__main__':
    main()
