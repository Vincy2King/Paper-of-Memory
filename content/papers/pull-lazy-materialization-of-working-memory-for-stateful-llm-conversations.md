# Pull: Lazy Materialization of Working Memory for Stateful LLM Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.14773v1
- Published: 2026-09-13
- Updated: 2026-09-13
- Authors: Jiangang Chen
- Tags: benchmark, compression, context, conversation
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.14773v1

## One-Sentence Summary
As LLM conversations grow to hundreds of turns, full-context injection incurs $O(N^2)$ cumulative token costs, while lossy summarization or hard truncation irreversibly discards...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As LLM conversations grow to hundreds of turns, full-context injection incurs $O(N^2)$ cumulative token costs, while lossy summarization or hard truncation irreversibly discards historical state.

进一步看，论文的核心做法或实验重点可以概括为：We propose Pull, a session router that maintains an addressable metadata directory via a local, deterministic Purifier (zero LLM calls, millisecond-level latency).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, context, conversation
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
As LLM conversations grow to hundreds of turns, full-context injection incurs $O(N^2)$ cumulative token costs, while lossy summarization or hard truncation irreversibly discards historical state. We propose Pull, a session router that maintains an addressable metadata directory via a local, deterministic Purifier (zero LLM calls, millisecond-level latency). At query time, the LLM lazily materializes only the turns it needs; unmaterialized turns remain accessible but collapsed. Unlike irreversible compression, Pull's materialization is reversible; subsequent queries can expand any collapsed turn. On LoCoEval (128 conversations, 12,780 turns), Pull reduces per-query context tokens (Phase 2) by 75.1 percent on single-hop tasks with equivalent quality ($Δ= -0.002$, n.s.) and by 72.0 percent on multi-hop tasks with no quality loss ($Δ= +0.017$). A controlled routing benchmark (7,831 queries x 10 methods) shows that entity lifecycle tracking is empirically a prerequisite for distance-independent routing. On BEAM 1M (14 conversations, 263 questions), Pull improves F1 by +55.2 percent over a truncation baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
