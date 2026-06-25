#!/usr/bin/env python3
import json
d = json.load(open('/tmp/s2_search_results.json'))
for k, v in d.items():
    print(f'{k}: {len(v)} papers')
    for p in v:
        print(f"  [{p.get('date','')[:10]}] {p.get('arxiv_id',''):15s} {p['title'][:70]}")
