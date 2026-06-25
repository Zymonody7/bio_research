#!/usr/bin/env python3
"""Search arxiv API for papers across 7 directions."""
import urllib.request
import time
import xml.etree.ElementTree as ET
import json

queries = [
    ('A', 'mNGS AI pathogen detection metagenomic'),
    ('B', 'clinical agent RAG medical knowledge graph'),
    ('C', 'RLHF medical alignment healthcare'),
    ('D', 'protein language model design'),
    ('E', 'genomic foundation model DNA'),
    ('F', 'multimodal clinical agent medical'),
    ('X', 'AI biology drug discovery novel')
]

all_papers = {}

for dir_label, q in queries:
    search_q = '+AND+'.join(q.split())
    url = f'https://export.arxiv.org/api/query?search_query=all:{search_q}&sortBy=submittedDate&sortOrder=descending&max_results=10'
    try:
        time.sleep(4)  # Be gentle with rate limits
        req = urllib.request.Request(url, headers={'User-Agent': 'ResearchBot/1.0 (research-paper-curation)'})
        resp = urllib.request.urlopen(req, timeout=20)
        data = resp.read().decode()
        
        # Parse XML
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        root = ET.fromstring(data)
        papers = []
        
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns)
            title_text = title.text.strip().replace('\n', ' ') if title is not None else 'N/A'
            
            # Extract arxiv ID from the id URL
            id_elem = entry.find('atom:id', ns)
            arxiv_url = id_elem.text.strip() if id_elem is not None else ''
            arxiv_id = arxiv_url.split('/abs/')[-1] if '/abs/' in arxiv_url else ''
            
            # Published date
            published = entry.find('atom:published', ns)
            pub_date = published.text[:10] if published is not None else 'N/A'
            
            # Authors
            authors = []
            for author in entry.findall('atom:author', ns):
                name = author.find('atom:name', ns)
                if name is not None:
                    authors.append(name.text.strip())
            
            # Abstract
            summary = entry.find('atom:summary', ns)
            abstract = summary.text.strip().replace('\n', ' ')[:300] if summary is not None else 'N/A'
            
            # Categories
            categories = []
            for cat in entry.findall('{http://arxiv.org/schemas/atom}primary_category'):
                categories.append(cat.get('term', ''))
            
            papers.append({
                'id': arxiv_id,
                'title': title_text,
                'authors': authors[:3],
                'date': pub_date,
                'abstract': abstract,
                'url': arxiv_url,
                'categories': categories,
                'direction': dir_label
            })
        
        all_papers[dir_label] = papers
        print(f'=== Direction {dir_label} ({q}): {len(papers)} papers ===')
        for p in papers:
            print(f"  [{p['date']}] {p['id']}: {p['title'][:80]}")
        print()
        
    except Exception as e:
        print(f'=== Direction {dir_label} ERROR: {e} ===')
        all_papers[dir_label] = []

# Save full results as JSON
with open('/tmp/arxiv_search_results.json', 'w') as f:
    json.dump(all_papers, f, indent=2)

print("\nResults saved to /tmp/arxiv_search_results.json")
print(f"Total papers found: {sum(len(v) for v in all_papers.values())}")
