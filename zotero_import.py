#!/usr/bin/env python3
"""
Zotero SQLite Direct Importer
Parses .bib file and inserts items directly into Zotero's zotero.sqlite database.
Run when Zotero is NOT running (database must be unlocked).

Usage: python3 zotero_import.py <bib_file> [--dry-run]
"""
import sys
import os
import json
import sqlite3
import hashlib
import uuid
import re
from datetime import datetime, timezone

# --- Config ---
ZOTERO_DB = "/Users/mondyzy/Zotero/zotero.sqlite"
LIBRARY_ID = 1
ITEM_TYPE_JOURNAL = 22  # journalArticle
ITEM_TYPE_PREPRINT = 22  # treat arXiv as journalArticle

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

    # Remove comments
    content = re.sub(r'(?m)^\s*%.*$', '', content)

    # Find all @type{key, ...} blocks
    pattern = r'@(\w+)\s*\{\s*(\w+)\s*,\s*(.*?)\}'
    # Use a simpler approach: split by entries
    blocks = re.split(r'(?=@\w+\s*\{)', content)

    for block in blocks:
        block = block.strip()
        if not block or not block.startswith('@'):
            continue

        # Extract type and key
        m = re.match(r'@(\w+)\s*\{\s*([^,]+)\s*,', block)
        if not m:
            continue
        entry_type = m.group(1)
        entry_key = m.group(2).strip()

        # Extract fields
        entry = {'type': entry_type, 'key': entry_key}
        # Find fields between braces
        rest = block[block.index(',', m.end()-1)+1:]
        
        # Parse field = value pairs
        field_pattern = r'(\w+)\s*=\s*'
        pos = 0
        while pos < len(rest):
            # Skip whitespace/newlines before field name
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

            # Read value (handle {...} and "..." and bare values)
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
            # Strip surrounding braces or quotes
            if value.startswith('{') and value.endswith('}'):
                value = value[1:-1]
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            if field_name in ('title', 'author', 'journal', 'year', 'doi', 'url',
                            'eprint', 'archiveprefix', 'note', 'keywords', 'abstract',
                            'volume', 'pages', 'publisher', 'number', 'month'):
                entry[field_name] = value

            # Skip comma
            while pos < len(rest) and rest[pos] in ',\s':
                pos += 1

        entries.append(entry)

    return entries


def insert_item(conn, entry, dry_run=False):
    """Insert a single item into Zotero database. Returns itemID if successful."""
    
    # Generate unique key
    item_key = str(uuid.uuid4())[:8].upper()
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    # Check for duplicates by DOI
    doi = entry.get('doi', '')
    if doi:
        cur = conn.execute(
            "SELECT id.itemID FROM itemData id "
            "JOIN itemDataValues idv ON id.valueID = idv.valueID "
            "JOIN fields f ON id.fieldID = f.fieldID "
            "WHERE f.fieldName = 'DOI' AND idv.value = ?", (doi,))
        existing = cur.fetchone()
        if existing:
            print(f"  SKIP (DOI exists): {doi}")
            return None

    # Check for duplicates by title
    title = entry.get('title', '')
    if title:
        cur = conn.execute(
            "SELECT id.itemID FROM itemData id "
            "JOIN itemDataValues idv ON id.valueID = idv.valueID "
            "JOIN fields f ON id.fieldID = f.fieldID "
            "WHERE f.fieldName = 'title' AND idv.value = ?", (title,))
        existing = cur.fetchone()
        if existing:
            print(f"  SKIP (title exists): {title[:60]}...")
            return None

    if dry_run:
        print(f"  DRY-RUN: Would insert: {title[:80]}")
        return -1

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

    # Handle arXiv
    if entry.get('eprint'):
        data_map['archive'] = 'arXiv'
        data_map['archiveLocation'] = entry['eprint']
        if not data_map['url']:
            data_map['url'] = f"https://arxiv.org/abs/{entry['eprint']}"

    # Handle note (goes to extra field)
    if entry.get('note'):
        data_map['extra'] = entry['note']

    for field_name, value in data_map.items():
        if not value:
            continue
        field_id = FIELD_IDS.get(field_name)
        if field_id is None:
            continue

        # Insert value (value is UNIQUE, so use INSERT OR IGNORE + SELECT)
        conn.execute(
            "INSERT OR IGNORE INTO itemDataValues (value) VALUES (?)", (value,))
        cur = conn.execute(
            "SELECT valueID FROM itemDataValues WHERE value = ?", (value,))
        value_id = cur.fetchone()[0]

        # Link item to value
        conn.execute(
            "INSERT INTO itemData (itemID, fieldID, valueID) VALUES (?, ?, ?)",
            (item_id, field_id, value_id))

    # Insert authors
    authors = bibtex_parse_authors(entry.get('author', ''))
    for order_idx, (first, last) in enumerate(authors):
        # Check if creator exists
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

    # Insert tags from keywords
    keywords = bibtex_parse_keywords(entry.get('keywords', ''))
    direction_tag = None
    for tag_name in keywords:
        if tag_name.startswith('Direction-'):
            direction_tag = tag_name
        # Check if tag exists
        cur = conn.execute("SELECT tagID FROM tags WHERE name = ?", (tag_name,))
        t = cur.fetchone()
        if t:
            tag_id = t[0]
        else:
            conn.execute("INSERT INTO tags (name) VALUES (?)", (tag_name,))
            tag_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        conn.execute(
            "INSERT INTO itemTags (itemID, tagID, type) VALUES (?, ?, 0)",
            (item_id, tag_id))

    # Add to collection
    # Also check for A/B/C/D/E/F/X direction tags
    for kw in keywords:
        if kw in DIRECTION_COLLECTIONS:
            coll_id = DIRECTION_COLLECTIONS[kw]
            conn.execute(
                "INSERT OR IGNORE INTO collectionItems (collectionID, itemID) "
                "VALUES (?, ?)", (coll_id, item_id))

    print(f"  INSERTED [{item_key}]: {title[:60]}..." if len(title) > 60 else f"  INSERTED [{item_key}]: {title}")
    return item_id


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <bib_file> [--dry-run]")
        sys.exit(1)

    bib_file = sys.argv[1]
    dry_run = '--dry-run' in sys.argv

    if not os.path.exists(bib_file):
        print(f"Error: file not found: {bib_file}")
        sys.exit(1)

    # Check if Zotero is running
    zotero_running = os.popen('pgrep -x zotero 2>/dev/null').read().strip()
    if zotero_running:
        print("ERROR: Zotero is running. Please close Zotero first.")
        print("  pkill -x zotero")
        sys.exit(1)

    if not os.path.exists(ZOTERO_DB):
        print(f"ERROR: Zotero database not found: {ZOTERO_DB}")
        sys.exit(1)

    print(f"Parsing: {bib_file}")
    entries = parse_bib_file(bib_file)
    print(f"Found {len(entries)} entries\n")

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    conn = sqlite3.connect(ZOTERO_DB)
    conn.execute("PRAGMA foreign_keys = ON")

    inserted = 0
    skipped = 0
    for entry in entries:
        result = insert_item(conn, entry, dry_run=dry_run)
        if result is not None:
            inserted += 1
        else:
            skipped += 1

    if not dry_run:
        conn.commit()

    conn.close()

    print(f"\n{'='*50}")
    print(f"Results: {inserted} inserted, {skipped} skipped (duplicates)")
    
    if not dry_run:
        print(f"\nDone! Restart Zotero: open -a Zotero")
        print(f"The {inserted} new items will appear in your library with tags and collections.")


if __name__ == '__main__':
    main()
