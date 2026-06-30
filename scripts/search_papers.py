#!/usr/bin/env python3
"""Search for papers using bioRxiv API and arxiv API"""
import json
import sys
import time
import urllib.request
import urllib.parse

SEEN_PAPERS_PATH = "/Users/mondyzy/research-papers/.seen_papers.json"
with open(SEEN_PAPERS_PATH) as f:
    seen_data = json.load(f)
seen_ids = set(seen_data.get("papers", {}).keys())

print(f"Loaded {len(seen_ids)} seen paper IDs")

# Search terms per direction
SEARCHES = {
    "A": ["mNGS AI pathogen", "metagenomic sequencing artificial intelligence pathogen detection", "microbiome AI diagnostic"],
    "B": ["clinical agent RAG knowledge graph", "medical AI agent diagnosis", "healthcare LLM agent retrieval augmented"],
    "C": ["RLHF medical alignment", "healthcare LLM safety alignment", "medical AI reward model"],
    "D": ["protein language model design", "protein generation foundation model", "antibody design language model"],
    "E": ["genomic foundation model DNA", "DNA language model", "single cell foundation model"],
    "F": ["multimodal clinical agent", "medical VLM diagnosis", "radiology AI agent"],
}

def search_semantic_scholar(query, limit=5):
    """Search Semantic Scholar API"""
    encoded = urllib.parse.quote(query)
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&limit={limit}&fields=title,externalIds,url,year,authors,abstract"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ResearchAgent/1.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read())
        return data.get("data", [])
    except Exception as e:
        print(f"  S2 error for '{query}': {e}")
        return []

def search_arxiv_api(query, max_results=5):
    """Search arXiv API"""
    encoded = urllib.parse.quote(query)
    url = f"https://export.arxiv.org/api/query?search_query=all:{encoded}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ResearchAgent/1.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        content = resp.read().decode("utf-8")
        # Simple XML parsing
        import re
        entries = re.findall(r'<entry>(.*?)</entry>', content, re.DOTALL)
        results = []
        for entry in entries:
            title_match = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
            id_match = re.search(r'<id>http://arxiv.org/abs/(.*?)</id>', entry)
            published_match = re.search(r'<published>(.*?)</published>', entry)
            authors_match = re.findall(r'<name>(.*?)</name>', entry)
            
            if title_match and id_match:
                arxiv_id = id_match.group(1).split('v')[0]
                results.append({
                    'title': title_match.group(1).strip().replace('\n', ' '),
                    'id': arxiv_id,
                    'year': published_match.group(1)[:4] if published_match else 'N/A',
                    'authors': ', '.join(authors_match[:3])
                })
        return results
    except Exception as e:
        print(f"  arXiv error for '{query}': {e}")
        return []

all_found = {}

for direction, queries in SEARCHES.items():
    all_found[direction] = []
    for q in queries:
        print(f"\nSearching [{direction}]: {q}")
        
        # Try Semantic Scholar
        papers = search_semantic_scholar(q)
        for p in papers:
            ext_ids = p.get("externalIds", {})
            arxiv_id = ext_ids.get("ArXiv", "")
            doi = ext_ids.get("DOI", "")
            paper_id = arxiv_id if arxiv_id else doi
            title = p.get("title", "")
            
            if paper_id and paper_id not in seen_ids and paper_id not in [pp['id'] for pp in all_found[direction]]:
                all_found[direction].append({
                    'id': paper_id,
                    'title': title,
                    'year': p.get('year', 'N/A'),
                    'authors': ', '.join([a.get('name', '') for a in (p.get('authors', []) or [])[:3]]),
                    'source': 'S2'
                })
                print(f"  NEW [{paper_id}] {title}")
        
        time.sleep(3)
        
        # Try arxiv API
        arxiv_papers = search_arxiv_api(q)
        for p in arxiv_papers:
            if p['id'] not in seen_ids and p['id'] not in [pp['id'] for pp in all_found[direction]]:
                all_found[direction].append(p)
                print(f"  NEW [{p['id']}] {p['title']}")
        
        time.sleep(3)

print("\n\n=== SUMMARY ===")
total = 0
for d, papers in all_found.items():
    print(f"Direction {d}: {len(papers)} new papers")
    total += len(papers)
    for p in papers:
        print(f"  [{p['id']}] {p['title']}")
print(f"\nTotal new papers: {total}")

# Save results
with open("/Users/mondyzy/research-papers/scripts/search_results.json", "w") as f:
    json.dump(all_found, f, indent=2, ensure_ascii=False)
