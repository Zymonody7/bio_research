# 📊 周报 2026-W26（June 22-25, 2026）

> **覆盖**: 4 个工作日（周一至周四） | **总收录**: 96 篇论文
> **方向覆盖**: A(mNGS) B(Clinical Agent) C(RLHF) D(Protein LM) E(Genomic FM) F(Multimodal) X(Serendipitous)
> **本周亮点**: Clinical Agent + RAG/KG 持续爆发 | PLM 从预测走向工程闭环 | 多模态临床 AI 向专科化发展

---

## 📈 本周统计

| 日期 | 论文数 | 🔥🔥直接相关 | 🔥相关 | 📎参考 | 📖综述 |
|------|--------|-------------|--------|--------|--------|
| 6/22 (周一) | 29 | 18 | 6 | 5 | 0 |
| 6/23 (周二) | 32 | — | — | — | — |
| 6/24 (周三) | 14 | 8 | 3 | 3 | 0 |
| 6/25 (周四) | 21 | 10 | 2 | 2 | 1 |
| **合计** | **96** | **~36** | **~11** | **~10** | **1** |

### 方向分布

| 方向 | 本周论文数 | 占比 | 趋势 |
|------|-----------|------|------|
| A: mNGS + AI Pathogen | 12 | 12.5% | 📊 稳定（review论文拉高数量） |
| B: Clinical Agent + RAG/KG | 16 | 16.7% | 📈📈 本周最热方向 |
| C: RLHF Medical Alignment | 11 | 11.5% | 📊 稳定 |
| D: Protein Language Models | 15 | 15.6% | 📈 显著增长 |
| E: Genomic Foundation Models | 9 | 9.4% | 📊 稳定 |
| F: Multimodal Clinical Agent | 16 | 16.7% | 📈📈 持续高位 |
| X: Serendipitous | 17 | 17.7% | 📊 稳定 |

---

## 🏆 本周 Top 5 论文

| # | 方向 | 论文 | 亮点 | 来源日期 |
|---|------|------|------|---------|
| 🥇 | B | Semantic Reasoning in Medicine: KG Across Five Key Domains | KG 在临床推理中的系统性综述 | 6/22 |
| 🥈 | E | How Post-Training Shapes Biological Reasoning Models | 揭示后训练对生物推理的关键影响 | 6/24 |
| 🥉 | F | VitalAgent: Tool-Augmented Physiological Monitoring | 可穿戴设备的 Agent 增强监测 | 6/22 |
| 4 | D | Integrating PLM and Automatic Biofoundry | PLM + 自动化生物铸造厂闭环 | 6/25 |
| 5 | B | MedBeads: Agent-Native Immutable Data Substrate | 医疗 AI Agent 的不可变数据基础设施 | 6/24 |

---

## 📋 各方向详细回顾

### A. mNGS + AI Pathogen Detection（12篇）

**关键论文：**
- 🔥🔥 **AI-Augmented Metagenomic Diagnostic for Early Detection** (6/25) — AI 增强的宏基因组诊断流水线，用于新兴微生物病原体的早期检测
- 🔥 **Performance of mNGS for Bloodstream Infections** (6/25) — 评估 mNGS 在血流感染诊断中的临床性能
- 🔥 **AI in Clinical Metagenomic Pathogen Detection: A Critical Review** (6/23) — AI 驱动的临床宏基因组病原体检测综述
- 📎 **FUNGAR: Detecting Antifungal Resistance from Metagenomic Reads** (6/22) — 从宏基因组测序 reads 检测抗真菌耐药突变
- 📎 **MARM: Malignancy Risk Prediction from Host-derived CNV** (6/25) — 利用宏基因组 CNV 分析预测癌症风险

**本周趋势：** mNGS 领域本周出现了一篇重要综述（AI in Clinical Metagenomic Pathogen Detection），系统梳理了 AI 在 mNGS 流水线中的集成方式和挑战。临床验证类论文持续增加，表明 mNGS 正从技术开发向临床落地加速。⚠️ 值得注意的是，mNGS + LLM 的直接交叉仍是白色空间。

### B. Clinical Agent + RAG/Knowledge Graph（16篇）

