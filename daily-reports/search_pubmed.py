#!/usr/bin/env python3
"""Search via PubMed E-utilities and bioRxiv API as fallback."""
import urllib.request
import re
import time
import json
import xml.etree.ElementTree as ET

all_papers = []

# PubMed search queries mapped to directions
pubmed_queries = [
    ('A', 'mNGS metagenomic pathogen detection artificial intelligence deep learning'),
    ('B', 'clinical decision support agent retrieval augmented generation knowledge graph'),
    ('C', 'reinforcement learning human feedback medical alignment large language model'),
    ('D', 'protein language model protein design generation foundation model'),
    ('E', 'genomic foundation model DNA language model genome pretraining'),
    ('F', 'multimodal medical agent clinical imaging diagnosis'),
    ('X', 'drug repurposing artificial intelligence clinical trial synthetic biology'),
]

def search_pubmed(query, retmax=5):
    """Search PubMed and return paper details."""
    papers = []
    try:
        # Step 1: Search
        search_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query.replace(" ", "+")}&retmax={retmax}&sort=date&retmode=json'
        req = urllib.request.Request(search_url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode())
        ids = data.get('esearchresult', {}).get('idlist', [])
        
        if not ids:
            return papers
        
        time.sleep(0.5)
        
        # Step 2: Fetch details
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
            
            # Get DOI from articleids
            doi = ''
            for aid in info.get('articleids', []):
                if aid.get('idtype') == 'doi':
                    doi = aid.get('value', '')
                    break
            
            pmid = info.get('uid', '')
            pubdate = info.get('pubdate', '')
            year = pubdate[:4] if pubdate else '2025'
            
            paper = {
                'id': doi if doi else f'PMID:{pmid}',
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

# Also try bioRxiv
def search_biorxiv():
    """Get recent bioRxiv papers."""
    papers = []
    try:
        url = 'https://api.biorxiv.org/details/biorxiv/2025-06-01/2025-06-29/0?format=json'
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode())
        collection = data.get('collection', [])
        
        # Filter for relevant papers
        keywords = ['mNGS', 'metagenomic', 'pathogen', 'clinical agent', 'RAG', 'knowledge graph',
                     'RLHF', 'alignment', 'protein language', 'protein design', 'genomic foundation',
                     'DNA language', 'multimodal', 'drug repurposing', 'clinical trial']
        
        for item in collection[:200]:
            title = item.get('title', '').lower()
            if any(kw.lower() in title for kw in keywords):
                paper = {
                    'id': item.get('doi', ''),
                    'title': item.get('title', ''),
                    'authors': [item.get('authors', '')[:100]],
                    'year': '2025',
                    'journal': 'bioRxiv',
                    'url': f"https://doi.org/{item.get('doi', '')}",
                }
                papers.append(paper)
    except Exception as e:
        print(f'  bioRxiv error: {e}', flush=True)
    return papers

# Search PubMed for each direction
for direction, query in pubmed_queries:
    print(f'\n=== Direction {direction}: PubMed ===', flush=True)
    papers = search_pubmed(query, retmax=5)
    for p in papers:
        p['direction'] = direction
        all_papers.append(p)
        print(f'  [{direction}] {p["id"]}: {p["title"][:80]}', flush=True)
    time.sleep(0.4)

# Search bioRxiv
print(f'\n=== bioRxiv recent ===', flush=True)
biorxiv_papers = search_biorxiv()
for p in biorxiv_papers[:10]:
    all_papers.append(p)
    print(f'  [X] {p["id"]}: {p["title"][:80]}', flush=True)

# Save
output = {'papers': all_papers, 'total': len(all_papers)}
with open('/tmp/pubmed_results.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f'\n=== TOTAL: {len(all_papers)} papers found ===')
