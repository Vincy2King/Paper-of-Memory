# MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.01386v1
- Published: 2026-05-02
- Updated: 2026-05-02
- Authors: Hung Pham Van, Nguyen Manh Hieu, Khang Pham Tran Tuan, Nam Le Hai, Linh Ngo Van, Nguyen Thi Ngoc Diep, Trung Le
- Tags: agent, benchmark, compression, context, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.01386v1

## One-Sentence Summary
Large Language Models (LLMs) lack persistent memory for long-term personalized conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) lack persistent memory for long-term personalized conversations.

进一步看，论文的核心做法或实验重点可以概括为：Existing graph-based memory systems suffer from information dilution, absent provenance tracking, and uniform retrieval that ignores query context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, conversation, long-term
- 检索关键词命中：memory retrieval, persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large Language Models (LLMs) lack persistent memory for long-term personalized conversations. Existing graph-based memory systems suffer from information dilution, absent provenance tracking, and uniform retrieval that ignores query context. We introduce MemORAI (Memory Organization and Retrieval via Adaptive Graph Intelligence), a framework that integrates three innovations: selective memory filtering with dual-layer compression to retain user-persona-relevant content, a provenance-enriched multi-relational graph tracking factual origins at the turn level, and query-adaptive subgraph retrieval with Dynamic Weighted PageRank that applies query-conditioned edge weighting. Evaluated on LOCOMO and LongMemEval benchmarks, MemORAI achieves state-of-the-art performance in memory retrieval and personalized response generation, demonstrating that selective storage, enriched representation, and adaptive retrieval are essential for coherent, personalized LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
