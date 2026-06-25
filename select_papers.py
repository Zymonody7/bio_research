#!/usr/bin/env python3
"""Select best papers for daily report based on relevance."""
import json

# Load all results
with open('/tmp/combined_papers.json', 'r') as f:
    all_papers = json.load(f)

# Curated selection - papers most relevant to our 6 directions
# Filter criteria: specific methodology, recent, actionable
selected = {
    "A": [
        # mNGS + AI pathogen detection
        {
            "title": "Performance of metagenomic next-generation sequencing for bloodstream infections",
            "authors": ["Qin Qiao", "Ya-Chan Ning", "Si Zhu"],
            "date": "2026-06-15",
            "venue": "Frontiers in Cellular and Infection Microbiology",
            "abstract": "Evaluates clinical performance of mNGS for bloodstream infection diagnosis, comparing with conventional culture methods.",
            "badge": "🔥",
            "relevance": "Directly evaluates mNGS clinical utility"
        },
        {
            "title": "AI-Augmented Metagenomic Diagnostic for Early Detection of Emerging Microbial Pathogens",
            "authors": ["V.Manjula", "Divya C P", "Shilpa C"],
            "date": "2026-05-11",
            "venue": "IJETMS",
            "abstract": "Proposes AI-augmented metagenomic diagnostic pipeline for early detection of emerging microbial pathogens.",
            "badge": "🔥🔥",
            "relevance": "Core direction: AI + mNGS for pathogen detection"
        },
        {
            "title": "Next-Generation Target Discovery in ESKAPE Pathogens: An AI-Driven Framework",
            "authors": ["Eleonora Chines", "Adriana Antonina Tempesta", "Ludovica Boscarelli"],
            "date": "2026-05-06",
            "venue": "Antibiotics",
            "abstract": "AI-driven framework for discovering novel targets in ESKAPE pathogens using genomic and transcriptomic data.",
            "badge": "🔥",
            "relevance": "AI + pathogen genomics"
        },
        {
            "title": "MARM: a framework for malignancy risk prediction from host-derived CNV in bronchial samples",
            "authors": ["Zhili Chang", "X D Wang", "Minchao Zhao"],
            "date": "2026-05-21",
            "venue": "Frontiers in Microbiology",
            "abstract": "Uses metagenomic data and CNV analysis for cancer risk prediction from clinical samples.",
            "badge": "📎",
            "relevance": "mNGS beyond infectious disease"
        },
    ],
    "B": [
        # Clinical Agent + RAG/Knowledge Graph
        {
            "title": "Mapis: A Knowledge-Graph Grounded Multi-Agent Framework for Evidence-Based PCOS Diagnosis",
            "authors": ["Zanxiang He", "Meng Li", "Liyun Shi"],
            "date": "2025-12-17",
            "arxiv_id": "2512.15398",
            "venue": "arXiv",
            "abstract": "Multi-agent framework grounded in knowledge graphs for evidence-based PCOS diagnosis with explainable reasoning.",
            "badge": "🔥🔥",
            "relevance": "Core direction: KG-grounded clinical agent"
        },
        {
            "title": "MedRAG: Enhancing Retrieval-augmented Generation with Knowledge Graph-Elicited Reasoning",
            "authors": ["Xuejiao Zhao", "Siyan Liu", "Su-Yin Yang"],
            "date": "2025-04-22",
            "venue": "arXiv",
            "abstract": "Enhances RAG with knowledge graph reasoning for medical question answering.",
            "badge": "🔥🔥",
            "relevance": "Core direction: Medical RAG + KG"
        },
        {
            "title": "Evaluating large language model workflows in clinical decision support for triage",
            "authors": ["Farieda Gaber", "Maqsood Shaik", "Fabio Allega"],
            "date": "2025-05-09",
            "venue": "npj Digital Medicine",
            "abstract": "Evaluates LLM workflows for clinical triage decision support in real-world settings.",
            "badge": "🔥",
            "relevance": "Clinical agent evaluation"
        },
    ],
    "C": [
        # RLHF Medical Alignment
        {
            "title": "Large Language Models in Healthcare and Medical Applications: A Review",
            "authors": ["Subhankar Maity", "Manob Jyoti Saikia"],
            "date": "2025-06-10",
            "venue": "Bioengineering",
            "abstract": "Comprehensive review of LLMs in healthcare covering alignment, safety, and medical applications.",
            "badge": "📖",
            "relevance": "Review of medical LLM alignment"
        },
        {
            "title": "Open challenges and opportunities in federated foundation models towards biomedical applications",
            "authors": ["Xingyu Li", "Peng Lu", "Yu-Ping Wang"],
            "date": "2025-01-04",
            "venue": "BioData Mining",
            "abstract": "Discusses federated learning challenges for aligning foundation models to biomedical tasks.",
            "badge": "📎",
            "relevance": "Federated alignment for medical AI"
        },
    ],
    "D": [
        # Protein Language Models
        {
            "title": "Integrating protein language models and automatic biofoundry for enhanced protein engineering",
            "authors": ["Qiang Zhang", "Wanyi Chen", "Ming Qin"],
            "date": "2025-02-11",
            "venue": "Nature Communications",
            "abstract": "Integrates protein language models with automated biofoundry for high-throughput protein engineering.",
            "badge": "🔥🔥",
            "relevance": "Core direction: PLM + automated engineering"
        },
        {
            "title": "Biophysics-based protein language models for protein engineering",
            "authors": ["Sam Gelman", "Bryce Johnson", "Chase R. Freschlin"],
            "date": "2025-09-01",
            "venue": "Nature Methods",
            "abstract": "Incorporates biophysical principles into protein language models for improved engineering predictions.",
            "badge": "🔥🔥",
            "relevance": "Core direction: Physics-informed PLMs"
        },
        {
            "title": "Sparse autoencoders uncover biologically interpretable features in protein language models",
            "authors": ["Onkar Singh Gujral", "Mihir Bafna", "Eric J. Alm"],
            "date": "2025-08-19",
            "venue": "PNAS",
            "abstract": "Uses sparse autoencoders to extract interpretable biological features from protein language model representations.",
            "badge": "🔥",
            "relevance": "PLM interpretability"
        },
        {
            "title": "De novo design of peptide binders to conformationally diverse targets with contrastive learning",
            "authors": ["Suhaas Bhat", "Kalyan Palepu", "Lauren Hong"],
            "date": "2025-01-22",
            "venue": "Science Advances",
            "abstract": "Uses contrastive learning with protein language models for de novo peptide binder design.",
            "badge": "🔥",
            "relevance": "PLM + generative design"
        },
    ],
    "E": [
        # Genomic Foundation Models
        {
            "title": "A foundation model of transcription across human cell types",
            "authors": ["Xi Fu", "Shentong Mo", "Alejandro Buendia"],
            "date": "2025-01-08",
            "venue": "Nature",
            "abstract": "Presents a foundation model for predicting transcription across diverse human cell types.",
            "badge": "🔥🔥",
            "relevance": "Core direction: Genomic FM"
        },
        {
            "title": "Benchmarking DNA foundation models for genomic and genetic tasks",
            "authors": ["Haonan Feng", "Lang Wu", "Bingxin Zhao"],
            "date": "2025-11-28",
            "venue": "Nature Communications",
            "abstract": "Systematic benchmarking of DNA foundation models across multiple genomic tasks.",
            "badge": "🔥🔥",
            "relevance": "Core direction: DNA FM benchmarking"
        },
        {
            "title": "Evaluating the representational power of pre-trained DNA language models for regulatory elements",
            "authors": ["Ziqi Tang", "Nirali Somia", "Yiyang Yu"],
            "date": "2025-07-14",
            "venue": "Genome Biology",
            "abstract": "Evaluates how well pre-trained DNA language models capture regulatory element information.",
            "badge": "🔥",
            "relevance": "DNA LM evaluation for regulation"
        },
        {
            "title": "scPRINT: pre-training on 50 million cells allows robust gene network predictions",
            "authors": ["Jérémie Kalfon", "Jules Samaran", "Gabriel Peyré"],
            "date": "2025-04-16",
            "venue": "Nature Communications",
            "abstract": "Single-cell foundation model pre-trained on 50M cells for gene network prediction.",
            "badge": "🔥🔥",
            "relevance": "Core direction: Single-cell FM"
        },
    ],
    "F": [
        # Multimodal Clinical Agent
        {
            "title": "A multimodal visual-language foundation model for computational ophthalmology",
            "authors": ["Danli Shi", "Weiyi Zhang", "J. Yang"],
            "date": "2025-06-21",
            "venue": "npj Digital Medicine",
            "abstract": "Multimodal VLM for ophthalmic imaging diagnosis and clinical decision support.",
            "badge": "🔥🔥",
            "relevance": "Core direction: Multimodal medical VLM"
        },
        {
            "title": "Adopting AI-assisted digital pathology imaging analysis in MASH histology assessment",
            "authors": ["Daniel Yan Zheng Lim", "Wei Qiang Leow", "Daniela Allende"],
            "date": "2026-06-18",
            "venue": "Clinical and Molecular Hepatology",
            "abstract": "AI-assisted digital pathology for liver disease assessment using multimodal imaging.",
            "badge": "🔥",
            "relevance": "Multimodal clinical pathology"
        },
    ],
    "X": [
        # Serendipitous finds
        {
            "title": "BioChemAIgent: An AI-driven Protein Modeling and Docking Framework for Structure-Based Drug Design",
            "authors": ["Behnam Yousefi", "Nora C. Laubach", "Sven Heins"],
            "date": "2026-01-22",
            "venue": "bioRxiv",
            "abstract": "AI agent framework for automated protein modeling and molecular docking in drug discovery.",
            "badge": "🔥🔥",
            "relevance": "Cross-disciplinary: AI agent + protein modeling"
        },
        {
            "title": "AI-Driven Antimicrobial Peptide Discovery: Mining and Generation",
            "authors": ["Paulina Szymczak", "Wojciech Zarzecki", "Jiejing Wang"],
            "date": "2025-06-03",
            "venue": "Accounts of Chemical Research",
            "abstract": "AI approaches for discovering and generating antimicrobial peptides.",
            "badge": "📎",
            "relevance": "AI + antimicrobial peptide design"
        },
    ]
}

# Count totals
total = sum(len(v) for v in selected.values())
hot = sum(1 for papers in selected.values() for p in papers if '🔥🔥' in p.get('badge', ''))

print(f"Selected {total} papers, {hot} directly relevant (🔥🔥)")
for d, papers in selected.items():
    print(f"\nDirection {d}: {len(papers)} papers")
    for p in papers:
        print(f"  {p['badge']} {p['title'][:70]}")
        print(f"     {p.get('date', 'N/A')} | {p.get('venue', 'N/A')}")
        if p.get('arxiv_id'):
            print(f"     arxiv:{p['arxiv_id']}")

# Save selected papers
with open('/tmp/selected_papers.json', 'w') as f:
    json.dump(selected, f, indent=2, ensure_ascii=False)
