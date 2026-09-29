# RoutePrism: Tracing Construction Order Effects in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34160v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Dong Xu, Zhangfan Yang, Jiantao Wu, Shipeng Zhang, Zexuan Zhu, Jiangqiang Li, Jun Zhang, Junkai Ji
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.34160v1

## One-Sentence Summary
Processing the same records in a different order can discard different evidence, yet endpoint accuracy alone cannot reveal what changed or whether it mattered.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Processing the same records in a different order can discard different evidence, yet endpoint accuracy alone cannot reveal what changed or whether it mattered.

进一步看，论文的核心做法或实验重点可以概括为：We introduce RoutePrism, a diagnostic protocol that builds memory twice from the same source pool in two processing orders, then traces which sources, compiled contexts, and answers differ.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Processing the same records in a different order can discard different evidence, yet endpoint accuracy alone cannot reveal what changed or whether it mattered. We introduce RoutePrism, a diagnostic protocol that builds memory twice from the same source pool in two processing orders, then traces which sources, compiled contexts, and answers differ. Because record content, timestamps, policy, and the answer model all stay fixed, any observed difference is localized to the memory construction step. A matched four-condition intervention tests whether a record displaced by reordering actually carried task-relevant evidence: restoring that single record recovers over 60 percentage points of lost accuracy, while substituting a non-supporting record of equal length does not. We evaluate the protocol on PersonaMem-32K (63 primary queries, 29 users) and 470 LongMemEval-S questions with histories spanning 38 to 62 sessions, replicating the core intervention across five answer models. Survivor selection, defined as the choice of which record a cluster retains, drives most source-level changes, while different memory policies (compaction, bounded recency, MemoChat-style summarization, A-MEM) produce distinct failure signatures at the source, context, and metadata layers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