**关键论文：**
- 🔥🔥 **Semantic Reasoning in Medicine: KG Across Five Key Domains** (6/22) — KG 在五个关键医疗领域中的系统性综述
- 🔥🔥 **HoT-SSM: Higher-order Temporal KG Reasoning with SSMs** (6/22) — SSM + Temporal KG 的临床推理新范式
- 🔥🔥 **RSA-KG: Graph-Based RAG for Recurrent Spontaneous Abortions** (6/23) — 基于图的 RAG 增强 AI KG 用于 RSA 诊断
- 🔥🔥 **MedRAG-Agent: Multi-Agent KG-Enhanced RAG** (6/23) — 多智能体 + KG 增强的医学 RAG 框架
- 🔥🔥 **MedBeads: Agent-Native Immutable Data Substrate** (6/24) — 医疗 AI Agent 的不可变数据基础设施
- 🔥🔥 **Mapis: KG-Grounded Multi-Agent for PCOS Diagnosis** (6/25) — 基于 KG 的多智能体 PCOS 诊断框架

**本周趋势：** Clinical Agent + RAG/KG 本周是论文数量最多的方向之一（16篇），且 🔥🔥 直接相关论文占比极高。三大趋势：① KG 作为临床推理的核心知识底座；② Multi-Agent + KG 的融合架构；③ Agent 原生数据基础设施（MedBeads）。HoT-SSM 将状态空间模型与 Temporal KG 结合，预示着 next-gen clinical KG 将融合高效序列建模与图推理。

### C. RLHF Medical Alignment（11篇）

**关键论文：**
- 🔥🔥 **PrivMedChat: End-to-End Differentially Private RLHF** (6/24) — 首个差分隐私 + RLHF 用于医疗对话
- 🔥 **RVPO: Risk-Sensitive Alignment via Variance Regularization** (6/24) — 方差正则化的风险敏感对齐
- 🔥 **Black-Box Behavioral Distillation Breaks Safety Alignment** (6/23) — 医疗 LLM 安全对齐的脆弱性
- 🔥 **CARES: Comprehensive Safety Evaluation in Medical LLMs** (6/23) — 医疗 LLM 安全性全面评估

**本周趋势：** RLHF 方向本周出现两个重要信号：① 差分隐私与 RLHF 的结合（PrivMedChat）解决了患者数据隐私问题；② 安全对齐的脆弱性被揭示（Black-Box Behavioral Distillation），这对临床部署提出了严峻挑战。

### D. Protein Language Models（15篇）

**关键论文：**
- 🔥🔥 **Integrating PLM and Automatic Biofoundry** (6/25) — PLM + 自动化生物铸造厂的工程闭环
- 🔥🔥 **Biophysics-based PLM for Protein Engineering** (6/25) — 物理信息的蛋白质语言模型
- 🔥🔥 **ProtFlow: Fast Protein Sequence Design via Flow Matching** (6/23) — 流匹配加速蛋白质序列设计
- 🔥🔥 **Protein Representation Learning with H-Bond Graphs** (6/22) — 基于氢键图的蛋白质表征学习
- 🔥🔥 **Structure-Aware Antibody Design with Inverse Folding** (6/22) — 结构感知的抗体设计

**本周趋势：** PLM 本周论文数量显著增长（15篇），且质量极高。最突出的趋势是 PLM 从预测工具向工程闭环演进——Nature Communications 上的 biofoundry 集成论文和 Nature Methods 上的物理信息 PLM 共同指向「语言模型预测 → 自动化实验验证 → 反馈优化」的闭环系统。

### E. Genomic Foundation Models（9篇）

**关键论文：**
- 🔥🔥 **How Post-Training Shapes Biological Reasoning Models** (6/24) — 后训练对生物推理的关键影响
- 🔥🔥 **Benchmarking DNA Foundation Models** (6/25) — DNA FM 的系统性基准测试
- 🔥🔥 **A Foundation Model of Transcription Across Human Cell Types** (6/25) — 跨细胞类型的转录基础模型（Nature）
- 🔥🔥 **scPRINT: Pre-training on 50M Cells** (6/25) — 5000万细胞预训练的单细胞基础模型
- 🔥🔥 **Gengram: Retrieval-Augmented Genomic FM** (6/24) — RAG 引入基因组基础模型

**本周趋势：** 基因组 FM 进入标准化基准测试时代（Benchmarking DNA FM），同时 Nature 上发表了跨细胞类型的转录基础模型，标志着该领域从实验室走向大规模临床应用。Gengram 将 RAG 引入基因组 FM，可能催生「检索增强组学」新范式。

### F. Multimodal Clinical Agent（16篇）

