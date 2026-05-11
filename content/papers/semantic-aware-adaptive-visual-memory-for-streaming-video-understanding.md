# Semantic-Aware Adaptive Visual Memory for Streaming Video Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.07897v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Hang Wu, Sherin Mary Mathews, Yujun Cai, Ming-Hsuan Yang, Yiwei Wang
- Tags: compression, long-term, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2605.07897v1

## One-Sentence Summary
Online streaming video understanding requires models to process continuous visual inputs and respond to user queries in real time, where the unbounded stream and unpredictable...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Online streaming video understanding requires models to process continuous visual inputs and respond to user queries in real time, where the unbounded stream and unpredictable query timing turn memory management into...

进一步看，论文的核心做法或实验重点可以概括为：Existing methods typically compress visual tokens via visual similarity heuristics, or augment compression with KV-cache-level retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Online streaming video understanding requires models to process continuous visual inputs and respond to user queries in real time, where the unbounded stream and unpredictable query timing turn memory management into a central challenge. Existing methods typically compress visual tokens via visual similarity heuristics, or augment compression with KV-cache-level retrieval. However, compression decisions rarely incorporate semantic signals, and retrieval is often added after compression is finalized, making the two stages hard to coordinate. We present SAVEMem, a training-free dual-stage framework that brings semantic awareness into memory generation and lets the retrieval scope adapt per query. In Stage~1, SAVEMem builds a three-tier streaming memory online under a constant memory budget. A fixed pseudo-question bank provides a lightweight semantic prior, so that long-term retention is shaped by semantic salience rather than visual similarity alone. In Stage~2, SAVEMem performs query-aware retrieval over this memory. An anchor-conditioned recency gate adapts the retrieval scope from short-term to mid- and long-term memory based on whether the query targets the present or the distant past. Within this scope, late interaction between query and memory tokens selects candidate frames for answering. Applied to Qwen2.5-VL without training, SAVEMem improves the OVO-Bench overall score from 52.27 to 62.69 and yields consistent gains on StreamingBench and ODV-Bench, while reducing peak GPU memory by 48\% at 128 frames over the backbone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
