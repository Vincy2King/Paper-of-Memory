# Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.02070v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Arman Behnam, Binghui Wang
- Tags: context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.02070v1

## One-Sentence Summary
Memory-augmented large language models must decide which memories to retain, and recent systems do so by estimating each memory's effect on task performance.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented large language models must decide which memories to retain, and recent systems do so by estimating each memory's effect on task performance.

进一步看，论文的核心做法或实验重点可以概括为：However, these estimates rely entirely on retrieved memories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented large language models must decide which memories to retain, and recent systems do so by estimating each memory's effect on task performance. However, these estimates rely entirely on retrieved memories. When a memory is never retrieved, store-level interventions produce identical outcomes, leaving its utility unidentified. This is a retrieval-level positivity violation, invisible to diagnostics that examine only memory operations. We introduce Causal Memory Policy (CMP), a causal framework that restores identification by intervening on retrieval itself, reserving a fixed number of context slots for memories sampled with known propensities. CMP estimates memory utility by self-normalized inverse propensity weighting under a balanced assignment design. We prove the causal factorization of memory utility through retrieval, the unbiasedness and exact variance of the estimator, and the optimal decision rule under irreversible operations. Empirically, identification fails for 54% of required memories on LongMemEval and 67% on LoCoMo, and the failure persists in a deployed memory system. CMP improves discrimination between required and non-required memories from 0.54 to 0.66 AUC. Finally, we show that identified memory utility alone is insufficient for retention decisions: per-query utility reaches 0.78 AUC on the query for which it is estimated, yet no aggregation available to a retention policy predicts a memory's value on unseen queries. Code is available at: https://anonymous.4open.science/r/cmp-release-D0C3/.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
