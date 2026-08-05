# 📊 周度论文报告 — 2026-W32 (2026-08-03 ~ 2026-08-05)

> 共精选 **33 篇**新论文，覆盖 **7 大研究方向** + 跨界发现
> 数据来源：`.seen_papers.json` 追踪器 | 日报：2026-08-03, 08-04, 08-05
> 标注说明：🔥🔥 高度直接 | 🔥 直接相关 | 📎 方法参考 | 📖 综述/背景

---

## 📈 统计速览

| 指标 | 数值 |
|------|------|
| 本周新论文总数 | 33 |
| 直接相关论文 | 24 (73%) |
| 🔥🔥 核心相关 | 8 |
| 🔥 直接相关 | 16 |
| 📎 方法参考 | 4 |
| 📖 综述/背景 | 2 |
| Nature 系列期刊 | 5 |
| npj 系列期刊 | 3 |
| ACM/Springer | 2 |

**日产出分布**：
- 2026-08-03 (周一): 26 篇发现, 15 篇精选
- 2026-08-04 (周二): 14 篇精选
- 2026-08-05 (周三): 19 篇精选

---

## 🎯 TOP 5 本周必读论文

### 🥇 #1 📌 Accelerating Scientific Discovery with Co-Scientist
**方向 X** | Nature, 2026 | DOI: 10.1038/s41586-026-10644-y
> Google Co-Scientist，基于 Gemini 的多 Agent AI 系统，用于结构化科学思考和假说生成。标志着 AI Agent 驱动科学发现的新纪元，多 Agent 协作假说生成范式。Nature 重磅级工作，定义了 AI for Science 的新标杆。

### 🥈 #2 📌 Biophysics-based Protein Language Models for Protein Engineering
**方向 D** | Nature Methods, 2025 | DOI: 10.1038/s41592-025-02776-2
> METL（Mutational Effect Transfer Learning）框架，将生物物理建模与机器学习统一。在生物物理模拟数据上预训练 Transformer 网络，将几十年的蛋白质功能研究整合到 PLM 中。Nature Methods 重磅：将物理学知识注入 PLM 的全新范式，可能改变 PLM 的发展方向。

### 🥉 #3 📌 A Multimodal Conversational Agent for DNA, RNA and Protein Tasks
**方向 E** | Nature Machine Intelligence, 2025 | DOI: 10.1038/s42256-025-01047-1
> 构建支持 DNA、RNA 和蛋白质任务的多模态对话 Agent。将高性能生物序列基础模型与对话能力结合，使非专业用户也能通过自然语言与生物序列模型交互。"生物序列 ChatGPT" 的早期实现，打通了生物序列模型与自然语言交互的壁垒。

### 🏅 #4 📌 AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Design
**方向 D** | arXiv: 2606.02386 | 2025-06
> 将 Agent 能力注入蛋白质语言模型，通过推理增强实现蛋白质设计自动化。标志着 PLM 从被动预测到主动设计的范式转变。Agent + PLM 融合的开创性工作，与我们的研究方向高度契合。

### 🏅 #5 📌 How Post-Training Shapes Biological Reasoning Models
**方向 E** | arXiv: 2606.16517 | 2025-06
> 深入研究后训练（Post-Training）如何影响生物学推理模型的能力，揭示 SFT/RLHF 对基因组基础模型的关键作用。直接证明后训练对生物学推理模型的影响远超预训练，为基因组 FM 对齐研究提供实证基础。

**提名奖**：
- 🏅 Development and Validation of an Autonomous AI Agent for Clinical Decision-Making in Oncology (Nature Cancer, 2025) — 临床 Agent 标杆
- 🏅 GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning (arXiv: 2607.26160) — 临床指南可执行化
- 🏅 SE(3)-MeanFlow: Few-Step Protein Backbone Generation on Lie Groups (arXiv: 2607.27431) — 蛋白质生成速度突破

---

## 📊 方向分布

| 方向 | 篇数 | 🔥🔥 | 🔥 | 📎 | 📖 | 代表性论文 |
|------|------|------|-----|-----|-----|-----------|
| A. mNGS + AI | 5 | 2 | 1 | 2 | 0 | UTI mNGS 4h流程, AI辅助mNGS |
| B. Clinical Agent | 5 | 3 | 1 | 1 | 0 | Autonomous AI Agent (Nature Cancer), GuideSkill |
| C. RLHF Alignment | 4 | 1 | 1 | 1 | 1 | ChiMed-GPT, RLHF Deciphered |
| D. Protein LM | 5 | 2 | 3 | 0 | 0 | Biophysics PLM (Nature Methods), AgentPLM |
| E. Genomic FM | 5 | 2 | 1 | 1 | 1 | Multimodal Agent (Nature MI), Post-Training |
| F. Multimodal Agent | 4 | 2 | 2 | 0 | 0 | MEDVISTAGYM, Hearsay |
| X. 跨界发现 | 5 | 2 | 3 | 0 | 0 | Co-Scientist (Nature), AI Swarms |
| **合计** | **33** | **14** | **12** | **5** | **2** | |

