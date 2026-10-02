# MemFit: Efficient Long-Term Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.00872v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Mitchell Piehl, Muchao Ye
- Tags: agent, benchmark, compression, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.00872v1

## One-Sentence Summary
Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications.

进一步看，论文的核心做法或实验重点可以概括为：Current memory systems rely on LLM agents to organize and consolidate memory, resulting in costly, inefficient write operations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications. Current memory systems rely on LLM agents to organize and consolidate memory, resulting in costly, inefficient write operations. To address this limitation, we propose MemFit, a long-term memory system for conversational agents that reduces the cost and latency of memory operations. Unlike existing systems that rely on expensive LLM calls for memory construction or discard surface-level details through compression, MemFit stores each turn verbatim in an append-only store with near-instantaneous, LLM-free insertion, indexing turns with segment summaries rather than replacing them. Additionally, MemFit uses an LLM-free, multi-path retrieval strategy that combines lexical and semantic signals with cross-encoder reranking over caption- augmented episodes in both textual and multimodal settings. Empirical results on three widely used benchmarks, LoCoMo, MemGallery, and LongMemEval-S, show that MemFit achieves state-of-the-art performance while reducing memory construction time and cost several-fold, providing a scalable and efficient solution for persistent agentic memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
