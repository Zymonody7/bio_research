#!/usr/bin/env python3
"""Additional searches for underrepresented directions."""
import json
import re
import urllib.request
import time

seen_ids = set()
with open('/tmp/seen_ids.txt') as f:
    for line in f:
        seen_ids.add(line.strip())

# Already found papers
with open('/tmp/detailed_results.json') as f:
    existing = json.load(f)
existing_ids = {p['id'] for p in existing}

def search_ss(query, direction, limit=8):
    papers = []
    try:
        url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query.replace(" ", "+")}&year=2025-2026&limit={limit}&fields=title,authors,year,abstract,externalIds,url,venue,publicationDate'
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode())
        
        for item in data.get('data', []):
            ext_ids = item.get('externalIds', {})
            arxiv_id = ext_ids.get('ArXiv', '')
            doi = ext_ids.get('DOI', '')
            pmid = ext_ids.get('PubMed', '')
            
            paper_id = arxiv_id if arxiv_id else (doi if doi else '')
            if not paper_id:
                continue
            
            # Skip seen
            if paper_id in seen_ids or paper_id in existing_ids:
                continue
            if doi in seen_ids or doi in existing_ids:
                continue
            
            authors = [a.get('name', '') for a in (item.get('authors') or [])[:3]]
            abstract = (item.get('abstract') or '')[:500]
            
            paper = {
                'id': paper_id,
                'doi': doi,
                'title': item.get('title', ''),
                'authors': authors,
                'year': str(item.get('year', 2025)),
                'abstract': abstract,
                'direction': direction,
                'url': item.get('url', ''),
                'venue': item.get('venue', ''),
                'pub_date': item.get('publicationDate', ''),
                'source': 'ss_additional'
            }
            papers.append(paper)
    except Exception as e:
        print(f'  SS error: {e}', flush=True)
    return papers

# Additional queries for underrepresented directions
additional = [
    ('B', 'medical AI agent diagnostic reasoning tool use'),
    ('B', 'clinical RAG retrieval augmented generation EHR'),
    ('B', 'medical knowledge graph integration LLM'),
    ('C', 'medical LLM safety alignment preference optimization'),
    ('C', 'healthcare AI alignment reward model clinical'),
    ('F', 'multimodal medical imaging AI diagnosis VLM'),
    ('F', 'medical vision language model clinical reasoning'),
    ('X', 'AI drug discovery molecular generation'),
    ('X', 'AI epidemiology surveillance outbreak detection'),
    ('A', 'metagenomic sequencing classification deep learning 2025'),
    ('D', 'protein design language model diffusion'),
]

new_papers = []
for direction, query in additional:
    print(f'Searching [{direction}] {query}...', flush=True)
    time.sleep(3.5)
    papers = search_ss(query, direction, limit=5)
    for p in papers:
        if not any(np['id'] == p['id'] for np in new_papers):
            new_papers.append(p)
            print(f'  NEW: [{p["direction"]}] {p["id"]}: {p["title"][:70]}', flush=True)
    print(f'  Found {len(papers)} new', flush=True)

# Save
with open('/tmp/additional_results.json', 'w') as f:
    json.dump(new_papers, f, indent=2)

print(f'\n=== Additional: {len(new_papers)} new papers ===')
