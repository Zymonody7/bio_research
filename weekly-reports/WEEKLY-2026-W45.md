# 📊 周度论文报告 — 2026-W45（Nov 2–4，周三中期编译）

> 覆盖: **3 期采集日**（11-02, 11-03, 11-04）· **45 篇**唯一新论文 · **6 大方向全覆盖**（A/B/C/D/F/X）
> 📌 **本周重点**：JAMIA 给出 RAG vs 长上下文迄今最干净的定量答案；基因组 FM 同周被"双重清算"（打不过 baselineLD + 评估通胀）又被"双重重建"（hEVO/Mendel 转向人群变异监督）；对齐信号三线换代——指南变过程奖励（GUIDER）、偏好被证明不稳（专家 ICC 仅 0.087–0.295）、推理时注入廉价有效
> 🚧 **说明**：本报告为周三中期编译，数据截至 11-04，W45 尚有 11-05～11-08 未采集；**W43、W44 两周周报缺失**，缺口登记见文末（tracker 中数据完整，可补编）
> 标注说明：🔥🔥 高度直接 | 🔥 直接相关 | 📎 方法参考 | 📖 综述/背景
> 数据源：`.seen_papers.json`（1,611 条 tracker）· 本周 67 条原始键 → 唯一化 **45 篇**（剔除 DOI/PMID 三键重复 22 个，集中在 11-04）

---

## 📈 统计速览

| 指标 | 数值 |
|------|------|
| 总篇数（Nov 2–4，唯一化后） | **45** |
| 🔥🔥 高度直接 | **14** |
| 🔥 直接相关 | **25** |
| 📎 方法参考 / 📖 综述 | 6 |
| 已出版期刊论文 | **27 篇（60%）** |
| 预印本（bioRxiv / medRxiv / Research Square / arXiv） | 18 篇（40%） |
| 高影响力期刊（Nature Methods / Radiology / Nat Commun / JAMIA / eLife / npj SBA / Nat Comput Sci / Comm Med / Sci Rep / ACL 2026 / Brief Bioinform） | **11 篇** |

## 📅 按日统计

| 日期 | 论文数 | 🔥🔥 | 核心主题 |
|------|--------|------|---------|
| 11-02（一） | 15 | 3 | MARG 指南生命周期智能体、GFM 打不过 baselineLD 审计、Nat Comms 评估通胀、CEDAR 儿科预测 |
| 11-03（二） | 15 | 5 | OncoAgents 3804 例前瞻性试验匹配、GUIDER 指南过程奖励、AlphaGenome 虚拟敲除、harness 污染实验 |
| 11-04（三） | 15 | 6 | JAMIA RAG vs 长上下文、hEVO/Mendel 人群变异 FM、VentPilot 离线 RL、精神科医师 ICC 危机 |
| **合计** | **45** | **14** | |

> ⚠️ 11-04 日报统计行写"🔥🔥 7 篇"，正文实际徽章为 6 篇（off-by-one），本表按正文实数计。

## 🧭 方向分布

| 方向 | 11-02 | 11-03 | 11-04 | 合计 | 趋势 |
|------|-------|-------|-------|------|------|
| A. mNGS + AI 病原检测 | 3 | 3 | 2 | **8** | → 检测性能与证据等级持续夯实（TB 序贯策略、PJI meta、AI-感染病综述），但 **mNGS×AI 判读仍未合流**——"宏基因组序列上的临床 AI 判读"是确认的发表空白 |
| B. 临床 Agent + RAG/KG | 3 | 3 | 3 | **9** | ↑ 最均衡方向：RAG vs 长上下文定量答案、约束式工具面（gSage）、KG 用于监管审查、试验匹配前瞻验证 |
| C. RLHF 医疗对齐 | 2 | 2 | 3 | **7** | ↑ 换代信号密集：GUIDER 过程奖励、VentPilot 离线 RL、指南注入 test-time 对齐 vs **专家一致性危机** |
| D. 基因组基础模型 | 3 | 3 | 3 | **9** | ↑ 双轨并进：审计线（GFM 不提升变异发现）与新范式线（hEVO/Mendel 人群变异监督、虚拟敲除）同周共振 |
| F. 多模态临床 Agent | 3 | 2 | 2 | **7** | → 三种编排范式成型（职级辩论 MARCH / 协议循环 MedPAO / 模块编排眼科 agent）+ Radiology 智能体综述定框架 |
| X. 跨界发现 | 1 | 2 | 2 | **5** | ↑ 评估通胀、harness 工程、RCT 盲法外部验证、EHR 草稿采纳纵向研究——跨界质量极高 |

