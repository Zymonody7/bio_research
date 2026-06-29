#!/usr/bin/env python3
"""Search arxiv with longer delays to avoid rate limits."""
import urllib.request
import re
import time
import json

queries = [
    ('A', 'mNGS+AI+pathogen+detection+metagenomic'),
    ('B', 'clinical+agent+RAG+knowledge+graph+medical'),
    ('C', 'RLHF+medical+alignment+healthcare'),
    ('D', 'protein+language+model+design'),
    ('E', 'genomic+foundation+model+DNA'),
    ('F', 'multimodal+clinical+agent+diagnosis'),
    ('X', 'drug+repurposing+AI+clinical+trial'),
]

all_papers = []

for i, (direction, q) in enumerate(queries):
    print(f'\n=== [{i+1}/7] Direction {direction} ===', flush=True)
    # Wait 8 seconds between requests
    if i > 0:
        print(f'  Waiting 8s...', flush=True)
        time.sleep(8)
    
    try:
        url = f'https://export.arxiv.org/api/query?search_query=all:{q}&sortBy=submittedDate&sortOrder=descending&max_results=5'
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearchBot/1.0 (research; mailto:research@example.com)'})
        resp = urllib.request.urlopen(req, timeout=30)
        data = resp.read().decode()
        
        count = data.count('<entry>')
        print(f'  Found {count} entries', flush=True)
        
        entries = data.split('<entry>')[1:]
        for entry in entries:
            try:
                pid_m = re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>', entry)
                title_m = re.search(r'<title>\s*([^<]+?)\s*</title>', entry)
                summary_m = re.search(r'<summary>\s*(.+?)\s*</summary>', entry, re.DOTALL)
                authors = re.findall(r'<name>([^<]+)</name>', entry)
                published_m = re.search(r'<published>(\d{4})', entry)
                updated_m = re.search(r'<updated>(\d{4}-\d{2}-\d{2})', entry)
                
                if pid_m and title_m:
                    pid = pid_m.group(1).strip()
                    title = title_m.group(1).strip().replace('\n', ' ')
                    abstract = summary_m.group(1).strip().replace('\n', ' ')[:400] if summary_m else ''
                    year = published_m.group(1) if published_m else '2025'
                    updated = updated_m.group(1) if updated_m else ''
                    
                    paper = {
                        'id': pid,
                        'title': title,
                        'authors': authors[:3],
                        'year': year,
                        'updated': updated,
                        'abstract': abstract,
                        'direction': direction,
                        'url': f'https://arxiv.org/abs/{pid}'
                    }
                    all_papers.append(paper)
                    print(f'  {pid}: {title[:90]}', flush=True)
            except Exception as e:
                print(f'  Parse error: {e}', flush=True)
                
    except Exception as e:
        print(f'  ERROR: {e}', flush=True)

output = {'papers': all_papers, 'total': len(all_papers)}
with open('/tmp/arxiv_results.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f'\n=== TOTAL: {len(all_papers)} papers found ===')
for p in all_papers:
    print(f"[{p['direction']}] {p['id']}: {p['title'][:80]}")
