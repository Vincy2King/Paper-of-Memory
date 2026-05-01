# When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.27003v1
- Published: 2026-04-29
- Updated: 2026-04-29
- Authors: Qisheng Hu, Quanyu Long, Wenya Wang
- Tags: agent, context, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2604.27003v1

## One-Sentence Summary
Memory-augmented LLM agents offer an appealing shortcut to continual learning: rather than updating model parameters, they accumulate experience in external memory, seemingly...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents offer an appealing shortcut to continual learning: rather than updating model parameters, they accumulate experience in external memory, seemingly sidestepping the stability-plasticity...

进一步看，论文的核心做法或实验重点可以概括为：We show that this challenge does not disappear but resurfaces at the memory level.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Memory-augmented LLM agents offer an appealing shortcut to continual learning: rather than updating model parameters, they accumulate experience in external memory, seemingly sidestepping the stability-plasticity dilemma of parametric learning. We show that this challenge does not disappear but resurfaces at the memory level. Under a limited context window, old and new experiences compete during retrieval, relocating the continual-learning bottleneck from parameter updates to memory access. To study this phenomenon, we introduce a (k,v) framework that disentangles two fundamental design axes of external memory: how experience is represented and how it is organized for retrieval. Across sequential-task experiments in ALFWorld and BabyAI, we find that abstract procedural memories transfer more reliably than detailed trajectories, while negative transfer disproportionately harms the hard cases. Moreover, finer-grained memory organization is not universally beneficial: designs that yield strong forward transfer can simultaneously induce severe forgetting. Together, these results reveal that external memory does not resolve the continual-learning problem; it reshapes it into a problem of memory representation and retrieval design.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
