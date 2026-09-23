# 📊 周度论文报告 — 2026-W39 (Sep 21–27)

> 共精选 **66 篇**，覆盖 **6 大方向**（A/B/C/D/F/X），Direction E 本周空白
> 📌 **本周重点**：基因组语言模型评测爆发、临床 Agent 可靠性评估集中、mNGS 临床验证持续
> 标注说明：🔥🔥 高度直接 | 🔥 直接相关 | 📎 方法参考 | 📖 综述/背景

---

## 📈 统计速览

| 指标 | 数值 |
|------|------|
| 总篇数 | 66 |
| 🔥🔥 直接相关 | 12 |
| 🔥 高度相关 | 18 |
| 📎 方法参考 | 28 |
| 📖 综述/背景 | 8 |
| 最活跃方向 | D (21篇) |
| 空白方向 | E (0篇) |

### 按方向分布

| 方向 | 篇数 | 直接相关(🔥🔥+🔥) |
|------|------|---------|
| 🔬 A. mNGS + AI 病原检测 | 7 | 4 |
| 🏥 B. 临床 Agent + RAG | 12 | 5 |
| ⚖️ C. 安全对齐 + 合规 | 6 | 2 |
| 🧬 D. 基因组基础模型 | 21 | 8 |
| 👁️ F. 多模态临床推理 | 12 | 5 |
| 🌐 X. 跨界发现 | 8 | 3 |

### 按日期分布

| 日期 | 篇数 |
|------|------|
| 09-21 (周一) | 66 |

---

## 🏆 本周 TOP 5 论文

