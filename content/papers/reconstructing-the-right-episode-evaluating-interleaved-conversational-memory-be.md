# Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:Fjk0QoHwlm
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Unknown
- Tags: benchmark, context, conversation
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=Fjk0QoHwlm

## One-Sentence Summary
Conversations with chat assistants increasingly span many topics in a single long-running thread, challenging memory systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Conversations with chat assistants increasingly span many topics in a single long-running thread, challenging memory systems.

进一步看，论文的核心做法或实验重点可以概括为：Existing long-context and memory benchmarks often expose session or topic boundaries, or probe direct personal-memory questions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：benchmark, context, conversation
- 检索关键词命中：conversational memory, memory benchmark, memory benchmarks
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Conversations with chat assistants increasingly span many topics in a single long-running thread, challenging memory systems. Existing long-context and memory benchmarks often expose session or topic boundaries, or probe direct personal-memory questions. These settings understate a harder assistant-memory regime: a flat mixed-topic thread where the system must infer which earlier episode makes a later task decision valid. We introduce SCALE-QA, a constraint-grounded task QA benchmark for flat unsegmented threads targeting episode integrity failure. The dataset contains 3,000 audited questions across 10 domains, uses deterministic four-way MCQ grading, and includes a deterministic runtime builder for user-specified mixed-topic context lengths; our experiments report settings through 1M tokens. SCALE-QA questions are ordinary task-oriented requests whose correct answer depends on causally related evidence introduced earlier in the conversation. We also propose Temporal-Semantic Interleaved Memory Reconstruction (TSIM), which segments the turn stream into coherent episodes and indexes them through a hierarchical multi-view memory stack with LLM-generated episode summaries. Experiments show that SCALE-QA challenges strong RAG baselines and long-context LLMs alike; across three open-source and proprietary LLMs, TSIM achieves the highest accuracy in every backend setting, gaining 5.6–17.6 accuracy points over the strongest corresponding baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
