# 📊 周度研究总结 — 2026年第23周 (6/1–6/4)

> **生成时间**: 2026-06-04 | **覆盖天数**: 4/4
> **总收录**: 54 篇 | **🔥🔥🔥/🔥🔥 直接相关**: 38 篇 | **🔥🔥🔥 级**（多篇范式级创新）

---

## 一、本周统计

| 日期 | 收录 | 🔥🔥/🔥 直接相关 | 亮点 |
|------|------|-------------------|------|
| 6/1 (一) | 13 | 11 | 知识蒸馏+mNGS、DNA扩散模型(SFID≈真实DNA)、VLM经验记忆(MICCAI) |
| 6/2 (二) | 10 | 6 | Agent自我改进(GRASP 40%→89%)、AutoSci科学全生命周期、推理时报告优化 |
| 6/3 (三) | 16 | 12 | Agent化蛋白质LM(ICML Workshop)、视觉化DNA模型、主动证据搜索Agent |
| 6/4 (四) | 15 | 13 | 医学RAG基准、可学习DNA tokenization、World Model进入医学 |
| **合计** | **54** | **42** | **四大趋势+三空白地带** |

### 方向分布

| 方向 | 一 | 二 | 三 | 四 | 合计 | 趋势 |
|------|----|----|----|----|------|------|
| A. mNGS+AI | 1 | 0 | 2 | 2 | 5 | 📈 回升 |
| B. 临床Agent+RAG | 2 | 3 | 3 | 3 | **11** | 🔥🔥🔥 最活跃 |
| C. RLHF对齐 | 2 | 0 | 2 | 2 | 6 | 📈 过程级对齐崛起 |
| D. 蛋白质LM | 2 | 2 | 3 | 2 | 9 | 🔥🔥 Agent化+反思潮 |
| E. 基因组FM | 2 | 2 | 3 | 2 | 9 | 🔥🔥 tokenization+视觉化 |
| F. 多模态Agent | 3 | 2 | 2 | 2 | 9 | 🔥🔥 主动证据搜索 |
| X. 跨界发现 | 2 | 1 | 1 | 2 | 6 | 🔥 记忆架构+世界模型 |

---

## 二、🏆 本周 TOP 5 论文

| # | 论文 | 方向 | 日期 | 理由 |
|---|------|------|------|------|
| **1** | **AgentPLM** (2606.02386) | D | 6/3 | 🔥🔥🔥 范式级！首次将Agent范式引入蛋白质语言模型——从「被动预言机」变为「主动推理+迭代优化」。ICML 2026 Workshop，开辟"Agentic PLM"新子方向 |
| **2** | **OpticalDNA** (2602.02014) | E | 6/3 | 🔥🔥🔥 范式级！将DNA序列转化为视觉布局→Vision Transformer，完全绕开传统tokenization的固有限制。"视觉化基因组学"可能改写DNA FM路线图 |
| **3** | **D3LM** (2603.01780) | E | 6/1 | 🔥🔥🔥 范式级！首次系统研究DNA离散扩散模型，SFID=10.92逼近真实DNA(7.85)，碾压自回归(HyenaDNA=29.16)。DNA生成质量的历史性突破 |
| **4** | **GRASP** (2605.29668) | B | 6/2 | 🔥🔥🔥 临床Agent自我改进的标志性工作：门控+回归预算→gpt-oss-120b成功率40.6%→88.8% (+118%)。带安全保障的Agent自我进化 |
| **5** | **MedExpMem** (2601.xxxx) | F | 6/1 | 🔥🔥🔥 VLM诊断Agent的「经验记忆」——将诊断失败转化为成对鉴别笔记，MICCAI 2026 Early Accept。"经验外化"——第三种知识获取范式 |

### 提名奖

| 论文 | 理由 |
|------|------|
| **ClinSeekAgent** (2605.20176) | 多模态「主动证据搜寻」范式，临床Agent从被动RAG到主动检索的跃迁 |
| **AutoSci** (2605.31468) | 首个科学全生命周期Agent系统，Schema-Governed记忆架构有望成为生物医学Agent标准 |
| **DNAChunker** (2601.03019) | 可学习DNA tokenization——固定k-mer破坏功能性基序已是共识，此工作是解决方案 |
| **MedCausalX** (2603.23085) | 因果推理+自我反思引入医学诊断链，与VeriMap的海市蜃楼发现形成互补 |
| **SEMA-RAG** (2605.17101) | 三智能体自演化RAG + MA-RAG语义冲突RAG，两者在同月出现显示领域方向收敛 |

