# 🧬 检验科Agent全链路调研报告

> **日期**: 2026-05-27
> **系统链路**: `mNGS检出 → 责任病原体判别 → 证据链+RAG → 报表生成 → 医生RLHF反馈 → Harness自进化飞轮 → 疫情预判`

---

## 一、方向D：mNGS责任病原体判别

### 🔑 最直接对标：GPAS（Global Pathogen Analysis System）

| 维度 | 详情 |
|------|------|
| **来源** | medRxiv 2026.02, 中国团队 |
| **网址** | https://gpas.nh.ac.cn |
| **GitHub** | https://github.com/GPAS-Team |
| **核心创新** | GenoDB（去冗余基因组库）+ DLA（动态库比对算法）+ GPAS-LLM（多Agent推理） |

**三个核心模块与技术路线：**

1. **GenoDB → 数据库层优化**
   - 对NCBI RefSeq做95% ANI聚类 + 图社区检测 → 库大小缩减到原来的 ~1/10
   - 保留了更高物种覆盖度、更低未分类读数比例
   - **启示**：你们做mNGS也可以构建自己的目标病原体精选库，缩减噪声

2. **DLA算法 → 判别层核心**
   - 融合 Kraken2（高灵敏度）+ Sylph（高特异性）
   - 锚定物种可靠性score ≥ τ_anchor → 用Kraken2混淆矩阵构建混合先验 → 统计检验（Poisson/NB）过滤假阳性
   - **关键数据**：4万样本混合集，GPAS平均 0.7 FP/样本 vs Kraken2 59.1 FP/样本；CAMI II上F1=0.925
   - 基因组覆盖模式识别：从24,164个宏基因组样本建参考库 → 去除96.8%假阳性，保留91.2%真阳性

3. **GPAS-LLM → Agent推理层**（多Agent系统）
   - Planner → Researcher → Reflector 三层Agent + 病原体知识图谱
   - 输出：**人类可读、循证的临床报告**

**⚠️ GPAS跟你做的是同一个方向，但它偏重"检出准确性"，你们偏重"责任病原体判别+下游闭环"。GPAS的GenoDB+DLA可以直接借鉴作为管线前处理层。**

### 📌 其他相关