**关键论文：**
- 🔥🔥 **VitalAgent: Tool-Augmented Physiological Monitoring** (6/22) — 可穿戴设备的 Agent 增强监测
- 🔥🔥 **MedRLM: Recursive Multimodal Health Intelligence** (6/24) — 递归多模态临床推理
- 🔥🔥 **CT-Agent: Multimodal-LLM for 3D CT QA** (6/24) — 首个 3D CT 影像的多模态 LLM Agent
- 🔥🔥 **XMedFusion: Knowledge-Guided Multimodal Perception** (6/22) — 知识引导的多模态融合
- 🔥🔥 **ArogyaSutra: Multi-Agent for Indic Languages** (6/22) — 多语言多模态临床推理

**本周趋势：** 多模态临床 AI 持续高位（16篇），两个重要方向：① 从通用型向专科化发展（眼科 VLM、CT-Agent、ICU EEG）；② 从被动诊断向主动监测转变（VitalAgent 的 reactive + proactive 监测）。

### X. 跨界发现（17篇）

**关键论文：**
- 🔥🔥 **SpatialAgent: Autonomous AI for Spatial Biology** (6/23) — 自主空间生物学 AI Agent（56 citations）
- 🔥🔥 **Toward Vibe Medicine: Self-Evolving Multi-Agent** (6/22) — 自进化多智能体临床决策
- 🔥🔥 **Towards World Models in Biomedical Research** (6/24) — 世界模型引入生物医学
- 🔥🔥 **BioChemAIgent: AI-driven Protein Modeling** (6/25) — AI 智能体驱动的蛋白质建模
- 🔥🔥 **SMDD-Bench: LLMs for Drug Design** (6/22) — LLM 在真实药物设计任务上的基准测试

---

## 🧠 前沿洞察与头脑风暴

### 本周三大核心信号

**1. Clinical Agent 的「基础设施化」**
本周 B 方向最显著的趋势是 Clinical Agent 正在从「模型能力竞赛」转向「基础设施建设」。MedBeads 提出的不可变数据底座、HoT-SSM 的 Temporal KG 推理、以及 RSA-KG 的图增强 RAG，共同描绘了一个清晰的图景：下一代临床 AI 的核心竞争力不在模型大小，而在知识组织和数据治理的基础设施质量。这与我们 renji_mngs 项目中 BGE-M3 + FAISS RAG 的架构方向高度一致。

**2. PLM 从「预测工具」到「工程引擎」的范式跃迁**
D 方向本周最令人兴奋的进展是 PLM 正在从单纯的序列预测工具演变为蛋白质工程的核心引擎。Nature Communications 的 biofoundry 集成论文展示了「PLM 预测 → 自动化实验验证 → 反馈优化」的完整闭环，而 Nature Methods 的物理信息 PLM 则将生物物理原理融入模型架构。这两条路线可能在未来 1-2 年内融合，催生真正的「AI 驱动蛋白质工厂」。

**3. 多模态临床 AI 的「专科化分裂」**
F 方向的 16 篇论文显示，多模态临床 AI 正在经历一场「专科化分裂」——从通用医学 VLM 分裂为眼科、放射科、ICU、病理等专科模型。这种分裂既是挑战（每个专科需要独立的数据和评估），也是机遇（专科模型在特定任务上超越通用模型）。对于我们 mNGS + LLM 的工作，这意味着可能需要开发专门针对「感染病原体」的多模态模型，而非依赖通用医学 VLM。

### 搜索空白与机会

| 空白区域 | 机会评估 | 建议搜索策略 |
|----------|---------|-------------|
| mNGS + LLM 直接结合 | ⭐⭐⭐ 极高 | "metagenomic" AND ("large language model" OR "foundation model") |
| 联邦 RLHF 医学对齐 | ⭐⭐ 中 | "federated RLHF medical" OR "differential privacy medical alignment" |
| 蛋白质 Agent 设计 | ⭐⭐⭐ 极高 | "AI agent protein engineering automated" |
| 多模态临床 Agent 安全验证 | ⭐⭐ 中 | "multimodal clinical agent safety verification" |

### 下周关注方向

1. **mNGS + LLM 交叉**：本周 mNGS 综述论文梳理了当前流水线，但 mNGS 数据直接输入 LLM 的工作仍稀缺，这是我们的核心机会窗口
2. **Clinical Agent 基础设施**：关注 MedBeads 等数据底座方案的实际实现和开源进展
3. **PLM + 自动化实验**：跟踪 biofoundry 集成论文的后续实验验证结果

---

*报告生成时间: 2026-06-25*
*数据来源: 每日论文日报 (6/22-6/25)*
*去重跟踪: .seen_papers.json (508+ papers tracked)*
