# Stashbird: Episode-Grounded Lifecycle Reconciliation for Conversational Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34242v2
- Published: 2026-09-28
- Updated: 2026-10-17
- Authors: Chidera Biringa, Lucas Yannul, Xiaowen Wang, Marco Ayala, Nicholas Yi, Alex Moyse, Nishant Manchanda, Vivek Gupta
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2609.34242v2

## One-Sentence Summary
AI agents require memory that remains consistent as conversational evidence changes.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI agents require memory that remains consistent as conversational evidence changes.

进一步看，论文的核心做法或实验重点可以概括为：We present Stashbird, an episode-grounded memory system that uses provenance to reconcile derived graph and retrieval state during updates and deletion.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
AI agents require memory that remains consistent as conversational evidence changes. We present Stashbird, an episode-grounded memory system that uses provenance to reconcile derived graph and retrieval state during updates and deletion. Repeated evidence extends support, corrections supersede prior active relations, and deletion removes unsupported state while preserving relations with remaining support. Under fixed semantic decisions, reconciliation produces correct final states in all 20 update sequences, compared with eight without reconciliation, and satisfies the defined checks across 263 deletion interventions. Across four long-term memory benchmarks, Stashbird achieves competitive question-answering accuracy and strong model efficiency. On LoCoMo, it uses 76.4x fewer ingestion prompt tokens than Graphiti and 8.1x fewer retrieval prompt tokens than reproduced Hindsight

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
