# LAM: Efficient Lossy Agent Memory Framework With A Retrieval-Score Error Bound

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32256v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Baixi Sun, Le Chen, Anjir Ahmed Chowdhury, Xiaolong Ma, Chih-Hsuan Yang, Mingze Xia, Syed Zawad, Sheng Di, Rajkumar Kettimuthu, Huihuo Zheng, Rajeev Thakur, Venkatram Vishwanath, Feng Yan
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.32256v1

## One-Sentence Summary
Agent memory grows as agents read inputs, reason, and call tools.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory grows as agents read inputs, reason, and call tools.

进一步看，论文的核心做法或实验重点可以概括为：Longer histories increase inference cost and eventually exceed the context window.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Agent memory grows as agents read inputs, reason, and call tools. Longer histories increase inference cost and eventually exceed the context window. LLM-based summarization reduces this history but adds latency and provides no explicit bound on information loss. We propose LAM, a Lossy Agent Memory system with three components: a deterministic deduplication rule with a substitution bound on retrieval scores - a bound on score perturbation, not a certificate of unchanged ranking; a memory manager that preserves the cached prefix and overlaps compaction with inference; and a performance model that estimates compaction costs before deployment. On 600 agent trajectories, LAM removes 22.47% of observation tokens while retaining 99.984% of the measured gold-patch evidence. At a fixed deletion set, the performance model predicts a 71.4x-91.6x end-to-end speedup from removing records before prefill instead of deleting them from a prefilled context. That benefit comes from the schedule rather than the rule and applies to any prefix-preserving test.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
