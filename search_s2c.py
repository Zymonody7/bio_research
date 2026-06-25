#!/usr/bin/env python3
"""Search remaining directions with very long delays - retry."""
import urllib.request
import urllib.parse
import time
import json

queries = [
    ('A', 'metagenomic next-generation sequencing pathogen detection machine learning'),
    ('C', 'reinforcement learning from human feedback medical alignment'),
    ('D', 'protein language model representation learning'),
    ('E', 'genomic foundation model pre-training DNA'),
    ('F', 'multimodal large language model clinical diagnosis')
]

all_papers = {}

for dir_label, q in queries:
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(q)}&limit=10&fields=title,authors,year,abstract,url,externalIds,publicationDate,venue&sort=publicationDate:desc'
    for attempt in range(3):
        try:
            time.sleep(15)  # Very long delay
            req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/2.0 (academic-research)'})
            resp = urllib.request.urlopen(req, timeout=30)
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
            break  # Success, move to next
            
        except Exception as e:
            print(f'  Direction {dir_label} attempt {attempt+1} ERROR: {e}')
            if attempt < 2:
                time.sleep(20)

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

print(f"\nTotal papers in all directions: {sum(len(v) for v in all_papers.values())}")
