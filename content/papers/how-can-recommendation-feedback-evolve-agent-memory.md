# How Can Recommendation Feedback Evolve Agent Memory?

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.37544v2
- Published: 2026-09-29
- Updated: 2026-09-30
- Authors: Shanwen Mao, Mingming Li, Hao Zhang, Zhiheng Li, Yige Wang, Penghua Yu, Junxiong Zhu
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.37544v2

## One-Sentence Summary
Content-generation agents continuously receive impressions, clicks, conversions, and negative feedback from recommendation systems, providing real-world outcome signals for...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Content-generation agents continuously receive impressions, clicks, conversions, and negative feedback from recommendation systems, providing real-world outcome signals for memory evolution.

进一步看，论文的核心做法或实验重点可以概括为：However, these signals are delayed and noisy, confounded by audience composition, placement, and recommendation policies, and may result from the combined influence of multiple memories, making accurate attribution...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Content-generation agents continuously receive impressions, clicks, conversions, and negative feedback from recommendation systems, providing real-world outcome signals for memory evolution. However, these signals are delayed and noisy, confounded by audience composition, placement, and recommendation policies, and may result from the combined influence of multiple memories, making accurate attribution difficult. Existing methods rely primarily on immediate feedback or semantic retrieval and therefore struggle to reliably translate recommendation outcomes into memory fitness. To address this challenge, we propose TIDE (Trajectory-Informed Directed Memory Evolution), an external memory evolution framework driven by delayed recommendation feedback. We further introduce Memory Evolution Gain (MEG), which measures the utility improvement of evolved memory over a no memory baseline on strictly future tasks. TIDE treats memory as a capacity-constrained population of experiences: temporal and semantic credit assignment estimates contextual fitness, while responsibility credit distributes outcome signals according to the memories referenced during generation. These signals are then used to reinforce, crossover, mutate, or evict memories. On an e-commerce membership marketing content-generation agent, TIDE achieves a +7.75-percentage-point MEG in offline temporal replay and significantly improves both unique click-through rate (UCTR) and activation rate in an online A/B test. On a delayed-label benchmark, TIDE achieves the lowest mean absolute error (MAE) and root mean squared error (RMSE) and the highest MEG among the compared methods, demonstrating its effectiveness.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
