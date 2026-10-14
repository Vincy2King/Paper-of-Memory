# REEL: Learning to Retrieve, Evaluate, and Evolve Visual Memory for Any Long-Horizon Multi-Shot Video Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.16632v1
- Published: 2026-10-12
- Updated: 2026-10-12
- Authors: Hang Xu, Guohui Zhang, Xiaoxiao Ma, Hu Yu, Jie Huang, Jiayin Xiao, Lin Song, Haoyang Huang, Nan Duan, Feng Zhao
- Tags: agent
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2610.16632v1

## One-Sentence Summary
Memory-based long-video generation aims to combine user control with long-range visual consistency.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-based long-video generation aims to combine user control with long-range visual consistency.

进一步看，论文的核心做法或实验重点可以概括为：We organize this process into three functional components: a planner, an adapter, and a generator.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Memory-based long-video generation aims to combine user control with long-range visual consistency. We organize this process into three functional components: a planner, an adapter, and a generator. Representative multi-shot systems couple memory to generator-specific interfaces or use predefined agent workflows, rather than independently training a memory policy for cross-shot objectives. We introduce REEL, a general-purpose visual-memory planner. Through a unified tool interface, REEL learns to retrieve references, create missing visual evidence, and update persistent memory. Backend-specific adapters translate its evidence plans into supported conditioning inputs, allowing the same policy to guide different black-box video generators. To train REEL, we construct two high-quality datasets, REEL-SFT-4k and REEL-RL-1k, covering diverse interaction patterns and prompt types. Training proceeds in three stages: supervised fine-tuning, single-shot Group Relative Policy Optimization (GRPO), and multi-shot GRPO. Multi-shot GRPO carries policy-generated memory across consecutive shots, so later outcomes guide earlier reference selection and memory updates. REEL-Bench tests identity preservation and intended state changes under text-only requests and timed reference-image uploads. On JoyAI-Echo~1.5 and MiniMax-H3, REEL improves cross-shot consistency on ST-Bench by 15.1\% and 20.7\%, and Core-100 on our proposed REEL-Bench by 2.41 and 8.32 points, respectively, over the no-memory baseline.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
