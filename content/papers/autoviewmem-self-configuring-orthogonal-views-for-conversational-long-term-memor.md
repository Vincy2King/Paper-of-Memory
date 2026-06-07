# AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory

- Source: OpenReview
- Venue: ACL ARR 2026 March Submission
- Paper ID: openreview:iWTQYgHSiH
- Published: 2026-06-07
- Updated: 2026-06-07
- Authors: Unknown
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/March/-/Submission
- URL: https://openreview.net/forum?id=iWTQYgHSiH

## One-Sentence Summary
Long-term memory is essential for large language model (LLM) agents to maintain consistency and personalization over extended interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 March Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory is essential for large language model (LLM) agents to maintain consistency and personalization over extended interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems typically rely on fixed granularities or static schemas, but these designs struggle when heterogeneous information---such as preferences, events, constraints, and temporal updates---is...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 March Submission
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/March/-/Submission

## Abstract Snapshot
Long-term memory is essential for large language model (LLM) agents to maintain consistency and personalization over extended interactions. Existing memory systems typically rely on fixed granularities or static schemas, but these designs struggle when heterogeneous information---such as preferences, events, constraints, and temporal updates---is entangled in a single representation, leading to semantic interference and unstable top-$K$ retrieval. We present AutoViewMem, a data-driven framework that organizes long-term conversational memory into self-configuring, low-overlap semantic views. AutoViewMem discovers candidate views from interaction traces, selects a compact complementary view set, and uses these views to guide write-time structured extraction of provenance-grounded memories. This representation-first design reduces semantic entanglement within each memory space, enabling simple top-$K$ similarity search to retrieve precise evidence without explicit routing or iterative retrieval. We further apply offline consolidation to improve memory compactness and consistency. Experiments on the LoCoMo benchmark show that AutoViewMem achieves competitive or improved performance over strong baselines on long-horizon question answering and reasoning, while maintaining an efficient and deployable inference pipeline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
