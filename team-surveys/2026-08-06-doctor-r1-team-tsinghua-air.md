# Doctor-R1 团队成果全景调研

> 📅 2026-08-06 | 🔍 基于 arXiv API + HTML 作者信息挖掘 | 📊 9 篇论文

---

## 🏛️ 团队信息

| 角色 | 姓名 | 单位 | 联系方式 |
|------|------|------|----------|
| **通讯作者/PI** | Weizhi Ma（马为之） | 清华大学计算机系 + AI研究院 | mawz@tsinghua.edu.cn |
| **通讯作者/PI** | Yang Liu（刘洋） | 清华大学AI学院 + 产业研究院(AIR) | liuyang2011@tsinghua.edu.cn |
| **核心一作** | Yunghwei Lai（赖云辉） | 清华大学 | — |
| **合作者** | Ziyue Wang, Kaiming Liu, Junkai Li, Peng Li 等 | 清华大学 | — |

**单位：** 清华大学计算机科学与技术系 / 人工智能研究院 / 产业研究院（AIR）

---

## 📚 完整论文列表

### 1. Agent Hospital（2024.05）⭐ 里程碑

**arXiv: 2405.02957 | ICLR 2025**

> *"A Simulacrum of Hospital with Evolvable Medical Agents"*

**核心思想：** 构建虚拟医院环境，所有患者、护士、医生都是 LLM 驱动的自主 Agent。医生 Agent 通过治疗大量虚拟患者来**自我进化**，无需人工标注。

**关键结果：**
- 治疗数万名虚拟患者后，进化后的医生 Agent 在 MedQA（USMLE）上超越 SOTA
- 从零构建完整的医疗模拟生态系统

**技术栈：** LLM Agent + 环境模拟 + 经验回放 + 自我进化

**对 renji_mngs 的价值：** Agent 模拟 + 进化训练范式可直接用于 triage agent 的能力提升

---

### 2. ToMBench（2024.02）

**arXiv: 2402.15052 | ACL 2024**

> *"Benchmarking Theory of Mind in Large Language Models"*

**核心思想：** 系统评估 LLM 的"心智理论"（ToM）——感知和推断他人心理状态的能力。

**关键创新：**
- 8 项任务、31 项社会认知能力
- 从零构建双语数据集，严格避免数据泄漏

**发现：** GPT-4 仍落后人类 10+ 个百分点

**对 doctor UI 的价值：** ToM 是临床对话 Agent 理解患者心理状态的基础

---

### 3. Patient-Zero（2025.09）⭐ 重要

**arXiv: 2509.11078**

> *"Scaling Synthetic Patient Agents to Real-World Distributions without Real Patient Data"*

**核心思想：** 从零开始生成合成患者数据，不需要任何真实医疗记录。

**关键创新：**
- **Medically-Aligned Hierarchical Synthesis：** 从抽象临床指南生成全面的患者记录（分层属性排列组合）
- **Dual-Track Cognitive Memory System：** 双轨认知记忆，解决"稳定性-可塑性困境"——Agent 在动态交互中保持临床一致性和人格一致性

**关键结果：**
- 人类专家评估认为合成数据与真实数据**不可区分**
- 下游模型 MedQA +24.0%，MMLU +14.5%

**对 doctor UI RLHF 的价值：** 直接解决医疗 RLHF 的数据稀缺和隐私问题

---

### 4. MAQuE（2025.09）

**arXiv: 2509.24958**

> *"The Dialogue That Heals: A Comprehensive Evaluation of Doctor Agents' Inquiry Capability"*

**核心思想：** 目前最大的医疗多轮问诊评估基准。

**关键创新：**
- **3,000 个逼真的模拟患者 Agent：** 多样化的语言模式、认知局限、情绪反应、被动信息披露倾向
- **五维评估框架：** 任务成功率、问诊能力、对话能力、问诊效率、患者体验

**发现：**
- 即使是最先进的模型在问诊能力上仍有很大提升空间
- 模型对真实患者行为变化高度敏感
- 不同评估维度之间存在 trade-off

**对 doctor UI 的价值：** 最合适的医生问诊能力评估基准之一

---

### 5. Doctor-R1（2025.10）⭐ 核心论文

**arXiv: 2510.04284 | ICLR 2026**

> *"Mastering Clinical Inquiry with Experiential Agentic Reinforcement Learning"*

**核心思想：** 训练 LLM 同时掌握临床决策和战略性共情问诊。

**三大组件：**
1. **多 Agent 交互环境：** 模拟真实门诊场景
2. **双层奖励架构：** 分别优化临床决策能力 + 沟通问诊能力
3. **经验仓库：** 基于高质量先前轨迹的策略学习

**关键结果：**
- 超越 SOTA 开源医疗 LLM
- 超越强力闭源模型
- 人类专家评估显示 superior 的临床能力和患者中心表现

**对 doctor UI RLHF 的价值：** 直接对标的项目，双层奖励架构可复用

---

### 6. Beyond Words（2026.02）

**arXiv: 2602.13832**

> *"Evaluating and Bridging Epistemic Divergence in User-Agent Interaction via Theory of Mind"*

**核心思想：** 评估和弥合用户与 Agent 之间的认知分歧，利用心智理论。

**对临床 AI 的价值：** 医生和患者（或用户和 AI）之间的理解鸿沟是临床部署的关键挑战