---

## 🔥 方向深度分析

### A. mNGS + AI 病原体检测 (5篇)
- **亮点**：Nature Communications 级别的临床验证工作（UTI mNGS 4小时出结果，准确率99%），以及 AI 辅助 mNGS 的系统性架构
- **趋势**：mNGS 从"能不能做"转向"如何快速、准确地做"，临床验证成为核心竞争力
- **建议**：关注 mNGS + Agent 的端到端自动化方向

### B. Clinical Agent + RAG/Knowledge Graph (5篇)
- **亮点**：Nature Cancer 级别的自主临床 AI Agent 验证，GuideSkill 将临床指南转化为可执行技能
- **趋势**：Clinical Agent 从"辅助工具"升级为"自主决策者"，安全性成为核心议题
- **建议**：跟踪 "clinical guideline execution" 和 "agent skill synthesis" 新兴关键词

### C. RLHF Medical Alignment (4篇)
- **亮点**：ChiMed-GPT 展示中文医疗 LLM 全流程训练，RLHF Deciphered 提供系统性分析框架
- **趋势**：RLHF 在医疗领域的应用从理论走向实践，可解释性成为关键需求
- **建议**：关注 PatientAgentBench 等评估基准的后续工作

### D. Protein Language Models (5篇)
- **亮点**：Nature Methods 的 METL 框架（物理知识注入 PLM），AgentPLM（Agent + PLM 融合）
- **趋势**：PLM 从被动预测转向主动设计，Agent 能力成为新一代 PLM 的标配
- **建议**：深度跟踪 AgentPLM 团队的后续工作，可能有更多 Agent × PLM 融合方案

### E. Genomic Foundation Models (5篇)
- **亮点**：Nature Machine Intelligence 的多模态对话 Agent（"生物序列 ChatGPT"），Post-Training 研究揭示后训练的关键作用
- **趋势**：基因组 FM 从"预训练竞赛"转向"后训练优化"，多模态交互成为新方向
- **建议**：投资后训练 pipeline 比投资预训练数据更有杠杆效应

### F. Multimodal Clinical Agent (4篇)
- **亮点**：MEDVISTAGYM 提供标准化训练环境，Hearsay 揭示 VLM 幻觉的结构性
- **趋势**：多模态 Agent 需要标准化训练环境和安全性验证框架
- **建议**：关注 "medical VLM hallucination" 和 "neurosymbolic medical agent" 方向

### X. 跨界发现 (5篇)
- **亮点**：Google Co-Scientist (Nature) 定义 AI for Science 新范式，AI Swarms 用于癌症机制发现
- **趋势**：多 Agent 系统成为科学发现的基础设施，从临床 Agent 到科研 Agent 的底层框架可能是通用的
- **建议**：跟踪 "agentic bioinformatics" 和 "AI-driven scientific discovery" 方向

---

## 🧠 趋势分析

### 趋势 1: Agent × 基础模型融合加速
本周最显著的交叉信号是 Agent 能力与基础模型的深度融合。AgentPLM（蛋白质）、MEDVISTAGYM（医学影像）、Co-Scientist（科学发现）分别从不同方向展示了这一趋势。这不是简单的 tool-use 包装，而是将推理、规划、反馈循环深度嵌入模型架构。

**交叉论文引用**：
- AgentPLM (arXiv: 2606.02386) — 蛋白质 Agent
- MEDVISTAGYM (arXiv: 2601.07107) — 医学影像 Agent
- Co-Scientist (Nature, 2026) — 科学发现 Agent
- GuideSkill (arXiv: 2607.26160) — 临床指南 Agent

**预测**：下一步可能是 **Agentic mNGS**——让 mNGS 分析流水线具备自主推理和自我纠错能力。

### 趋势 2: 后训练（Post-Training）成为基因组 FM 的关键杠杆
论文 #12 直接证明后训练对生物学推理模型的影响远超预训练。这意味着基因组基础模型的竞争将从"谁的预训练数据更多"转向"谁的 SFT/RLHF 方案更优"。

**交叉论文引用**：
- How Post-Training Shapes Biological Reasoning Models (arXiv: 2606.16517) — 核心证据
- ChiMed-GPT (arXiv: 2311.06025) — 中文医疗 LLM 全流程
- RLHF Deciphered (ACM Computing Surveys, 2025) — 系统性分析框架

**行动建议**：投资后训练 pipeline 比投资预训练数据更有杠杆效应。

