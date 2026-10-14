# 📊 周度论文报告 — 2026-W42（Oct 8–12，周三中期编译 + W41 尾段补编）

> 覆盖: **4 期采集日**（10-08, 10-09, 10-11, 10-12）· **59 篇**唯一新论文 · **6 大方向全覆盖**（A/B/C/D/F/X）
> 📌 **本周重点**：Science 发布 Biomni 自主生物医学研究 Agent、Nature Medicine 连发 MedFound / MedGemma、基因组 FM 进入"自我审视期"（4 篇审计/探针论文集中出现）、医疗 RLHF 转向"程序化/共识式奖励"
> 🚧 **说明**：W41 周报（Oct 7）只覆盖到周三，本报告补编其尾段（Oct 8/9/11）+ W42 周一（Oct 12）；10-10、10-13、10-14 无 tracker 记录（日报缺口，见"问题与改进"）
> 标注说明：🔥🔥 高度直接 | 🔥 直接相关 | 📎 方法参考 | 📖 综述/背景
> 数据源：`.seen_papers.json`（1,224 条 tracker）· 唯一化后 59 篇（剔除 DOI/PMID/W-prefix 三重键重复 12 组 + 跨日重复 1 组）

---

## 📈 统计速览

| 指标 | 数值 |
|------|------|
| 总篇数（Oct 8–12，唯一化后） | **59** |
| 🔥🔥 高度直接 | **20** |
| 🔥 直接相关 | ~24 |
| 📎 方法参考 / 📖 综述 | ~15 |
| 高影响力期刊（Science / NatMed / NatBiotechnol / NatMethods / NatComms / Cancer Discov / npj DigitMed / Cell Rep Med / Patterns / IJCAI / Bioinformatics 等） | **~15 篇** |
| 预印本（arXiv / bioRxiv / medRxiv） | 23 篇（39%） |

## 📅 按日统计

| 日期 | 论文数 | 🔥🔥 | 核心主题 |
|------|--------|------|---------|
| 10-08（四） | 16 | 6 | Science Biomni、NatMed MedFound/MedGemma、GPN-MSA、COBRA 恶意反馈防御 |
| 10-09（五） | 15 | 3 | ResidencyRL/ConRub-Med 共识奖励、AgentEYE/EviDx 证据型诊断 agent、基因组 LM 基准 |
| 10-11（日） | 15 | 6 | Tangermeme、基因组 FM"压力测试"三连、自主放疗规划、EMR 自进化多智能体 |
| 10-12（一） | 13 | 5 | GFM 监管机制局限审计×2、EHR-RobustGym、复杂性悖论（GPT-5 通用 agent）、Cerberus |
| **合计** | **59** | **20** | |

## 🧭 方向分布

| 方向 | 10-08 | 10-09 | 10-11 | 10-12 | 合计 | 趋势 |
|------|-------|-------|-------|-------|------|------|
| A. mNGS + AI 病原检测 | 3 | 2 | 2 | 1 | **8** | ↑ 从"检出病原"走向"表型推断"：药敏预测、耐药组画像、谱系感知分类 |
| B. 临床 Agent + RAG/KG | 3 | 2 | 3 | 4 | **12** | ↑ 最活跃方向：agent 系统工程化（路由/成本/自进化/工作流语言） |
| C. RLHF 医疗对齐 | 3 | 3 | 3 | 2 | **11** | ↑ 奖励结构设计时代：共识 rubric、神经符号对齐、人机回环风险处置 |
| D. 基因组基础模型 | 3 | 3 | 3 | 4 | **13** | ↑ 量最大：审计论文集中出现 + 双向 SSM 架构创新并行 |
| F. 多模态临床 Agent | 3 | 3 | 3 | 1 | **10** | → 专科落地密集：眼科/放疗/病理/内镜 + MedGemma 开放基座 |
| X. 跨界发现 | 1 | 2 | 1 | 1 | **5** | → 组学数据挖掘 agent、药企 R&D agent、工作流语言桥接 |

