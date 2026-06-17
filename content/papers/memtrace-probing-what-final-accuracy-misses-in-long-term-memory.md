# MemTrace: Probing What Final Accuracy Misses in Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.17328v1
- Published: 2026-06-15
- Updated: 2026-06-15
- Authors: Xianxuan Long, Zhikai Chen, Shenglai Zeng, Shouren Wang, Kai Guo, Jiliang Tang
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.17328v1

## One-Sentence Summary
LLM agents increasingly maintain long-term memory of user facts across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents increasingly maintain long-term memory of user facts across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Yet such memory is usually evaluated by aggregating accuracy over question rows or episodes.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM agents increasingly maintain long-term memory of user facts across sessions. Yet such memory is usually evaluated by aggregating accuracy over question rows or episodes. Because this approach scores question rows independently, even when several questions probe the same fact, it cannot show how that fact behaves as conditions change. We introduce MemTrace, a benchmark whose unit of measurement is the knowledge point: a single typed fact about the user, rather than an individual question. MemTrace probes each fact along three controlled dimensions: memory age, defined by how many sessions ago the fact appeared in the history; question type, covering current state, earlier state, and trajectory of change; and evidence condition, covering present, missing, and contradicted-by-false-premise settings. Evaluating 13 memory-system configurations across four paradigms, we find that similar pooled accuracy hides different failures: recovering a fact's current and earlier states does not imply tracking how it changed, and safe abstention does not imply correcting a false premise. The dominant bottleneck is evidence use, not retrieval: when systems fail, the evidence was retrievable 10 times more often than it was missing. These results suggest that improving long-term memory requires better use of reachable evidence, not simply more storage or retrieval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
