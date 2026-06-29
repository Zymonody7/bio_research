#!/usr/bin/env python3
"""Combine all search results, deduplicate, and get detailed info."""
import json
import re
import urllib.request
import time

# Load seen IDs
seen_ids = set()
with open('/tmp/seen_ids.txt') as f:
    for line in f:
        seen_ids.add(line.strip())

print(f"Loaded {len(seen_ids)} seen paper IDs")

# Load PubMed results
with open('/tmp/pubmed_results.json') as f:
    pubmed = json.load(f)

# Load Semantic Scholar results
with open('/tmp/ss_results.json') as f:
    ss = json.load(f)

# Combine and deduplicate
all_papers = {}
for p in pubmed.get('papers', []) + ss.get('papers', []):
    pid = p['id']
    # Normalize ID for dedup check
    check_id = pid
    if pid.startswith('10.'):
        # DOI format - already in seen
        pass
    elif re.match(r'\d{4}\.\d+', pid):
        # arxiv format - check as-is
        pass
    
    # Skip if already seen
    if check_id in seen_ids:
        continue
    
    # Skip duplicates within this batch
    if pid in all_papers:
        continue
    
    all_papers[pid] = p

print(f"After dedup: {len(all_papers)} new papers")

# Categorize by direction
by_direction = {}
for p in all_papers.values():
    d = p.get('direction', 'X')
    if d not in by_direction:
        by_direction[d] = []
    by_direction[d].append(p)

for d, papers in sorted(by_direction.items()):
    print(f"\n=== Direction {d} ({len(papers)} papers) ===")
    for p in papers:
        print(f"  {p['id']}: {p['title'][:80]}")
        if p.get('abstract'):
            print(f"    Abstract: {p['abstract'][:150]}...")

# Save combined results
output = {
    'papers': list(all_papers.values()),
    'total': len(all_papers),
    'by_direction': {d: len(ps) for d, ps in by_direction.items()}
}
with open('/tmp/combined_results.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\n=== FINAL: {len(all_papers)} unique new papers ===")