---

## 🏆 TOP 5 论文（跨日排名）

### 1. 🔥🔥 Biomni: Autonomous biomedical research with an AI agent
**作者未记录（tracker 仅存 DOI）** — *Science*, 2026 · [DOI: 10.1126/science.adz4351]
- Science 正刊发表的自主生物医学研究 Agent：给定研究目标，自主拆解任务、检索文献/数据库、设计并执行分析流程。
- **与你项目的关联**：这是"检验科 Agent"的上游镜像——Biomni 验证了 agent 在生物医学领域自主执行多步研究任务的可行性，其任务分解与工具编排模式可直接参考进 orchestrator 设计；Science 背书意味着该范式进入主流视野。
- 建议：精读其 agent 架构与评测协议，摘取工具注册/任务分解模块。

### 2. 🔥🔥 MedGemma: open medical vision-language model
**作者未记录（tracker 仅存 DOI）** — *Nature Medicine*, 2026 · [DOI: 10.1038/s41591-026-04626-w]
- 开放权重的医学多模态基础模型（影像+文本），Nature Medicine 发表并配套开放权重，是目前最强的可自部署医学 VLM 基座。
- **与你项目的关联**：检验报告多模态理解（形态学图片+结构化指标）的候选基座；比闭源 API 更适合医院内网部署场景，直接回应数据不出院的合规约束。
- 建议：列入基座模型选型 shortlist，评估其在检验形态学任务上的 zero-shot 表现。

### 3. 🔥🔥 The complexity paradox of generalist AI agents in medicine: exploring GPT-5
**npj Digital Medicine**, 2026 · [DOI: 10.1038/s41746-026-03325-7]
- 提出"复杂性悖论"：通用 agent 在医学任务上，任务复杂度提升时收益并不单调增长，某些复杂场景反而劣于专用流水线。
- **与你项目的关联**：这是对"一个大 agent 包打天下"路线的直接警示——检验科 Agent 的分诊→专项流水线分层架构（triage + specialist tools）恰好是该悖论的工程化解法，此文可作为架构论证的核心引用。
- 建议：精读，提炼其复杂度分层评测方法，用于自家 agent 的评测设计。

### 4. 🔥🔥 MedFound: generalist medical language model
**Nature Medicine**, 2026 · [DOI: 10.1038/s41591-024-03416-6]
- 通用医学语言模型，大规模临床文本预训练 + 临床任务适配，Nature Medicine 正刊。
- **与你项目的关联**：与方向 C（医疗对齐）直接呼应——MedFound 展示"通用预训练→临床对齐"两段式路线的天花板，是对照自家 LLM 选型的基准锚点。
- 建议：与本周 ConRub-Med、神经符号对齐论文联读，拼出"医学 LM 能力-安全"完整图景。

### 5. 🔥🔥 GPN-MSA: DNA language model with multispecies alignment for variant effects
**Nature Biotechnology**, 2026 · [DOI: 10.1038/s41587-024-02511-w]
- 用多物种比对（MSA）上下文增强 DNA 语言模型的变异效应预测，Nature Biotechnology 发表——与上周 GPN-Star（Nature）同一系列的延续。
- **与你项目的关联**：方向 D 的标杆演进线：从单序列 FM → 比对上下文增强，验证"进化信息注入"是基因组 FM 下一个主战场。
- 建议：与本周的 GFM 审计论文（见趋势③）对照阅读——架构增益 vs 任务局限两条线索交叉验证。

## 🎖 提名奖

