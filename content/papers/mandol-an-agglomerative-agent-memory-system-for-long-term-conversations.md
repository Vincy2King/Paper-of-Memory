# Mandol: An Agglomerative Agent Memory System for Long-Term Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.29778v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Yuhan Zhang, Zhiyuan Guo, Ziheng Zeng, Wei Wang, Wentao Wu, Lijie Xu
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: cs.DB, cs.AI, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2606.29778v1

## One-Sentence Summary
Long-term conversational agents need to remember and query cross-session, multi-typed information with complex correlations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational agents need to remember and query cross-session, multi-typed information with complex correlations.

进一步看，论文的核心做法或实验重点可以概括为：Existing agent memory systems rely on heterogeneous vector and graph databases, which fragment memory information and cause high cross-database I/O latency.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.DB, cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Long-term conversational agents need to remember and query cross-session, multi-typed information with complex correlations. Existing agent memory systems rely on heterogeneous vector and graph databases, which fragment memory information and cause high cross-database I/O latency. For retrieval, common RAG-style methods tend to introduce noise, miss correlated clues, and lack token budget control, degrading LLM accuracy and efficiency. We propose Mandol, an agglomerative memory system that consolidates fragmented memory representations and storage into a unified memory-native architecture. Its core components include: (1) a hierarchical memory model that organizes memory into a basic layer representing raw memory information and a high-level abstract layer that agglomerates basic memories into traceable abstract memories, both uniformly represented as structured semantic graphs; (2) an agglomerative semantic data structure combining SemanticMap and SemanticGraph, which natively fuses key-value, vector, and graph structures and provides unified hybrid retrieval operators to eliminate cross-database I/O; and (3) a quantitative query mechanism with query-adaptive routing, quantitative denoising and conflict resolution, and token-constrained context generation, all without involving LLMs during retrieval. Experiments on two widely used long-term conversation benchmarks, LoCoMo and LongMemEval, show that Mandol achieves the best overall accuracy among representative agent memory systems. For performance comparison, Mandol also obtains a 5.4x retrieval speedup and a 4.8x insertion speedup under 10 QPS concurrent load, while still maintaining low latency on consumer-grade hardware.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
