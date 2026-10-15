# STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.19386v1
- Published: 2026-10-14
- Updated: 2026-10-14
- Authors: Guanhua Zhu, Hanwen Li, Zhi Wei, Mengnan Du, Chenxi Yuan
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.19386v1

## One-Sentence Summary
Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards.

进一步看，论文的核心做法或实验重点可以概括为：Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undifferentiated pool indexed by embedding similarity, with no typed abstraction hierarchy.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards. Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undifferentiated pool indexed by embedding similarity, with no typed abstraction hierarchy. They never forget or deduplicate, and are prone to negative transfer, where a superficially similar but directionally opposite experience is recalled and its concrete steps are copied verbatim, actively harming the agent. We introduce STRATA, a structured, outcome-grounded, self-maintaining memory that organizes experience into a three-layer graph of atomic skills and code snippets, task workflows and generalized meta-frameworks, connected by typed edges. STRATA maintains itself through five mechanisms sharing one similarity geometry: a multi-dimensional similarity that scores retrieval by operation and target; a typed reflector crystallizing procedures from successes and pitfalls from failures; community detection that induces meta-frameworks; pressure-triggered garbage collection with articulation-point protection; and contrast edges that flag confusable, direction-opposite experiences. Across four interactive benchmarks (AppWorld, WebArena, ALFWorld, ScienceWorld), two frozen backbones and seven baselines, STRATA attains the best average score while simultaneously using the lowest latency and fewest environment steps of any memory-augmented method, and 44% fewer lines of injected memory than the most context-hungry baseline. We isolate two failure modes of prior memories: single-level memory degrades sharply as the task set grows, and single-level concrete memories suffer catastrophic negative transfer, which contrast edges repair, lifting ScienceWorld from 78.7 to 96.7 within the same system.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