| 论文 | 方向 | 提名理由 |
|------|------|---------|
| **Perseus**（Bioinformatics, 10.1093/bioinformatics/btag687） | A | 谱系感知的 Kraken2 长读长分类修正——mNGS 分析层国产化/精细化的直接参考，🔥🔥 |
| **Agentic discovery of blood biomarker from distilled private health records**（arXiv 2610.04749） | B | Agent 从私有 EHR 蒸馏数据中自主发现血液生物标志物——检验科 Agent 的"上游发现"同构场景，🔥🔥 |
| **EviDx: Evidence-Aware Active Diagnosis**（arXiv 2608.24570） | F | 证据感知主动诊断 agent，脚手架式设计与检验科主动提示场景高度契合，🔥 |
| **Neurosymbolic Alignment for Physiologically-Safe Clinical LMs**（arXiv 2608.24534） | C | 神经符号方法保证临床 LM 生理安全约束——比纯 RLHF 更硬的安全保证，🔥🔥 |
| **The phage stress test**（bioRxiv 10.64898/2026.09.23.753910） | D | 噬菌体预测"压力测试"揭示基因组 LM 泛化真相，审计型评测设计范本，🔥 |
| **Tangermeme**（Nature Methods, 10.1038/s41592-026-03254-z） | D | 顺式调控逻辑解读的深度学习工具箱——D 方向的可复用基础设施，🔥 |
| **CRC-Router: Risk-Constrained Routing for Medical Agentic AI**（arXiv 2609.30714） | F | 风险约束路由——回应复杂性悖论的工程方案，与 TOP 3 构成完整论证链，🔥🔥 |

---

## 📡 跨方向核心信号

### 信号①：Agent 系统工程化元年 — 从"能不能做"到"怎么部署稳" — Biomni → CRC-Router → EHR-RobustGym

| 论文 | 方向/日 | 贡献 |
|------|---------|------|
| Biomni (Science) | B / 10-08 | 自主研究 agent 正刊验证，范式确立 |
| CRC-Router (arXiv 2609.30714) | F / 10-11 | 风险约束的 agent 路由：高危任务强制人工/专用模型 |
| EHR-RobustGym (arXiv 2609.39371) | B / 10-12 | 临床 agent 鲁棒性训练基准：噪声 EHR 下的推理 |
| EMR Self-Evolving Multi-Agent (arXiv 2609.15161) | B / 10-11 | 经验挖掘与复用实现 agent 自进化 |
| DeepMed Search (IJCAI 2026) | B / 10-11 | 开源医学深度研究 agent 平台 |
| Workflow languages 桥接 (PLoS Comput Biol) | X / 10-12 | LLM agent 与工作流形式语言的互操作 |

**洞察**：本周 6 篇论文共同标志 agent 研究从"能力展示"转向"部署工程"——路由、鲁棒性、自进化、工作流标准化四个部署必答题同时出现。复杂性悖论（TOP 3）给出了理论约束，CRC-Router 给出工程解，EHR-RobustGym 给出评测工具——一条完整的"问题→理论→方案→评测"证据链在一周内成型。

> **行动建议**：检验科 Agent 的 orchestrator 设计直接采用"风险约束路由"模式：低危查询走通用 LLM，高危（如危急值提示）强制走规则校验+人工确认通道。把 EHR-RobustGym 的噪声注入思路移植到检验数据 agent 的评测集构建中。

### 信号②：医疗 RLHF 进入"奖励结构设计"时代 — 从人类偏好到共识/程序化信号 — COBRA → ConRub-Med → 神经符号对齐

| 论文 | 方向/日 | 贡献 |
|------|---------|------|
| COBRA (Sci Rep) | C / 10-08 | 共识奖励机制抵御恶意 RLHF 反馈 |
| ConRub-Med (arXiv 2608.10996) | C / 10-09 | 共识 rubric 的可验证奖励 |
| ResidencyRL (arXiv 2608.07418) | C / 10-09 | 模拟临床环境中的 RL 训练闭环 |
| Neurosymbolic Alignment (arXiv 2608.24534) | C / 10-11 | 符号约束保证生理安全 |
| RASPER (arXiv 2610.02979) | C / 10-11 | 奖励对齐的临床摘要→下游预测联动 |
| PiPrO (PLOS Digital Health) | C / 10-08 | 参与式偏好优化 |

