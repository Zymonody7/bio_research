#!/usr/bin/env python3
"""Search arxiv API for specific preprints."""
import urllib.request
import urllib.parse
import time
import xml.etree.ElementTree as ET
import json

queries = [
    ('A', 'cat:q-bio.GN+AND+all:mNGS'),
    ('B', 'cat:cs.AI+AND+all:clinical+AND+all:RAG'),
    ('C', 'cat:cs.CL+AND+all:RLHF+AND+all:medical'),
    ('D', 'cat:q-bio.BM+AND+all:protein+AND+all:language+model'),
    ('E', 'cat:q-bio.GN+AND+all:genomic+AND+all:foundation+model'),
    ('F', 'cat:cs.AI+AND+all:multimodal+AND+all:medical+AND+all:agent'),
    ('X', 'cat:q-bio.QM+AND+all:AI+AND+all:drug+AND+all:discovery'),
]

results = {}
ns = {'atom': 'http://www.w3.org/2005/Atom'}

for dir_label, q in queries:
    url = f'https://export.arxiv.org/api/query?search_query={q}&sortBy=submittedDate&sortOrder=descending&max_results=5'
    try:
        time.sleep(6)
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/2.0 (mailto:research@example.com)'})
        resp = urllib.request.urlopen(req, timeout=20)
        data = resp.read().decode()
        root = ET.fromstring(data)
        papers = []
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns)
            title_text = title.text.strip().replace('\n', ' ') if title is not None else 'N/A'
            id_elem = entry.find('atom:id', ns)
            arxiv_url = id_elem.text.strip() if id_elem is not None else ''
            arxiv_id = arxiv_url.split('/abs/')[-1] if '/abs/' in arxiv_url else ''
            published = entry.find('atom:published', ns)
            pub_date = published.text[:10] if published is not None else 'N/A'
            authors = []
            for author in entry.findall('atom:author', ns):
                name = author.find('atom:name', ns)
                if name is not None:
                    authors.append(name.text.strip())
            summary = entry.find('atom:summary', ns)
            abstract = summary.text.strip().replace('\n', ' ')[:400] if summary is not None else 'N/A'
            papers.append({
                'id': arxiv_id, 'title': title_text, 'authors': authors[:3],
                'date': pub_date, 'abstract': abstract, 'url': arxiv_url,
                'direction': dir_label
            })
        results[dir_label] = papers
        print(f'=== Dir {dir_label}: {len(papers)} papers ===')
        for p in papers:
            print(f'  [{p["date"]}] {p["id"]}: {p["title"][:75]}')
        print()
    except Exception as e:
        print(f'=== Dir {dir_label} ERROR: {e} ===')
        results[dir_label] = []

with open('/tmp/arxiv_api_results.json', 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f'Total: {sum(len(v) for v in results.values())}')
