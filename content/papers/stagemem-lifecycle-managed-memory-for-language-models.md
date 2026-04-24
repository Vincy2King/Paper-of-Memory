# StageMem: Lifecycle-Managed Memory for Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.16774v1
- Published: 2026-04-18
- Updated: 2026-04-18
- Authors: Jiarui Han
- Tags: long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2604.16774v1

## One-Sentence Summary
Long-horizon language model systems increasingly rely on persistent memory, yet many current designs still treat memory primarily as a static store: write an item, place it into...

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon language model systems increasingly rely on persistent memory, yet many current designs still treat memory primarily as a static store: write an item, place it into memory, and retrieve it later if needed.

进一步看，论文的核心做法或实验重点可以概括为：We argue that this framing does not adequately capture the practical memory-control problem in deployed LLM systems.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-horizon language model systems increasingly rely on persistent memory, yet many current designs still treat memory primarily as a static store: write an item, place it into memory, and retrieve it later if needed. We argue that this framing does not adequately capture the practical memory-control problem in deployed LLM systems. In realistic settings, the difficulty is often not merely forgetting useful information, but retaining too many uncertain items, forgetting important content in the wrong order, and giving users little trust in what will persist over time. We propose StageMem, a lifecycle-managed memory framework that treats memory as a stateful process rather than a passive repository. StageMem organizes memory into three stages -- transient, working, and durable memory -- and models each item with explicit confidence and strength. This separates shallow admission from long-term commitment: information may first be written at low cost and only later be promoted, retained, updated, or evicted as evidence and pressure evolve. Under controlled pressure regimes, this decomposition helps preserve late-important content while keeping memory burden and deeper-tier pollution more controlled. Adapted external tasks provide boundary evidence that the same schema remains compatible with stronger retrieval structure outside pure synthetic control. We present StageMem as a principled decomposition of the memory-control problem for language model systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
