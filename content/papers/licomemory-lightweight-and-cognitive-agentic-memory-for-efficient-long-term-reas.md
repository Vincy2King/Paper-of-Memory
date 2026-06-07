# LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning

- Source: OpenReview
- Venue: ACL ARR 2026 January Submission
- Paper ID: openreview:r5h2um8UsH
- Published: 2026-03-20
- Updated: 2026-06-07
- Authors: Unknown
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/January/-/Submission
- URL: https://openreview.net/forum?id=r5h2um8UsH

## One-Sentence Summary
Large Language Model (LLM) agents exhibit remarkable conversational and reasoning capabilities but remain constrained by limited context windows and the lack of persistent memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 January Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large Language Model (LLM) agents exhibit remarkable conversational and reasoning capabilities but remain constrained by limited context windows and the lack of persistent memory.

进一步看，论文的核心做法或实验重点可以概括为：Recent efforts address these limitations via external memory architectures, often employing graph-based representations, yet most adopt flat, entangled structures that intertwine semantics with topology, leading to...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 January Submission
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/January/-/Submission

## Abstract Snapshot
Large Language Model (LLM) agents exhibit remarkable conversational and reasoning capabilities but remain constrained by limited context windows and the lack of persistent memory. Recent efforts address these limitations via external memory architectures, often employing graph-based representations, yet most adopt flat, entangled structures that intertwine semantics with topology, leading to redundant representations, unstructured retrieval, and degraded efficiency and accuracy. To resolve these issues, we propose LiCoMemory, an end-to-end agentic memory framework for real-time updating and retrieval, which introduces CogniGraph, a lightweight hierarchical graph that utilizes entities and relations as semantic indexing layers, and employs temporal and hierarchy-aware search with integrated reranking for adaptive and coherent knowledge retrieval. Experiments on long-term dialogue benchmarks, LoCoMo and LongMemEval, show that LiCoMemory not only outperforms established baselines in temporal reasoning, multi-session consistency, and retrieval efficiency, but also notably reduces update latency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