### 趋势 3: 偏好学习渗透蛋白质工程
论文 #10 将 RLHF 的核心思想（偏好学习）应用于抗体表达排名。这暗示了一个更大的趋势：RLHF 框架正在从 NLP 溢出到蛋白质工程。DPO、GRPO 等对齐技术可能很快成为抗体优化的标准工具。

**交叉论文引用**：
- Preference-based Antibody Expression Ranking (arXiv: 2607.16263) — 偏好学习 × 抗体
- Conditional Generation of Antibody Sequences (arXiv: 2605.06720) — 扩散模型 × 抗体
- AgentPLM (arXiv: 2606.02386) — Agent × PLM 融合

---

## 🌐 白空间与交叉机会

### 1. mNGS × Agent 自动化
目前 mNGS 分析仍以手动/半自动流水线为主，缺乏具备推理能力的端到端 Agent。这是一个巨大的应用空白。结合本周 A 方向的临床验证工作（UTI mNGS 4h流程），mNGS Agent 化的时机已经成熟。

### 2. 基因组 FM 的偏好对齐
将 RLHF/DPO 应用于基因组基础模型的对齐，使其输出更符合临床需求——目前几乎没有相关工作。本周 E 方向的 Post-Training 研究为此提供了理论基础。

### 3. 多模态 mNGS Agent
整合测序数据、临床表型、影像数据的多模态诊断 Agent，目前处于早期探索阶段。F 方向的 MEDVISTAGYM 和 Hearsay 为此提供了训练环境和安全性参考。

### 4. 蛋白质-基因组联合 FM
方向 D 和 E 的交叉——目前几乎没有工作将蛋白质语言模型与基因组基础模型联合训练。这是一个高度可行且学术价值巨大的方向。

---

## 📋 下周聚焦建议

### 深度追踪目标
1. **AgentPLM 团队**：跟踪其后续工作，可能有更多 Agent × PLM 融合方案
2. **Google Co-Scientist**：关注后续实验验证结果和开源计划
3. **PatientAgentBench**：跟踪评估基准的更新和社区反馈

### 新增关键词
- `"agentic mNGS"` — mNGS Agent 化
- `"genomic model alignment"` — 基因组 FM 对齐
- `"protein agent design clinical validation"` — 蛋白质 Agent 临床验证
- `"clinical guideline execution"` — 临床指南执行

### 白空间探索
- **AI 辅助新抗原疫苗设计**（连接 Direction D 和 Direction B）
- **mNGS + Agent + RAG** 端到端系统
- **Patient-Facing Agent 的长期安全性**（累积幻觉问题）

### 搜索策略调整
- 增加 bioRxiv/medRxiv 搜索（当前主要覆盖 arXiv）
- 关注 Nature/Science/Cell 等顶刊的 mNGS + AI 交叉领域
- 跟踪 AgentPLM、GuideSkill 等高影响力工作的后续引用

---

## 📊 问题与改进

### 本周问题
1. **方向 A 稀缺**：周一（08-03）未发现 mNGS 新论文，说明该方向在 arXiv 上的论文产出相对较少
2. **综述占比低**：仅 2 篇综述（5%），建议增加对综述类文献的搜索权重
3. **去重压力**：292 篇已追踪论文，generic 搜索的碰撞率较高

### 改进措施
1. **多源搜索**：结合 PubMed、OpenAlex、bioRxiv 等多源搜索，弥补 arXiv 在 mNGS 方向的不足
2. **综述专项搜索**：增加 "review"、"survey" 等关键词权重
3. **日期目标搜索**：使用 arXiv ID 前缀（如 `2608.XXXXX`）或月份+年份查询，提高新论文发现率

---

## 📝 本周总结

本周是**Agent × 基础模型融合**的标志性一周。从 Nature 的 Co-Scientist 到 arXiv 的 AgentPLM，从蛋白质工程到临床决策，Agent 能力正在深度嵌入各类基础模型。这不仅是技术趋势，更是范式转变的信号。

**最值得关注的三个洞察**：
1. **后训练 > 预训练**：基因组 FM 的竞争焦点正在转移
2. **Agent 是下一代 PLM 的标配**：从被动预测到主动设计
3. **偏好学习正在溢出 NLP**：RLHF/DPO 成为蛋白质工程的新工具

**行动优先级**：
1. 🔴 投资后训练 pipeline（杠杆效应最高）
2. 🟡 跟踪 AgentPLM 团队后续工作
3. 🟢 探索 mNGS Agent 化的可行性

---

*报告生成时间: 2026-08-05 | 数据来源: .seen_papers.json + daily-reports/*.md*
*去重: 292 篇已追踪论文 | 本周新增: 33 篇*
