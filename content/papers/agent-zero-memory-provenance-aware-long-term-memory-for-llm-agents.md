# Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.29606v1
- Published: 2026-08-30
- Updated: 2026-08-30
- Authors: Ming Wu, Pengyuan Zhu
- Tags: agent, benchmark, conversation, episodic, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.29606v1

## One-Sentence Summary
Large language model (LLM) agents need durable, faithful memory of everything a user or organization has said and stored, yet most memory systems commit to a single organizing...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents need durable, faithful memory of everything a user or organization has said and stored, yet most memory systems commit to a single organizing structure (a fact store, a vector index,...

进一步看，论文的核心做法或实验重点可以概括为：We present Agent Zero Memory, a provenance-aware long-term memory system that distils a user's conversations, files, and connected sources into three parallel memory systems, each capturing a different facet of the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, episodic, long-term, retrieval
- 检索关键词命中：episodic memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language model (LLM) agents need durable, faithful memory of everything a user or organization has said and stored, yet most memory systems commit to a single organizing structure (a fact store, a vector index, or a knowledge graph) and inherit its blind spots. We present Agent Zero Memory, a provenance-aware long-term memory system that distils a user's conversations, files, and connected sources into three parallel memory systems, each capturing a different facet of the same history: an episodic Memory Events timeline that makes when and what changed first-class, an associative entity-event knowledge graph that links people and projects across sessions, and a semantic, curated, citation-locked Hierarchical Documentary Memory (HDM) of durable facts. A retrieval turn runs an intent gate (so self-contained turns add no latency), a source router, and three concurrent agentic searches, one per system, each a tool-using loop over hybrid (embedding + lexical) search under agent-controlled filters; their grounded, cited answers are integrated into one answer with a single confidence. We formalize the reading discipline: every learned item is a provenanced item carrying its origin, timestamp, and evidence pointer, and every answer is read under a citation lock, so it may cite only evidence its reader actually opened; fabrication is structurally excluded and the system abstains rather than guesses. On two public benchmarks the system sets a new state of the art: 95.60% on LongMemEval and 93.60% on LoCoMo, improving over the strongest prior systems by +0.73 and +1.10 points. A controlled study across eight backbone LLMs characterizes the accuracy-cost-latency frontier: accuracy varies by only 3.4 points while per-query cost varies by ~30x, with near-state-of-the-art quality at up to 20x lower cost per query, the signature of memory-driven, rather than model-driven, quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
