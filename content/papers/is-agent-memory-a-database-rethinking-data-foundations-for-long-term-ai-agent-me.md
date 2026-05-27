# Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.26252v1
- Published: 2026-05-25
- Updated: 2026-05-25
- Authors: Abdelghny Orogat, Essam Mansour
- Tags: agent, context, long-term, retrieval
- Categories: cs.AI, cs.DB
- URL: http://arxiv.org/abs/2605.26252v1

## One-Sentence Summary
Long-running AI agents need persistent memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running AI agents need persistent memory.

进一步看，论文的核心做法或实验重点可以概括为：Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, persistent memory
- 来源分类信息：cs.AI, cs.DB

## Abstract Snapshot
Long-running AI agents need persistent memory. Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions. Current agent memory systems and database paradigms treat memory as storage. They localize correctness at records, embeddings, or edges. Each supplies only some of the capabilities that long-term memory requires. The result is four recurring failure modes: unregulated growth, missing semantic revision, capacity-driven forgetting, and read-only retrieval. In our vision, long-term agent memory is a new data-management workload. Its correctness is a property of the state trajectory, not of individual records. We formalize this as Governed Evolving Memory (GEM). GEM replaces record-level database operations with four state-level operators: ingestion, revision, forgetting, and retrieval. Six correctness conditions govern how the state evolves. Three structural observations establish that no record-level system can satisfy these conditions, regardless of the storage model. We realize the abstraction in MemState, a prototype on a property-graph backend. MemState validates feasibility and exposes the gap to a native engine. We outline three research directions that define memory-centric data management as a workload.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
