# Driving on Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.31029v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Christian Löwens, Thorben Funke, Alexandru Paul Condurache
- Tags: benchmark
- Categories: cs.CV, cs.LG, cs.RO
- URL: http://arxiv.org/abs/2608.31029v1

## One-Sentence Summary
End-to-end autonomous driving models plan future trajectories from raw sensor input.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：End-to-end autonomous driving models plan future trajectories from raw sensor input.

进一步看，论文的核心做法或实验重点可以概括为：While earlier driving benchmarks often measured deviation from the human trajectory, current benchmarks such as NAVSIM and Bench2Drive evaluate models with richer simulation-based metrics intended to capture safe and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CV, cs.LG, cs.RO

## Abstract Snapshot
End-to-end autonomous driving models plan future trajectories from raw sensor input. While earlier driving benchmarks often measured deviation from the human trajectory, current benchmarks such as NAVSIM and Bench2Drive evaluate models with richer simulation-based metrics intended to capture safe and compliant driving. A high benchmark score should reflect that a model can understand the scene in front of it and act accordingly. But how much of that score specifically comes from reacting to the dynamic part of that scene? To probe this, we remove a model's camera input and replace it with memories from prior drives at the same location. The retrieved memories can provide persistent scene information, including road layout and location-conditioned regularities, but not the current traffic state. Surprisingly, memory is nearly sufficient on NAVSIM, reaching or even exceeding the performance of leading end-to-end methods without actually observing the evaluated scene. Our results suggest that a high NAVSIM score does not require a planner to react to the current traffic scene and should be treated with caution. This effect is benchmark-dependent: driving from memory causes substantially larger performance drops on Bench2Drive and RealEngine. We provide our code at https://github.com/boschresearch/MemoryDrivoR .

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
