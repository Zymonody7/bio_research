#!/usr/bin/env python3
"""Fetch new papers from arxiv listing pages and filter for relevant ones."""
import urllib.request
import re
import json
import time
import xml.etree.ElementTree as ET

ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

# Step 1: Scrape IDs from listing pages
def scrape_listing(category):
    url = f"https://arxiv.org/list/{category}/new"
    try:
        html = urllib.request.urlopen(url, timeout=15).read().decode('utf-8')
        ids = re.findall(r'href\s*=\s*"/abs/(\d{4}\.\d{4,5})"', html)
        return list(dict.fromkeys(ids))[:40]
    except Exception as e:
        print(f"  Error scraping {category}: {e}")
        return []

print("Step 1: Scraping listing pages...")
all_ids = {}
for cat in ['cs.AI', 'cs.CL', 'cs.LG', 'q-bio.GN', 'q-bio.BM', 'stat.ML']:
    ids = scrape_listing(cat)
    all_ids[cat] = ids
    print(f"  {cat}: {len(ids)} IDs")
    time.sleep(1)

# Combine and deduplicate
combined_ids = []
for ids in all_ids.values():
    combined_ids.extend(ids)
combined_ids = list(dict.fromkeys(combined_ids))
print(f"\nTotal unique IDs: {len(combined_ids)}")

# Step 2: Fetch details in batches
def fetch_batch(ids):
    papers = []
    for i in range(0, len(ids), 10):
        batch = ids[i:i+10]
        batch_str = ','.join(batch)
        url = f"https://export.arxiv.org/api/query?id_list={batch_str}&max_results=10"
        try:
            resp = urllib.request.urlopen(url, timeout=25)
            root = ET.fromstring(resp.read())
            for entry in root.findall('a:entry', ns):
                title_el = entry.find('a:title', ns)
                title = title_el.text.strip().replace('\n', ' ') if title_el is not None else 'N/A'
                
                id_el = entry.find('a:id', ns)
                arxiv_id = id_el.text.strip().split('/abs/')[-1] if id_el is not None else 'N/A'
                arxiv_id_clean = re.sub(r'v\d+$', '', arxiv_id)
                
                pub_el = entry.find('a:published', ns)
                published = pub_el.text[:10] if pub_el is not None else 'N/A'
                
                authors_els = entry.findall('a:author', ns)
                authors = ', '.join(a.find('a:name', ns).text for a in authors_els[:5] if a.find('a:name', ns) is not None)
                
                sum_el = entry.find('a:summary', ns)
                summary = sum_el.text.strip()[:400] if sum_el is not None else ''
                
                cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns)[:3])
                
                papers.append({
                    'id': arxiv_id_clean,
                    'title': title,
                    'authors': authors,
                    'published': published,
                    'abstract': summary,
                    'categories': cats
                })
        except Exception as e:
            print(f"  Batch error: {e}")
        time.sleep(5)  # Rate limit
    return papers

print("\nStep 2: Fetching paper details...")
papers = fetch_batch(combined_ids[:50])
print(f"Fetched {len(papers)} papers")

# Step 3: Filter for relevant directions
keywords = {
    'A': ['mngs', 'metagenomic', 'pathogen', 'microbiome', 'amplicon', 'sequencing', 'antimicrobial', 'resistance', 'outbreak', 'viral', 'epidemiol'],
    'B': ['clinical agent', 'rag', 'knowledge graph', 'medical diagnosis', 'ehr', 'clinical reasoning', 'medical agent', 'clinical agent', 'diagnostic'],
    'C': ['rlhf', 'alignment', 'safety', 'preference optimization', 'dpo', 'medical', 'clinical safety', 'reward model'],
    'D': ['protein', 'antibody', 'peptide', 'enzyme', 'protein design', 'protein language', 'protein structure', 'binding'],
    'E': ['genomic', 'dna', 'single cell', 'transcriptome', 'gene expression', 'genome', 'chromatin', 'regulatory'],
    'F': ['multimodal', 'medical imaging', 'vlm', 'radiology', 'pathology', 'clinical', 'medical vision', 'diagnostic imaging'],
    'X': ['drug discovery', 'drug design', 'molecular', 'compound', 'therapeutic']
}

filtered = {d: [] for d in keywords}
for paper in papers:
    title_lower = paper['title'].lower()
    abstract_lower = paper.get('abstract', '').lower()
    text = title_lower + ' ' + abstract_lower
    for d, kws in keywords.items():
        if any(kw in text for kw in kws):
            # Avoid duplicates across directions
            if paper['id'] not in [p['id'] for p in filtered[d]]:
                filtered[d].append(paper)

for d, p_list in filtered.items():
    print(f"\nDirection {d}: {len(p_list)} relevant papers")
    for p in p_list[:3]:
        print(f"  [{p['id']}] {p['title'][:80]}")
        print(f"    Published: {p['published']} | Cats: {p['categories'][:50]}")

with open('/tmp/filtered_papers.json', 'w') as f:
    json.dump(filtered, f)
print("\nFiltered results saved to /tmp/filtered_papers.json")
