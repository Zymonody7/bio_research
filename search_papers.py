#!/usr/bin/env python3
"""Search arxiv for papers in 7 directions."""
import urllib.request
import xml.etree.ElementTree as ET
import json
import time
import re

ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

def search_arxiv(query, max_results=8):
    """Search arxiv API."""
    url = f"https://export.arxiv.org/api/query?search_query={query}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    try:
        resp = urllib.request.urlopen(url, timeout=30)
        root = ET.fromstring(resp.read())
        papers = []
        for entry in root.findall('a:entry', ns):
            title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
            arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
            arxiv_id_clean = re.sub(r'v\d+$', '', arxiv_id)
            published = entry.find('a:published', ns).text[:10]
            authors = ', '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns)[:5])
            summary = entry.find('a:summary', ns).text.strip()[:400]
            cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns)[:3])
            papers.append({
                'id': arxiv_id_clean,
                'title': title,
                'authors': authors,
                'published': published,
                'abstract': summary,
                'categories': cats
            })
        return papers
    except Exception as e:
        return [{'error': str(e)}]

# Search queries for each direction
queries = {
    'A': 'all:mNGS+AND+all:pathogen+AND+all:detection',
    'B': 'all:clinical+AND+all:agent+AND+all:RAG+AND+all:diagnosis',
    'C': 'all:RLHF+AND+all:medical+AND+all:safety',
    'D': 'all:protein+AND+all:language+AND+all:generation',
    'E': 'all:genomic+AND+all:foundation+AND+all:DNA',
    'F': 'all:multimodal+AND+all:medical+AND+all:imaging',
    'X': 'all:drug+AND+all:discovery+AND+all:agent'
}

all_results = {}
for d, query in queries.items():
    print(f"Searching Direction {d}...")
    r = search_arxiv(query, max_results=8)
    all_results[d] = r
    if r and 'error' not in r[0]:
        print(f"  Found {len(r)} papers")
        for p in r[:3]:
            print(f"  [{p['id']}] {p['title'][:80]}")
    else:
        print(f"  Error: {r[0].get('error', 'unknown') if r else 'empty'}")
    time.sleep(6)  # Rate limit

with open('/tmp/arxiv_final.json', 'w') as f:
    json.dump(all_results, f)
print("\nAll results saved to /tmp/arxiv_final.json")
