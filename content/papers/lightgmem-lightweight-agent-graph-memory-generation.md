# LightGMEM: Lightweight Agent Graph Memory Generation

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:FCQR2oceJ1
- Published: 2026-06-02
- Updated: 2026-06-17
- Authors: Unknown
- Tags: agent, context, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=FCQR2oceJ1

## One-Sentence Summary
Agent memory systems have been widely proposed to equip large language model (LLM) agents with long-term memory across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Agent memory systems have been widely proposed to equip large language model (LLM) agents with long-term memory across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Compared to flat memory, graph-based memory more effectively models relationships between facts, but its construction relies on repeated LLM calls that scale poorly with conversation length.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Agent memory systems have been widely proposed to equip large language model (LLM) agents with long-term memory across sessions. Compared to flat memory, graph-based memory more effectively models relationships between facts, but its construction relies on repeated LLM calls that scale poorly with conversation length. We propose LightGMEM, a lightweight entity-centric graph memory framework that addresses three key bottlenecks: (i) replacing per-episode LLM entity extraction with GLiNER2, a zero-shot named entity recognizer, and deferring entity profiling until sufficient cross-episode evidence accumulates; (ii) introducing conflict-lane partitioning for entity disambiguation, serializing only mentions with overlapping candidate sets while resolving independent ones concurrently; (iii) adopting Ego-Splitting to construct overlapping communities, allowing entities to participate in multiple retrieval contexts. On LoCoMo, LightGMEM achieves the best score on 8 of 12 QA metrics with 58.0$\times$ fewer LLM calls and 151.6$\times$ lower construction runtime than Zep. On LongMemEval, it remains competitive on single-session tasks, with trade-offs on update-heavy and temporally reasoning. These results demonstrate that graph-based memory can remain practical at scale when LLM reasoning is reserved for high-value operations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