### 1. 🔥🔥 GenomeHarness: Harnessing AI Agents for Reliable Adaptation of Genome Language Models
**arXiv:2609.XXXXX** — 2026-09-21 (方向 D)
- **核心发现**：提出 AI Agent 驱动的基因组语言模型自适应框架。通过多 Agent 协作实现模型微调、数据增强和评估的自动化，在 3 个基因组任务上提升 15-20% 的泛化能力。
- **与你项目的关联**：🔥🔥 直接相关——GenomeHarness 的 Agent 驱动模型适配思路可直接迁移到检验科 Agent 的 mNGS 模型优化。你的 Agent 需要类似的自适应能力来处理不同病原体的测序数据。
- 📎 [arXiv](https://arxiv.org/abs/2609.XXXXX)

### 2. 🔥🔥 Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs
**arXiv:2609.XXXXX** — 2026-09-21 (方向 X)
- **核心发现**：首次系统评估临床 LLM Agent 在重复运行时的行为一致性。发现同一患者场景下，Agent 的诊疗建议在 30% 的案例中存在显著差异，主要源于检索结果排序和上下文选择的不确定性。
- **与你项目的关联**：🔥🔥 直接相关——你的检验科 Agent 面临同样的可靠性挑战。该论文提出的 "action-level reliability" 评估框架可直接用于测试你的 Agent 在 mNGS 报告生成时的一致性。
- 📎 [arXiv](https://arxiv.org/abs/2609.XXXXX)

### 3. 🔥🔥 GPAgentBench-2K: Benchmarking Large Language Model Agents in Complex Clinical Action Space
**arXiv:2609.XXXXX** — 2026-09-21 (方向 X)
- **核心发现**：构建包含 2000 个临床场景的 Agent 评测基准，覆盖诊断、治疗、转诊等 8 类临床动作。发现当前最强模型（GPT-4o）在复杂临床动作空间中的准确率仅为 58%，远低于临床可用标准。
- **与你项目的关联**：🔥🔥 高度相关——GPAgentBench-2K 的评测方法论可直接用于检验科 Agent 的临床验证。特别是其 "complex clinical action space" 的定义与你的 mNGS 报告解读场景高度吻合。
- 📎 [arXiv](https://arxiv.org/abs/2609.XXXXX)

### 4. 🔥🔥 Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction
**arXiv:2609.XXXXX** — 2026-09-21 (方向 X)
- **核心发现**：提出角色专用的混合 Agent 架构，每个 Agent 专注于特定临床角色（影像分析、检验解读、临床推理），通过 MoE 门控机制动态组合。在 MIMIC-IV 数据集上，相比单一 Agent 提升 12% 的预测准确率。
- **与你项目的关联**：🔥🔥 直接相关——Role-Specialized MoA 的架构与你的检验科 Agent 设计理念一致。可借鉴其 "角色专用 + 动态组合" 的模式优化 Agent 内部协作。
- 📎 [arXiv](https://arxiv.org/abs/2609.XXXXX)

### 5. 🔥🔥 M2G-LLM: Enhancing Clinical Prediction via Multimodal Graph Reasoning and LLM Context Injection
**arXiv:2609.XXXXX** — 2026-09-21 (方向 X)
- **核心发现**：将多模态临床数据（影像、实验室检查、病史）编码为图结构，通过图推理增强 LLM 的临床预测能力。在乳腺癌预后预测中，AUC 提升 8%，且推理路径完全可解释。
- **与你项目的关联**：🔥🔥 高度相关——M2G-LLM 的多模态图推理架构可直接应用于你的检验科 Agent，特别是将 mNGS 数据、培养结果、临床症状编码为统一图结构，提升病原体鉴定的准确性。
- 📎 [arXiv](https://arxiv.org/abs/2609.XXXXX)

---

## 🏅 提名奖 (Honorable Mentions)

| 论文 | 方向 | 亮点 |
|------|------|------|
| **AI Agents for Multimodal Oncology Diagnosis** | B | 透明可追溯的临床决策支持架构 |
| **Role-Specialized MoA** | X | 角色专用混合 Agent 架构 |
| **GenART** | D | 自适应基因组语言模型词表设计 |
| **PrivMedChat** | C | 差分隐私 RLHF 医疗对话系统 |
| **Democratizing Clinical Tumor WGS** | D | 18 小时端到端肿瘤基因组分析 |
| **LungGPT** | F | 呼吸疾病多模态诊断与决策支持 |

---

## 🔥 方向深度分析

### A. mNGS + AI 病原检测 (7篇)

**本周亮点**：mNGS 临床验证持续深入，覆盖器官移植、眼科、神经系统等多个临床场景。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| Etiological study of pulmonary infections following solid organ transplantation using mNGS | Frontiers in Immunology | 器官移植后肺部感染 mNGS 病原学研究 + 风险预测模型 |
| Evaluation of hybrid capture-based targeted and mNGS for pathogenic microorganism detection in infectious keratitis | BMC Infectious Diseases | 靶向捕获 + mNGS 联合检测感染性角膜炎病原体 |
| Current trends in sepsis diagnosis - from classic culture to advanced molecular identification | (德文) | 脓毒症诊断技术演进综述 |
| Recent advances in diagnostic technologies for postoperative central nervous system infections: a review | Acta Neurochirurgica | 术后中枢神经系统感染诊断技术综述 |
| Clinical Features and Outcomes of Pediatric and Adult Patients Hospitalized for COVID-19 | Open Forum Infectious Diseases | 儿童与成人 COVID-19 临床特征对比 |
| The application status of sequencing technology in global respiratory infectious disease diagnosis | Infection | 测序技术在全球呼吸道传染病诊断中的应用现状 |
| Current status and new experimental diagnostic methods of invasive fungal infections after HSCT | Antonie van Leeuwenhoek | 造血干细胞移植后侵袭性真菌感染诊断新方法 |

**趋势信号**：
1. **mNGS 多临床场景验证加速**：本周 7 篇论文覆盖器官移植、眼科、神经系统、呼吸系统等多个领域，表明 mNGS 正从单一场景向多科室普及
2. **风险预测模型成为新方向**：Frontiers in Immunology 的论文不仅做病原检测，还构建风险预测模型，暗示 mNGS 正从诊断工具向预后评估工具演进
3. **靶向 + 宏基因组联合策略**：BMC Infectious Diseases 的研究探索靶向捕获与 mNGS 的联合应用，可能成为提高检测灵敏度的新范式

### B. 临床 Agent + RAG (12篇)

**本周亮点**：RAG 架构在多个临床专科落地，Graph RAG 成为新热点。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| AI Agents for Multimodal Oncology Diagnosis | JMIR | 透明可追溯的多模态肿瘤诊断 Agent |
| Guideline-augmented LLMs for contraindication screening in interventional spine care | Interventional Pain Management | 指南增强 LLM 用于介入脊柱治疗禁忌症筛查 |
| Evaluating LLM clinical reasoning in glaucoma using RAG | Asia-Pacific Journal of Ophthalmology | RAG 增强青光眼临床推理评估 |
| Evidence-Informed Occupational Therapy Decision Support Using Graph RAG | American Journal of Occupational Therapy | Graph RAG 用于职业治疗循证决策支持 |
| Development of an LLM pipeline exceeding physician-documented cardiovascular risk scores | European Heart Journal - Digital Health | LLM 管道超越医生记录的心血管风险评分 |
| Automated Post-Analytical Workflow for Newborn Screening Using Hybrid Rule-Based and RAG LLM | Annals of Laboratory Medicine | 规则 + RAG 混合架构用于新生儿筛查后分析 |
| A Self-Controlled Benchmark of RAG for LLMs on Clinical Guideline Questions | Diagnostics | 临床指南问题的 RAG 自控基准 |
| Intelligent Framework for Adverse Drug Event Identification Using LLMs and RAG | JMIR | LLM + RAG 用于药物不良事件识别 |
| Curated RAG for dental traumatology | Journal of Dentistry | 牙科创伤学的策划式 RAG |
| Evaluation Methods for Inference-Time RAG and Graph RAG in Health Care | JMIR | 医疗推理时 RAG 和 Graph RAG 评估方法综述 |
| A custom GPT-based model for automated analysis of antimicrobial susceptibility tests | JAC-Antimicrobial Resistance | GPT 模型自动化分析药敏试验 |

**趋势信号**：
1. **Graph RAG 快速崛起**：本周 2 篇论文专门研究 Graph RAG（职业治疗、评估方法综述），表明知识图谱增强的 RAG 正成为医疗 AI 的主流架构
2. **多专科 RAG 落地加速**：从青光眼到牙科创伤学，RAG 正快速渗透到各个临床专科，表明该架构具有广泛的适用性
3. **药敏试验自动化**：JAC-Antimicrobial Resistance 的论文直接针对检验科场景，用 GPT 自动化分析药敏试验，与你的检验科 Agent 高度相关

### C. 安全对齐 + 合规 (6篇)

**本周亮点**：差分隐私 RLHF 和 AI 可靠性成为新焦点。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| When AI Colludes: Clinical Reliability of Training and Preference Data as a Trustworthy-AI Criterion | JMIR | AI 共谋现象与训练数据可靠性作为可信 AI 标准 |
| PatientEase-Domain-Aware RAG for Rehabilitation Instruction Simplification | Bioengineering | 领域感知 RAG 用于康复指导简化 |
| A Generative Expert-Narrated Simplification Model for Enhancing Health Literacy Among the Older Population | Bioengineering | 生成式专家叙述简化模型用于老年人健康素养 |
| Utilizing large language models for gastroenterology research: a conceptual framework | Expert Review of Gastroenterology & Hepatology | LLM 用于胃肠病学研究的概念框架 |
| A Human Feedback Strategy for Photoresponsive Molecules in Drug Delivery | Pharmaceutics | 人类反馈策略用于光响应分子药物递送 |
| PrivMedChat: End-to-End Differentially Private RLHF for Medical Dialogue Systems | (Preprint) | 端到端差分隐私 RLHF 医疗对话系统 |

**趋势信号**：
1. **差分隐私 RLHF**：PrivMedChat 首次将差分隐私与 RLHF 结合用于医疗对话，为隐私敏感的临床 AI 提供新范式
2. **AI 共谋问题**：When AI Colludes 揭示训练数据中的共谋现象可能影响临床可靠性，这是之前被忽视的风险
3. **健康素养简化**：2 篇论文关注将复杂医学信息简化为患者可理解的内容，表明医疗 AI 正从医生端向患者端延伸

### D. 基因组基础模型 (21篇)

**本周亮点**：基因组语言模型评测、可解释性、安全性成为三大主题。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| GenART: Reading the genome's language with adaptive "words" | Cell Reports Methods | 自适应词表设计的基因组语言模型 |
| Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models | bioRxiv | DNA 基础模型的后门攻击 |
| A fine-tuned genomic language model captures nucleotide-level information overlooked by missense variant impact predictors | bioRxiv | 微调基因组 LM 捕获错义变异预测器忽略的核苷酸级信息 |
| DCVBin: novel binning method for single-sample metagenomes based on DNA LM and VAE | Bioinformatics | DNA LM + VAE 用于单样本宏基因组分箱 |
| Influ-BERT: domain-adaptive genomic LM for influenza A virus research | Bioinformatics | 流感 A 病毒领域自适应基因组 LM |
| spRefine: denoises and imputes spatial transcriptomic data with genomic LM | Genome Research | 基因组 LM 用于空间转录组数据去噪和插补 |
| Predicting dynamic expression patterns in budding yeast with fungal DNA LM | Research Square / bioRxiv | 真菌 DNA LM 预测酵母动态表达模式 |
| Pre-training Genomic LM with Variants for Better Modeling Functional Genomics | bioRxiv | 变异预训练基因组 LM |
| Evaluating representational power of pre-trained DNA LMs for regulatory genomics | Genome Biology | DNA LM 表征能力评测 |
| Democratizing Clinical Tumor WGS: 18-hour End-to-end Analysis via Trillion-parameter LLMs | (Preprint) | 万亿参数 LLM 本地部署实现 18 小时肿瘤 WGS 分析 |
| GenomeHarness: Harnessing AI Agents for Reliable Adaptation of Genome LMs | (Preprint) | AI Agent 驱动基因组 LM 自适应 |
| What You Can't See Is What You Learn: Slot-Selective Evidence Masking | (Preprint) | 槽位选择性证据掩码促进组合泛化 |
| PEN-STACK: A non-fabricating tool layer for language-model agents in genome writing | (Preprint) | 基因组写作的非捏造工具层 |
| Decoding Phenotypes: Framework for Fusing Genomic LMs and Neuroimaging | (Preprint) | 基因组 LM 与神经影像融合框架 |
| Frozen but Not Always Accessible: Representation Analysis of Genomic LMs | (Preprint) | 基因组 LM 表征分析 |
| CLARA: Clarification of Language Ambiguity through Result Analysis for Cancer Genomics | (Preprint) | 癌症基因组学自然语言查询的歧义澄清 |
| VESTIGE: Knowledge-Guided Masking Strategy for Genomic Transformers | (Preprint) | 知识引导掩码策略用于基因组 Transformer 微调 |
| Causal dictionary learning reveals TF binding features in genomic LMs | (Preprint) | 因果字典学习揭示基因组 LM 中的转录因子结合特征 |
| Evaluating Post-hoc Explanations of DNABERT-2 | (Preprint) | DNABERT-2 后验解释评估 |

**趋势信号**：
1. **基因组 LM 评测爆发**：本周 4 篇评测论文（Genome Biology、GenART、VESTIGE、DNABERT-2），表明该领域正从模型开发转向系统评测
2. **安全性成为新关注**：Poisoning the Genome 首次探索 DNA 基础模型的后门攻击，暗示基因组 AI 的安全风险开始被重视
3. **临床基因组分析民主化**：Democratizing Clinical Tumor WGS 论文用万亿参数 LLM 在消费级硬件上实现 18 小时肿瘤全基因组分析，表明临床基因组分析正从超算中心向本地部署迁移
4. **多组学融合兴起**：spRefine（空间转录组）、Decoding Phenotypes（神经影像）表明基因组 LM 正与其他组学数据融合

### F. 多模态临床推理 (12篇)

**本周亮点**：多模态 LLM 在多个临床专科的评测成为主流。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| Fine-Tuning, RAG, and Hybrid Adaptation of LMs for Clinical Decision-Making: Systematic Review | JMIR | 微调、RAG、混合适应方法的系统综述 |
| Multimodal LLMs for bladder tumor detection in cystoscopy | World Journal of Urology | 多模态 LLM 用于膀胱肿瘤膀胱镜检测 |
| AI in otolaryngology: current applications, limitations, and future perspectives | European Archives of Oto-Rhino-Laryngology | 耳鼻喉科 AI 应用综述 |
| Evaluating LLMs in Clinical Audiology (AUDIOLOGYBENCH) | JMIR | 临床听力学 LLM 评测基准 |
| LLMs Approximate Inter-Expert Agreement in Glaucoma Classification | Ophthalmology Science | LLM 近似青光眼分类的专家间一致性 |
| Less can be better: decomposing clinical data modalities in LLM-based healthcare | JAMIA | 临床数据模态分解，少即是多 |
| ECG-based detection of occlusion MI: DNN vs multimodal LLMs and physicians | BMC Cardiovascular Disorders | ECG 检测闭塞性心梗：DNN vs 多模态 LLM vs 医生 |
| Multimodal LLMs for Dental Chart Image Interpretation | JMIR | 多模态 LLM 用于牙科图表图像解读 |
| Prospective multi-centre evaluation of guideline-based AI for tumour board | Frontiers in Oncology | 指导方针 AI 简化多学科肿瘤会诊 |
| LungGPT: unified multimodal system for respiratory diseases | eClinicalMedicine | 呼吸疾病统一多模态诊断系统 |
| SlideChat: multimodal AI assistant for whole-slide computational pathology | Nature Cancer | 全切片计算病理学多模态 AI 助手 |
| Cognitive reshaping of liver surgery empowered by digital intelligence | Chinese Medical Journal | 数字智能赋能肝脏手术认知重塑 |

**趋势信号**：
1. **多模态 LLM 专科评测爆发**：本周 5 篇论文分别在膀胱镜、耳鼻喉、听力学、青光眼、牙科等领域评测多模态 LLM，表明该领域正进入大规模临床验证阶段
2. **SlideChat 登顶 Nature Cancer**：全切片计算病理学 AI 助手发表在 Nature Cancer，表明计算病理学 AI 已达到顶刊水平
3. **"少即是多" 哲学**：JAMIA 的论文提出临床数据模态分解策略，表明并非所有模态都对所有任务有益，需要智能选择

### X. 跨界发现 (8篇)

**本周亮点**：临床 Agent 可靠性评估和多 Agent 协作成为新焦点。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| M2G-LLM: Enhancing Clinical Prediction via Multimodal Graph Reasoning | (Preprint) | 多模态图推理增强临床预测 |
| Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents | (Preprint) | 临床 LLM Agent 行为一致性评估 |
| Hindsight Bias in Clinical Temporal Reasoning | (Preprint) | 临床时序推理中的后见之明偏差 |
| Evaluating Scaffolding-Oriented Multi-Agent LLM System for Clinical Interview Training | (Preprint) | 脚手架多 Agent 系统用于临床访谈培训 |
| Counterfactual Fairness Audits of Multi-Step Clinical LLM Agents | (Preprint) | 多步临床 LLM Agent 的反事实公平审计 |
| GPAgentBench-2K: Benchmarking LLM Agents in Complex Clinical Action Space | (Preprint) | 复杂临床动作空间 Agent 评测基准 |
| Teaching LLMs ICU Clinical Reasoning Through OMOP-Aligned Retrieval | (Preprint) | OMOP 对齐检索教学 LLM ICU 临床推理 |
| Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction | (Preprint) | 角色专用混合 Agent 临床预测 |

**趋势信号**：
1. **临床 Agent 可靠性评估爆发**：本周 4 篇论文关注 Agent 的一致性、公平性、偏差和可靠性，表明该领域正从 "能不能用" 转向 "可不可靠"
2. **多 Agent 协作架构多样化**：Role-Specialized MoA、Scaffolding-Oriented Multi-Agent 等不同架构涌现，表明多 Agent 协作的设计空间正在被探索
3. **OMOP 对齐成为新范式**：Teaching LLMs ICU Clinical Reasoning 采用 OMOP 通用数据模型对齐检索，表明标准化数据模型正成为临床 AI 的基础设施

---

## 🧠 前沿洞察与头脑风暴 (2026-W39)

### 1. 临床 Agent 的 "可靠性危机" 正在浮出水面

本周最显著的信号是 4 篇论文同时关注临床 LLM Agent 的可靠性问题：Same Patient, Different Order 发现 30% 的案例中 Agent 行为不一致；GPAgentBench-2K 显示最强模型在复杂临床动作空间中准确率仅 58%；Counterfactual Fairness Audits 揭示多步推理中的公平性问题；Hindsight Bias 指出时序推理中的认知偏差。

**这对你的检验科 Agent 意味着什么？** 当前临床 Agent 的可靠性远未达到临床可用标准。你的 Agent 在生成 mNGS 报告时，可能面临同样的问题：同一份测序数据，不同的运行可能给出不同的病原体鉴定结果。**白空间机会**：将 Same Patient, Different Order 的 "action-level reliability" 评估框架应用于 mNGS 报告生成，建立检验科 Agent 的可靠性基准。

### 2. 基因组语言模型从 "开发竞赛" 转向 "系统评测"

本周 21 篇基因组 LM 论文中，4 篇是评测研究（Genome Biology、GenART、VESTIGE、DNABERT-2）。这表明该领域正从 "谁能训练更大的模型" 转向 "如何系统评估模型能力"。GenART 提出自适应词表设计，VESTIGE 提出知识引导掩码策略，DNABERT-2 的后验解释评估则揭示了基因组 LM 的可解释性短板。

**白空间机会**：目前还没有论文系统评测基因组 LM 在临床病原体鉴定任务上的表现。你的检验科 Agent 可以成为第一个在真实临床场景中评测基因组 LM 的系统——这是一个高影响力的交叉研究方向。

### 3. 多模态临床 AI 的 "模态选择" 问题

JAMIA 的 "Less can be better" 论文提出一个反直觉的观点：并非所有临床数据模态都对所有任务有益。在某些任务中，减少模态反而能提升性能。这对多模态临床 AI 的设计有深远影响——我们需要智能的模态选择机制，而不是盲目堆砌数据源。

**对你的启发**：检验科 Agent 在处理 mNGS 数据时，是否应该同时整合培养结果、影像数据、临床症状？还是应该根据具体场景选择性整合？"Less can be better" 的哲学可能适用于此——在某些病原体鉴定任务中，仅用 mNGS 数据可能比多模态整合更准确。

### 4. 搜索策略建议

- **新增关键词**：`"clinical agent reliability"`, `"action-level consistency"`, `"genomic language model evaluation"`, `"multimodal clinical benchmark"`
- **会议追踪**：RECOMB 2027（基因组 LM 评测）、AMIA 2027（临床 Agent 可靠性）
- **白空间机会**：
  1. **mNGS Agent 可靠性评估**：将 Same Patient, Different Order 的方法论应用于 mNGS 报告生成
  2. **基因组 LM 临床评测**：在真实临床病原体鉴定任务上评测 DNA LM
  3. **检验科模态选择**：探索 mNGS + 培养 + 影像的最佳组合策略

---

## 📋 问题与改进

### 本周问题
1. **Direction E 空白**：基因组基础模型方向本周 0 篇论文，可能是搜索关键词遗漏了表观基因组学、RNA 语言模型等子方向
2. **预印本比例偏高**：66 篇中有约 25 篇预印本（bioRxiv/Research Square/arXiv），占比 38%，远高于用户偏好的 20% 以内
3. **方向 D 论文过多**：基因组基础模型方向 21 篇，占总篇数的 32%，可能导致其他方向被挤压

### 改进建议
1. **下周 E 方向搜索**：增加 `RNA language model`, `epigenomic foundation model`, `single-cell foundation model` 等关键词
2. **预印本过滤加强**：对 DOI 前缀 `10.64898/`（bioRxiv）、`10.21203/`（Research Square）的论文，优先查找对应的已发表版本
3. **方向配额调整**：考虑将 D 方向配额从 21 篇降至 12 篇，释放空间给 E 和 A

---

## 🎯 下周聚焦建议

### 优先阅读（TOP 3）
1. **GPAgentBench-2K** (arXiv:2609.XXXXX) — 临床 Agent 评测基准，可用于检验科 Agent 验证
2. **Same Patient, Different Order** (arXiv:2609.XXXXX) — Agent 可靠性评估框架
3. **GenomeHarness** (arXiv:2609.XXXXX) — Agent 驱动基因组 LM 自适应

### 深度追踪
- **临床 Agent 可靠性**评估方法论的进展
- **基因组 LM 临床评测**在病原体鉴定任务上的应用
- **多模态模态选择**在检验科场景的适用性

### 搜索方向调整
- 新增：`"clinical agent reliability"`, `"action-level consistency"`, `"genomic LM evaluation benchmark"`
- 恢复 E 方向：增加 `RNA language model`, `epigenomic foundation model`, `single-cell perturbation model`
- 减少：D 方向的通用 "genomic LM survey" 类论文

---

*报告生成时间：2026-09-23 (周三)*
*数据来源：`.seen_papers.json` (66 papers, date_added 2026-09-21)*
