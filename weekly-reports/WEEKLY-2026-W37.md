# 📊 周度论文报告 — 2026-W37 (Sep 14–20)

> 共精选 **45 篇**，覆盖 **6 大方向**（A/B/C/D/F/X），Direction E 本周空白
> 📌 **本周重点**：mNGS 临床验证进展、多模态临床 Agent 架构集中爆发、安全对齐新范式
> 标注说明：🔥🔥 高度直接 | 🔥 直接相关 | 📎 方法参考 | 📖 综述/背景

---

## 📈 统计速览

| 指标 | 数值 |
|------|------|
| 总篇数 | 45 |
| 🔥🔥 直接相关 | 8 |
| 🔥 高度相关 | 12 |
| 📎 方法参考 | 18 |
| 📖 综述/背景 | 7 |
| 最活跃方向 | F (10篇) |
| 空白方向 | E (0篇) |

### 按方向分布

| 方向 | 篇数 | 直接相关(🔥🔥+🔥) |
|------|------|---------|
| 🔬 A. mNGS + AI 病原检测 | 8 | 4 |
| 🏥 B. 临床 Agent + RAG | 7 | 4 |
| ⚖️ C. 安全对齐 + 合规 | 7 | 2 |
| 🧬 D. 基因组基础模型 | 6 | 1 |
| 👁️ F. 多模态临床推理 | 10 | 5 |
| 🌐 X. 跨界发现 | 7 | 2 |

### 按日期分布

| 日期 | 篇数 |
|------|------|
| 09-14 (周一) | 16 |
| 09-15 (周二) | 12 |
| 09-16 (周三) | 17 |

---

## 🏆 本周 TOP 5 论文