---

## 三、🔬 本周趋势分析

### 趋势 1：「Agent化」全面渗透生物医学AI —— 从工具到范式

本周最显著的元趋势。Agent不再是独立的工具类别，而是正在成为底层计算范式的扩展。

**证据链**：
- 6/1：SEMA-RAG（三智能体自演化RAG）、MA-RAG（语义冲突驱动多轮检索）→ Agent架构用于临床推理
- 6/2：GRASP（Agent自我改进，40%→89%）→ Agent不仅执行任务，还能自我进化
- 6/3：AgentPLM（Agent+蛋白质LM）→ Agent范式渗透进蛋白质设计；ClinSeekAgent（主动证据搜索）→ 从被动消费变为主动获取
- 6/4：异构多Agent医学框架（2605.29744）→ 通用协调器+专科推理器；Medical AI Scientist（2603.28589）→ 自主提出假设+设计实验

**交叉机会**：AgentPLM × GRASP 的自我改进机制 —— 蛋白质设计Agent不只是"生成序列"，而是"设计→评估→反思→再设计"的闭环。这正是 renji_mngs 的临床Agent也在追求的自我进化能力。

**白空间**：Agentified Bio-tools — 尚未出现将 AlphaFold / Rosetta / AutoDock 等经典生物信息学工具"Agent化"的统一框架。当前的工具调用（Tool-First Agent，2605.xxx）仍是函数级封装，缺少Agent级的推理编排。

---

### 趋势 2：从「输出对齐」到「过程对齐」—— 医学AI安全范式转型

本周多条线索指向同一个转向：对齐的关注点从最终输出向整个推理过程迁移。

**证据链**：
- 6/1：VeriMap（自验证海市蜃楼：生成器错误→验证器错误几率×57）→ 输出自验证不可靠
- 6/2：GRASP的回归预算（每次改进不破坏已有能力）→ 过程级安全保障
- 6/3：复合越狱攻击（RLHF抑制而非消除有害能力，组合后ASR 14%→71%）→ 单层输出防御失效；Medea的选择性拒绝+过度对齐谄媚检测→"自知对错"的过程能力
- 6/4：MedCausalX（显式因果图推理链）→ 不仅答案对，推理链也要因果一致；Multi-Agent Consensus Alignment（2605.30698）→ 多Agent讨论过程必须锚定于视觉证据

**交叉机会**：Process-Level Preference Optimization for Clinical Reasoning —— 将GRASP的回归预算 + MedCausalX的因果推理链 + VeriMap的外部验证器组合成临床Agent的安全推理栈。这可能是 renji_mngs 临床Agent下一步安全设计的核心架构。

**白空间**：多Agent系统的联合出错分析 —— 5个Agent达成共识但全错的临床风险 > 单Agent错误。尚无系统研究。

---

### 趋势 3：「视觉化」突破序列建模瓶颈 —— 基因组学遇见CV

本周出现了一种全新思路：将生物序列问题重新构建为计算机视觉问题，利用CV领域的成熟架构。

**证据链**：
- 6/1：D3LM（DNA离散扩散，6-mer非重叠分词）→ 仍在序列空间内突破
- 6/3：OpticalDNA（DNA序列→视觉布局→ViT）→ 完全跳出序列空间；GC-MoE（H&E图像+基因组引导→单细胞表达预测）→ 图像→基因表达的CV路径
- 6/4：DNAChunker（可学习tokenization）→ 仍属序列空间的最优方案，与OpticalDNA构成互补路径

**交叉机会**：OpticalDNA × mNGS —— 将病原体基因组的k-mer特征图转化为视觉输入，利用预训练ViT进行物种分类。这可能绕过传统比对工具的速度瓶颈。

**白空间**：DNA Vision Transformer的规模化规律尚未探索；与D3LM的结构化扩散生成能否结合（视觉化DNA→扩散生成新调控元件）？

---

### 趋势 4：DNA Tokenization 共识形成 —— 固定k-mer=瓶颈，可学习/视觉化=出路

本周E方向三篇论文从不同角度触及同一瓶颈，形成罕见的领域共识信号。

**证据链**：
- 6/1：AntigenLM（保留基因组8段结构→性能大幅提升）→ 证明「结构信息在tokenization中丢失」
- 6/3：OpticalDNA（视觉化绕过tokenization）→ 最激进的解决方案
- 6/4：DNAChunker（自适应可学习tokenization）→ 保留序列空间的最优解

