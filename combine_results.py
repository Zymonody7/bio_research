#!/usr/bin/env python3
"""Read all search results, deduplicate, and select best papers."""
import json

# Load OpenAlex results
with open('/tmp/openalex_full.json', 'r') as f:
    openalex = json.load(f)

# Load Semantic Scholar results
with open('/tmp/s2_search_results.json', 'r') as f:
    s2 = json.load(f)

# Load dedup tracker
with open('/Users/mondyzy/research-papers/.seen_papers.json', 'r') as f:
    seen_data = json.load(f)
seen_ids = set(seen_data.get('papers', {}).keys())

# Combine and deduplicate
all_papers = {}

# Add Semantic Scholar papers first (they have arxiv IDs)
for dir_label, papers in s2.items():
    for p in papers:
        paper_id = p.get('arxiv_id', '') or p.get('doi', '') or p.get('title', '')
        if paper_id not in seen_ids and p.get('title'):
            if dir_label not in all_papers:
                all_papers[dir_label] = []
            all_papers[dir_label].append(p)

# Add OpenAlex papers
for dir_label, papers in openalex.items():
    for p in papers:
        paper_id = p.get('arxiv_id', '') or p.get('doi', '') or p.get('title', '')
        if paper_id not in seen_ids and p.get('title'):
            if dir_label not in all_papers:
                all_papers[dir_label] = []
            # Check if already added from S2
            existing_titles = [ep.get('title', '') for ep in all_papers.get(dir_label, [])]
            if p.get('title') not in existing_titles:
                all_papers[dir_label].append(p)

print("=== DEDUPLICATED RESULTS ===")
for dir_label in sorted(all_papers.keys()):
    papers = all_papers[dir_label]
    print(f"\nDirection {dir_label}: {len(papers)} unique papers")
    for i, p in enumerate(papers):
        arxiv_info = f" [arxiv:{p.get('arxiv_id', '')}]" if p.get('arxiv_id') else ""
        print(f"  {i+1}. [{p.get('date', '')[:10]}] {p['title'][:80]}{arxiv_info}")
        print(f"     Authors: {', '.join(p.get('authors', [])[:3])}")
        print(f"     Venue: {p.get('venue', 'N/A')}")

total = sum(len(v) for v in all_papers.values())
print(f"\n\nTotal unique papers: {total}")
print(f"Papers already seen: {len(seen_ids)}")

# Save combined results
with open('/tmp/combined_papers.json', 'w') as f:
    json.dump(all_papers, f, indent=2, ensure_ascii=False)