**洞察**：连续第三周强化同一趋势：裸人类偏好（preference）被系统性替换为可验证、可聚合、可防御的奖励结构——共识 rubric（多评审取共识）、模拟环境（环境即奖励）、符号约束（硬规则即奖励）。RASPER 进一步把奖励对齐与下游临床效用（EHR 预测）挂钩，奖励不再是"像人说话"而是"对临床结果负责"。

> **行动建议**：若检验科 Agent 后续做微调，优先采用 rubric-based 奖励（把 LIS 指南规则编码成可核验 rubric），避免昂贵且不可靠的人类偏好标注。

### 信号③：基因组 FM 的"自我审视期" — 审计/探针论文一周四连 — GFM 局限 → Splice 探针 → 噬菌体压力测试 → Kidzoi

| 论文 | 方向/日 | 贡献 |
|------|---------|------|
| Limitations of GFMs for regulatory mechanisms (bioRxiv) | D / 10-12 | GFM 解码顺式调控机制的能力上限审计 |
| Probing GFMs with splice-variant perturbations (bioRxiv) | D / 10-12 | 剪接变异扰动探测 FM 内部表征 |
| Phage stress test (bioRxiv) | D / 10-11 | 噬菌体场景压力测试泛化性 |
| LAMBDA (NAR Genom Bioinform) | D / 10-09 | 噬菌体检测基准 |
| Cerberus (bioRxiv) | D / 10-12 | 双向 state space block 提升效率与精度 |
| SUCCEED (Nat Commun) | D / 10-08 | 大规模监督多任务 DNA FM |
| MutationProjector (Cancer Discovery) | D / 10-08 | 癌症基因型 FM |

**洞察**：D 方向出现罕见的"审计集群"——4 篇论文从不同角度追问同一问题：基因组 FM 到底学到了什么？答案偏冷峻：调控机制解码能力有限、剪接需专门扰动才能探明、噬菌体域泛化脆弱。这与 SUCCEED/Cerberus 的"更大更强"叙事形成张力——架构创新派与任务审计派的对话正在成型，这通常是领域走向成熟的前兆。

> **行动建议**：方向 D 的跟踪策略调整为"双轨"：架构线（Cerberus、GPN-MSA）与审计线（局限/探针/压力测试）等权重跟踪；审计类论文对"该不该把 GFM 接入检验流程"的决策价值高于架构论文。

### 信号④：mNGS 越过"检出病原"，进入"表型与耐药推断" — BAL 指纹 → WGS 药敏 → Perseus

| 论文 | 方向/日 | 贡献 |
|------|---------|------|
| Metagenomic fingerprints in BAL (npj Digit Med) | A / 10-08 | mNGS 指纹区分肺部疾病（超越病原检出） |
| Rapid AST via WGS+mNGS (mSystems) | A / 10-08 | 快速药敏预测 |
| Nanopore AMR determinants (Microb Genom) | A / 10-09 | 纳米孔直接关联耐药基因与宿主病原 |
| Perseus (Bioinformatics) | A / 10-11 | 谱系感知长读长分类修正 |
| Resistome AI profiling 综述 | A / 10-12 | AI 耐药组画像方法学综述 |

**洞察**：A 方向本周所有论文共享一个转向：mNGS 的价值锚点从"有什么菌"移到"菌是什么表型"（耐药性、疾病分型）。这与检验科的核心职能（药敏报告、疾病鉴别）比病原检出更近——是 A 方向近期与用户项目关联度最高的一周。

> **行动建议**：将"mNGS AST / mNGS resistome"加入 A 方向常驻检索词（下周生效，见搜索策略）。

### 信号⑤：临床数据 agent 化 — 从病历到组学数据的自主挖掘 — 血液标志物发现 → Omics Discovery Agents

| 论文 | 方向/日 | 贡献 |
|------|---------|------|
| Blood biomarker from private EHR (arXiv 2610.04749) | B / 10-11 | Agent 蒸馏私有病历自主发现血液标志物 |
| Computable longitudinal patient journeys (PMID 42742184) | B / 10-12 | 结构化+非结构化 EHR 的可计算纵向病程 |
| Omics data discovery agents (PLoS Comput Biol) | X / 10-12 | 组学数据检索-再分析-综合 agent |
| AZ Research Assistant (arXiv 2608.12395) | X / 10-09 | 药企 R&D 自主 agent 系统 |