- **Frontiers 2025**：[AI-assisted mNGS pathogen identification](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2025.1634194/full) — AI辅助mNGS病原体检出综述
- **PMC 2025**：[AI-powered viral mNGS for outbreak](https://pmc.ncbi.nlm.nih.gov/articles/PMC12833367) — AI驱动的病毒mNGS快速疫情分析

---

## 二、方向B：证据链条 + 临床报表生成

### 🔑 MedGraphRAG（Oxford, ACL 2025）

| 维度 | 详情 |
|------|------|
| **来源** | 牛津大学, ACL 2025 long paper |
| **GitHub** | https://github.com/ImprintLab/Medical-Graph-RAG |
| **核心** | 基于图的RAG框架，专为医学循证回答设计 |

- 图结构链接PubMed文献、UMLS概念、临床指南
- 检索→推理→引用三重保障
- **直接可用的开源代码**，可接入你们的renji_mngs RAG管线

### 🔑 KARE（GE Healthcare + UIUC, ICLR 2025）

| 维度 | 详情 |
|------|------|
| **论文** | ICLR 2025 — Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval |
| **核心创新** | 多层次医学知识图谱 + 层级社区检测 + 动态知识检索 |
| **知识来源** | UMLS + PubMed + LLM生成洞察 |

- 层次化社区检测 → 把大图拆成有意义的亚群 → 精准检索
- 输出**解释链条**（explanatory chains）而不是黑盒答案

### 🔑 MedChain-Agent

| 维度 | 详情 |
|------|------|
| **论文** | arXiv:2412.01605 |
| **规模** | 12,163个临床病例，19个专科，156个子类别 |
| **特色** | 5阶段临床工作流：转诊→问诊→检查→诊断→治疗 |
| **关键模块** | MedCase-RAG：从历史病例中检索学习，自适应响应 |

**🔥 对你们的意义**：MedChain的工作流设计直接适配 mNGS → 证据检索 → 鉴别诊断 → 报表输出的管线。MedCase-RAG可以用作你们的"历史病例反馈学习"模块。

---

## 三、方向A：临床Agent RLHF/偏好对齐

### 🔑 Healthcare AI GYM + TT-OPD

| 维度 | 详情 |
|------|------|
| **论文** | arXiv:2605.02943 |
| **GitHub** | https://github.com/minstar/Healthcare_GYM |
| **核心发现** | 医学Agent做多轮RL训练时存在三大病理：回答爆炸、多轮坍塌、蒸馏不稳定 |

**关键发现：**
- 标准GRPO在医学多轮场景下会**退化**——模型学会"写得更长"而非"用工具"
- TT-OPD（Turn-Level Truncated On-Policy Distillation）通过逐轮KL正则保持多轮工具使用
- **Agentic-textual transfer gap**：RL提升了操作能力，但不迁移到文本QA

**🔥 对你们的直接启示**：
- 你们用医生反馈做RLHF时，**必须设计逐轮奖励而非终端奖励**，否则Agent会坍塌成"写一篇长报告"而不是"多步推理"
- Healthcare AI GYM的5维奖励函数（准确+过程+安全+格式+连贯）可直接参考
- TT-OPD框架可用于你们的harness飞轮中的在线学习部分

### 🔑 ClinMPO（精神科临床RL对齐）

| 维度 | 详情 |
|------|------|
| **论文** | arXiv:2602.06449 |
| **方法** | 从4,474篇精神病学期刊构建EBM奖励模型 → RL优化8B模型 |
| **结果** | Qwen3-8B在复杂病例上达到31.4%诊断准确率，超过人类基准30.8% |

**启示**：用循证医学文献构建奖励模型是可行路线，你们可以从检验科文献+指南中构建专属的mNGS奖励模型。

### 🔑 End-to-End Differentially Private RLHF for Medical Dialogue

| 维度 | 详情 |
|------|------|
| **论文** | arXiv:2603.03054 |
| **方法** | 配对的医生回答 vs 非专家回答 → 偏好对 → DP训练 |
| **启示** | 隐私保护的RLHF管线，适合医院数据合规需求 |

### 🔑 MMedPO（ICML 2025）

| 维度 | 详情 |
|------|------|
| **方法** | 临床感知多模态偏好优化，解决Med-VLM的模态对齐问题 |
| **结果** | 相比现有偏好优化方法，报告生成任务提升51.7% |

---

## 四、方向C：Agent自进化 / Harness飞轮

### 🔑 Continual Harness（Princeton + DeepMind, 2026.05）

这是整个调研中**与你设想的harness飞轮最接近**的框架。

| 维度 | 详情 |
|------|------|
| **论文** | arXiv:2605.09998 |
| **核心** | reset-free的在线自进化Agent harness |
| **Harness四组件** | System Prompt + Sub-agents + Skills + Memory |

**架构（双层循环）：**
```
内循环（Agent Loop）：每步观察→动作→结果
外循环（Refinement Loop）：每F步读轨迹窗口→识别失败签名→编辑4个组件→无需重置环境
```

**失败签名类型**：导航循环、工具调用失败、目标停滞、遗漏探索

**模型-Harness共学习**：
- 在线DAgger（256步rollout）→ PRM打分 → 低奖励窗口由Gemini-3.1-pro教师重标 → 软SFT更新
- **结果**：Gemma-4开源模型在Pokémon Red上持续进步，无需重置

**🔥 直接映射到你们的场景：**

| Continual Harness概念 | 你们的检验科Agent映射 |
|----------------------|---------------------|
| System Prompt `p` | mNGS判读策略、临床指南摘要 |
| Sub-agents `𝒢` | 病原体判别Agent、证据检索Agent、报表生成Agent |
| Skills `𝒦` | 覆盖分析、耐药基因检测、流行病学统计 |
| Memory `ℳ` | 历史案例库、反馈对、疾病爆发模式 |
| Refiner | 医生反馈驱动的自动策略更新 |
| PRM + Teacher | 专家标注 + 自动奖励建模 |

**⚠️ 这个框架的核心洞察**：harness不应该由人工维护，而应该从Agent的**失败轨迹**中自动学习改进。你们医生反馈RLHF本质上就是这个Refinement Loop。

### 🔑 NVIDIA Data Flywheel

- [NVIDIA NeMo Microservices](https://developer.nvidia.com/blog/maximize-ai-agent-performance-with-data-flywheels-using-nvidia-nemo-microservices)：企业级数据飞轮方案
- 数据收集 → 标注 → 训练 → 评估 → 部署 → 再收集闭环

### 🔑 TheraAgent（Self-Improving Therapeutic Agent）

| 维度 | 详情 |
|------|------|
| **论文** | arXiv:2605.05963 |
| **方法** | generate-reflect-refine 迭代管线 + TheraJudge自动评估 |
| **结果** | HealthBench治疗规划任务SOTA |

**启示**：将报表生成从"一次生成"改为"生成→自我评估→优化"的迭代范式，即使没有医生反馈也能自改进。

---

## 五、方向E：检验数据 → 疫情预警

### 🔑 JMIR 2026：AI Agents + Epidemic Intelligence框架

| 维度 | 详情 |
|------|------|
| **论文** | [JMIR 2026;28:e86936](https://www.jmir.org/2026/1/e86936) |
| **核心** | 四柱框架：监测 → 风险评估 → 早期预警 → **AI Agent决策支持** |
| **创新** | 将传统三柱扩展到四柱，AI Agent作为"7×24小时数字流行病学家" |

**关键概念 "Golden Window"**：从检测到响应之间的短暂窗口期，及时干预（如疫苗研发和部署）可以最大限度限制传播。

**🔥 这正是你们想做的**：当mNGS检出某病原体频率上升时，Agent不应只报告，而应预判可能的爆发、给出预警级别和建议干预措施。

### 🔑 Frontiers 2025 系统综述

- [AI in early warning systems](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1609615/full)：AI驱动的传染病早期预警系统综述
- 覆盖ML/DL/NLP在疫情监测中的应用
- 关键数据源：EHR、社交媒体、气候数据、移动数据、**实验室检验数据**

### 🔑 DHIS2 + AI Triage（坦桑尼亚，实战案例）

- [AI-Driven Alert Triage in Tanzania](https://dhis2.org/ai-driven-alert-triage-tanzania)：AI驱动的监测告警分类
- 平均分诊时间从36小时降至接近即时

---

## 六、综合技术路线建议

基于以上调研，建议按以下层次构建系统：

```
┌─────────────────────────────────────────────────────────┐
│                    Harness 飞轮层 (方向C)                   │
│  Continual Harness → 自动从反馈轨迹优化Prompt/Skills/Memory │
├─────────────────────────────────────────────────────────┤
│                    RLHF 偏好对齐层 (方向A)                   │
│  TT-OPD 逐轮奖励 + ClinMPO式文献奖励模型 + 医生反馈对         │
├─────────────────────────────────────────────────────────┤
│                  证据链+报表层 (方向B)                        │
│  MedGraphRAG 图检索 + KARE 社区检索 + MedChain 多阶段工作流    │
├─────────────────────────────────────────────────────────┤
│                  病原体判别层 (方向D)                         │
│  GPAS GenoDB去冗余 + DLA混合算法 + 覆盖模式识别                │
├─────────────────────────────────────────────────────────┤
│                  疫情预判层 (方向E)                           │
│  四柱框架 + 实验室数据趋势检测 + Golden Window预警             │
└─────────────────────────────────────────────────────────┘
```

### 🎯 优先级建议

| 优先级 | 调研方向 | 具体行动 | 预期时间 |
|:--:|------|------|:--:|
| **P0** | GPAS 对齐 | Clone GPAS源码，理解GenoDB+DLA+LLM Agent架构，映射到renji_mngs管线 | 2周 |
| **P0** | MedGraphRAG | Clone源码，评估能否直接替换你们现有的FAISS RAG，测试证据链质量 | 1周 |
| **P1** | Healthcare AI GYM | 用TT-OPD框架改造你们现有的RLHF管线，防止"回答爆炸" | 3周 |
| **P1** | Continual Harness | 设计你们的Harness四组件（Prompt/Skills/Memory/Sub-agents），定义Refinement Loop | 4周 |
| **P2** | 疫情预判 | 基于JMIR四柱框架，设计检验数据→趋势检测→自动预警的管道 | 6周 |
| **P3** | TheraAgent | 引入generate-reflect-refine范式优化报表质量 | 2周 |

### ⚠️ 关键风险

1. **RLHF坍塌风险**：多轮医学Agent直接用GRPO/DPO会退化成"写长文"，必须参考TT-OPD的逐轮奖励设计
2. **证据幻觉**：GraphRAG虽好，但医学知识图谱构建成本高，建议先用GPAS式的结构化KG + PubMed检索的混合方案
3. **Harness过拟合**：Continual Harness在游戏环境验证，医疗场景的"奖励信号"更稀疏、更延迟，需要设计更强的安全护栏

---

## 📋 执行摘要

**核心发现**：5个方向都有2025-2026年的最新对标工作，且大多有开源代码。

| 方向 | 最直接对标 | 代码可用 | 紧急度 |
|------|---------|:--:|:--:|
| D.mNGS判别 | **GPAS**（GenoDB+DLA+LLM Agent） | ✅ GitHub | 🔴 P0 |
| B.证据链 | **MedGraphRAG**（Oxford ACL'25） + **KARE**（ICLR'25） | ✅ 有 | 🔴 P0 |
| A.RLHF | **Healthcare AI GYM + TT-OPD** + **ClinMPO** | ✅ 有 | 🟡 P1 |
| C.飞轮 | **Continual Harness**（Princeton+DeepMind） | 📄 论文 | 🟡 P1 |
| E.预警 | **JMIR 四柱框架** | 📄 论文 | 🟢 P2 |

**决策建议**：从P0开始——先clone GPAS和MedGraphRAG源码跑通，验证管线可行性，再逐步接入TT-OPD RLHF和Continual Harness飞轮。不要一上来就做全栈，选最小可行闭环（检出→判别→报表→反馈→改进）跑起来再说。
