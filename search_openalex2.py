#!/usr/bin/env python3
"""Get full details from OpenAlex and try arxiv API for remaining directions."""
import urllib.request
import urllib.parse
import time
import json

# More targeted OpenAlex searches
queries = [
    ('A', 'mNGS metagenomic next generation sequencing pathogen artificial intelligence machine learning clinical'),
    ('B', 'clinical decision support large language model retrieval augmented generation knowledge graph medical'),
    ('C', 'reinforcement learning human feedback RLHF medical LLM alignment preference optimization healthcare'),
    ('D', 'protein language model PLM protein foundation model enzyme design structure prediction'),
    ('E', 'genomic foundation model DNA language model gene expression pre-training transformer'),
    ('F', 'multimodal large language model medical clinical diagnosis vision language radiology pathology agent'),
    ('X', 'AI agent drug discovery protein design biological language model breakthrough'),
]

all_papers = {}

for dir_label, q in queries:
    params = urllib.parse.urlencode({
        'search': q,
        'filter': 'from_publication_date:2025-01-01,type:article|review',
        'sort': 'relevance_score:desc',
        'per_page': 6,
        'select': 'id,doi,title,authorships,publication_date,abstract_inverted_index,primary_location,concepts'
    })
    url = f'https://api.openalex.org/works?{params}'
    
    try:
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
                abstract = ' '.join(w for _, w in word_positions)[:500]
            else:
                abstract = ''
            
            authors = []
            for authorship in work.get('authorships', [])[:4]:
                author_name = authorship.get('author', {}).get('display_name', '')
                if author_name:
                    authors.append(author_name)
            
            doi = work.get('doi', '') or ''
            arxiv_id = ''
            if 'arxiv.org' in doi:
                arxiv_id = doi.split('/')[-1]
            
            primary_loc = work.get('primary_location', {}) or {}
            source = primary_loc.get('source', {}) or {}
            venue = source.get('display_name', '')
            
            # Get concepts
            concepts = []
            for c in work.get('concepts', [])[:5]:
                concepts.append(c.get('display_name', ''))
            
            papers.append({
                'openalex_id': work.get('id', ''),
                'arxiv_id': arxiv_id,
                'doi': doi.replace('https://doi.org/', ''),
                'title': work.get('title', 'N/A'),
                'authors': authors,
                'date': work.get('publication_date', ''),
                'abstract': abstract,
                'venue': venue,
                'concepts': concepts,
                'direction': dir_label
            })
        
        all_papers[dir_label] = papers
        print(f'Direction {dir_label}: {len(papers)} papers')
        for p in papers:
            arxiv_info = f" [arxiv:{p['arxiv_id']}]" if p['arxiv_id'] else ""
            print(f"  [{p.get('date','')[:10]}] {p['title'][:80]}{arxiv_info}")
        print()
        
    except Exception as e:
        print(f'Direction {dir_label} ERROR: {e}')
        all_papers[dir_label] = []

# Save
with open('/tmp/openalex_full.json', 'w') as f:
    json.dump(all_papers, f, indent=2, ensure_ascii=False)

total = sum(len(v) for v in all_papers.values())
print(f"\nTotal: {total} papers")
