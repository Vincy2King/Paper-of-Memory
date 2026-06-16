# When Users Don’t Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:jaAA72U0tr
- Published: 2026-06-02
- Updated: 2026-06-16
- Authors: Unknown
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=jaAA72U0tr

## One-Sentence Summary
Large Language Models (LLMs) are increasingly deployed as long-horizon conversational agents, motivating growing interest in memory systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) are increasingly deployed as long-horizon conversational agents, motivating growing interest in memory systems.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks primarily evaluate memory through QA-style probing rather than in-situ conversational usage.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：conversational memory, memory benchmark, memory retrieval
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Large Language Models (LLMs) are increasingly deployed as long-horizon conversational agents, motivating growing interest in memory systems. However, existing benchmarks primarily evaluate memory through QA-style probing rather than in-situ conversational usage. We introduce LOCOMO-CONV, a conversational memory benchmark derived from LoCoMo with four query styles: dialog, implicit, counterfactual, and composed. Across four representative memory systems, we evaluate both retrieval recall and end-to-end response quality. Our experiments show that conversational framing exposes substantial retrieval gaps overlooked by QA benchmarks, especially on implicit and composed queries, which multi-facet query rewriting narrows for raw-turn but not abstractive memory. We further find that strong retrieval does not fully translate into response quality, and that implicit queries exhibit silent grounding, where memory improves contextual grounding without explicitly surfacing the gold fact. These results point to reasoning-based memory elaboration as a promising direction, and we release auxiliary supportive_memory annotations capturing conversationally useful context beyond the original gold evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
