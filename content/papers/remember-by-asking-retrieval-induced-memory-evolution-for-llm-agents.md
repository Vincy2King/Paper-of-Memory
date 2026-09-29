# Remember by Asking: Retrieval-Induced Memory Evolution for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34438v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Wanqi Zhou, Jiawei Lu, Yang Wang, Zhaolong Xing, Zhen Chen, Ai Han, Haoyue Shi
- Tags: agent, compression, context, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.34438v1

## One-Sentence Summary
Long-term memory is essential for language agents to maintain coherent and effective behavior over extended, multi-session interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for language agents to maintain coherent and effective behavior over extended, multi-session interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems mainly use retrieval at read time, while write-time memory formation still relies on direct extraction or compression.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term memory is essential for language agents to maintain coherent and effective behavior over extended, multi-session interactions. Existing memory systems mainly use retrieval at read time, while write-time memory formation still relies on direct extraction or compression. However, when future information needs are unknown, compressing an entire interaction in one pass can overlook locally important details that may matter later. To this end, we introduce RIME, a retrieval-induced memory framework that shifts memory construction from monolithic compression toward evidence-centered integration. RIME uses generic self-questions to retrieve focused dialogue evidence and grounds memory formation in both the retrieved evidence and relevant historical memories, which are jointly reconciled into an evolving memory bank with temporal and provenance information. At inference time, compressed memory serves as the primary rather than the sole source of evidence: when it cannot support an answer, RIME retrieves relevant source dialogue together with its local context to recover information omitted during memory formation, without resorting to full-history processing. Extensive experiments on LoCoMo with Qwen3-235B-A22B and GPT-5.6 Sol show that RIME consistently achieves the best performance across all three quality metrics among the compared methods, while requiring substantially fewer query-time LLM tokens.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
