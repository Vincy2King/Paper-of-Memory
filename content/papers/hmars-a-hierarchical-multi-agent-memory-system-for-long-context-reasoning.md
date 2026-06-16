# HMARS: A Hierarchical Multi-Agent Memory System for Long-Context Reasoning

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:4CDX6PQRVs
- Published: 2026-06-02
- Updated: 2026-06-16
- Authors: Unknown
- Tags: agent, benchmark, context, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=4CDX6PQRVs

## One-Sentence Summary
Long-context reasoning requires models to access, retrieve, and integrate evidence scattered across documents, dialogues, and accumulated interaction histories.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-context reasoning requires models to access, retrieve, and integrate evidence scattered across documents, dialogues, and accumulated interaction histories.

进一步看，论文的核心做法或实验重点可以概括为：Standard retrieval-augmented generation reduces this problem to top-$K$ chunk retrieval, but such passive access can discard relevant evidence before reasoning begins, especially when relevance depends on broader...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Long-context reasoning requires models to access, retrieve, and integrate evidence scattered across documents, dialogues, and accumulated interaction histories. Standard retrieval-augmented generation reduces this problem to top-$K$ chunk retrieval, but such passive access can discard relevant evidence before reasoning begins, especially when relevance depends on broader context. We propose HMARS, a hierarchical multi-agent memory system that treats long contexts as managed memory rather than a flat retrieval corpus. Sub-agents maintain grounded access to bounded memory regions, mid-agents manage regional context and provide query-specific coordination, and a frontier model performs final reasoning over retrieved evidence pages. To evaluate this view, we construct two diagnostic benchmarks targeting evidence breadth and context-dependent relevance. Across long-document and multi-turn memory tasks, HMARS achieves the best overall performance against retrieval, reranking, full-context, graph-based, and agentic long-context baselines. Evidence coverage analysis further shows that its gains come from retrieving the required supporting evidence more completely, rather than merely changing the final answer prompt.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
