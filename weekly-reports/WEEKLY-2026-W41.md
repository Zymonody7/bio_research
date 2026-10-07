# 📊 周度论文报告 — 2026-W41（Oct 5–7，周三中期编译）

> 覆盖: **3 期日报**（10-05, 10-06, 10-07）· **59 篇**新论文 · **6 大方向全覆盖**（A/B/C/D/F/X）
> 📌 **本周重点**：Nature Medicine / Nature / Nature Biomedical Engineering 三刊连发临床 Agent 与基因组 FM 重磅工作、医学 RLHF 进入"奖励结构设计"时代、临床 Agent 从答题走向可部署系统
> 🚧 **说明**：本周为周三中期编译（Oct 5–7），周四–周日数据待补；**同时补编 W40 缺口**（Oct 1–4 共 73 篇，见文末补编节）
> 标注说明：🔥🔥 高度直接 | 🔥 直接相关 | 📎 方法参考 | 📖 综述/背景
> 数据源：`.seen_papers.json`（1,155 条 tracker）· 期刊论文与预印本混合（预印本占比约 42%，C/D/F 方向为主）

---

## 📈 统计速览

| 指标 | 数值 |
|------|------|
| 总篇数（Oct 5–7） | **59** |
| 🔥🔥 高度直接 | **20** |
| 🔥 直接相关 | ~22 |
| 📎 方法参考 / 📖 综述 | ~8 |
| 高影响力期刊（Nature / NatMed / NatBiomedEng / Cell Rep Med / npj / JAMIA / JMIR / IEEE Trans 等） | **~16 篇** |
| 预印本（arXiv / bioRxiv / medRxiv / Research Square） | ~25 篇（42%） |

## 📅 按日统计

| 日期 | 论文数 | 🔥🔥 | 核心主题 |
|------|--------|------|---------|
| 10-05（一） | 25 | 4 | 指南锚定 RAG 实证、RL 患者轨迹奖励、基因组 FM 训练分布重设计、agent 监管评估 |
| 10-06（二） | 18 | 9 | Nature Medicine 院内 Agent、安全训练反噬、rubric reward hacking、基因组 FM 信任栈 |
| 10-07（三） | 16 | 7 | GPN-Star（Nature）、cfDNA 语言模型、程序化奖励 GRPO、Agent 自进化与记忆 |
| **合计** | **59** | **20** | |

## 🧭 方向分布

| 方向 | 10-05 | 10-06 | 10-07 | 合计 | 趋势 |
|------|-------|-------|-------|------|------|
| A. mNGS + AI 病原检测 | 5 | 3 | 2 | **10** | ↓ 量缩质升：从工具综述走向数据分析层（MARM、ZILA-SRM、EUCAST 权威评估） |
| B. 临床 Agent + RAG/KG | 4 | 3 | 3 | **10** | → 指南锚定连续三天出证据；agent 评测从答题换代为证据搜集 |
| C. RLHF 医疗对齐 | 5 | 3 | 3 | **11** | ↑ 本周最强叙事：非人类奖励信号 → 安全训练反噬 → 程序化奖励修复 |
| D. 基因组基础模型 | 5 | 4 | 3 | **12** | ↑ Nature 级成色大考 + 隐私/tokenization/物理先验三线并进 |
| F. 多模态临床 Agent | 3 | 3 | 2 | **8** | ↑ NatMed/NatBiomedEng 双旗舰：可部署架构 + 专家行为监督 |
| X. 跨界发现 | 3 | 2 | 3 | **8** | → 安全评估、组学数据 agent、实时幻觉探测 |

---

## 🏆 本周 TOP 5 论文