---

## 🏆 TOP 5 论文（跨日排名）

### 1. 🔥🔥 Evaluating retrieval-augmented generation versus long-context input for clinical reasoning over electronic health records
**Myers S, Dligach D, Miller TA, Barr S, et al.** — *JAMIA*, 2026 · [DOI: 10.1093/jamia/ocag139]
- 三个跨院可复现 EHR 任务 × 三模型 × 变量上下文：**RAG 用 <8K token 在抽取类任务上超过长上下文（+0.17–9.83 F1）**，抗生素时间线打平，但诊断生成任务对所有方法纹丝不动——瓶颈从上下文长度转移到病历文档变异与评测天花板。
- **与你项目的关联**：这是"检验科 Agent 上下文策略"的决策树级参考——报告解读、指南查询这类抽取/检索型任务应默认走 RAG（省 token 且更准），生成/判断型任务则需重设计评测而非堆上下文。错误分析还指出跨院转诊信息缺失是共同上限，与检验数据跨机构可得性问题同构。
- 建议：精读，摘出其任务×上下文配置表作为 orchestrator 上下文策略的直接依据。
- 📎 [JAMIA](https://doi.org/10.1093/jamia/ocag139) | PMID 42710003

### 2. 🔥🔥 Genomic heterogeneity inflates the performance of variant pathogenicity predictions
**Lu B, Liu X, Lin P-Y, Brandes N** — *Nature Communications*, 2026 · [DOI: 10.1038/s41467-026-78623-5]
- 系统复核"全基因组变异致病性预测精度惊人"的报道：性能被**混合不同致病性基线流行率的变异类别**严重虚高；按变异类型分层重建基准后模型真实分辨力显著缩水。
- **与你项目的关联**：本周最高影响力期刊之一，且与 D 方向"GFM 打不过 baselineLD"审计从预测侧与发现侧共同确立**"分层基线 + 功能富集评估"作为基因组 AI 的新评估语法**——凡涉及变异解读类供应商/模型选型，先看其评估是否分层。
- 建议：作为基因组 AI 能力声明的"默认质询依据"引用。
- 📎 [Nature Communications](https://doi.org/10.1038/s41467-026-78623-5)

### 3. 🔥🔥 A genomic foundation model for interpreting human genetic diversity（hEVO）
**Xu Q, Wu Z, Dong M, et al.** — *bioRxiv* 预印本 · [DOI: 10.64898/2026.10.19.760276]
- 用 **63,809 人、55 万份 WGS 重建的 47.84 亿条单倍型序列**做预训练、完全不用临床/功能标签，对 Evo 2/NT/GPN 在 19 项主比较中赢 18 项；6 个变异基准零微调泛化，ClinVar 回溯可识别后来被降级的致病变异。
- **与你项目的关联**：与同周的 **Mendel**（Research Square，variant-centric 目标把 SNV 等位预测 0.311→0.984）构成同一趋势的两个实现——GFM 训练目标正从"预测保守序列"转向"预测人群中的变异"。这条主线是方向 D 下一阶段的选型基准，也是变异解读类检验项目（药物基因组学）的基座候选观察对象。
- 建议：与 Mendel 联读，跟踪其后续 peer-review 进展与权重开放情况。
- 📎 [bioRxiv](https://doi.org/10.64898/2026.10.19.760276)

### 4. 🔥🔥 Latent Decision Flow Rewards for Clinical Guideline Reasoning（GUIDER）
**Bhatt G, Žitnik M** — arXiv 2610.38709, 2026 · [DOI: 10.48550/arxiv.2610.38709]
- 把临床指南编码为**条件决策流**做过程监督，形式化 path–answer gap 与 path multiplicity 两个新概念；Qwen3-14B 上 MedGUIDE 加权准确率 82.5、指南依从 73.5，超最强临床 RL 基线 3.3/3.1 分，跨域（AMEGA-LLM/RealMedQA/CancerGUIDE）胜出。
- **与你项目的关联**：把"指南依从"从评测指标变成训练信号——与 MARG（指南生命周期）、CheXPO-v2（KG 一致性奖励）连成"过程奖励"主线。检验场景的 CLSI/EUCAST 规则正是同构的"可编码决策流"，是把 C 方向方法红利输送到检验报告生成的最短路径。
- 建议：精读其决策流编码方式，评估把检验指南改写为 decision-flow 的工作量。
- 📎 [arXiv](https://arxiv.org/abs/2610.38709)

### 5. 🔥🔥 Transforming oncology clinical trial matching through neuro-symbolic, multi-agent AI and an oncology-specific knowledge graph: a prospective evaluation in 3804 patients
**Loaiza-Bonilla A, Yost C, Kurnaz S, et al.** — *ESMO Real World Data and Digital Oncology*, 2026 · [DOI: 10.1016/j.esmorw.2026.100706]
- 前瞻性 3,804 例连续患者、157,367 个试验页面实测：**OncoAgents + OncoGraph F1 = 0.82 vs GPT-4 zero-shot 0.47 / CoT 0.67**；单患者筛查 120 分钟 → 30 分钟，亚组公平性最大差距仅 ~7pt，消融证明 KG grounding 与多智能体分解各自贡献显著。
- **与你项目的关联**：目前公开文献中**证据等级最高的"临床试验匹配智能体"前瞻性研究**——"LLM 抽取 + 本体接地的确定性资格推理 + 人机复核"是可直接复用的部署蓝图，与 gSage/ARGUS 共同定义本周的"约束式架构"主线。
- 建议：精读其四组件架构与双医师金标准协议（κ=0.92），作为 orchestrator 分层设计的对照案例。
- 📎 [ESMO RWDO](https://doi.org/10.1016/j.esmorw.2026.100706) | PMID 42004487

## 🎖 提名奖

| 论文 | 方向 | 提名理由 |
|------|------|---------|
| **MARG: Multi-agent AI for liver disease guideline development and maintenance**（Comm Med, 10.1038/s43856-026-01961-4） | B | 智能体从"用指南"进到"造/修指南"，4 轮结构化辩论解决 95.8% 推荐冲突——辩论分歧点天然是 preference pair，🔗 C 方向，🔥🔥 |
| **gSage: Optimizing genomics-aware clinical agents in precision oncology**（npj Syst Biol Appl, 10.1038/s41540-026-00753-9） | B | **20 个精选工具五轴全胜 200+ 工具无约束 agent**——"约束式工具面 > 工具广度"是本周最可直接落地的设计结论，🔥🔥 |
| **VentPilot: offline RL + 重症医师偏好反馈的通气推荐**（J Intensive Care, 10.1186/s40560-026-00947-7） | C | 离线 RL + 偏好奖励 + Mayo 外部验证 1,011 例——RLHF 思想在非 LLM 临床控制上的完整落地，fitted Q-evaluation 可迁移，🔥🔥 |
| **Expert Evaluation and the Limits of Human Feedback in Mental Health AI Safety Testing**（arXiv 2601.18061） | C | 3 名精神科医师 ICC 仅 0.087–0.295、Krippendorff α 低至 −0.203——**对 RLHF 根基假设的直接检验**，本周对 reward modeling 冲击最大，🔥🔥 |
| **Functional motif detection via in silico ablation using AlphaGenome**（Brief Bioinform, 10.1093/bib/bbag422） | D | 基础模型 + 虚拟扰动 + CUT&RUN 真实验证——GFM 从打分器变假说生成器的范式，🔥🔥 |
| **Genomic foundation models do not yet boost common variant discovery beyond standard functional annotations**（bioRxiv, 10.64898/2026.10.13.758880） | D | 27 个 UK Biobank 性状上 GPN-Star 反而少发现位点、增益低于 baselineLD——首篇核心生产场景的 GFM 负面审计，🔥🔥 |
| **mNGS for tuberculosis diagnosis: enhanced performance and cost-effectiveness**（Microbiol Spectrum, 10.1128/spectrum.00970-26） | A | 3,757 例/16,776 项检测：**"先 WHO 推荐检测、阴性再补 mNGS"序贯策略 AUC 0.823**——A 方向本周最佳，直接回答 AI 判读该接在哪一棒，🔥 |
| **Learning When to Collaborate: SMART-Med 不确定性路由**（arXiv 2610.33544） | F | 按需协作 + 全本地部署，回应多智能体算力/延迟/隐私三重成本，🔥 |
| **Harness engineering enables multi-agent LLM system to generate cross-domain hypotheses**（bioRxiv, 10.64898/2026.10.25.761203） | X | 匹配 harness 下模型升级收益消失甚至反转——**harness 污染**被摆上台面，全领域 agent 对比的方法论警告，🔥🔥 |
| **AI-based prognosis and chemo benefit on SWOG-8814: blinded external validation**（medRxiv, 10.64898/2026.10.21.26366092） | X | 锁定权重→盲法→RCT 生存终点，AI 生物标志物证据链最高配置，对标 21 基因检测，🔥🔥 |

---

## 📡 趋势分析

### 趋势①：临床 agent 进入"约束式架构"时代 — 可靠性来自被约束的证据面，而非被放开的工具面

| 论文 | 方向/日 | 贡献 |
|------|---------|------|
| JAMIA RAG vs long-context | B / 11-04 | 抽取型任务 <8K token 检索即最优；诊断生成对所有方法无感——**上下文也要被约束** |
| gSage（npj SBA） | B / 11-03 | 20 个精选领域工具 + 版本化知识栈，五轴全胜 200+ 工具 agent |
| ARGUS（PMID 42926727） | D / 11-03 | 458 个确定性 TF 模型作证据源，无证据即**显式弃权** |
| OncoAgents（ESMO RWDO） | B / 11-03 | 本体接地的确定性资格推理 + 人机复核，F1 0.82 vs 0.47 |
| SMART-Med（arXiv 2610.33544） | F / 11-02 | 不确定性路由：多数查询单 agent 解决，仅不确定样本触发多智能体 |
| MARG（Comm Med） | B / 11-02 | 结构化辩论 4 轮解决 95.8% 冲突——冲突消解也有固定协议 |
| MedPAO-VL / MARCH | F / 11-02, 11-03 | 协议合规循环 / 职级层级辩论：把组织约束直接编码进架构 |

**洞察**：本周至少 7 篇互不相识的论文独立收敛到同一判断——agent 的可靠性不来自工具/上下文/协作的扩张，而来自**证据面与流程的收缩**（精选工具、弃权协议、路由门控、协议约束、职级结构）。这与 RAG 之后的架构演进方向一致：从"能调什么"转向"允许信什么"。JAMIA 那篇是同一逻辑在上下文维度的证明。

> **行动建议**：检验科 Agent orchestrator 下一版把三条约束写进设计规范：① 工具面收敛为 20 个以内的检验领域工具（gSage 模式）；② 关键判断组件带"证据不足即弃权"接口（ARGUS 模式）；③ 低置信样本强制升舱到规则校验+人工通道（SMART-Med 路由）。

### 趋势②：基因组 FM 同周被"双重清算"又被"双重重建" — 旧范式失效与新范式登场同时发生

| 论文 | 方向/日 | 角色 |
|------|---------|------|
| GFM 不提升共同变异发现（bioRxiv） | D / 11-02 | **清算**：27 性状上增益低于 baselineLD，GPN-Star 反而减发现 |
| Genomic heterogeneity inflates...（Nat Commun） | X / 11-02 | **清算**：致病性预测头条数字来自评估设计而非模型能力 |
| Harness engineering（bioRxiv） | X / 11-03 | **清算**：匹配 harness 后模型升级收益消失 |
| hEVO（bioRxiv） | D / 11-04 | **重建**：人群单倍型多样性本身做监督，19 项比 18 胜 |
| Mendel（Research Square） | D / 11-04 | **重建**：variant-centric 目标 SNV 预测 0.311 → 0.984 |
| AlphaGenome 虚拟敲除（Brief Bioinform） | D / 11-03 | **重建**：打分器 → 虚拟扰动 + 真实表观验证的假说生成器 |
| HiCFoundation（Nature Methods） | D / 11-03 | **重建**：一维序列 → 三维基因组结构模态 FM |

**洞察**：清算与重建其实是同一句话的两半：**以"保守序列补全"为目标的 GFM 既学不到稀疏变异的分辨率，其宣称的收益又大量来自评估自由度**——于是 hEVO/Mendel 直接换掉监督信号（人群变异分布），AlphaGenome/HiCFoundation 换掉任务形态（虚拟扰动、结构模态）。一周之内"旧范式为什么不行"和"新范式怎么补"同时交付，这通常是范式切换加速的信号。

> **行动建议**：D 方向跟踪策略改为"**审计线 + 换代线**"双轨等权：审计线决定"能不能信"，换代线决定"该选谁"。涉及变异解读的检验项目（药物基因组/肿瘤 panel 解读）暂不以旧范式 GFM 分数作选型依据，等 hEVO/Mendel 类模型 peer-review 后再评估。

### 趋势③：对齐信号三线换代 — 指南成奖励、偏好遭质疑、推理时上位

| 论文 | 方向/日 | 换代方向 |
|------|---------|---------|
| GUIDER（arXiv 2610.38709） | C / 11-03 | 指南 → **流级过程奖励**（训练信号） |
| CheXPO-v2（arXiv 2512.17213） | C / 11-02 | KG 三元组一致性 → **原子级过程奖励** |
| 金标准 ICD 编码 DPO（BMC MIDM） | C / 11-02 | 金标准标签 → **免费偏好对** |
| VentPilot（J Intensive Care） | C / 11-04 | 偏好奖励 → **非 LLM 临床控制策略** + 多中心外部验证 |
| 指南增强 prompt（J Exp Orthopaedics） | C / 11-04 | **test-time 对齐**：不改权重，GPT-4o 胜率 +11.8pt |
| 精神科医师 ICC 危机（arXiv 2601.18061） | C / 11-04 | **反向信号**：专家一致性 0.087–0.295，聚合标签 = 算术折中 |

**洞察**：C 方向的重心正在同时发生三个位移：① 信号来源从"人类偏好"移到**可验证结构**（指南、金标准、KG、环境）；② 时机从训练时移到推理时（指南注入的廉价收益）；③ 最根本的——**连"人类偏好"这个原料本身都被证明不稳**（分歧来自相互自洽的临床框架而非测量误差）。三者合起来指向：未来的对齐不是"更准地聚合专家"，而是"**结构化可验证信号 + 显式建模分歧**"。

> **行动建议**：若做检验报告生成微调，优先级排序：guideline-as-process-reward（GUIDER 模式，CLSI 规则可编码）> 金标准 DPO（有报告审核记录即可造偏好对）> 人类偏好标注（最贵且本周证据最弱）。关注 `expert disagreement reward modeling` 是否已有人占位。

## 🔮 白空间与交叉机会

1. **mNGS × AI 判读合流（本周被明确证实的空白）**：11-04 A 方向观察显示 "mNGS + LLM/agent" 主检索仅 7 条——现有 mNGS 文献停在检测性能与序贯策略，AI 研究停在影像/文本，**两者尚未合流**。TB 论文恰好给出接入位点：AI 判读放在"WHO 推荐检测阴性后的第二棒"。这是 A×B×C 三方向方法交叉的第一个明确落点。
2. **分歧保留的奖励建模**：精神科 ICC 论文指出聚合标签抹掉有据的专业分歧，但没给出替代方案的实证——**多头奖励模型 / 分歧结构化保留**在医疗安全条目上的效果无人测过，一个可直接开做的实验。
3. **Agent 对比的 harness 预注册 registry**：harness 污染被证实后，"公开 prompt/schema/工具面/查询预算否则不入表"的评测登记制度是天然的白空间——谁先做谁定义领域证据标准。
4. **人群 GFM 的跨 ancestry 公平性 benchmark**：hEVO/Mendel 兴起后，不同 ancestry 上等位基因分数校准的标准化评测尚无 benchmark——与检验参考区间的人群分层问题直接相通。
5. **（承接 W42）检验危急值报告的分级软验证器**：GUIDER + mNGS meta 金标准口径 + 专家复核结论，三样材料本周齐备，构造"报告生成的流级奖励"技术上已无障碍。

## 🎯 下周聚焦

1. **精读优先级**：① JAMIA RAG vs 长上下文（上下文策略决策树）② gSage + ARGUS（约束式架构两个样板）③ hEVO + Mendel 联读（D 选型基准）④ GUIDER（检验指南可编码性评估）⑤ OncoAgents（前瞻验证协议）
2. **架构迭代输入**：把"20 工具收敛 + 弃权接口 + 不确定性升舱"写进 orchestrator 下一版设计规范（趋势①行动建议三条）
3. **跟踪主题**：D 方向双轨（审计线 vs 换代线）；C 方向分歧建模；A 方向"序贯策略第二棒"接入证据

## 🔍 搜索策略调整（下周生效）

- 方向 D 新增词族：`variant-centric`, `haplotype pretraining`, `ancestry`, 保留模型名录查询（Nucleotide Transformer / DNABERT / HyenaDNA / Evo / Caduceus）
- 方向 C 新增常驻：`expert disagreement reward modeling`, `preference data inter-rater reliability medical`, `rubric-conditioned alignment`；arXiv 常驻 `clinical + guideline/process reward`、`simulation + RL + intake/interview`
- 方向 A 改两段式：先以临床问题为锚（新适应证/序贯策略），再单独 OpenAlex 搜 `metagenomic` × `foundation model`/`agent`；补充 `spectral microbiology + machine learning`、`LLM + pathogen report`
- 方向 B/X 新增：`implementation science LLM`, `workflow fit adoption longitudinal`, `regulatory document agent`, `harness matched evaluation agent`
- 来源：增加每日 bioRxiv API 的 **agent + biology** 定向扫描（本周 MCP/agent 类预印本产出稳定，不必等 PubMed 稀疏才兜底）
- 白空间先发扫描：`"critical value" AND "LLM agent"`, `"disagreement-aware reward"`, `"harness" AND "agent benchmark"`

## ⚠️ 问题与改进

1. **Tracker 三键重复持续恶化**：11-04 单日 37 条原始键仅 15 篇唯一论文（同一篇被 `10.x/...`、去前缀 DOI、PMID 三个键入库，如 Spectrum TB 论文 3 键、JAMIA 3 键）；本周 67→45。W42 已报告过同问题但未修复——**入库脚本需在写入前做 PMID→DOI 归一 + 去前缀合并**，否则 tracker 体积虚增约 25%。
2. **11-04 日报统计 off-by-one**：统计行声称 🔥🔥 7 篇，正文徽章 6 篇——cron 统计逻辑与正文徽章不同步，建议统计行由正文徽章反算。
3. **周报缺口（W42 尾段 + W43 + W44 全周）**：详见文末缺口登记。tracker 数据完整，9 期日报文件均在磁盘，可在任意一次周报中批量补编。
4. **管线中断记录**：tracker 在 **10-22～10-29 连续 8 天无任何记录**（日报文件同期也缺失），另有 10-13/10-14/10-16 空档——疑似 cron 停摆，建议核查 10 月下旬的 cron 执行日志；中断期文献未回捞（属于真实的采集缺口，非 tracker 记录问题）。
5. 仓库工作目录存在大量临时文件（`.tmp_*.json`、`candidates*.json`），已用显式 `git add weekly-reports/` 规避误提交。

## 📎 附：缺口登记（供后续补编）

| 周期 | 采集日 | 原始键 | 唯一化 | 方向分布 | 状态 |
|------|--------|--------|--------|---------|------|
| W42 尾段 | 10-15, 10-17, 10-18 | 97 | 57 | A8 B11 C9 D11 F11 X7 | 周报未覆盖（W42 报告止于 10-12） |
| W43 | 10-19, 10-20, 10-21 | 50 | 44 | A7 B8 C7 D11 F8 X3 | **无周报**；10-22～10-25 管线中断 |
| W44 | 10-30, 10-31, 11-01 | 48 | 39 | A6 B7 C6 D9 F7 X4 | **无周报**；10-26～10-29 管线中断 |
| W45（本周） | 11-02, 11-03, 11-04 | 67 | **45** | A8 B9 C7 D9 F7 X5 | 本报告；11-05～11-08 待采集 |

---

*编译时间：2026-11-04（周三）· 数据源：`.seen_papers.json` v1,611 条 + 11-02/03/04 三期日报 · 唯一化规则：DOI/PMID/去前缀三键归一 + 标题模糊匹配 (>0.75)*
