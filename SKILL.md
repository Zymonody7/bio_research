---
name: clinical-paper-monitor
description: "Daily clinical AI paper monitoring: search 6 directions, generate reports, import to Zotero with PDFs, push to GitHub."
version: 1.0.0
author: mondyzy
---

# Clinical AI Paper Monitor

Daily automated paper curation for clinical AI research across 6 core directions.
Generates structured reports, imports to Zotero with PDFs, and pushes to GitHub.

## Research Directions

| ID | Direction | Keywords |
|----|-----------|----------|
| A | mNGS + AI pathogen detection | metagenomic NGS, responsible pathogen ID, AI pathogen detection |
| B | Clinical Agent + RAG/KG | clinical decision support, medical KG, RAG healthcare, evidence chain |
| C | RLHF Medical Alignment | clinician preference, reward modeling, DPO/PPO clinical, medical alignment |
| D | Protein Language Models | pLM, ESM, structure prediction, antibody design, protein generation |
| E | Genomic Foundation Models | DNA language model, Evo, DNABERT, genomic pre-training, variant effect |
| F | Multimodal Clinical Agent | VLM clinical, medical imaging agents, multimodal diagnosis |
| X | Cross-directional / Serendipity | Biological FMs, clinical NLP, medical AI breakthroughs |

## Project Context

Researcher (mondyzy) is working on:
1. Fine-tuned model for mNGS responsible pathogen identification
2. LLM + RAG/KG for evidence chains and clinical report generation
3. Doctor-facing UI collecting RLHF data → harness agent
4. Protein and genomic large models research

## File Structure

```
~/research-papers/
├── daily-reports/     # YYYY-MM-DD.md daily markdown reports
├── bibtex/            # YYYY-MM-DD.bib for Zotero import
├── .seen_papers.json  # Deduplication tracker (arXiv IDs, DOIs)
├── zotero_import.py   # Direct Zotero SQLite importer + PDF downloader
└── .git/              # Git repo → github.com/Zymonody7/bio_research
```

## Zotero Collections (auto-created)

- Direction-A: mNGS+AI病原检出 (ID 50)
- Direction-B: 临床Agent+RAG/KG (ID 51)
- Direction-C: RLHF医学对齐 (ID 52)
- Direction-D: 蛋白质大模型 (ID 53)
- Direction-E: 基因组大模型 (ID 54)
- Direction-F: 多模态临床Agent (ID 55)
- Direction-X: 跨界发现 (ID 56)

## Cron Job

ID: `f573103c3534`
Schedule: daily at 09:00
Actions: search → dedup → report → bibtex → Zotero import → GitHub push
Delivery: origin (current chat)

## Zotero Importer

Script: `~/research-papers/zotero_import.py`

```bash
# Usage
python3 zotero_import.py bibtex/YYYY-MM-DD.bib              # Import with PDFs
python3 zotero_import.py bibtex/YYYY-MM-DD.bib --dry-run    # Preview only
python3 zotero_import.py bibtex/YYYY-MM-DD.bib --no-pdf     # Skip PDF download
```

Features:
- Direct SQLite insertion (no plugin needed)
- Auto PDF download for arXiv papers
- Auto-tagging from bib keywords (Direction tags)
- Auto-collection assignment
- Duplicate detection by DOI and title
- Must close Zotero before running (script auto-checks)

## Report Format

Each daily report includes:
- 6 direction sections (1-3 papers each)
- Relevance badges: 🔥🔥/🔥 = directly relevant, 📎 = method reference, 📖 = review
- One-liner takeaways + project relevance notes
- Cross-directional discoveries section
- Statistics table
- Top 3 recommended reads

## Deduplication

File: `~/research-papers/.seen_papers.json`
- Tracks all previously reported papers by arXiv ID or DOI
- Cron agent reads this FIRST before searching
- New papers appended after each run
- Format: `{"papers": {"id": {"date_added": "...", "direction": "A", "title": "..."}}}`

## GitHub

Repo: `github.com/Zymonody7/bio_research`
Remote: `git@github.com:Zymonody7/bio_research.git`
Branch: `main`

## blogwatcher-cli

Installed at: `~/bin/blogwatcher-cli`
Can be used for RSS monitoring of specific journals (optional enhancement).

## Setup Notes

1. Zotero must be installed at `/Applications/Zotero.app`
2. Zotero data at `/Users/mondyzy/Zotero/zotero.sqlite`
3. No plugins required — uses direct SQLite access
4. gh CLI authenticated for GitHub push
5. Python 3.9+ with no external dependencies (stdlib only)
