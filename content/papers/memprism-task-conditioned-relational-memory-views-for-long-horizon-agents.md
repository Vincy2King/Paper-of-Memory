# MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.06745v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Zhisheng Chen, Bingfan Zeng, Bangde Cao, Zhengwei Xie, Yuxuan Li, Jinhan Li, Zheng Lu, Xiangchen Guan, Zikai Xiao, Rui Qian, Jingwei Song
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.06745v1

## One-Sentence Summary
Long-horizon agents rely on memory to reuse experiences, yet existing memory systems often assume that evidence can be directly consumed through a fixed representation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon agents rely on memory to reuse experiences, yet existing memory systems often assume that evidence can be directly consumed through a fixed representation.

进一步看，论文的核心做法或实验重点可以概括为：This leads to representation mismatch, where relevant information is available but not organized for the current decision.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon agents rely on memory to reuse experiences, yet existing memory systems often assume that evidence can be directly consumed through a fixed representation. This leads to representation mismatch, where relevant information is available but not organized for the current decision. To this end, we propose MemPrism, a task-conditioned relational memory framework that separates persistent experience storage from decision-time working memory. MemPrism records interactions as the event stream and dynamically constructs relational views according to the current task context. A lightweight view policy selects the relation structure, evidence range, outcome condition, and granularity, while a deterministic composer and render transform historical facts into a temporary optical working-memory view for a frozen task policy. Experiments on long-horizon embodied and web-agent benchmarks show that MemPrism consistently improves the task performance, especially as trajectories become longer, while reducing memory token consumption. Furthermore, the learned view policy transfers across different VLMs without additional adaptation, demonstrating the effectiveness of task-conditioned relational views as a general memory interface for agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
