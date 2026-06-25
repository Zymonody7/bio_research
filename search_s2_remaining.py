#!/usr/bin/env python3
"""Search remaining directions via Semantic Scholar API, one at a time."""
import urllib.request
import urllib.parse
import time
import json
import sys

# Read existing results
try:
    with open('/tmp/s2_search_results.json', 'r') as f:
        all_papers = json.load(f)
except:
    all_papers = {}

# Directions still needed
queries = [
    ('A', 'metagenomic next-generation sequencing pathogen detection deep learning clinical'),
    ('C', 'reinforcement learning human feedback medical alignment healthcare safety'),
    ('D', 'protein language model representation learning enzyme design'),
    ('E', 'genomic foundation model DNA sequence pre-training transformer'),
    ('F', 'multimodal medical AI agent clinical diagnosis vision language'),
]

for dir_label, q in queries:
    if dir_label in all_papers and len(all_papers[dir_label]) > 0:
        print(f'Direction {dir_label} already has {len(all_papers[dir_label])} papers, skipping')
        continue
    
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(q)}&limit=10&fields=title,authors,year,abstract,url,externalIds,publicationDate,venue&sort=publicationDate:desc'
    
    for attempt in range(3):
        try:
            print(f'Searching Direction {dir_label} (attempt {attempt+1})...', flush=True)
            time.sleep(20)  # Long delay
            req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/2.0 (academic-paper-curation)'})
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
            print(f'  Direction {dir_label}: {len(papers)} papers found')
            for p in papers:
                arxiv_info = f" [arxiv:{p['arxiv_id']}]" if p['arxiv_id'] else ""
                print(f"    [{p.get('date','?')[:10]}] {p['title'][:70]}{arxiv_info}")
            print()
            break  # Success
            
        except Exception as e:
            print(f'  ERROR: {e}')
            if attempt < 2:
                time.sleep(30)

# Save all results
with open('/tmp/s2_search_results.json', 'w') as f:
    json.dump(all_papers, f, indent=2, ensure_ascii=False)

total = sum(len(v) for v in all_papers.values())
print(f"\nTotal papers across all directions: {total}")
for d, papers in all_papers.items():
    print(f"  {d}: {len(papers)} papers")
