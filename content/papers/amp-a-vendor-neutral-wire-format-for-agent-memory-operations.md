# AMP: A Vendor-Neutral Wire Format for Agent Memory Operations

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.01138v1
- Published: 2026-05-31
- Updated: 2026-05-31
- Authors: Thamilvendhan Munirathinam
- Tags: agent, benchmark, context, episodic, long-term
- Categories: cs.CR, cs.AI, cs.DC
- URL: http://arxiv.org/abs/2606.01138v1

## One-Sentence Summary
Agent-memory frameworks - mem0, Letta/MemGPT, Cognee, Zep/Graphiti, MemoryOS, MemTensor - each ship their own SDK, storage layout, and operational vocabulary.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent-memory frameworks - mem0, Letta/MemGPT, Cognee, Zep/Graphiti, MemoryOS, MemTensor - each ship their own SDK, storage layout, and operational vocabulary.

进一步看，论文的核心做法或实验重点可以概括为：There is no shared wire format: every integration is bespoke, every migration rebuilds memory from scratch, and no framework ships a governance surface that lets a human review writes before they enter long-term storage.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI, cs.DC

## Abstract Snapshot
Agent-memory frameworks - mem0, Letta/MemGPT, Cognee, Zep/Graphiti, MemoryOS, MemTensor - each ship their own SDK, storage layout, and operational vocabulary. There is no shared wire format: every integration is bespoke, every migration rebuilds memory from scratch, and no framework ships a governance surface that lets a human review writes before they enter long-term storage. We present memorywire, a JSON-Schema 2020-12 wire format for five memory operations (remember, recall, forget, merge, expire) over four memory types (semantic, episodic, procedural, emotional), with a MemoryStore interface, a fan-out router, and an optional HITL governance channel. We describe an open-source reference implementation with five backend adapters (sqlite-vec, mem0, Letta, Cognee, pgvector); a microbenchmark on a 100-fact / 50-query labelled corpus achieving recall@5 = 1.000 on the 42 labelled queries with ingest p50 = 37.8 ms and recall p50 = 40.6 ms; an adversarial-fusion experiment showing Reciprocal Rank Fusion holds recall@5 = 1.000 across a 1-of-N rank-0 injection sweep (K in {0,5,...,50}) where max fusion collapses to 0.500 with 80% leak at K >= 5; and a 16-scenario cross-adapter conformance suite passing 68 of 80 cells with zero failures. The contribution is not a new algorithm; it is a packaging of established components (RRF, FSMs, STM/LTM consolidation, diff-and-approve workflows) into a venue-neutral protocol with an empirically validated reference, positioned to compose with the Model Context Protocol rather than compete with it.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
