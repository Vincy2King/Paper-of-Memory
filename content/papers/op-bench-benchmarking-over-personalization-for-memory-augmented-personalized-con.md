# OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents

- Source: OpenReview
- Venue: ACL ARR 2026 March Submission
- Paper ID: openreview:qRtPIkjN7P
- Published: 2026-06-07
- Updated: 2026-06-07
- Authors: Unknown
- Tags: agent, benchmark, conversation, long-term
- Categories: aclweb.org/ACL/ARR/2026/March/-/Submission
- URL: https://openreview.net/forum?id=qRtPIkjN7P

## One-Sentence Summary
Memory-augmented conversational agents enable personalized interactions using long-term user memory and have gained substantial traction.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 March Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory-augmented conversational agents enable personalized interactions using long-term user memory and have gained substantial traction.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks primarily focus on whether agents can recall and apply user information, while overlooking whether such personalization is used appropriately.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 March Submission
- 高亮主题命中：agent, benchmark, conversation, long-term
- 检索关键词命中：memory-augmented
- 来源分类信息：aclweb.org/ACL/ARR/2026/March/-/Submission

## Abstract Snapshot
Memory-augmented conversational agents enable personalized interactions using long-term user memory and have gained substantial traction. However, existing benchmarks primarily focus on whether agents can recall and apply user information, while overlooking whether such personalization is used appropriately. In fact, agents may overuse personal information, producing responses that feel forced, intrusive, or socially inappropriate to users. We refer to this issue as **over-personalization**. In this work, we formalize over-personalization into three types: Irrelevance, Repetition, and Sycophancy, and introduce **OP-Bench**, a benchmark of 1,700 verified instances constructed from long-horizon dialogue histories. Using OP-Bench, we evaluate multiple large language models and memory-augmentation methods, and find that over-personalization is widespread when memory is introduced. Further analysis reveals that agents tend to retrieve and over-attend to user memories even when unnecessary. We further evaluate existing post-processing strategies for mitigating this issue, but find that they provide only limited improvements and often reduce personalization performance. Our results highlight over-personalization as a challenging and largely unresolved problem in memory-augmented dialogue systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
