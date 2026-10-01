# Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.39166v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Mingjian Gao, Zhaocheng Li, Haoyang Huang, Wenqiao Zhang, Yingjie Niu, Hao Zhou, Chao Li, Juncheng Li, Siliang Tang, Yueting Zhuang
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.39166v1

## One-Sentence Summary
Persistent spatial memory enables embodied agents to navigate familiar environments across repeated visits.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent spatial memory enables embodied agents to navigate familiar environments across repeated visits.

进一步看，论文的核心做法或实验重点可以概括为：However, targets may move while unobserved, including during navigation, making remembered locations unreliable by the time an agent arrives.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent spatial memory enables embodied agents to navigate familiar environments across repeated visits. However, targets may move while unobserved, including during navigation, making remembered locations unreliable by the time an agent arrives. Despite advances in memory retrieval and state prediction, accounting for continued hidden world evolution and revising beliefs under limited visibility remain challenging. We study Evolving-World Navigation, where agents infer target locations from intermittent observations, predict their states at inspection time, and revise beliefs using visual evidence. We propose EvolvingNav, which constructs a time-indexed belief from timestamped 3D object histories through a structured persistence-relocation model. The belief distinguishes persistence at the last observed location from relocation to alternative locations and retains probability mass outside the known candidate set. An event-driven filter propagates the current belief as time elapses, forecasts target occupancy at candidate inspection times, and incorporates new RGB-D evidence. Negative observations downweight location hypotheses according to calibrated, visibility-conditioned detection probabilities, while evidence tracking prevents repeated use of the same observations. A frozen, zero-shot vision-language controller uses the updated belief to choose actions and replan. We further introduce EvoWorld-Bench, a benchmark grounded in human activity traces, comprising 54 scenes and 803,680 tasks with controlled changes before and during navigation. In simulation and real-robot experiments, EvolvingNav improves navigation success and search efficiency over the evaluated baselines. Paired experiments show the clearest gains under learnable temporal patterns, while ablations demonstrate the value of preserving uncertainty and incorporating visibility-aware evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
