# Stashbird: Efficient Speaker-Indexed Memory for Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34242v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Chidera Biringa, Lucas Yannul, Xiaowen Wang, Marco Ayala, Nicholas Yi, Alex Moyse, Nishant Manchanda, Vivek Gupta
- Tags: agent, benchmark, conversation, episodic, long-term, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2609.34242v1

## One-Sentence Summary
AI agents require memory that preserves information across user-agent exchanges, user-to-user conversations, and group conversations with or without agent participation, while...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI agents require memory that preserves information across user-agent exchanges, user-to-user conversations, and group conversations with or without agent participation, while supporting updates as evidence changes or...

进一步看，论文的核心做法或实验重点可以概括为：We present Stashbird, an agent memory system that links source episodes to derived memory state through explicit provenance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, episodic, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
AI agents require memory that preserves information across user-agent exchanges, user-to-user conversations, and group conversations with or without agent participation, while supporting updates as evidence changes or is removed. We present Stashbird, an agent memory system that links source episodes to derived memory state through explicit provenance. Stashbird organizes memory into episodic records, semantic relations, community summaries, and persisted graph state, with lifecycle operations for incremental updates and episode-level deletion. We evaluate question-answering accuracy and model-facing workload across four long-term memory benchmarks. On LoCoMo, Stashbird uses 76.4x fewer ingestion prompt tokens than Graphiti. Compared with reproduced Hindsight on the same benchmark, it uses 8.1x fewer retrieval prompt tokens, with accuracy 1.6 percentage points lower. It achieves higher accuracy than Hindsight on LongMemEval-S and GroupMemBench and comparable accuracy on EverMemBench.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
