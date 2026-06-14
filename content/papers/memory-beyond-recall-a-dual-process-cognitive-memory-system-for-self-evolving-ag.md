# Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:ywl53zPXu0
- Published: 2026-06-02
- Updated: 2026-06-14
- Authors: Unknown
- Tags: agent, benchmark, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=ywl53zPXu0

## One-Sentence Summary
Long-term memory for an LLM agent is more than retrieving the right passage at the right time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory for an LLM agent is more than retrieving the right passage at the right time.

进一步看，论文的核心做法或实验重点可以概括为：Current memory systems collapse belief revision, causal coupling, and cross-domain abstraction into a single retrieval surface tuned for surface recall, and consequently struggle on implicit personalisation that...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Long-term memory for an LLM agent is more than retrieving the right passage at the right time. Current memory systems collapse belief revision, causal coupling, and cross-domain abstraction into a single retrieval surface tuned for surface recall, and consequently struggle on implicit personalisation that requires reasoning over how a user has evolved. We propose DPCM, which reorganises agent memory along a *cognitive capability hierarchy* ascending from raw inputs and atomic facts, through diachronic belief trajectories and identity, to domain schemas, latent intentions and cross-domain patterns. The hierarchy is driven by two processes inheriting the architectural split of dual-process theory: a synchronous daytime writer (SYSTEM 1) that records belief revisions as doubly linked supersedes chains, and an asynchronous nighttime engine (SYSTEM 2) that induces schemas and intentions and sweeps for cross-domain collisions abstracted into higher-level core schemas. On LongMemEval, PersonaMem and PersonaMem-v2, enabling SYSTEM 2 contributes most where the benchmark rewards implicit cross-session inference (up to +5.20 on PersonaMem-v2) and least on span recall, matching the architectural prediction.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
