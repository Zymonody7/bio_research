#!/usr/bin/env python3
"""Search OpenAlex API for papers - it has generous rate limits."""
import urllib.request
import urllib.parse
import time
import json

queries = [
    ('A', 'metagenomic next-generation sequencing mNGS pathogen detection artificial intelligence deep learning'),
    ('C', 'reinforcement learning human feedback medical alignment healthcare language model'),
    ('D', 'protein language model representation learning enzyme design structure'),
    ('E', 'genomic foundation model DNA sequence pre-training transformer language'),
    ('F', 'multimodal medical AI agent clinical diagnosis vision language model radiology'),
]

all_papers = {}

for dir_label, q in queries:
    params = urllib.parse.urlencode({
        'search': q,
        'filter': 'from_publication_date:2025-01-01,is_oa:true',
        'sort': 'publication_date:desc',
        'per_page': 8,
        'select': 'id,doi,title,authorships,publication_date,abstract_inverted_index,primary_location'
    })
    url = f'https://api.openalex.org/works?{params}'
    
    for attempt in range(3):
        try:
            print(f'Searching Direction {dir_label} (attempt {attempt+1})...', flush=True)
            time.sleep(1)
            req = urllib.request.Request(url, headers={
                'User-Agent': 'HermesResearch/2.0 (mailto:research@example.com)',
                'Accept': 'application/json'
            })
            resp = urllib.request.urlopen(req, timeout=20)
            data = json.loads(resp.read().decode())
            
            papers = []
            for work in data.get('results', []):
                # Reconstruct abstract from inverted index
                abstract_idx = work.get('abstract_inverted_index', {})
                if abstract_idx:
                    word_positions = []
                    for word, positions in abstract_idx.items():
                        for pos in positions:
                            word_positions.append((pos, word))
                    word_positions.sort()
                    abstract = ' '.join(w for _, w in word_positions)[:400]
                else:
                    abstract = ''
                
                authors = []
                for authorship in work.get('authorships', [])[:3]:
                    author_name = authorship.get('author', {}).get('display_name', '')
                    if author_name:
                        authors.append(author_name)
                
                # Extract arxiv ID from DOI if available
                doi = work.get('doi', '') or ''
                arxiv_id = ''
                if 'arxiv.org' in doi:
                    arxiv_id = doi.split('/')[-1]
                
                primary_loc = work.get('primary_location', {}) or {}
                source = primary_loc.get('source', {}) or {}
                venue = source.get('display_name', '')
                
                papers.append({
                    'openalex_id': work.get('id', ''),
                    'arxiv_id': arxiv_id,
                    'doi': doi.replace('https://doi.org/', ''),
                    'title': work.get('title', 'N/A'),
                    'authors': authors,
                    'date': work.get('publication_date', ''),
                    'abstract': abstract,
                    'venue': venue,
                    'direction': dir_label
                })
            
            all_papers[dir_label] = papers
            print(f'  Direction {dir_label}: {len(papers)} papers found')
            for p in papers:
                arxiv_info = f" [arxiv:{p['arxiv_id']}]" if p['arxiv_id'] else ""
                print(f"    [{p.get('date','')[:10]}] {p['title'][:70]}{arxiv_info}")
            print()
            break
            
        except Exception as e:
            print(f'  ERROR: {e}')
            if attempt < 2:
                time.sleep(5)

# Merge with previous Semantic Scholar results
try:
    with open('/tmp/s2_search_results.json', 'r') as f:
        prev = json.load(f)
    for k, v in all_papers.items():
        if v:  # Only update if we got results
            prev[k] = v
    all_papers = prev
except:
    pass

with open('/tmp/s2_search_results.json', 'w') as f:
    json.dump(all_papers, f, indent=2, ensure_ascii=False)

total = sum(len(v) for v in all_papers.values())
print(f"\nTotal papers across all directions: {total}")
for d, papers in all_papers.items():
    print(f"  {d}: {len(papers)} papers")
