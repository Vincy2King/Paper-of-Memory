# RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.02508v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Yi Yang, Zhennan Chen, Yihong Zhuang, Tiehan Fan, Yinan Chen, Jian Li, Jian Yang, Ying Tai
- Tags: agent
- Categories: cs.LG, cs.CL
- URL: http://arxiv.org/abs/2608.02508v1

## One-Sentence Summary
Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges.

进一步看，论文的核心做法或实验重点可以概括为：First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.LG, cs.CL

## Abstract Snapshot
Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory Reinforcement Learning (RoMeRL), which represents the growing trajectory-indexed utility space using a fixed-dimensional per-task memory state factorized by outcome polarity and memory dynamics. RoMeRL incorporates new experiences through a fixed set of semantic coordinates whose contents are updated or replaced over time, thereby concentrating feedback over a bounded utility support. Theoretically, we show that this reduced-order parameterization increases the average feedback received by each utility coordinate and characterize the steady-state occupancy of erroneous coordinates under a generic coordinate-transition model. Empirically, across ALFWorld and LifelongAgentBench, RoMeRL improves task performance, reduces the Cold-Q ratio by 80.0%, increases feedback density by approximately 6.0 times, reduces the maintained memory size by 84.4%, and cuts LLM calls by 21.1%. These results show that reduced-order utility states support efficient self-evolving agent memory while limiting persistent reward contamination. Code is available at: https://github.com/YOUNG-fnxm/RoMeRL

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
