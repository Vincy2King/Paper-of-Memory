# PROCED-MEM: BENCHMARKING PROCEDURAL MEMORY RETRIEVAL IN LANGUAGE AGENTS ACROSS DOMAINS

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents Poster
- Paper ID: openreview:4YhU3BZgoZ
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: Ishant Kohar, Aswanth Krishnan
- Tags: agent, benchmark, context, retrieval
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=4YhU3BZgoZ

## One-Sentence Summary
We introduce Proced-Mem, a benchmark for procedural memory retrieval in language agents with two sub-domains: text-based household tasks (ALFWorld) and real computer...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：We introduce Proced-Mem, a benchmark for procedural memory retrieval in language agents with two sub-domains: text-based household tasks (ALFWorld) and real computer environments (OSWorld).

进一步看，论文的核心做法或实验重点可以概括为：Evaluating retrieval independently of downstream execution is critical because current agent evaluations conflate retrieval with planning and execution, masking whether agents retrieve relevant procedures or succeed...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents Poster
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
We introduce Proced-Mem, a benchmark for procedural memory retrieval in language agents with two sub-domains: text-based household tasks (ALFWorld) and real computer environments (OSWorld). Evaluating retrieval independently of downstream execution is critical because current agent evaluations conflate retrieval with planning and execution, masking whether agents retrieve relevant procedures or succeed despite poor memory access. Proced-Mem evaluates up to seven methods across text, visual, and lexical modalities, using an LLM-as-judge protocol for ALFWorld and a leave-one-out protocol with hierarchical ground truth at two granularity levels for OSWorld. Across both sub-domains, we find a generalization cliff (30–42% MAP degradation on novel contexts) and a granularity-method reversal where visual features rank first at coarse retrieval but last at fine-grained procedural matching. Proced-Mem provides the first diagnostic framework for identifying such failure modes, enabling the principled design of retrieval systems that generalize across granularity levels and modalities.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
