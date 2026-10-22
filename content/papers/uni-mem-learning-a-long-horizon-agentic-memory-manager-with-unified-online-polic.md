# Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.29671v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Zhiqian Xia, Jielong Tang, Ling-An Zeng, Shixiong Kai, Rong Yao, Hao Kong, Xiao Dong, Wei Wang, Mingxuan Yuan, Siyu Xia, Haifeng Xia
- Tags: agent, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.29671v1

## One-Sentence Summary
Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval.

进一步看，论文的核心做法或实验重点可以概括为：Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction supervision, limiting co-adaptation between the two stages.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval. Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction supervision, limiting co-adaptation between the two stages. In this paper, we explore end-to-end online RL for a unified memory manager (Uni-Mem) that learns both capabilities under a shared policy. However, joint optimization with existing RL algorithms such as GRPO faces confounded group comparisons and sparse feedback over long memory-management trajectories. To this end, we propose Stage-Decoupled GRPO, which alternates construction and retrieval optimization while controlling variation from the other stage within each rollout group, yielding stage-specific learning signals. We further introduce Event-Wise Credit Assignment (ECA), which localizes feedback to responsible events and propagates event-level advantages to their constituent operations. Experiments on LoCoMo and LongMemEval show that Uni-Mem outperforms the strongest RL-based memory, demonstrating the effectiveness of jointly learning memory construction and retrieval via Stage-Decoupled GRPO and ECA.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
