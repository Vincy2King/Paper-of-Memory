# Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.04897v1
- Published: 2026-05-06
- Updated: 2026-05-06
- Authors: Joshua Adler, Guy Zehavi
- Tags: agent, conversation, retrieval
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2605.04897v1

## One-Sentence Summary
Extraction at ingestion is the wrong primitive for agent memory: content discarded before the query is known cannot be recovered at retrieval time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Extraction at ingestion is the wrong primitive for agent memory: content discarded before the query is known cannot be recovered at retrieval time.

进一步看，论文的核心做法或实验重点可以概括为：We propose True Memory, a six-layer architecture that shifts the center of the system from a storage schema to a multi-stage retrieval pipeline operating over events preserved verbatim.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
Extraction at ingestion is the wrong primitive for agent memory: content discarded before the query is known cannot be recovered at retrieval time. We propose True Memory, a six-layer architecture that shifts the center of the system from a storage schema to a multi-stage retrieval pipeline operating over events preserved verbatim. The full system runs as a single SQLite file on commodity CPU with no external database, vector index, graph store, or GPU. On LoCoMo (1,540 questions across 10 multi-session conversations), True Memory Pro reaches 93.0% accuracy (3-run mean) against 61.4% for Mem0, 65.4% for Supermemory, approximately 71% for Zep, and 94.5% for EverMemOS under a matched gpt-4.1-mini answer model. On LongMemEval (500 questions), True Memory Pro reaches 87.8% (3-run mean). On BEAM-1M (700 questions at the 1-million-token scale), True Memory Pro reaches 76.6% (3-run mean), above the prior published result of 73.9% for Hindsight. A 56-configuration ablation shows a 1.3-percentage-point spread within the top-performing configuration family.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
