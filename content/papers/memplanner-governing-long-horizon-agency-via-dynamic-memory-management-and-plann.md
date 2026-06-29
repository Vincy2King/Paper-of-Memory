# MEMPLANNER: Governing Long-Horizon Agency via Dynamic Memory Management and Planning

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:jvZt1ZRynU
- Published: 2026-06-02
- Updated: 2026-06-29
- Authors: Unknown
- Tags: agent, context
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=jvZt1ZRynU

## One-Sentence Summary
Large Language Model (LLM) agents often struggle with long-horizon tasks, as their limited context windows are easily overwhelmed by irrelevant information.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large Language Model (LLM) agents often struggle with long-horizon tasks, as their limited context windows are easily overwhelmed by irrelevant information.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented agents typically rely on rigid, predefined workflows, which lack the flexibility to adapt to diverse task demands.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, context
- 检索关键词命中：memory-augmented
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Large Language Model (LLM) agents often struggle with long-horizon tasks, as their limited context windows are easily overwhelmed by irrelevant information. Existing memory-augmented agents typically rely on rigid, predefined workflows, which lack the flexibility to adapt to diverse task demands. To address this, we introduce MemPlanner, an autonomous, plan-driven memory agent designed for strategic information management. Unlike traditional systems, MemPlanner employs a plan-then-execute paradigm: the agent first reasons about an optimal memory strategy tailored to the current context, then autonomously orchestrates a sequence of operations. This process is grounded in a hierarchical memory architecture comprising Core Memory for global context and Topic Memory for fine-grained details. By utilizing a progressive disclosure mechanism via a "header-as-index" format, the agent can scan the memory landscape efficiently and retrieve information gradually, minimizing context redundancy. Optimized through reinforcement learning, MemPlanner learns adaptive policies to distill high-level insights and organize factual knowledge. Extensive experiments confirm that MemPlanner achieves substantial improvements over existing agents, demonstrating superior robustness and strategy adaptation in complex, long-horizon environments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