| # | 论文 | 方向/日期 | 期刊 | 理由 |
|---|------|----------|------|------|
| **1** | **On-premise medical AI agents for reliable clinical decision-making**（Zhang, Wölflein, Ferber, Clusmann et al., DOI 10.1038/s41591-026-04609-x, PMID 42744896） | F / 10-06 | **Nature Medicine** | 机构可部署临床 agent 的参考架构：院内运营控制 + 多视角不确定性估计 + 选择性自主。检验科 Agent 项目最直接的对标文献——部署治理而非刷分，正是你项目的差异化主轴 |
| **2** | **GPN-Star: Predicting genome-wide functional constraints**（Ye, Benegas, Albors et al., PMID 42717086） | D / 10-07 | **Nature** | 正面回应"基因组 LM 打不过经典进化统计量"的根本质疑。功能约束预测是基因组 FM 的成色试金石，Nature 发表标志该问题进入主流视野，也是判断 D 方向论文价值的标尺 |
| **3** | **RL over Patient Trajectories for Clinical Reasoning in EHR Foundation Models**（Xiao, Zhang, Singh, Naumann, Poon, Gao, Microsoft Research, arXiv 2609.12277） | C×B / 10-05 | arXiv（预印本） | 把 RLHF 的偏好对齐替换为"患者轨迹上的临床决策对齐"——奖励来自真实预后而非人类偏好标注，结构性绕开医疗 RLHF 最大瓶颈。虽为预印本，但范式冲击力本周最强，C×B 天然交叉信号 |
| **4** | **Pathology-CoT: learning visual chain-of-thought agents from expert whole-slide image diagnosis behaviour**（Wang, Wu, Herndon, Elder et al., DOI 10.1038/s41551-026-01739-y, PMID 42498734） | F / 10-06 | **Nature Biomedical Engineering** | 用会话录制器无扰捕获病理专家阅片导航行为，转换为 agent 监督信号——"隐性知识数据化"新范式，可迁移到内镜/超声/手术及检验形态学复核流程 |
| **5** | **Toward generalizable prediction of cancer signal using a cell-free DNA language model**（Xu, Bao, Huang, Zhang et al., PMID 42285091） | D / 10-07 | **Cell Reports Medicine** | cfDNA 语言模型实现跨用途（早筛/MRD/治疗后分层）可泛化癌种信号预测——基因组 FM 从"基准刷分"走向临床可迁移性的关键一步，与检验科液体活检业务直接相邻 |

### 提名奖

| 论文 | 方向/日期 | 理由 |
|------|----------|------|
| **AI Safety Training Can be Clinically Harmful**（arXiv 2604.23445） | C / 10-06 | 安全对齐产生临床危害的机制证据：表面共情 0.91–1.00 vs 最高严重度治疗适宜性崩塌至 0.22–0.33，挑战"安全训练=医疗安全"默认假设 |
| **DobicVLM: GRPO + 临床程序化奖励对齐胸片报告生成**（arXiv 2607.18988） | C / 10-07 | 与昨日 reward hacking 论文形成"问题→修复"闭环：可验证的程序化奖励直击 rubric-RL 弱点 |
| **CipherGenome: Homomorphic Inference for Genomic MoE**（arXiv 2609.35883） | D / 10-06 | 基因组 FM 隐私推理白区：15.1B MoE 上实证单专家服务器 99.8% 重构基因组，module-LWE 同态外包协议 |
| **Guideline-grounded LLMs for genome-informed clinical recommendations from EHR**（Xin, Davis, Weng et al., JAMIA, DOI 10.1093/jamia/ocag171） | B / 10-06 | eMERGE 精准医学队列中指南锚定抽取基因组知情风险评估——临床 agent 与基因组医学的直接接口，与 10-05 妇瘤指南锚定 RAG 构成连续证据 |
| **CASE: From Given to Gathered Evidence**（arXiv 2609.39566） | B / 10-07 | 把临床 agent 评测从"给定证据推理"推向"主动搜集纵向证据"——agentic RAG 评测范式换代 |
| **CheckAMG**（bioRxiv 10.64898/2026.09.23.753886） | D×A / 10-05 | 基因组 LM 识别病毒辅助基因：病毒/细胞边界判定是 FM 表征优势场景，D→A 交叉样板 |

---

## 🔬 本周趋势分析

### 趋势 1：医学 RLHF 进入"奖励结构设计"时代 — 从标注瓶颈到可验证奖励

三天形成完整叙事链，指向同一结论：医学对齐的瓶颈不在偏好数据规模，而在奖励的可验证性与评测的临床效度。

| 论文 | 日期/方向 | 贡献 |
|------|----------|------|
| RL over Patient Trajectories（arXiv 2609.12277） | 10-05 / C | 奖励信号从人类偏好改为患者纵向轨迹上的决策正确性 |
| AI Safety Training Can be Clinically Harmful（arXiv 2604.23445） | 10-06 / C | 安全训练让模型表演性共情，高严重度下治疗适宜性崩塌 |
| Scoring Higher, Answering Worse: Reward Hacking in Rubric-Based RL（arXiv 2609.38847） | 10-06 / C | 加权 rubric 聚合可被补偿性 hack："分数更高、答案更差" |
| DobicVLM: 程序化奖励 + GRPO（arXiv 2607.18988） | 10-07 / C | 修复路径：临床规则可验证奖励替代主观偏好 |
| The Alignment Paradox in Infertility Care（JMIR, PMID 42766421） | 10-07 / C | 算法指标提升与临床决策效用脱钩的实证警示 |
| Multimodal Bidirectional DPO（IEEE JBHI, PMID 42348377） | 10-07 / C | 理解↔生成双向对齐，偏好优化在医学 MLLM 的系统化应用 |

