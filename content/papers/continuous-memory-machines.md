# Continuous Memory Machines

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07907v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Ciaran Regan, Kai Arulkumaran, Luke Darlow, Stefania Druga, Sebastian Risi, Llion Jones
- Tags: context, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.07907v1

## One-Sentence Summary
Recurrent neural networks typically compress information into a single vector-valued recurrent state, forcing short-term computation and long-term retention to share the same...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recurrent neural networks typically compress information into a single vector-valued recurrent state, forcing short-term computation and long-term retention to share the same representation.

进一步看，论文的核心做法或实验重点可以概括为：Past extensions alleviate this bottleneck by increasing the memory capacity or separating timescales, but lack the combination of rapid neuron-level processing and longer-term retention found in biology.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Recurrent neural networks typically compress information into a single vector-valued recurrent state, forcing short-term computation and long-term retention to share the same representation. Past extensions alleviate this bottleneck by increasing the memory capacity or separating timescales, but lack the combination of rapid neuron-level processing and longer-term retention found in biology. To that end, we introduce the Continuous Memory Machine (CMM), a recurrent architecture with matrix-valued short- and long-term memory states serving distinct functional roles. Building on the Continuous Thought Machine (CTM), the CMM's short-term memory tracks recent neural activity, with uniquely parameterized neuron-level models learning to use these activity patterns for computation. A persistent long-term memory stores information for later use, with a Transformer jointly updating both memory stores, providing an expressive bidirectional read--write mechanism such that each store can reorganize its own contents and both read from and write to the other. Across algorithmic, in-context learning, and recurrent reasoning tasks, the CMM outperforms a broad suite of baselines, exhibiting stronger generalization than prior memory-augmented networks while preserving the CTM's interpretable attention patterns. Code is available at https://github.com/SakanaAI/continuous-memory-machines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