**洞察**：两个原本独立的领域（EHR 挖掘、组学数据重分析）本周同时 agent 化，且方法收敛——检索→再分析→综合的三段式。对检验科而言，"血液标志物发现 agent"是最接近的同构场景：检验数据本质就是结构化血液指标流。

> **行动建议**：将本信号列为周度交叉观察固定项；若"检验科 Agent"二期规划涉及标志物挖掘，blood biomarker agent 论文是第一篇要精读的。

---

## 🔮 白空间与交叉机会

1. **风险约束 + 检验危急值**：CRC-Router 的风险路由从未有人在检验场景（危急值自动审核、异常结果主动提示）中实现——交叉空白，具备发论文/做产品的双重空间。
2. **GFM 审计 × 检验基因组学**：审计型评测（压力测试、探针）从未被应用于临床宏基因组/耐药基因场景——用 D 方向的审计方法论做 A 方向的选型评测。
3. **共识 rubric 奖励 × LIS 指南**：把 CLSI/EUCAST 规则编译成可核验 rubric 作为 agent 微调奖励——C 方向方法 × A/B 方向场景，目前无人占位。

## ⚠️ 问题与改进

1. **Tracker 三键重复入库（本周最突出问题）**：10-12 单日 26 条原始记录仅 14 条唯一论文——同一论文被 DOI、PMID、W-prefix 三重键入库（如 GlyRAG 3 键、EndoCADx 3 键），且 MedGemma 跨日重复（10-08 DOI 入库、10-12 PMID 再入库）。**改进**：入库脚本增加"入库前跨格式去重"（PMID→DOI 映射后再判断），周报编译侧已有唯一化兜底，但 tracker 体积虚增（1224 条实际约少 15%）。
2. **日报缺口**：10-10、10-13、10-14 无 tracker 记录。10-13/14 为本报告编译时点之后/当日，属正常；**10-10（周六）缺失需核查 cron 是否失败**。
3. **W-prefix 键来源不明**：`W72xxxxxx` 格式键（约 12 个）疑似某中文库/爬虫来源 ID，与 DOI 键并存造成冗余——建议追溯来源并在入库时归一为 DOI。

## 🎯 下周聚焦

1. **精读优先级**：① Biomni（架构）② 复杂性悖论（评测方法）③ CRC-Router（路由模式）④ Perseus（mNGS 分析层）⑤ blood biomarker agent（二期规划预研）
2. **跟踪主题**：agent 部署工程（路由/鲁棒性/自进化）延续为 B/F 双方向主轴；GFM 审计线在 D 方向等权重跟踪
3. **架构迭代输入**：把"风险约束路由"作为检验科 Agent orchestrator 下一版设计的第一参考模式

## 🔍 搜索策略调整（下周生效）

- 新增常驻检索词：`"metagenomic" AND "antimicrobial susceptibility"`, `"resistome" AND ("machine learning" OR "foundation model")`（方向 A 表型化转向）
- 新增：`"risk-constrained routing"`, `"agent robustness benchmark clinical"`（方向 B 部署工程化）
- 新增：`"genomic foundation model" AND ("limitation" OR "probing" OR "stress test")`（方向 D 审计线）
- 会议追踪：**IJCAI 2026**（本周 DeepMed Search 入选）、AAAI 2027 CFP 关注 clinical agent track
- 白空间机会：`"critical value" AND "LLM agent"`、`"rubric reward" AND "laboratory"`——先发扫描确认占位情况

---

*编译时间：2026-10-14 20:00 CST · 数据源：`.seen_papers.json` v1,224 条 · 唯一化规则：DOI/PMID/W-prefix 三键归一 + 标题模糊匹配 (>0.78)*