**洞察**：与 W40 后段（10-02 DPO-Clin 实体级偏好、Clinical-R1 多维规则奖励）连读，2026 下半年医学对齐主流配方已清晰：**非人类/可验证奖励 × 细粒度（实体/token 级）信号 × 临床效度评测**。单纯成对偏好数据路线正在过时。
**行动建议**：检验科报告生成/审核的 RL 训练应优先设计程序化可验证奖励（单位、参考范围、危急值逻辑天然规则化），DobicVLM 的奖励工程可直接拆解复用。

### 趋势 2：临床 Agent 的"部署化"转折 — 从答题分数到系统工程

| 论文 | 日期/方向 | 贡献 |
|------|----------|------|
| On-premise medical AI agents（NatMed） | 10-06 / F | 院内治理 + 不确定性估计 + 选择性自主的参考架构 |
| Baichuan-M4（arXiv 2606.08982） | 10-06 / F | 工业界首个"连续照护"agent 技术报告：span 级奖励 + 训练部署一致 harness |
| CASE: Given→Gathered Evidence（arXiv 2609.39566） | 10-07 / B | 评测换代：证据主动搜集能力成为新基准 |
| ProMem-agent（IJMI, PMID 42784988） | 10-07 / B | 程序性记忆：纵向 ICU 轨迹压缩为可复用单元 |
| MedRSI（arXiv 2609.24838） | 10-07 / F | 临床对齐约束下的递归自进化 |
| MedPrune（arXiv 2610.06695） | 10-07 / F | 多模态多 agent 通信拓扑演化与剪枝 |
| RegLLM / AgentBoundary（arXiv, 10-05） | X | 监管感知评估 + 反事实安全评估（W41 开周即出，与 On-premise 遥相呼应） |

**洞察**：agent 能力来源正从人工设计转向自身经验（记忆 + 自进化），部署评估从"答对率"转向"监管边界内行为合规 + 不确定性可校准"。NatMed 背书的院内部署与 arXiv 上的自进化探索构成"现在能落地"与"下一代形态"的双轨。
**行动建议**：检验科 Agent 的架构叙事可直接引用 On-premise 论文的三要素（治理、不确定性估计、选择性自主）；评测设计从静态 QA 分数转向工作流能力（CASE 范式）。

### 趋势 3：基因组 FM 的"成色大考" — 评价标准整体迁移

| 论文 | 日期/方向 | 贡献 |
|------|----------|------|
| GPN-Star（Nature） | 10-07 / D | 功能约束预测正面回应"打不过进化统计量"质疑 |
| cfDNA language model（Cell Rep Med） | 10-07 / D | 临床液体活检场景的跨用途可迁移性 |
| PlantCAD2（Cell Genomics, PMID 42567165） | 10-07 / D | 扩展上下文 + 物种特异 + 单核苷酸分辨率的跨物种架构答案 |
| CipherGenome / Motif-Vocab / VANDAM（arXiv） | 10-06 / D | 信任栈（隐私推理）、生物学先验 tokenization、物理先验入训练目标 |
| LOAM / CheckAMG / Evo progressive FT / QAC 负结果 | 10-05 / D | 训练分布重设计 + 泄漏感知评估下领域先验仍然强大 |
| （W40 补编）Evo 2（Nature）、Mendel、GenoME（NAR）、癌症基因型 FM（Cancer Discovery） | 10-01~04 | 7B 超 40B、变异中心目标修复预训练缺陷、MoE 多组学整合 |

**洞察**：D 方向连续一周没有"刷分式"论文成为头条，取而代之的是四类问题：**能否超越进化方法**（GPN-Star）、**能否临床迁移**（cfDNA LM）、**能否合规部署**（CipherGenome 信任栈）、**监督信号是否命中真实错误模式**（Mendel/QAC）。这与 C 方向"奖励结构设计"殊途同归——竞争点从规模转向监督与评测的有效性。
**行动建议**：跟踪 D 方向论文时优先看评测协议（泄漏感知、进化基线、临床迁移），而非 leaderboard 分数；bioRxiv q-bio.GN 的 benchmark/负结果类论文值得 RSS 监控。