**收敛判断**：固定k-mer破坏功能性基序已成为领域共识。三种解决方案形成光谱：DNAChunker（改良序列tokenization）→ D3LM的6-mer离散扩散（中间地带）→ OpticalDNA（完全跳出序列空间）。2026年下半年可能出现融合方案。

**白空间**：病原体特异性的DNA tokenization —— 现有工作关注人类基因组（功能元件），但mNGS场景关注物种间鉴别性k-mer、耐药基因边界。需要定制化研究。

---

## 四、白空间与交叉机会

### 🔴 高优先级 (可直接用于现有项目)

1. **renji_mngs × DNAChunker/Tokenization**: 病原体定制的可学习tokenization策略——关注物种间鉴别性k-mer（而非人类功能性基序），可作为mNGS基因组表征的预处理优化
2. **renji_mngs × GRASP的安全机制**: 将回归预算（regression budget）机制引入临床Agent的自我改进流程，确保每次RAG策略更新不退化
3. **harness agent × MedCausalX的因果推理链**: 将医生UI收集的RLHF数据构造为因果图标注（疾病→症状→检查→诊断）而非简单的偏好对

### 🟡 中优先级 (需要额外研发)

4. **Multi-modal Agent × OpticalDNA思路**: 将病原体基因组特征图 + 临床表现 + 检验指标全部视觉化后输入多模态VLM进行联合诊断——「视觉化全信息临床Agent」
5. **Process-Level RLHF for Clinical Reasoning**: 结合GRASP的门控 + MedCausalX的因果链 + VeriMap的跨模型验证，构建推理步骤级的安全对齐流水线
6. **AgentPLM × 湿实验验证闭环**: Agent化蛋白质LM + 自动化合成/筛选 = 「设计→实验→反馈→再设计」闭合循环

### 🟢 低优先级 (长期跟踪)

7. **World Model × mNGS 预警系统**: 流行病学世界模型 + 检验科mNGS实时数据 → 微观病原体预警
8. **Medical AI Scientist 的临床验证**: 自主假设→实验→论文闭环在真实临床场景的可行性验证

---

## 五、问题与改进

| 问题 | 状态 | 影响 |
|------|------|------|
| 6/4 cron delivery 错误: `no delivery target resolved for deliver=origin` | 🔴 需修复 | 当天日报未推送到飞书，用户未收到通知 |
| 方向A (mNGS+AI) 本周仅5篇，持续偏少 | 🟡 观察中 | 宏基因组FM方向可能处于产出间歇期，建议6月中旬补充搜索 |
| 周二报告存在统计不一致（header写12篇，统计表合计10篇） | 🟡 格式 | 应统一为统计表数字，header为概览估计值 |
| 周报推送延迟至周四晚 | 🟢 已改进 | 以往更晚，本周已在周四当天完成 |

---

## 六、下周聚焦

### 📖 深度阅读
- **AgentPLM (2606.02386)**：ICML 2026 Workshop — Agent与PLM的具体耦合方式、推理增强解码的实现细节
- **D3LM (2603.01780)**：离散扩散的scaling潜力——50M→500M+是否出现突变？训练细节和消融实验
- **GRASP (2605.29668)**：回归预算机制的数学细节——如何量化"不退化"保证

### 🔍 搜索策略微调
- 新增关键词: `"process-level" OR "step-level" alignment clinical reasoning 2026`
- 新增关键词: `"agentic" protein OR biology OR genomics tool integration 2026`
- 新增关键词: `"multi-agent failure" OR "collective hallucination" clinical diagnosis 2026`
- 关注 **ICML 2026 正式论文**（预计6月中旬公开）——多个workshop论文将升级
- 方向A补充搜索：`metagenomic foundation model pathogen detection 2026` + bioRxiv新提交

### 📅 会议日历
- ICML 2026 Workshops (多篇本周论文来源，正式论文即将公开)
- MICCAI 2026 Early Accept (MedExpMem已收录)

### 🔧 基础设施
- 修复 cron delivery 问题：`deliver=origin` 在当前飞书配置下无法解析 → 改用 `deliver=local` 或配置正确的飞书 target ID
- 统一日报统计数字规范（header概览 vs 统计表）

---

*报告结束 | 下次周报: 2026-06-11 (第24周)*
