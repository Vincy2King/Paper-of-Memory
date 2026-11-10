# TrajLift: Lifting Memory Recall Trajectories with Latency-Modulated Heat Diffusion

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.12197v1
- Published: 2026-11-09
- Updated: 2026-11-09
- Authors: Jiawen Kang, Jinchao Li, Mingyu Cui, Junan Li, Xixin Wu, Helen Meng
- Tags: benchmark, context, retrieval
- Categories: cs.CL, cs.AI, q-bio.NC
- URL: http://arxiv.org/abs/2611.12197v1

## One-Sentence Summary
Verbal memory retrieval carries rich diagnostic information for Alzheimer's disease through the order, hesitation, and categorical organization of recalled words, yet...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Verbal memory retrieval carries rich diagnostic information for Alzheimer's disease through the order, hesitation, and categorical organization of recalled words, yet computational modeling of this retrieval process...

进一步看，论文的核心做法或实验重点可以概括为：A key challenge is that timing and hierarchical structure are diagnostically entangled: the diagnostic meaning of retrieval timing depends on its hierarchical context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL, cs.AI, q-bio.NC

## Abstract Snapshot
Verbal memory retrieval carries rich diagnostic information for Alzheimer's disease through the order, hesitation, and categorical organization of recalled words, yet computational modeling of this retrieval process remains largely unexplored. A key challenge is that timing and hierarchical structure are diagnostically entangled: the diagnostic meaning of retrieval timing depends on its hierarchical context. We propose TrajLift, a spectral framework that models verbal recall as timed trajectories on a hierarchical graph. Our central mechanism is latency-modulated heat diffusion on the semantic hierarchy, a unified operator that lifts each recalled word into a representation of both multi-scale hierarchical structure and continuous retrieval timing. Formal analysis shows that the resulting representation is first-order separable into structural and temporal components with spectral selectivity across hierarchical levels. On synthetic benchmarks requiring structure-time interaction, TrajLift stays near-perfect on deep hierarchies where all baselines fail. On real-world clinical data, we show that TrajLift outperforms diverse baselines by jointly modeling timing and semantic structure, with gains that grow as retrieval timing becomes more informative.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
