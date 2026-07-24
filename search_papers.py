#!/usr/bin/env python3
"""Search arxiv via API for papers in our directions."""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import re
import sys

def search_arxiv(query, max_results=3):
    """Search arxiv API and return papers."""
    base_url = "https://export.arxiv.org/api/query"
    encoded_query = urllib.parse.quote(query)
    params = f"search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    url = f"{base_url}?{params}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Hermes-Research/1.0'})
        resp = urllib.request.urlopen(req, timeout=20)
        xml_data = resp.read().decode('utf-8')
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        root = ET.fromstring(xml_data)
        papers = []
        for entry in root.findall('atom:entry', ns):
            title_el = entry.find('atom:title', ns)
            summary_el = entry.find('atom:summary', ns)
            published_el = entry.find('atom:published', ns)
            id_el = entry.find('atom:id', ns)
            if title_el is None or id_el is None:
                continue
            title = ' '.join(title_el.text.strip().split())
            summary = ' '.join(summary_el.text.strip().split())[:200] if summary_el is not None and summary_el.text else ""
            published = published_el.text if published_el is not None else ""
            arxiv_url = id_el.text.strip()
            arxiv_match = re.search(r'(\d{4}\.\d{4,5})', arxiv_url)
            paper_id = arxiv_match.group(1) if arxiv_match else arxiv_url
            papers.append({
                'id': paper_id, 'title': title, 'url': arxiv_url,
                'summary': summary, 'published': published,
            })
        return papers
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []

queries = [
    ("A", "cat:q-bio.GN AND all:metagenomic AND all:AI"),
    ("A", "all:microbiome AND all:AI AND all:pathogen AND all:detection"),
    ("B", "all:clinical AND all:agent AND all:RAG AND all:medical"),
    ("B", "all:medical AND all:knowledge AND all:graph AND all:diagnosis"),
    ("C", "all:RLHF AND all:medical AND all:alignment"),
    ("C", "all:healthcare AND all:safety AND all:LLM AND all:reinforcement"),
    ("D", "all:protein AND all:language AND all:model AND all:design"),
    ("D", "all:antibody AND all:design AND all:deep AND all:learning"),
    ("E", "cat:q-bio.GN AND all:foundation AND all:model AND all:DNA"),
    ("E", "all:genomic AND all:language AND all:model AND all:DNA"),
    ("F", "all:multimodal AND all:medical AND all:agent AND all:diagnosis"),
    ("F", "all:medical AND all:imaging AND all:agent AND all:VLM"),
    ("X", "all:drug AND all:discovery AND all:agent AND all:AI"),
    ("X", "all:protein AND all:folding AND all:AI AND all:design"),
]

all_papers = {}
for direction, query in queries:
    papers = search_arxiv(query, max_results=3)
    for p in papers:
        if p['id'] not in all_papers:
            p['direction'] = direction
            all_papers[p['id']] = p
    print(f"[{direction}] '{query[:50]}...' -> {len(papers)} papers", file=sys.stderr)

print(json.dumps(list(all_papers.values()), indent=2))
print(f"\nTotal: {len(all_papers)}", file=sys.stderr)
