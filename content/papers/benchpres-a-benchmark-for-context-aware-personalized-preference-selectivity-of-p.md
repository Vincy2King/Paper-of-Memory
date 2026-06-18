# BenchPreS: A Benchmark for Context-Aware Personalized Preference Selectivity of Persistent-Memory LLMs

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:cn9Bn4mXv6
- Published: 2026-06-02
- Updated: 2026-06-17
- Authors: Unknown
- Tags: benchmark, context
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=cn9Bn4mXv6

## One-Sentence Summary
Large language models (LLMs) increasingly store user preferences in persistent memory to support personalization across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models (LLMs) increasingly store user preferences in persistent memory to support personalization across interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, in third-party communication settings governed by social and institutional norms, some user preferences may be inappropriate to apply.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Large language models (LLMs) increasingly store user preferences in persistent memory to support personalization across interactions. However, in third-party communication settings governed by social and institutional norms, some user preferences may be inappropriate to apply. We introduce BenchPreS, which evaluates whether memory-based user preferences are appropriately applied or suppressed across communication contexts. Using two complementary metrics, Misapplication Rate (MR) and Appropriate Application Rate (AAR), we find even frontier LLMs struggle to apply preferences in a context-sensitive manner. Models with stronger preference adherence exhibit higher rates of over-application, and neither reasoning capability nor selectivity-oriented prompting fully resolve this issue. These results suggest that current LLMs treat preferences as globally enforceable rules rather than as context-dependent normative signals.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
