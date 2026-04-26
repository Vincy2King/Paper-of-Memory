# ENGRAM: Effective, Lightweight Memory Orchestration for Conversational Agents

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents
- Paper ID: openreview:qajz4UkgIw
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: Daivik Patel, Shrenik Patel
- Tags: agent, benchmark, context, conversation, episodic, long-term, retrieval
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=qajz4UkgIw

## One-Sentence Summary
Large language models (LLMs) deployed in user-facing applications require long-horizon consistency: the capacity to remember prior interactions, respect user preferences, and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models (LLMs) deployed in user-facing applications require long-horizon consistency: the capacity to remember prior interactions, respect user preferences, and ground reasoning in past events.

进一步看，论文的核心做法或实验重点可以概括为：However, contemporary memory systems often adopt complex architectures such as knowledge graphs, multi-stage retrieval, and operating-system–style schedulers, which introduce engineering complexity and reproducibility...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents
- 高亮主题命中：agent, benchmark, context, conversation, episodic, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
Large language models (LLMs) deployed in user-facing applications require long-horizon consistency: the capacity to remember prior interactions, respect user preferences, and ground reasoning in past events. However, contemporary memory systems often adopt complex architectures such as knowledge graphs, multi-stage retrieval, and operating-system–style schedulers, which introduce engineering complexity and reproducibility challenges. We present ENGRAM, a lightweight state-of-the-art memory system that organizes conversation into three canonical memory types—episodic, semantic, and procedural—through a single router and retriever. Each user turn is converted into typed memory records with normalized schemas and embeddings and persisted in a database. At query time, the system retrieves top-k dense neighbors per type, merges results with simple set operations, and provides relevant evidence as context to the model. ENGRAM attains state-of-the-art results on the LoCoMo benchmark, a realistic multi-session conversational question-answering (QA) suite for long-horizon memory, and exceeds the full-context baseline by 15 absolute points on LongMemEval, an extended-horizon conversational benchmark, while using only $\approx 1\%$% of the tokens. Our results suggest that careful memory typing and straightforward dense retrieval enable effective long-term memory management in language models, challenging the trend toward architectural complexity in this domain.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
