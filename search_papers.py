#!/usr/bin/env python3
"""Search arxiv for papers across 6 directions."""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
import sys

def search_arxiv(query, max_results=5):
    """Search arxiv API and return parsed results."""
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(max_results)
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HermesBot/1.0"})
        response = urllib.request.urlopen(req, timeout=30)
        data = response.read().decode("utf-8")
        
        # Parse XML
        root = ET.fromstring(data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        
        results = []
        for entry in root.findall("atom:entry", ns):
            title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
            arxiv_id_url = entry.find("atom:id", ns).text.strip()
            arxiv_id = arxiv_id_url.split("/abs/")[-1]
            summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")[:300]
            published = entry.find("atom:published", ns).text[:10]
            
            authors = []
            for author in entry.findall("atom:author", ns)[:3]:
                name = author.find("atom:name", ns).text.strip()
                authors.append(name)
            
            results.append({
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": authors,
                "abstract": summary,
                "published": published,
            })
        
        return results
    except Exception as e:
        return [{"error": str(e)}]


searches = {
    "A": [
        "mNGS AI pathogen detection",
        "metagenomic sequencing deep learning",
    ],
    "B": [
        "clinical agent RAG knowledge graph",
        "medical LLM agent retrieval augmented",
    ],
    "C": [
        "RLHF medical alignment",
        "reinforcement learning human feedback medical",
    ],
    "D": [
        "protein language model design",
        "protein foundation model fitness",
    ],
    "E": [
        "genomic foundation model DNA",
        "single cell foundation model",
    ],
    "F": [
        "multimodal medical VLM clinical",
        "medical vision language model diagnosis",
    ],
    "X": [
        "drug discovery agent AI",
        "bioinformatics agent protein design",
    ],
}

all_results = {}
for direction, queries in searches.items():
    dir_results = []
    seen_ids = set()
    for q in queries:
        print(f"Searching [{direction}] {q}...", file=sys.stderr)
        results = search_arxiv(q, max_results=4)
        for r in results:
            if "error" not in r and r["arxiv_id"] not in seen_ids:
                seen_ids.add(r["arxiv_id"])
                dir_results.append(r)
        time.sleep(3)  # Rate limit
    all_results[direction] = dir_results[:4]
    print(f"Direction {direction}: {len(all_results[direction])} papers", file=sys.stderr)

print(json.dumps(all_results, indent=2))
