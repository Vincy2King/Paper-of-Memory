# AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:Dc7Dp22hLN
- Published: 2026-12-31
- Updated: 2026-04-21
- Authors: Yupeng Huo, Yaxi Lu, Zhong Zhang, Haotian Chen, Yankai Lin
- Tags: agent, benchmark, context
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=Dc7Dp22hLN

## One-Sentence Summary
Equipping agents with memory is essential for solving real-world long-horizon problems.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Equipping agents with memory is essential for solving real-world long-horizon problems.

进一步看，论文的核心做法或实验重点可以概括为：However, most existing agent memory mechanisms rely on static and hand-crafted workflows.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
Equipping agents with memory is essential for solving real-world long-horizon problems. However, most existing agent memory mechanisms rely on static and hand-crafted workflows. This limits the performance and generalization ability of these memory designs, which highlights the need for a more flexible, learning-based memory framework. In this paper, we propose AtomMem, which reframes memory management as a dynamic decision-making problem. We deconstruct high-level memory processes into fundamental atomic CRUD (Create, Read, Update, Delete) operations, transforming the memory workflow into a learnable decision process. By combining supervised fine-tuning with reinforcement learning, AtomMem learns an autonomous, task-aligned policy to orchestrate memory behaviors tailored to specific task demands. Experimental results across 3 long-context benchmarks demonstrate that the trained AtomMem-8B consistently outperforms prior static-workflow memory methods. Further analysis of training dynamics shows that our learning-based formulation enables the agent to discover structured, task-aligned memory management strategies, highlighting a key advantage over predefined routines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
