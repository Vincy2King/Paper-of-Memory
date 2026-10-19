# From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.23313v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Shangze Li, Yanyu Yao, Derong Xu, Zhi Zheng, Tong Xu
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.23313v1

## One-Sentence Summary
Long-term agent memory requires recovering answer-relevant evidence dispersed across turns and sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term agent memory requires recovering answer-relevant evidence dispersed across turns and sessions.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems increasingly use structured memories and adaptive retrieval, yet often pass retrieved or expanded units directly to the reader, coupling memory addressing with evidence presentation and leaving the...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, conversational memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term agent memory requires recovering answer-relevant evidence dispersed across turns and sessions. Existing systems increasingly use structured memories and adaptive retrieval, yet often pass retrieved or expanded units directly to the reader, coupling memory addressing with evidence presentation and leaving the final context redundant or incomplete. To address this gap, we propose MemCompile, a query-conditioned evidence compilation framework for long-term conversational memory. Given a query, the Address Plane locates relevant support through compact source-linked descriptors and capacity-aware Cells, while a normalization boundary resolves heterogeneous retrieval hits to stable SourcePacket identities. Its Evidence Plane then allocates a bounded evidence budget across complementary packets, admits limited additional support, and renders the retained claims associated with each selected packet into an answer-ready context. MemCompile achieves 80.52% Judge Accuracy on LoCoMo and extends the empirical quality-cost Pareto frontier to a higher-quality regime. Its strong performance on LongMemEval-S further suggests that the benefits of query-conditioned compilation generalize across long-term conversational-memory benchmarks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
