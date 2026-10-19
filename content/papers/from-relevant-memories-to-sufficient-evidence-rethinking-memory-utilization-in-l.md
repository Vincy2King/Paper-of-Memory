# From Relevant Memories to Sufficient Evidence: Rethinking Memory Utilization in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.22668v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Shixuan Li, Wei Yang, Peiyu Zhang, Anzhe Cheng, Heng Ping, Xiaole Zhang, Jesse Thomason, Xuezhe Ma, Yue Zhao, Paul Bogdan
- Tags: agent, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.22668v1

## One-Sentence Summary
Long-term memory enables LLM agents to reuse past experiences, yet retrieving relevant memories does not necessarily provide sufficient evidence for answering a query.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables LLM agents to reuse past experiences, yet retrieving relevant memories does not necessarily provide sufficient evidence for answering a query.

进一步看，论文的核心做法或实验重点可以概括为：Essential information may remain fragmented across memory records, obscured by abstraction, or disconnected from the relations required for reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory enables LLM agents to reuse past experiences, yet retrieving relevant memories does not necessarily provide sufficient evidence for answering a query. Essential information may remain fragmented across memory records, obscured by abstraction, or disconnected from the relations required for reasoning. We identify this relevance-sufficiency gap and propose QEMem, a framework that reformulates memory utilization as the construction of query-specific evidence sets, shifting the focus from individual retrieval relevance to collective evidential support. QEMem integrates three complementary mechanisms: query-guided discovery retrieves evidence across multiple memory granularities; source-grounded reification organizes it into structured ViewCards with explicit evidential roles and source references; and sufficiency-guided refinement selectively recovers missing information. Operating on existing memory stores without modifying memory formation, QEMem achieves 91.43% LLM-judge accuracy on LoCoMo with Claude Opus 4.5, outperforming the strongest evaluated baseline, MemR$^3$, by 7.6 percentage points and NEMORI by 10.7 points under a shared memory store. Further analyses demonstrate improved evidence coverage and strong performance on questions requiring cross-session evidence integration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
