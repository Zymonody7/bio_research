#!/usr/bin/env python3
"""Curate the best papers across all directions."""
import json
import urllib.request
import time

# Load all results
with open('/tmp/detailed_results.json') as f:
    detailed = json.load(f)

with open('/tmp/additional_pubmed.json') as f:
    additional = json.load(f)

# Curated selection of the most relevant papers per direction
# Based on title relevance, recency, and journal quality
curated = []

# Direction A: mNGS + AI pathogen detection
curated.extend([
    {'id': '10.1016/j.mimet.2026.107592', 'direction': 'A', 'relevance': 'high', 'reason': 'Comprehensive review of AI in clinical mNGS'},
    {'id': '10.1109/IC2E365635.2025.11167377', 'direction': 'A', 'relevance': 'high', 'reason': 'AI-Driven Pathogen Detection Systems'},
    {'id': '10.1186/s13073-025-01480-2', 'direction': 'A', 'relevance': 'high', 'reason': 'Simultaneous pathogen + AMR gene detection'},
    {'id': '10.1093/bib/bbaf592', 'direction': 'A', 'relevance': 'medium', 'reason': 'FGeneBERT for metagenomic gene function'},
])

# Direction B: Clinical Agent + RAG/KG
curated.extend([
    {'id': '10.3389/fmed.2025.1716327', 'direction': 'B', 'relevance': 'high', 'reason': 'Self-correcting Agentic Graph RAG for hepatology'},
    {'id': '10.1038/s41746-026-02869-y', 'direction': 'B', 'relevance': 'high', 'reason': 'Autonomous AI agent for ED clinic knowledge+data'},
    {'id': '10.1093/jamia/ocag110', 'direction': 'B', 'relevance': 'high', 'reason': 'CUI-Curate: GraphRAG for clinical concept normalization'},
    {'id': '10.1016/j.jbi.2026.105045', 'direction': 'B', 'relevance': 'high', 'reason': 'Comprehensive survey of AI agents in healthcare'},
    {'id': '10.1007/s11548-026-03694-0', 'direction': 'B', 'relevance': 'medium', 'reason': 'EchoAgent: guideline-centric reasoning for echo'},
])

# Direction C: RLHF Medical Alignment
curated.extend([
    {'id': '10.1016/j.ejrad.2025.111984', 'direction': 'C', 'relevance': 'high', 'reason': 'RLHF alignment of LLMs with radiologists'},
    {'id': '10.1109/JBHI.2026.3707092', 'direction': 'C', 'relevance': 'high', 'reason': 'Multimodal Bidirectional DPO and Instruction Tuning'},
])

# Direction D: Protein Language Models
curated.extend([
    {'id': '10.1093/bib/bbag293', 'direction': 'D', 'relevance': 'high', 'reason': 'ProtDML: label-aware protein function representation'},
    {'id': '10.1093/bib/bbag257', 'direction': 'D', 'relevance': 'high', 'reason': 'KSDiffusion: conditional diffusion for phosphorylation'},
    {'id': '10.1016/j.jare.2025.11.046', 'direction': 'D', 'relevance': 'medium', 'reason': 'Language models for antifungal generation'},
])

# Direction E: Genomic Foundation Models
curated.extend([
    {'id': '10.1109/TCBBIO.2026.3705107', 'direction': 'E', 'relevance': 'high', 'reason': 'Adapting Evo genome FM for functional genomics'},
    {'id': '10.64898/2026.05.14.725245', 'direction': 'E', 'relevance': 'high', 'reason': 'DamageFormer: multimodal DNA lesion detection'},
    {'id': '10.1093/bfgp/elag005', 'direction': 'E', 'relevance': 'high', 'reason': 'LM self-training reduces labeled data 99%'},
    {'id': '10.1101/2025.08.27.672609', 'direction': 'E', 'relevance': 'medium', 'reason': 'PlantCAD2: long-context DNA LM cross-species'},
    {'id': '10.1109/TCBBIO.2025.3614354', 'direction': 'E', 'relevance': 'medium', 'reason': 'DeepGene: pan-genome foundation model'},
])

# Direction F: Multimodal Clinical Agent
curated.extend([
    {'id': '10.1002/mco2.70833', 'direction': 'F', 'relevance': 'medium', 'reason': 'GenAI and LLMs in clinical oncology review'},
    {'id': '10.1038/s41591-026-04503-6', 'direction': 'F', 'relevance': 'high', 'reason': 'Generative AI clinical decision support in primary care'},
])

# Direction X: Serendipitous
curated.extend([
    {'id': '10.1038/s43588-026-00998-8', 'direction': 'X', 'relevance': 'high', 'reason': 'FLOWR: flow matching for de novo drug design'},
    {'id': 'PMID:42317811', 'direction': 'X', 'relevance': 'high', 'reason': 'Knowledge Graph + LLM for disease prediction'},
])

print(f"Curated {len(curated)} papers to check")

# Get full details for all curated papers
final_papers = []
seen_ids = set()
with open('/tmp/seen_ids.txt') as f:
    for line in f:
        seen_ids.add(line.strip())

def get_details(paper_id):
    try:
        if paper_id.startswith('10.'):
            url = f'https://api.semanticscholar.org/graph/v1/paper/DOI:{paper_id}?fields=title,authors,year,abstract,externalIds,url,venue,publicationDate'
        elif paper_id.startswith('PMID:'):
            pmid = paper_id.replace('PMID:', '')
            url = f'https://api.semanticscholar.org/graph/v1/paper/PMID:{pmid}?fields=title,authors,year,abstract,externalIds,url,venue,publicationDate'
        else:
            return None
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read().decode())
    except:
        return None

for c in curated:
    pid = c['id']
    if pid in seen_ids:
        print(f"SKIP (seen): {pid}")
        continue
    
    print(f"Fetching [{c['direction']}] {pid}...", end=' ', flush=True)
    time.sleep(2)
    details = get_details(pid)
    
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
            'direction': c['direction'],
            'relevance': c['relevance'],
            'reason': c['reason'],
            'url': details.get('url', ''),
            'venue': details.get('venue', ''),
            'pub_date': details.get('publicationDate', ''),
        }
        final_papers.append(paper)
        print(f'✓')
    else:
        print(f'✗')

# Save final curated list
with open('/tmp/final_curated.json', 'w') as f:
    json.dump(final_papers, f, indent=2)

print(f"\n=== FINAL: {len(final_papers)} curated papers ===")
by_dir = {}
for p in final_papers:
    d = p['direction']
    by_dir[d] = by_dir.get(d, 0) + 1
for d, c in sorted(by_dir.items()):
    print(f"  Direction {d}: {c} papers")
