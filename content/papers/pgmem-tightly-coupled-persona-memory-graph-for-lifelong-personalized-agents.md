# PGMem: Tightly Coupled Persona-Memory Graph for Lifelong Personalized Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01708v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Wonjun Choi, Yerim Kim, Yukyung Lee, Susik Yoon
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.01708v1

## One-Sentence Summary
Long-term personalized dialogue agents must track user preferences as their personas evolve.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term personalized dialogue agents must track user preferences as their personas evolve.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems organize past events well, but store personas as flat profiles detached from the events that justify them.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term personalized dialogue agents must track user preferences as their personas evolve. Existing memory systems organize past events well, but store personas as flat profiles detached from the events that justify them. This loose coupling leads to the memory-persona validity gap and the persona-aware retrieval gap. We propose PGMem, a heterogeneous persona-memory graph that connects event and persona nodes through typed provenance and evidence edges, keeping each persona signal traceable to the events that support or revise it. At retrieval time, PGMem expands from query-relevant seeds and ranks signals by evidential validity. Across three benchmarks with small language model backbones, PGMem consistently outperforms summary-based, persona-aware, graph-structured, and agentic memory baselines, and improves performance as the context grows. The source code of PGMem is available at https://github.com/wonjunchoi23/pgmem/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
