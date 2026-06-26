# Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.26511v1
- Published: 2026-06-25
- Updated: 2026-06-25
- Authors: Neeraj Yadav
- Tags: agent, benchmark, retrieval
- Categories: cs.CL, cs.AI, cs.ET, cs.LG
- URL: http://arxiv.org/abs/2606.26511v1

## One-Sentence Summary
Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time.

进一步看，论文的核心做法或实验重点可以概括为：When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CL, cs.AI, cs.ET, cs.LG

## Abstract Snapshot
Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates. We present MemStrata, a retrieval memory maintaining temporal validity. It stores facts like RAG, preserving static recall, but when a fact's value is contradicted, a deterministic (subject, relation, object) supersession rule retires the stale value in a bi-temporal ledger - with no similarity threshold and no LLM call. Across six benchmarks run locally with a 7B model, MemStrata ties RAG on static knowledge and reaches 0.95-1.00 accuracy on evolving knowledge (where RAG reaches 0.20-0.47). The central result is the stale-fact-error rate: when required to answer, RAG serves superseded values 15-40% of the time; MemStrata drives this to ~0%, a failure class RAG cannot avoid. MemStrata achieves this at retrieval latency (~2.1s) versus ~16-18s for LLM-reranking baselines. We release the harness, datasets, and a marker-free evaluation protocol for memory under knowledge evolution.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
