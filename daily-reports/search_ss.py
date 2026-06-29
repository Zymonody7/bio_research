#!/usr/bin/env python3
"""Search arxiv via RSS feed and Semantic Scholar API."""
import urllib.request
import re
import time
import json

all_papers = []

# Arxiv RSS feeds for different categories
rss_feeds = [
    ('A', 'https://rss.arxiv.org/rss/q-bio.GN'),  # Genomics
    ('D', 'https://rss.arxiv.org/rss/q-bio.BM'),  # Biomolecules
    ('E', 'https://rss.arxiv.org/rss/q-bio.GN'),  # Genomics
]

# Semantic Scholar search queries
ss_queries = [
    ('A', 'mNGS metagenomic pathogen detection AI deep learning'),
    ('B', 'clinical agent RAG knowledge graph medical LLM'),
    ('C', 'RLHF medical alignment healthcare LLM'),
    ('D', 'protein language model design generation'),
    ('E', 'genomic foundation model DNA language'),
    ('F', 'multimodal clinical agent medical imaging'),
    ('X', 'drug repurposing AI clinical trial'),
]

def search_semantic_scholar(query, direction, limit=5):
    """Search Semantic Scholar API."""
    papers = []
    try:
        url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query.replace(" ", "+")}&year=2025-2026&limit={limit}&fields=title,authors,year,abstract,externalIds,url'
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode())
        
        for item in data.get('data', []):
            ext_ids = item.get('externalIds', {})
            arxiv_id = ext_ids.get('ArXiv', '')
            doi = ext_ids.get('DOI', '')
            pmid = ext_ids.get('PubMed', '')
            
            paper_id = arxiv_id if arxiv_id else (doi if doi else f'PMID:{pmid}')
            authors = [a.get('name', '') for a in (item.get('authors') or [])[:3]]
            
            paper = {
                'id': paper_id,
                'title': item.get('title', ''),
                'authors': authors,
                'year': str(item.get('year', 2025)),
                'abstract': (item.get('abstract') or '')[:400],
                'direction': direction,
                'url': item.get('url', ''),
                'source': 'semantic_scholar'
            }
            papers.append(paper)
    except Exception as e:
        print(f'  SS error: {e}', flush=True)
    return papers

# Search Semantic Scholar
for direction, query in ss_queries:
    print(f'\n=== Direction {direction}: Semantic Scholar ===', flush=True)
    time.sleep(3)  # Rate limit
    papers = search_semantic_scholar(query, direction, limit=5)
    for p in papers:
        all_papers.append(p)
        print(f'  [{direction}] {p["id"]}: {p["title"][:80]}', flush=True)

# Also try arxiv via web page extraction
print('\n=== Arxiv direct search ===', flush=True)
arxiv_searches = [
    ('A', 'mNGS+AI+pathogen'),
    ('B', 'clinical+agent+RAG+knowledge+graph'),
    ('D', 'protein+language+model'),
    ('E', 'genomic+foundation+model'),
]

for direction, q in arxiv_searches:
    time.sleep(5)
    try:
        url = f'https://arxiv.org/search/?searchtype=all&query={q}&start=0'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
        resp = urllib.request.urlopen(req, timeout=20)
        html = resp.read().decode()
        
        # Extract paper IDs and titles from HTML
        # Arxiv search results have class "list-title"
        ids = re.findall(r'arXiv:(\d{4}\.\d+)', html)
        titles = re.findall(r'<p class="title is-5 mathjax">\s*([^<]+)', html)
        
        for pid, title in zip(ids[:5], titles[:5]):
            title = title.strip()
            if not any(p['id'] == pid for p in all_papers):
                paper = {
                    'id': pid,
                    'title': title,
                    'authors': [],
                    'year': '2025',
                    'abstract': '',
                    'direction': direction,
                    'url': f'https://arxiv.org/abs/{pid}',
                    'source': 'arxiv_search'
                }
                all_papers.append(paper)
                print(f'  [{direction}] {pid}: {title[:80]}', flush=True)
    except Exception as e:
        print(f'  Arxiv search error: {e}', flush=True)

# Save
output = {'papers': all_papers, 'total': len(all_papers)}
with open('/tmp/ss_results.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f'\n=== TOTAL from SS+Arxiv: {len(all_papers)} papers ===')
