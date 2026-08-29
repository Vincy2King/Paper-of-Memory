# Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles

- Source: OpenReview
- Venue: ACL ARR 2026 August Submission
- Paper ID: openreview:8oUXCzERe8
- Published: 2026-08-04
- Updated: 2026-08-28
- Authors: Unknown
- Tags: agent, benchmark, compression, context, long-term
- Categories: aclweb.org/ACL/ARR/2026/August/-/Submission
- URL: https://openreview.net/forum?id=8oUXCzERe8

## One-Sentence Summary
Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 August Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured.

进一步看，论文的核心做法或实验重点可以概括为：We make three contributions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 August Submission
- 高亮主题命中：agent, benchmark, compression, context, long-term
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：aclweb.org/ACL/ARR/2026/August/-/Submission

## Abstract Snapshot
Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured. We make three contributions. First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations. Second, we present Profile-Graph Memory (ProGraph), a two-layer memory architecture combining (i) profile expansion -- substring-matched traversal of entity names that naturally appear in LLM-written profile narratives, a minimal alternative to explicit knowledge-graph construction -- and (ii) compression residuals -- exact dates, quantities, and named items co-extracted with each profile update at zero extra API cost. Third, a full-grid ablation shows cross-benchmark mechanism specialization: profile expansion drives multi-hop reasoning (-22.6pp on MemHop when removed) while compression residuals drive precision recall (-8.6pp on LoCoMo when not co-extracted), with cross-effects under 3pp within a single architecture. ProGraph averages 80.1% on MemHop (matching the FullContext reference) and 78.4% on LoCoMo (exceeding FullContext by 11.3pp), outperforming Mem0, A-Mem, HippoRAG, and RAG on both. We release MemHop, ProGraph, and baseline implementations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
