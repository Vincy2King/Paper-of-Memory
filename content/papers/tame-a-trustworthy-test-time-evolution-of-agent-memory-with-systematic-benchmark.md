# TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:0FnWcX2SgR
- Published: 2026-06-02
- Updated: 2026-06-20
- Authors: Unknown
- Tags: agent, benchmark
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=0FnWcX2SgR

## One-Sentence Summary
Test-time evolution of agent memory represents a pivotal paradigm for advancing AGI, as it strengthens complex reasoning through experience accumulation without requiring...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Test-time evolution of agent memory represents a pivotal paradigm for advancing AGI, as it strengthens complex reasoning through experience accumulation without requiring parameter updates.

进一步看，论文的核心做法或实验重点可以概括为：However, even during benign task evolution, agent safety alignment remains vulnerable—a phenomenon known as Agent Memory Misevolution.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Test-time evolution of agent memory represents a pivotal paradigm for advancing AGI, as it strengthens complex reasoning through experience accumulation without requiring parameter updates. However, even during benign task evolution, agent safety alignment remains vulnerable—a phenomenon known as Agent Memory Misevolution. To evaluate this phenomenon, we construct the Trust-Memevo benchmark and find that agents exhibit an overall decline in trustworthiness across multiple tasks during benign task evolution. To address this issue, we propose TAME, a trust-aware memory evolution framework in which a shared memory bank is jointly governed by an Executor and an Evaluator. The Executor retrieves and applies transferable experiences to support task solving, while the Evaluator assesses the contribution of each utilized experience to the outcome and produces trust-aware feedback to guide subsequent memory use. This executor–evaluator loop enables memory to be selectively reinforced, cautiously reused, and continuously expanded over time. Experiments show that TAME mitigates memory misevolution while achieving strong task performance. In particular, on the GPT-5.2 AIME benchmark, TAME improves accuracy by 14.6 percentage points over the strongest existing method and maintains competitive trustworthiness.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