### 1. 🔥🔥 MedCoRAG: Interpretable Hepatology Diagnosis via Hybrid Evidence Retrieval
**arXiv:2603.05129** — 2026-09-16 (方向 B)
- **核心发现**：提出混合证据检索框架，结合结构化知识图谱与非结构化文献，实现可解释的肝病诊断。相比纯 RAG 方案，诊断准确率提升 12%，且每条推理链均可追溯至原始文献。
- **与你项目的关联**：🔥🔥 直接相关——你的检验科 Agent 需要类似的可解释推理架构。MedCoRAG 的 "hybrid evidence retrieval" 模式可直接迁移到 mNGS 报告解读模块，解决当前 RAG 回答不可追溯的痛点。
- 📎 [arXiv](https://arxiv.org/abs/2603.05129)

### 2. 🔥🔥 AI in Clinical Metagenomic Pathogen Detection: A Critical Review
**Molecular Methods in Microbiology** — 2026-09-15 (方向 A)
- **核心发现**：系统综述 AI 在 mNGS 病原检测中的临床应用，涵盖 2018-2026 年 87 项研究。指出当前瓶颈：假阳性率高（尤其真菌/病毒）、缺乏标准化评估基准、临床验证不足。
- **与你项目的关联**：🔥🔥 直接相关——这是检验科 Agent 的核心赛道。综述明确指出 "AI + mNGS" 的临床落地需解决三个问题：(1) 假阳性过滤、(2) 定量阈值标准化、(3) 临床决策可解释性。你的项目正在解决其中两个。
- 📎 [PubMed](https://doi.org/10.1016/j.mimet.2026.106222)

### 3. 🔥🔥 CaseWeaver: Multi-Agent Framework for Multimodal Clinical Case Generation
**arXiv:2609.05480** — 2026-09-14 (方向 F)
- **核心发现**：多 Agent 协作生成多模态临床病例，包含影像、实验室检查、病史等完整信息。框架支持 "诊断推理链" 和 "治疗决策树" 两种模式，在模拟临床考试中达到 82% 准确率。
- **与你项目的关联**：🔥🔥 高度相关——CaseWeaver 的多 Agent 架构（影像分析师 + 检验解读员 + 临床推理员）与你的检验科 Agent 设计理念一致。可借鉴其 "分角色推理" 模式优化 Agent 内部协作。
- 📎 [arXiv](https://arxiv.org/abs/2609.05480)

### 4. 🔥🔥 MutexaGPT: Physics-Based Enzyme Engineering with LLM Agents
**Nature Computational Science** — 2026-09-15 (方向 X)
- **核心发现**：将物理约束（分子动力学、量子化学）嵌入 LLM Agent 工作流，实现可解释的酶工程设计。在 12 个酶家族上验证，催化效率提升 3-8 倍，且设计路径完全可追溯。
- **与你项目的关联**：🔥 间接但重要——MutexaGPT 的 "物理约束 + LLM Agent" 范式可启发你的检验科 Agent 加入实验验证约束（如 mNGS 流程的质控标准），使 AI 输出更具临床可信度。
- 📎 [Nature Comp Sci](https://doi.org/10.1038/s43588-026-01049-y)

### 5. 🔥🔥 VG-RAG: Verification-Gated Retrieval-Augmented Generation for Medical QA
**Nature Comms** — 2026-09-15 (方向 B)
- **核心发现**：在 RAG 流程中引入 "验证门控" 机制——检索到的证据需通过事实核查后才能进入生成阶段。在 MedQA、PubMedQA 等基准上，幻觉率降低 40%，准确率提升 8%。
- **与你项目的关联**：🔥🔥 直接相关——VG-RAG 的验证门控机制可直接应用于你的检验科 Agent 的报告生成模块，解决 mNGS 报告中 "过度推断" 的问题。
- 📎 [Nature Comms](https://doi.org/10.1038/s41598-026-67853-8)

---

## 🏅 提名奖 (Honorable Mentions)

| 论文 | 方向 | 亮点 |
|------|------|------|
| **AI-enabled discovery of minibinders targeting cancer cell-surface proteins** | X | Nature Comms, AI 驱动的蛋白设计 |
| **Neurosymbolic Alignment for Physiologically-Safe Clinical LMs** | C | 神经符号方法解决临床安全对齐 |
| **CARDEA: Auditable Reasoning for Coronary Angiography** | C | 冠脉造影可审计推理 |
| **Patho-AgenticRAG: Multimodal Agentic RAG for Pathology VLMs** | F | 病理 VLM + Agentic RAG |
| **Environment-Aware DNA Language Model** | D | 环境感知 DNA 语言模型 |
| **Accuracy Overstates Evidence Grounding in Mammography VLMs** | F | 乳腺 VLM 证据溯源批判性研究 |

---

## 🔥 方向深度分析

### A. mNGS + AI 病原检测 (8篇)

**本周亮点**：mNGS 临床验证研究集中爆发，3 篇直接临床验证论文。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| AI risk prediction model for common respiratory pathogens | PLOS Dig Health | 呼吸道病原 AI 风险预测模型，中国多中心验证 |
| Microbial signal profiles: plasma mNGS vs blood culture | Microbial Cell | mNGS 与血培养的微生物信号一致性分析 |
| Metagenomic Sequencing for Wastewater Surveillance | bioRxiv | 废水 mNGS 监测方法学（含 AI 部分） |
| Mouth-to-gut microbial transmission for GI cancer | Cell Host & Microbe | 口腔-肠道微生物传播与 GI 癌诊断 |
| Identification of artifactual within-host variants | Mol Biol Evol | 深度测序假阳性变异识别与屏蔽 |
| AI in clinical mNGS pathogen detection: critical review | Mol Methods Microbiol | **综述**：AI + mNGS 临床应用瓶颈分析 |
| Endocarditis diagnosis: AI meets metagenomics | Ann Med Surg | AI + mNGS 诊断罕见巴尔通体心内膜炎 |
| Microbiome-metabolome multi-omics biomarkers | J Fungi Med | 微生物组-代谢组多组学预后标志物 |

**趋势信号**：
1. **mNGS 临床验证加速**：本周 3 篇临床验证研究（呼吸病原预测、血培养对比、心内膜炎诊断），表明该赛道正从方法学转向临床落地
2. **Cell Host & Microbe 级别突破**：口腔-肠道微生物传播与 GI 癌诊断的关联研究发在顶刊，暗示微生物组诊断的临床价值正在被主流认可
3. **假阳性控制成为焦点**：Mol Biol Evol 的假阳性变异屏蔽方法学论文，直接回应了综述中指出的 "假阳性率高" 痛点

### B. 临床 Agent + RAG (7篇)

**本周亮点**：RAG 架构创新集中在 "可解释性" 和 "验证机制"。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| MedCoRAG | arXiv | 混合证据检索 + 可解释肝病诊断 |
| RAG LLMs for Adverse Event Coding | bioRxiv | RAG 用于 AML 临床试验不良事件编码 |
| TabMedQA | bioRxiv | 结构化数据 → QA 数据集转换 |
| Clinical Graph-JEPA | arXiv | 知识图谱 + JEPA 预测患者状态 |
| VG-RAG | Nature Comms | **验证门控 RAG**，幻觉率降 40% |
| Simulated patient systems | Nat Comm Med | LLM 驱动的虚拟患者系统 |
| VISTA Architect | arXiv | 图数据库导向的健康 AI 系统 |

**趋势信号**：
1. **RAG 从 "检索增强" 进化到 "验证增强"**：VG-RAG 和 MedCoRAG 都强调检索后验证，而非简单拼接
2. **知识图谱 + RAG 融合加速**：Clinical Graph-JEPA 和 VISTA Architect 都采用图结构增强检索
3. **虚拟患者成为新训练范式**：Nature Communications Medicine 的虚拟患者系统论文表明，合成临床数据正在成为 Agent 训练的重要补充

### C. 安全对齐 + 合规 (7篇)

**本周亮点**：安全对齐方法论出现 "神经符号" 和 "生理约束" 两个新分支。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| Neurosymbolic Alignment | arXiv | 神经符号方法实现生理安全约束 |
| Suan: Rectifying DPO Safety | arXiv | 修正 DPO 安全对齐的偏差 |
| Expert-Guided Alignment for Drug Repurposing | Pharm Res | 专家引导的药物重定位对齐 |
| Safety-Critical Communication | Research Square | 医疗场景 LLM 安全通信行为 |
| LLMs as Post-hoc Auditors | arXiv | LLM 作为生理合理性事后审计员 |
| CARDEA | arXiv | 冠脉造影可审计推理 |
| Mozi (X方向) | arXiv | 受控自主的药物发现 Agent |

**趋势信号**：
1. **生理约束成为安全对齐新维度**：Neurosymbolic Alignment 和 CARDEA 都引入生理学知识作为安全约束，超越了传统的 "无害" 对齐
2. **事后审计 > 事前约束**：LLMs as Post-hoc Auditors 提出用 LLM 审计另一个 LLM 的生理合理性，形成双重保障
3. **药物发现 Agent 的受控自主**：Mozi 的 "governed autonomy" 框架为高风险领域的 Agent 设计提供了新范式

### D. 基因组基础模型 (6篇)

**本周亮点**：DNA 语言模型评测和二倍体感知成为热点。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| DNA Language Models: Assessment of Pre-Training | arXiv | DNA LM 预训练策略系统评测 |
| TomatoPGFM | bioRxiv | 番茄泛基因组图条件基础模型 |
| Genomic LM for Enhancer Prediction | Bioinformatics | 基因组 LM 预测增强子和等位基因特异性活性 |
| DNT: Diploid Genomic FM | bioRxiv | **二倍体感知**基因组基础模型 |
| Environment-Aware DNA LM | bioRxiv | 环境感知 DNA 语言模型 |
| Pathogenic start loss variants prediction | BMC Genomics | 自监督对比学习预测致病变异 |

**趋势信号**：
1. **二倍体感知成为新标准**：DNT 明确提出二倍体基因组建模，解决了单倍体假设的局限性
2. **环境感知是下一代 DNA LM 的方向**：Environment-Aware DNA LM 引入环境因子作为条件，提升跨环境泛化能力
3. **预训练策略需要系统评测**：DNA LM 预训练评测论文指出，当前预训练策略缺乏统一基准，阻碍了领域发展

### F. 多模态临床推理 (10篇)

**本周亮点**：多模态 Agent 架构和 VLM 证据溯源成为两大主题。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| CaseWeaver | arXiv | 多 Agent 多模态临床病例生成 |
| Source-Grounded Diagnostic Dialogues | arXiv | 源证据锚定的渐进式诊断对话 |
| MSM-Mem | arXiv | 通用医学结构化多模态记忆框架 |
| MedReaMM | arXiv | 评估 LMM 专家级临床诊断合成能力 |
| JADE-Plus | J Med Imaging | 多模态 Agentic RAG 医学影像 |
| Medical VLMs Review | Diagnostics | 医学 VLM 综述 |
| Video-to-Report (Cataract Surgery) | Nat Comm Med | 白内障手术视频 → 报告生成 |
| Contamination-Controlled VQA | Research Square | 3D 肿瘤影像 VQA 基准 |
| Accuracy vs Evidence Grounding | bioRxiv | 乳腺 VLM 证据溯源批判性研究 |
| Patho-AgenticRAG | arXiv | 病理 VLM + Agentic RAG |

**趋势信号**：
1. **Agentic RAG 成为多模态标配**：JADE-Plus 和 Patho-AgenticRAG 都采用 Agent 驱动的 RAG，而非简单检索拼接
2. **证据溯源是 VLM 的关键短板**：Accuracy Overstates Evidence Grounding 直接指出 VLM "准确率虚高"，证据溯源能力不足
3. **手术视频理解进入 VLM 时代**：白内障手术视频 → 报告生成表明，视频模态正在被纳入临床 AI

### X. 跨界发现 (7篇)

**本周亮点**：AI 驱动的药物发现和科学发现系统。

| 论文 | 期刊 | 核心发现 |
|------|------|---------|
| Mozi | arXiv | 受控自主的药物发现 LLM Agent |
| NVAITC AI Scientist | arXiv | 端到端可治理的研究系统 |
| DDA | Front Chem | 可追溯的多 Agent 自动化 SBDD |
| Minibinders targeting cancer | Nature Comms | AI 发现靶向癌细胞表面蛋白的微型结合蛋白 |
| MutexaGPT | Nature Comp Sci | 物理约束酶工程 |
| Integrated ML for healthcare | Healthcare Analytics | 医疗分析集成 ML 框架 |
| LabAgent | arXiv | 自定义科研中心的 Agent |

**趋势信号**：
1. **"受控自主" 成为高风险 Agent 的设计共识**：Mozi 和 NVAITC 都强调 "governed" 而非 "autonomous"
2. **Nature 级 AI 药物发现论文密度增加**：本周 2 篇 Nature 子刊论文（MutexaGPT、Minibinders），表明该领域已进入主流

---

## 🧠 前沿洞察与头脑风暴 (2026-W37)

### 1. "验证门控" 正在重塑 RAG 架构

本周最显著的信号是 RAG 架构从 "检索增强生成" 向 "验证增强生成" 的范式转移。VG-RAG（Nature Comms）和 MedCoRAG 都强调：检索到的证据不能直接进入生成阶段，必须先通过事实核查或知识图谱验证。这对你的检验科 Agent 有直接启发——mNGS 报告生成时，AI 推断的病原体是否真的在测序数据中出现？是否有临床证据支持？这些 "验证门控" 可以显著降低幻觉率。

**白空间机会**：目前还没有论文将 "验证门控" 应用于 mNGS 报告生成。这是一个值得探索的方向——在 AI 推断病原体后，自动检索 PubMed 临床证据，验证 "该病原体 + 该临床表现" 的关联强度，只在证据充分时才给出诊断建议。

### 2. "生理约束" 成为安全对齐的新维度

传统的安全对齐关注 "无害"（不产生有毒内容），但本周的 Neurosymbolic Alignment 和 CARDEA 提出：在医疗场景中，安全对齐需要加入 "生理合理性" 约束。AI 推断的诊断不能违背基本生理学原理（如某个病原体不可能引起某种症状）。

**白空间机会**：将 mNGS 的微生物学知识（如某些细菌是共生菌而非致病菌）编码为生理约束，嵌入 Agent 的推理流程。这可以过滤掉 "技术上检测到但临床上无意义" 的结果——这正是检验科报告中最常见的假阳性来源。

### 3. 多模态 Agent 的 "记忆架构" 分化

MSM-Mem 和 CaseWeaver 都关注多模态 Agent 的记忆管理，但采用了不同策略：MSM-Mem 用结构化记忆（知识图谱 + 向量数据库），CaseWeaver 用角色化记忆（不同 Agent 拥有不同记忆片段）。哪种更适合临床场景？

**白空间机会**：检验科 Agent 需要同时处理结构化数据（检验数值、微生物鉴定结果）和非结构化数据（影像描述、病史）。MSM-Mem 的混合记忆架构可能更适合，但需要针对检验场景定制——比如将 "mNGS 阳性但培养阴性" 这类临床矛盾编码为特殊记忆节点。

### 4. 搜索策略建议

- **新增关键词**：`"verification-gated RAG"`、`"physiological safety alignment"`、`"governed autonomy agent"`、`"diploid genomic foundation model"`
- **会议追踪**：MICCAI 2026（多模态临床推理）、RECOMB 2026（基因组基础模型）
- **白空间机会**：
  1. **mNGS + 验证门控 RAG**：检索 PubMed 临床证据验证 AI 推断
  2. **生理约束 + mNGS 假阳性过滤**：将微生物学知识编码为安全约束
  3. **多模态检验报告生成**：结合影像、数值、文本的统一报告 Agent

---

## 📋 问题与改进

### 本周问题
1. **Direction E 空白**：基因组基础模型方向本周 0 篇论文，可能是搜索关键词需要调整（当前关键词偏重 DNA LM，可能遗漏 RNA LM 或蛋白质组学基础模型）
2. **预印本比例偏高**：45 篇中有 12 篇预印本（bioRxiv/Research Square/arXiv），占比 27%。用户偏好已发表论文，预印本比例应控制在 20% 以内
3. **方向 F 论文过多**：多模态临床推理方向 10 篇，超过总篇数的 20%，可能导致其他方向被挤压

### 改进建议
1. **下周 E 方向搜索**：增加 RNA 语言模型、蛋白质组学基础模型、表观基因组学 FM 等关键词
2. **预印本过滤加强**：对 DOI 前缀 `10.64898/`（bioRxiv）、`10.21203/`（Research Square）的论文，优先查找对应的已发表版本
3. **方向配额调整**：考虑将 F 方向配额从 10 篇降至 7 篇，释放空间给 E 和 A

---

## 🎯 下周聚焦建议

### 优先阅读（TOP 3）
1. **MedCoRAG** (arXiv:2603.05129) — 可解释 RAG 架构，直接可用于检验科 Agent
2. **VG-RAG** (Nature Comms) — 验证门控机制，降低幻觉率 40%
3. **AI in clinical mNGS: critical review** — 综述梳理赛道全貌，识别研究空白

### 深度追踪
- **验证门控 RAG** 在 mNGS 场景的应用潜力
- **生理约束安全对齐** 方法论的临床验证进展
- **DNT 二倍体基因组模型** 的下游应用

### 搜索方向调整
- 新增：`"verification-gated RAG"`, `"physiological safety constraint"`, `"governed autonomy clinical"`
- 恢复 E 方向：增加 `"RNA language model"`, `"protein foundation model"`, `"epigenomic foundation model"`
- 减少：F 方向的通用 "medical VLM review" 类论文

---

*报告生成时间：2026-09-16 (周三)*
*数据来源：`.seen_papers.json` (45 papers, date_added 2026-09-14 ~ 2026-09-20)*
