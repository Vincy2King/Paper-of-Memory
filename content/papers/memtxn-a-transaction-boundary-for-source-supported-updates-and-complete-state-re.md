# MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.27834v1
- Published: 2026-07-30
- Updated: 2026-07-30
- Authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia
- Tags: agent, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.27834v1

## One-Sentence Summary
Persistent memory lets long-running large language model agents reuse information across sessions and tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory lets long-running large language model agents reuse information across sessions and tasks.

进一步看，论文的核心做法或实验重点可以概括为：Yet errors in writable memory can persist and corrupt future behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Persistent memory lets long-running large language model agents reuse information across sessions and tasks. Yet errors in writable memory can persist and corrupt future behavior. Existing systems improve storage and retrieval, but they do not provide a transaction boundary for reliable updates and recovery. We therefore propose MemTxn, a governance layer outside the answer model. MemTxn verifies whether an update is supported by its source. It also selects the visible version when facts conflict and restores the application-visible state after a fault. The system uses Ordered PatchTest to validate writes, a Temporal Resolver to select versions, and a durable snapshot journal to recover state. On an item-disjoint audit, MemTxn accepts all 60 supported originals and rejects all 179 hard negatives. Under persistent multi-key faults on LongMemEval-S and LoCoMo states, it restores the complete declared active map without knowing the actual physical write set. On MemoryAgentBench FactConsolidation, MemTxn achieves the highest average F1 across all twelve answer-model configurations. It outperforms Dense by 17.06--24.07 points in five representative settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
