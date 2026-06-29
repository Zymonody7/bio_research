#!/usr/bin/env python3
import urllib.request
import re
import time
import json

queries = [
    ('A', 'mNGS AI pathogen detection metagenomic deep learning'),
    ('B', 'clinical agent RAG knowledge graph medical LLM'),
    ('C', 'RLHF medical alignment healthcare LLM safety'),
    ('D', 'protein language model design generation'),
    ('E', 'genomic foundation model DNA language pretraining'),
    ('F', 'multimodal clinical agent medical imaging diagnosis'),
    ('X', 'drug repurposing AI clinical trial synthetic biology proteomics multi-omics'),
]

all_papers = []

for direction, query in queries:
    print(f'\n=== Direction {direction}: {query} ===', flush=True)
    try:
        q = query.replace(' ', '+')
        url = f'https://export.arxiv.org/api/query?search_query={q}&sortBy=submittedDate&sortOrder=descending&max_results=6'
        req = urllib.request.Request(url, headers={'User-Agent': 'HermesResearch/1.0 (research agent)'})
        resp = urllib.request.urlopen(req, timeout=20)
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
                
                if pid_m and title_m:
                    pid = pid_m.group(1).strip()
                    title = title_m.group(1).strip().replace('\n', ' ')
                    abstract = summary_m.group(1).strip().replace('\n', ' ')[:300] if summary_m else ''
                    year = published_m.group(1) if published_m else '2025'
                    
                    paper = {
                        'id': pid,
                        'title': title,
                        'authors': authors[:3],
                        'year': year,
                        'abstract': abstract,
                        'direction': direction,
                        'url': f'https://arxiv.org/abs/{pid}'
                    }
                    all_papers.append(paper)
                    print(f'  [{direction}] {pid}: {title[:80]}', flush=True)
            except Exception as e:
                print(f'  Parse error: {e}', flush=True)
                
    except Exception as e:
        print(f'  Error: {e}', flush=True)
    
    time.sleep(4)

output = {'papers': all_papers, 'total': len(all_papers)}
with open('/tmp/arxiv_results.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f'\nTotal papers found: {len(all_papers)}')
