# RaMem: Contextual Reinstatement for Long-term Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.22844v1
- Published: 2026-06-22
- Updated: 2026-06-22
- Authors: Wei Yang, Bryce Kan, Shixuan Li, Li Li, Yuehan Qin, Jiate Li, Paul Bogdan, Jesse Thomason
- Tags: agent, benchmark, context, episodic, long-term, retrieval
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2606.22844v1

## One-Sentence Summary
Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts.

进一步看，论文的核心做法或实验重点可以概括为：Recent memory systems have made past experiences more persistent, compact, and retrievable, but retrieval alone does not ensure that a memory provides valid evidence for the current query.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks, retrieval memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts. Recent memory systems have made past experiences more persistent, compact, and retrievable, but retrieval alone does not ensure that a memory provides valid evidence for the current query. When experiences are compressed into reusable fragments, memories from different situations may appear equally relevant if they involve recurring entities or user states. We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. To address this problem, we propose Contextual Reinstatement for Agentic Memory (RaMem), a framework that turns retrieved memory fragments into contextually verifiable evidence. RaMem operates through four coordinated stages: (i) evidence anchoring grounds each memory in its original episodic conditions, especially event time, mention time, session span, and participants; (ii) recall condition induction derives the evidence conditions implied by the query; (iii) validity-aware retrieval uses these conditions to prioritize context-compatible memories while retaining content-relevant candidates as fallback evidence; and (iv) context-preserved synthesis keeps the selected memories' structured context available to the generator. Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