### 趋势 4：指南锚定（guideline-grounded）成为临床 RAG 的共识知识源

| 论文 | 日期/方向 | 贡献 |
|------|----------|------|
| Guideline-anchored RAG in gynecologic oncology（Gynecol Oncol, DOI 10.1016/j.ygyno.2026.07.005） | 10-05 / B | 三配置对照实证：指南 > 文献 > 无检索 |
| Guideline-grounded chatbots in rheumatology（J Med Syst, PMID 42830368） | 10-06 / B | 13 家中心 + 6 患者组织真实部署的多中心评估 |
| Guideline-grounded genome-informed recs from EHR（JAMIA） | 10-06 / B | eMERGE 队列：指南锚定抽取基因组知情临床建议 |
| CDTD/CTDT-Agent（Front Digit Health, PMID 42819271） | 10-07 / B | 来源锚定 + 多学科分工的整合照护工程范本 |

**洞察**：从单点实证（10-05）→ 多中心真实部署（10-06 双篇）→ 跨学科整合（10-07），三天内完成"知识源选型"共识沉淀：临床 RAG 的知识源应是结构化、可版本化的指南与共识，而非非结构化文献。对检验科场景尤其重要——检验指南/行业标准/专家共识是天然的锚定知识源。

---

## 🌐 白空间与交叉机会

### 🔴 高优先级（可直接用于检验科 Agent 项目）

1. **检验科 Agent × 指南锚定 RAG**：JAMIA eMERGE 的"基因组知情建议抽取"与检验报告解释、建议生成直接同构。落地动作：将检验医学指南/共识（含 CLSI、行业标准）构建为锚定知识源，复现 Guideline-anchored RAG 的三配置对照实验设计。
2. **可验证奖励 × 检验报告生成**：DobicVLM 的程序化奖励范式迁移到检验报告场景——单位、参考范围、危急值触发逻辑天然规则化，是 programmatic reward 的理想试验田；同时吸收 reward hacking 教训（协议级 rubric 设计）。
3. **mNGS 数据价值再挖掘**：MARM（BALF 宿主 CNV 肿瘤风险预测，PMID 42254492）证明同一 mNGS 测序数据可开辟全新任务空间——检验科存量 mNGS 数据的宿主信号挖掘是低垂果实。

### 🟡 中优先级（需要额外研发）

4. **实时幻觉探测**：calibrated hidden-state probes（JBI, PMID 42447946）在显式 FPR 约束下实现 token 级实时检测——检验报告解释 agent 的安全底座，从"生成后过滤"推进到"生成中探测"。
5. **Agent 记忆架构与评测**：ProMem-agent、GLoC-EHR、STAM 三线并进但缺标准评测——纵向检验结果解读（复查趋势、治疗响应）需要记忆分层设计，基准空白即是机会。

### 🟢 低优先级（长期跟踪）

6. **组学数据 discovery agents**（PLoS Comp Biol, PMID 42837398）：已发表组学数据的计算再利用管线；**基因组 FM 隐私推理**（CipherGenome）：若医院侧部署基因组 FM 需提前布局。

---

## 🧠 W40 补编速览（Oct 1–4，73 篇）

> W40 周报（Sep 28–30）编译后 Oct 1–4 未回填，本节基于 `.seen_papers.json` 与 4 期日报补编。⚠️ 去重说明：Mantis（10-01 同日 DOI+PMID 双条目）、CASE（10-04 与 10-07 跨周双条目）、CTDT-Agent（10-02 与 10-07 跨周双条目）在 tracker 中各占两键，实际唯一论文数为 70 篇。

| 日期 | 论文数 | 方向分布（A/B/C/D/F/X） | 核心主题 |
|------|--------|------------------------|---------|
| 10-01（四） | 18 | 3/2/3/4/2/4 | GenoME（NAR）、Mantis（PNAS 机理仿真 FM）、场景化偏好学习三件套 |
| 10-02（五） | 15 | 2/3/3/3/3/1 | DPO-Clin 实体级偏好、ConceptCLIP（NatBiomedEng）、PlantGFM（Adv Sci） |
| 10-03（六） | 15 | 2/3/2/3/3/3 | Evo 2（Nature）、癌症基因型 FM（Cancer Discovery）、AgentClinic（npj DM）、IFCC 检验 agentic AI 意见 |
| 10-04（日） | 25 | 2/3/3/2/3/12 | Mendel 变异中心目标、PathoBERT、StrokeAgent（超神经科医生 17pp）、可审计性成为一级设计目标 |

