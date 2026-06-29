#!/usr/bin/env python3
"""Get detailed abstracts for promising papers and search for more."""
import json
import re
import urllib.request
import time

# Load seen IDs
seen_ids = set()
with open('/tmp/seen_ids.txt') as f:
    for line in f:
        seen_ids.add(line.strip())

def get_paper_details(paper_id):
    """Get full details for a paper from Semantic Scholar."""
    try:
        # Try DOI first
        if paper_id.startswith('10.'):
            url = f'https://api.semanticscholar.org/graph/v1/paper/DOI:{paper_id}?fields=title,authors,year,abstract,externalIds,url,publicationDate,venue'
        elif re.match(r'\d{4}\.\d+', paper_id):
            url = f'https://api.semanticscholar.org/graph/v1/paper/ARXIV:{paper_id}?fields=title,authors,year,abstract,externalIds,url,publicationDate,venue'
        elif paper_id.startswith('PMID:'):
            pmid = paper_id.replace('PMID:', '')
            url = f'https://api.semanticscholar.org/graph/v1/paper/PMID:{pmid}?fields=title,authors,year,abstract,externalIds,url,publicationDate,venue'
        else:
            return None
        
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read().decode())
        return data
    except Exception as e:
        return None

# Curated list of promising papers to check
papers_to_check = [
    # Direction A - mNGS + AI
    ('A', '10.1016/j.mimet.2026.107592', 'AI in clinical metagenomic pathogen detection review'),
    ('A', '10.1186/s12879-025-11814-5', 'Clinical utility of mNGS'),
    ('A', '10.1109/IC2E365635.2025.11167377', 'AI-Driven Pathogen Detection'),
    ('A', '10.1002/admt.202500025', 'Deep Learning Immunoassay Microfluidic'),
    
    # Direction B - Clinical Agent + RAG
    ('B', '10.1016/j.parkreldis.2026.108292', 'Multi-agent conversational AI clinical'),
    ('B', '10.3389/fmed.2025.1716327', 'Self-correcting Agentic Graph RAG hepatology'),
    ('B', '10.1093/eurjcn/zvag029', 'AI Agent Delirium Screening'),
    
    # Direction C - RLHF Medical
    ('C', '10.1016/j.ejrad.2025.111984', 'Aligning LLMs with radiologists RLHF'),
    
    # Direction D - Protein Language Models
    ('D', '10.1093/bib/bbag293', 'ProtDML protein function'),
    ('D', '10.1002/advs.75931', 'ProSiteHunter protein-nucleic'),
    ('D', '10.1093/bib/bbag257', 'KSDiffusion phosphorylation'),
    ('D', '2606.25865', 'Molexar multimodal molecular foundation'),
    
    # Direction E - Genomic Foundation Models
    ('E', '10.1109/TCBBIO.2026.3705107', 'Adapting Evo for functional genomics'),
    ('E', '10.1038/s44259-026-00219-2', 'resLens antibiotic resistance'),
    ('E', '2502.03499', 'Omni-DNA unified genomic FM'),
    ('E', '10.64898/2026.05.22.727045', 'OryzaG3 rice pangenome'),
    ('E', '10.64898/2026.05.14.725245', 'DamageFormer DNA lesion'),
    ('E', '10.1093/bfgp/elag005', 'LM self-training labeled data 99%'),
    
    # Direction F - Multimodal Clinical
    ('F', '10.1002/mco2.70833', 'GenAI LLMs clinical oncology'),
    
    # Direction X
    ('X', '10.1021/acs.jcim.9b00365', 'Drug Repositioning Database'),
]

results = []
for direction, pid, hint in papers_to_check:
    if pid in seen_ids:
        continue
    
    print(f'Checking [{direction}] {pid}...', end=' ', flush=True)
    details = get_paper_details(pid)
    time.sleep(1.5)
    
    if details and details.get('title'):
        ext_ids = details.get('externalIds', {})
        arxiv_id = ext_ids.get('ArXiv', '')
        doi = ext_ids.get('DOI', pid if pid.startswith('10.') else '')
        
        authors = [a.get('name', '') for a in (details.get('authors') or [])[:3]]
        abstract = (details.get('abstract') or '')[:500]
        
        paper = {
            'id': arxiv_id if arxiv_id else pid,
            'doi': doi,
            'title': details.get('title', ''),
            'authors': authors,
            'year': str(details.get('year', 2025)),
            'abstract': abstract,
            'direction': direction,
            'url': details.get('url', f'https://doi.org/{doi}' if doi else ''),
            'venue': details.get('venue', ''),
            'pub_date': details.get('publicationDate', ''),
        }
        results.append(paper)
        print(f'✓ {details.get("title", "")[:60]}')
    else:
        print(f'✗ not found')

# Save
with open('/tmp/detailed_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f'\n=== Got details for {len(results)} papers ===')
for p in results:
    print(f"[{p['direction']}] {p['id']}: {p['title'][:70]}")
    print(f"  Authors: {', '.join(p['authors'])}")
    print(f"  Abstract: {p['abstract'][:120]}...")
