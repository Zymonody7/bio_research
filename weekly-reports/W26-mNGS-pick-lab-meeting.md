# 🔬 组会汇报推荐：mNGS 方向最佳论文

## 📄 推荐论文

**Artificial intelligence in clinical metagenomic pathogen detection: A critical review of pipeline integrations, challenges, and future directions**

| 字段 | 内容 |
|------|------|
| **作者** | Jiayue Dai, Xinru Tan, Jun Ma |
| **年份** | 2026 |
| **期刊** | Methods in Microbiology |
| **DOI** | [10.1016/j.mimet.2026.107592](https://doi.org/10.1016/j.mimet.2026.107592) |
| **关键词** | mNGS, AI, pathogen detection, metagenomic, pipeline integration |
| **收录日期** | 2026-06-23 |

---

## 🎯 为什么选这篇？

1. **综述性质 = 组会最佳选题**：一篇综述能让全组快速建立共同知识背景，比单篇 research paper 更适合 group meeting
2. **高度对口**：直接覆盖「AI × mNGS 病原体检测」的流水线集成、挑战和未来方向，与我们的 mNGS + LLM 路线完全契合
3. **2026 年发表**：最新综述，涵盖到 2025-2026 年的最新进展
4. **DOI 可查**：发表在 Methods in Microbiology，有正式 DOI，方便组员提前阅读

---

## 📋 组会汇报大纲（建议 15-20 分钟）

### 一、背景与动机（3 分钟）
- mNGS 在临床病原体检测中的价值：无偏倚、广谱、快速
- 当前 mNGS 临床应用的瓶颈：
  - 计算需求大（TB 级数据处理）
  - 参考数据库偏差（有限的参考基因组）
  - 解读困难（大量候选病原体，需临床判断）

### 二、AI 在 mNGS 流水线中的集成方式（5 分钟）
- **序列质控与预处理**：AI 辅助的去宿主、质量过滤
- **物种分类与注释**：深度学习分类器（如 CNN/RNN 用于 read-level 分类）
- **耐药基因检测**：AI 预测耐药表型（参考 FUNGAR 等工作）
- **临床解读与报告生成**：LLM 辅助的自动化报告（这是我们最感兴趣的环节）

### 三、关键挑战（5 分钟）
1. **数据库偏差**：参考基因组的不完整性导致假阴性
2. **计算可扩展性**：从实验室到临床的 scaling 挑战
3. **假阳性控制**：低丰度病原体的检测特异性
4. **可解释性**：AI 决策过程的临床可信度
5. **标准化**：不同平台/流程的结果可比性

### 四、与我们工作的关联（3 分钟）
- 我们的 mNGS + LLM 路线正好处于这篇综述提出的「临床解读与报告生成」环节
- 综述中提到的数据库偏差问题，可以通过 LLM 的世界知识部分弥补
- 可以讨论：LLM 是否能作为 mNGS 流水线的「最后一公里」——从候选病原体列表到临床可操作的诊断报告

### 五、讨论问题（2 分钟）
1. 综述中提到的 AI 集成方案，哪些最适合我们的 mNGS + LLM 架构？
2. 我们是否可以在 renji_mngs 项目中引入综述提到的某些 AI 模块？
3. mNGS 数据直接输入 LLM（而非传统流水线）的可行性如何？

---

## 🔗 相关论文（组会可延伸讨论）

| 论文 | 方向 | 关联点 |
|------|------|--------|
| FUNGAR (2602.16728) | A | AI 从 mNGS reads 检测抗真菌耐药突变 |
| AI-Augmented Metagenomic Diagnostic (6/25) | A | AI 增强的 mNGS 诊断流水线 |
| MedRAG-Agent (6/23) | B | 多智能体 + KG 增强的医学 RAG |
| MedBeads (2602.01086) | B | Agent 原生不可变数据基础设施 |

---

*准备时间: 2026-06-25*
*来源: 周报 W26 mNGS 方向论文池*
