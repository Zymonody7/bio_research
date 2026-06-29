#!/usr/bin/env python3
"""Additional PubMed searches for underrepresented directions."""
import urllib.request
import json
import time

seen_ids = set()
with open('/tmp/seen_ids.txt') as f:
    for line in f:
        seen_ids.add(line.strip())

with open('/tmp/detailed_results.json') as f:
    existing = json.load(f)
existing_ids = {p['id'] for p in existing}
existing_dois = {p.get('doi', '') for p in existing}

def search_pubmed(query, retmax=6):
    papers = []
    try:
        search_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query.replace(" ", "+")}&retmax={retmax}&sort=date&retmode=json'
        req = urllib.request.Request(search_url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode())
        ids = data.get('esearchresult', {}).get('idlist', [])
        
        if not ids:
            return papers
        
        time.sleep(0.4)
        
        detail_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={",".join(ids)}&retmode=json'
        req2 = urllib.request.Request(detail_url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp2 = urllib.request.urlopen(req2, timeout=15)
        detail_data = json.loads(resp2.read().decode())
        
        for uid in ids:
            info = detail_data.get('result', {}).get(uid, {})
            if not info or 'title' not in info:
                continue
            
            authors = info.get('authors', [])
            author_names = [a.get('name', '') for a in authors[:3]]
            
            doi = ''
            for aid in info.get('articleids', []):
                if aid.get('idtype') == 'doi':
                    doi = aid.get('value', '')
                    break
            
            pmid = info.get('uid', '')
            pubdate = info.get('pubdate', '')
            year = pubdate[:4] if pubdate else '2025'
            
            paper_id = doi if doi else f'PMID:{pmid}'
            
            # Skip seen
            if paper_id in seen_ids or paper_id in existing_ids:
                continue
            if doi and (doi in seen_ids or doi in existing_ids):
                continue
            
            paper = {
                'id': paper_id,
                'pmid': pmid,
                'doi': doi,
                'title': info.get('title', ''),
                'authors': author_names,
                'year': year,
                'journal': info.get('fulljournalname', ''),
                'url': f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/' if pmid else '',
            }
            papers.append(paper)
    except Exception as e:
        print(f'  PubMed error: {e}', flush=True)
    return papers

# Additional searches
queries = [
    ('B', 'retrieval augmented generation clinical decision support LLM 2025'),
    ('B', 'medical knowledge graph large language model clinical'),
    ('B', 'clinical AI agent reasoning tool use medical'),
    ('C', 'reinforcement learning human feedback medical LLM alignment safety'),
    ('C', 'preference optimization medical language model clinical'),
    ('F', 'multimodal medical imaging AI diagnosis vision language model'),
    ('F', 'medical VLM clinical reasoning radiology pathology'),
    ('X', 'artificial intelligence drug discovery molecular generation 2025'),
    ('X', 'AI epidemiology infectious disease surveillance outbreak'),
    ('A', 'metagenomic next generation sequencing pathogen identification AI 2025'),
    ('D', 'protein design language model diffusion generation 2025'),
    ('E', 'DNA foundation model genome language model pretraining 2025'),
]

new_papers = []
for direction, query in queries:
    print(f'PubMed [{direction}] {query[:50]}...', flush=True)
    papers = search_pubmed(query, retmax=5)
    for p in papers:
        p['direction'] = direction
        if not any(np['id'] == p['id'] for np in new_papers):
            new_papers.append(p)
            print(f'  NEW: {p["id"]}: {p["title"][:70]}', flush=True)
    time.sleep(0.5)

with open('/tmp/additional_pubmed.json', 'w') as f:
    json.dump(new_papers, f, indent=2)

print(f'\n=== Additional PubMed: {len(new_papers)} new papers ===')
