# Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01947v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Zhaotian Gu, Jie Su, Weiwei Wang, Chang Liu, Tianyi Qian, Dahui Wang
- Tags: compression
- Categories: q-bio.NC, cs.AI, cs.NE
- URL: http://arxiv.org/abs/2608.01947v1

## One-Sentence Summary
The ability to robustly maintain and update continuous variables is a hallmark of working memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The ability to robustly maintain and update continuous variables is a hallmark of working memory.

进一步看，论文的核心做法或实验重点可以概括为：While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：working memory
- 来源分类信息：q-bio.NC, cs.AI, cs.NE

## Abstract Snapshot
The ability to robustly maintain and update continuous variables is a hallmark of working memory. While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds, instead shattering the state space into discretized point attractors. To bridge this gap, we draw inspiration from divisive normalization, a canonical neural computation widely observed across cortical circuits, and propose the Recurrent Divisive Normalization Network (RDNN), a minimal and algebraically isolated model of dynamic division. Through dynamical systems analysis on canonical working memory tasks, we demonstrate that this biophysical constraint allows the network to converge to robust, high-fidelity slow manifolds. Furthermore, we analyze the gradient dynamics of divisive normalization during Backpropagation Through Time (BPTT), showing that it introduces an activity-dependent local gradient scaling. This scaling dampens parameter updates in highly active regimes, which empirically aligns with a significant self-compression of the network's effective rank, confining the recurrent dynamics to a tight, low-dimensional subspace while avoiding the optimization pathologies associated with explicit low-rank factorization. Finally, ablations demonstrate that while subtractive inhibition can maintain static memories, divisive normalization is mathematically essential to prevent manifold shattering under time-varying inputs. Our findings identify divisive normalization not merely as a biological artifact, but as a critical computational mechanism for learning high-fidelity continuous representations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