---

### 7. Beyond "I Don't Know"（2026.04）

**arXiv: 2604.17293**

> *"Evaluating LLM Self-Awareness in Discriminating Data and Model Uncertainty"*

**核心思想：** 评估 LLM 区分"数据不确定性"（aleatoric）和"模型不确定性"（epistemic）的能力。

**对临床 AI 的价值：** 临床 AI 必须知道自己"不知道什么"——这是安全部署的基础

---

### 8. MUCAR（2025.06）

**arXiv: 2506.17046**

> *"Benchmarking Multilingual Cross-Modal Ambiguity Resolution for Multimodal Large Language Models"*

**核心思想：** 多语言多模态歧义消解基准。

**对临床 AI 的价值：** 跨语言临床 AI 的参考

---

### 9. TheraAgent（2026.05）⭐ 最新

**arXiv: 2605.05963 | ACL 2026**

> *"Self-Improving Therapeutic Agent for Precise and Comprehensive Treatment Planning"*

**核心思想：** 用**迭代生成-判断-修正**流水线取代一次性生成，模拟人类专家的治疗方案制定过程。

**关键创新：**
- **TheraJudge：** 治疗方案专用的评估模块，在推理循环中执行临床标准
- 从粗糙不完整的草稿逐步转化为精确、全面、安全的治疗方案

**关键结果：**
- HealthBench SOTA
- 专家评估 **86% 胜率 vs 人类医生**
- TheraJudge 与 HealthBench 高度一致

**对 renji_mngs 的价值：** triage → treatment pipeline 可直接借鉴迭代修正范式

---

## 🧠 团队研究脉络

```
2024 ────────────────────────────────────────────────────────────── 2026
  │                                                                 │
  ├─ Agent Hospital (ICLR'25)                                      │
  │   虚拟医院环境 + Agent自我进化                                   │
  │                                                                 │
  ├─ ToMBench (ACL'24)                                             │
  │   LLM心智理论评估                                                │
  │                                                                 │
  │   ├─ Patient-Zero (2025.09)                                    │
  │   │   零数据合成患者                                              │
  │   │                                                             │
  │   ├─ MAQuE (2025.09)                                           │
  │   │   医生问诊能力评估基准                                        │
  │   │                                                             │
  │   ├─ Doctor-R1 (ICLR'26)                                       │
  │   │   RL训练临床问诊+决策                                        │
  │   │                                                             │
  │   ├─ Beyond Words (2026.02)                                    │
  │   │   用户-Agent认知对齐                                         │
  │   │                                                             │
  │   ├─ Beyond "I Don't Know" (2026.04)                           │
  │   │   LLM不确定性感知                                            │
  │   │                                                             │
  │   └─ TheraAgent (ACL'26) ⭐                                    │
  │       治疗规划Agent（迭代修正）                                   │
  └─────────────────────────────────────────────────────────────────┘
```

**研究脉络：** 模拟环境 → 患者生成 → 评估基准 → RL训练 → 不确定性感知 → 治疗规划

---

## 💡 对你项目的核心价值

| 你的项目 | 可参考成果 | 具体价值 |
|---------|-----------|---------|
| **Doctor UI RLHF** | Doctor-R1 + Patient-Zero + MAQuE | 双层奖励架构 + 合成患者数据 + 评估基准 |
| **renji_mngs triage** | TheraAgent + Agent Hospital | 迭代修正范式 + Agent 进化训练 |
| **多模态临床 Agent** | Beyond Words + Beyond "I Don't Know" | 心智理论 + 不确定性感知 |

---

## 📊 决策建议

1. **最值得精读的非 Doctor-R1 论文：** TheraAgent（2605.05963）——最新、ACL 2026、直接对 treatment pipeline 有价值
2. **最值得复用的方法：** Patient-Zero 的双轨认知记忆系统——解决合成患者数据的一致性问题
3. **最值得关注的评估工具：** MAQuE——评估 doctor UI 的问诊能力
4. **团队后续动态：** 产出非常密集（2024-2026 已 9 篇），建议定期监控

---

## 📎 论文链接汇总

| # | 论文 | arXiv | 会议 |
|---|------|-------|------|
| 1 | Agent Hospital | [2405.02957](https://arxiv.org/abs/2405.02957) | ICLR 2025 |
| 2 | ToMBench | [2402.15052](https://arxiv.org/abs/2402.15052) | ACL 2024 |
| 3 | Patient-Zero | [2509.11078](https://arxiv.org/abs/2509.11078) | — |
| 4 | MAQuE | [2509.24958](https://arxiv.org/abs/2509.24958) | — |
| 5 | Doctor-R1 | [2510.04284](https://arxiv.org/abs/2510.04284) | ICLR 2026 |
| 6 | Beyond Words | [2602.13832](https://arxiv.org/abs/2602.13832) | — |
| 7 | Beyond "I Don't Know" | [2604.17293](https://arxiv.org/abs/2604.17293) | — |
| 8 | MUCAR | [2506.17046](https://arxiv.org/abs/2506.17046) | — |
| 9 | TheraAgent | [2605.05963](https://arxiv.org/abs/2605.05963) | ACL 2026 |

---

*调研时间: 2026-08-06 | 🔍 基于 arXiv API + HTML 元数据 | 📋 已导入 Zotero*
