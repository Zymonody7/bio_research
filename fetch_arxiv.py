#!/usr/bin/env python3
import urllib.request
import xml.etree.ElementTree as ET

arxiv_ids = [
    "2509.13300",  # A - AmpliconHunter
    "2602.07905",  # B - MedCoG
    "2511.04720",  # B - RADAR
    "2603.03054",  # C - PrivMedChat
    "2602.22973",  # C - Expert AI Diagnostic Alignment
    "2510.03370",  # D - InstructPLM-mu
    "2509.07983",  # D - Steering PLMs
    "2601.22203",  # E - Gengram
    "2604.06549",  # E - Genomic LMs fail positional
    "2604.16570",  # E - In Search of Lost DNA
    "2506.19835",  # F - MAM
    "2605.11224",  # F - ABRA
    "2605.08445",  # F - Benchmarking Gen/Agentic AI
    "2602.00019",  # X - AutoBinder Agent
    "2507.11588",  # X - SToFM
]

id_list = ",".join(arxiv_ids)
api_url = f"http://export.arxiv.org/api/query?id_list={id_list}&max_results=20"

req = urllib.request.Request(api_url)
data = urllib.request.urlopen(req).read().decode('utf-8')

root = ET.fromstring(data)
ns = {
    'atom': 'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom'
}

entries = root.findall('atom:entry', ns)
for e in entries:
    eid = e.find('atom:id', ns).text.split('/')[-1]
    title = e.find('atom:title', ns).text.strip().replace('\n', ' ')
    authors = [a.find('atom:name', ns).text for a in e.findall('atom:author', ns)]
    published = e.find('atom:published', ns).text[:10]
    abstract = e.find('atom:summary', ns).text.strip().replace('\n', ' ')[:800]
    primary = e.find('arxiv:primary_category', ns)
    subject = primary.attrib.get('term', '') if primary is not None else ''
    
    print(f"=== {eid} ===")
    print(f"Title: {title}")
    print(f"Authors: {', '.join(authors[:6])}")
    print(f"Published: {published}")
    print(f"Subject: {subject}")
    print(f"Abstract: {abstract}")
    print()
