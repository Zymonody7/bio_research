#!/usr/bin/env python3
"""Search remaining directions with longer delays."""
import urllib.request
import urllib.parse
import time
import json

queries = [
    ('A', 'metagenomic sequencing AI pathogen identification clinical'),
    ('C', 'RLHF alignment medical healthcare safety fine-tuning'),
    ('D', 'protein language model structure prediction design'),
    ('E', 'genomic foundation model DNA sequence pretrain'),
    ('F', 'multimodal medical agent clinical diagnosis vision'),
    ('X', 'AI biology breakthrough protein drug discovery agent')
]

all_papers = {}

for dir_label, q in queries:
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(q)}&limit=10&fields=title,authors,year,abstract,url,externalIds,publicationDate,venue&sort=publicationDate:desc'
    try:
        time.sleep(10)  # Longer delay
        req = urllib.request.Request(url, headers={'User-Agent': 'ResearchBot/1.0 (research)'})
        resp = urllib.request.urlopen(req, timeout=25)
        data = json.loads(resp.read().decode())
        
        papers = []
        for paper in data.get('data', []):
            ext_ids = paper.get('externalIds', {})
            arxiv_id = ext_ids.get('ArXiv', '')
            doi = ext_ids.get('DOI', '')
            
            year = paper.get('year', 0)
            if year and year < 2025:
                continue
                
            papers.append({
                'arxiv_id': arxiv_id,
                'doi': doi,
                'title': paper.get('title', 'N/A'),
                'authors': [a.get('name', '') for a in paper.get('authors', [])[:3]],
                'year': year,
                'date': paper.get('publicationDate', ''),
                'abstract': (paper.get('abstract', '') or '')[:400],
                'url': paper.get('url', ''),
                'venue': paper.get('venue', ''),
                'direction': dir_label
            })
        
        all_papers[dir_label] = papers
        print(f'=== Direction {dir_label}: {len(papers)} papers ===')
        for p in papers:
            arxiv_info = f" [arxiv:{p['arxiv_id']}]" if p['arxiv_id'] else ""
            print(f"  [{p.get('date','?')[:10]}] {p['title'][:70]}{arxiv_info}")
        print()
        
    except Exception as e:
        print(f'=== Direction {dir_label} ERROR: {e} ===')
        all_papers[dir_label] = []

# Merge with previous results
try:
    with open('/tmp/s2_search_results.json', 'r') as f:
        prev = json.load(f)
    prev.update(all_papers)
    all_papers = prev
except:
    pass

with open('/tmp/s2_search_results.json', 'w') as f:
    json.dump(all_papers, f, indent=2, ensure_ascii=False)

print(f"\nTotal papers found: {sum(len(v) for v in all_papers.values())}")
