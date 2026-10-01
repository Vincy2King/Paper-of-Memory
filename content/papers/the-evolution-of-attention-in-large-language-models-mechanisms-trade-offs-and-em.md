# The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.39661v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Zhentao Tan, Jingyi Shen, Yanbo Li, Yao Liu, Yue Wu, Jieping Ye
- Tags: compression, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.39661v1

## One-Sentence Summary
Self-attention gives LLMs fine-grained, query-dependent access to context, but dense token interactions incur quadratic prefill cost and a key--value cache growing with context...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Self-attention gives LLMs fine-grained, query-dependent access to context, but dense token interactions incur quadratic prefill cost and a key--value cache growing with context length.

进一步看，论文的核心做法或实验重点可以概括为：Research thus spans explicit-memory compression, sparse access, recurrent state construction, structured state dynamics, and heterogeneous mechanism composition.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：memory compression, persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Self-attention gives LLMs fine-grained, query-dependent access to context, but dense token interactions incur quadratic prefill cost and a key--value cache growing with context length. Research thus spans explicit-memory compression, sparse access, recurrent state construction, structured state dynamics, and heterogeneous mechanism composition. This survey analyzes these developments as model-internal contextual memory. We introduce a five-dimensional lens---Memory Representation, Memory Update, Access, Readout, and Integration---describing what is represented, how it changes, what is query-eligible, how it is read, and how readouts form outputs. This lens compares overlapping research lines without imposing one computational model. We reconstruct mechanism-level developments and architectural adoption using 59 release-level records from 14 major model lineages and 11 high-performing open-weight endpoints. First, explicit-memory and recurrent-state methods retain distinct interfaces but increasingly control overlapping memory functions. Second, heterogeneous architectures increasingly coordinate across network depth: layer-wise composition distributes complementary memory processing across representational stages, while cross-layer reuse carries selected memory and routing artifacts forward. Depth thus becomes a dimension along which contextual memory is constructed and managed. Third, these developments motivate a stateful multidimensional memory-routing hypothesis: persistent memory is organized across temporal scope, network depth, substrate type, and representation granularity, while coordinated Sparse Write and Sparse Read determine what is maintained and what contributes to each query. Overall, efficient sequence architecture design increasingly concerns the organization, lifecycle, and selective use of contextual memory rather than an isolated Attention operator.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