**补编 TOP 5**：
1. **Evo 2**（Nature, 10-03）— 全生命域基因组建模与设计，7B 超 40B，perplexity 作为评价指标失效
2. **Mantis**（PNAS, 10-01）— 纯机理仿真训练的传染病预测 FM，零样本部署新场景（数据驱动↔仿真驱动第三条路线）
3. **IFCC: From automation to agentic AI in laboratory medicine**（CCLM, 10-03）— 检验医学 agentic AI 的学会级路线图，你项目最权威的背景引用
4. **Mendel**（bioRxiv, 10-04）— 变异中心预训练目标修复整个领域的监督缺陷：SNV 等位基因预测 0.311→0.984
5. **AgentClinic**（npj DM, 10-03）— 工具型临床 agent 多模态评测基准，直接可借鉴到检验科 Agent 评测设计

**补编交叉信号**：①监督信号对齐贯穿 C/D 两方向（Mendel 变异中心目标 ↔ PrecepTron 医生级 judge / When Rubrics Fail）——竞争点在监督是否命中真实错误模式；②可审计性成为临床 agent 一级设计目标（StrokeAgent 证据链、Synthetic Hospital 溯源链、IFCC 验证门禁叙事）——与 W41 的 On-premise/CASE 直接衔接；③基因组 FM 双场景落地：低成本临床检测（cfDNA/ULP-WGS）与合成生物学设计（PlantGFM）。

---

## ⚠️ 问题与改进

| 问题 | 状态 | 影响 |
|------|------|------|
| W40 周报 Oct 1–4 未编译（周中编译后无回填机制） | ✅ 本次已补编 | 73 篇数据曾无周度综合视角 |
| 去重漏网 3 起：CASE（arXiv 前缀键 vs 裸键，跨方向 F/B）、CTDT-Agent（DOI 键 vs PMID 键，标题 CDTD/CTDT 变体）、Mantis（同日 DOI+PMID 双键） | 🟡 | tracker 键格式异构（`10.48550/arxiv.` 前缀、裸 arXiv ID、`PMID:` 前缀混存）；fuzzy title 闸门在标题变体下未触发。建议：写入端统一键规范化（arXiv→裸 ID、DOI→小写、PMID→`PMID:` 前缀），curation 打印候选池前强制两道闸门 |
| 预印本占比 42%（C/D/F 方向为主） | 🟡 | 符合"C 方向 PubMed 命中极少、arXiv 为主源"的务实策略；但用户偏好已出版——OpenAlex 周轮询发表版的机制需保持 |
| 10-05 tracker 方向标签与日报分区不一致（废水监测、DNA 条形码记 A，日报正文在 X） | 🟢 | 不影响检索与去重，仅统计口径差异 |

## 🎯 下周聚焦

### 📖 深度阅读
- **On-premise medical AI agents**（NatMed）— 逐层拆解：院内部署拓扑、不确定性估计方法、选择性自主的权限设计
- **RL over Patient Trajectories**（Microsoft Research）— 奖励信号构造细节与轨迹质量量化方法
- **GPN-Star**（Nature）— 功能约束预测的评测协议设置，作为 D 方向论文价值判断标尺

### 🔍 搜索策略微调
- C 方向：维持 arXiv 优先 + OpenAlex 周轮询发表版；新增精准子式 `"GRPO" OR "programmatic reward" OR "clinical decision-making"`
- A 方向：加 `"host-derived" OR "risk prediction" OR "analytical validation"` 限定（微生物组关联研究占宽泛查询 80%+）
- D 方向：bioRxiv q-bio.GN RSS 监控；`"genomic language model" + benchmark/evaluation` 设为独立子式
- 通用：候选 DOI 经 OpenAlex 反查验证元数据（本周多起 DOI-标题错配）

### 🔧 基础设施
- **去重键规范化补丁**：写入端统一键格式 + curation 打印池前强制两道闸门（本周 3 起漏网均为键格式/标题变体问题）
- **周报补编自动化**：周中编译（周三）后若周四 cron 未回填，下周编译时自动带上缺口区间（本次手动补编 Oct 1–4 的模式固化为规则）

---

*报告生成: 2026-10-07（周三中期编译）| 数据源: .seen_papers.json (1,155 条) | 下次编译: 2026-10-14（W42，含 W41 全周回填）*
