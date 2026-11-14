# MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.15315v1
- Published: 2026-11-11
- Updated: 2026-11-11
- Authors: Mingxi Zou, Yinghui Xu, Jiaxiang Chen, Langzhang Liang, Wei Zhu, Peng Ye, Runkai Zhao, Ruoxi Jiang, Sijin Chen, Song Wang, Zhuo Wang, Lizhen Qu, Zenglin Xu
- Tags: context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.15315v1

## One-Sentence Summary
Language models evolve, but the observations, revisions, and context accumulated through user interactions should remain usable.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language models evolve, but the observations, revisions, and context accumulated through user interactions should remain usable.

进一步看，论文的核心做法或实验重点可以概括为：Each new model must be able to retrieve past evidence, track revisions, and add new observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Language models evolve, but the observations, revisions, and context accumulated through user interactions should remain usable. Each new model must be able to retrieve past evidence, track revisions, and add new observations. We present MIGRO, a decoupled long-term memory system that treats experience as a persistent state shared across successive language models. MIGRO follows a simple principle: preserve historical evidence exactly, organize it approximately, and decide what to retrieve only when the question is known. We call this asymmetric fidelity with deferred selectivity. A shared semantic index supports retrieval, while exact records retain observations and their historical relationships. Because models differ in vocabulary and tokenization, host-specific interfaces convert selected evidence into inputs the receiving model can use. Reversible encoding reduces archival storage while enabling exact recovery. The shared state and its access interfaces let successive hosts read and extend the accumulated experience. On matched LoCoMo states, MIGRO scores 7.3% higher and uses 99.3% less private memory than the strongest quality baseline. After handoff, continued writing retains 99.9% of full-history rebuilding quality by extending the inherited state. On million-token BEAM histories, MIGRO uses 57.5% less private storage on average than the most compact baseline. MIGRO combines high answer quality, continued memory growth across hosts, and low storage cost. Code is available at https://github.com/zOUMINGXI/MIGRO.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
