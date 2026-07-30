# A Graph-Native Bitemporal Memory Store for Conversational AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.26520v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Alp Niksarli, Gopesh Baheti
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: cs.DB, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2607.26520v1

## One-Sentence Summary
Conversational AI agents commonly lack persistent memory across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational AI agents commonly lack persistent memory across sessions.

进一步看，论文的核心做法或实验重点可以概括为：The obvious fixes like injecting full chat histories into the context window, or delegating to a third-party memory service, either exhaust the model's context budget or send personal data through infrastructure the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.DB, cs.AI, cs.IR

## Abstract Snapshot
Conversational AI agents commonly lack persistent memory across sessions. The obvious fixes like injecting full chat histories into the context window, or delegating to a third-party memory service, either exhaust the model's context budget or send personal data through infrastructure the user does not control. We describe a memory store that avoids both problems: an agent-local Neo4j property graph augmented with HNSW vector indexes and a full bitemporal data model. Each memory is stored as an immutable identity node linked to versioned content nodes carrying two closed-open time intervals: valid time (when the fact was true in the world) and transaction time (when the database recorded it). This design supports point-in-time semantic retrieval without physically overwriting history. Semantic edges between related memories are maintained automatically at write time using cosine similarity over 1024-dimensional embeddings. We evaluate the system on LongMemEval, a 500-question benchmark spanning six question types designed to stress long-term memory. Across 60 sampled questions, the current-state semantic search path achieves 46.7% R@10 overall, rising to 80% on knowledge-update questions. The time-travel path yields 80% R@10 on knowledge-update but decreases recall on temporal-reasoning questions (50% to 37.5%), a consequence of post-filter dilution that points directly to a concrete design improvement. We discuss what these results reveal about the limits of pure retrieval for different question types and what each failure mode suggests for future work.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
