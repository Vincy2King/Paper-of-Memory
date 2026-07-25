# RUMBA: Russian User Memory Benchmark

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.21447v1
- Published: 2026-07-23
- Updated: 2026-07-23
- Authors: Elizaveta Shevtsova, Inna Glebkina, Mark Baushenko, Pavel Gulyaev, Alena Fenogenova
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2607.21447v1

## One-Sentence Summary
The ability to handle long-term memory in LLMs is becoming increasingly critical, yet existing benchmarks remain English-centric and rely on aggregate retrieval metrics, failing...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The ability to handle long-term memory in LLMs is becoming increasingly critical, yet existing benchmarks remain English-centric and rely on aggregate retrieval metrics, failing to capture interactions between long-...

进一步看，论文的核心做法或实验重点可以概括为：To address this, we introduce RUMBA (Russian User Memory BenchmArk) - a new benchmark for long-term conversational memory that provides a fine-grained taxonomy of memory-centric question types and a unified...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
The ability to handle long-term memory in LLMs is becoming increasingly critical, yet existing benchmarks remain English-centric and rely on aggregate retrieval metrics, failing to capture interactions between long-range context, temporal information, and reasoning. To address this, we introduce RUMBA (Russian User Memory BenchmArk) - a new benchmark for long-term conversational memory that provides a fine-grained taxonomy of memory-centric question types and a unified methodology accounting for semantic type, session scope, temporal reasoning, and the explicitness of temporal expressions. RUMBA consists of timestamped user-assistant dialogues with QA pairs requiring retrieval, combination, and reasoning across sessions. While designed for Russian, we also provide an aligned English subset under the same methodology. We evaluate contemporary memory systems and long-context models, and show how RUMBA serves as a diagnostic tool to analyze model behavior across benchmark slices and identify strengths and failure modes of different memory mechanisms.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
