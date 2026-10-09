# Learning infinite context windows in recurrent architectures via spatial neural computing

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.10690v1
- Published: 2026-10-07
- Updated: 2026-10-07
- Authors: Aleix Salvador-Pomarol, Arthur N. Montanari, Earl K. Miller, Adilson E. Motter, Jorge Cortés
- Tags: benchmark, context, long-term
- Categories: cs.LG, eess.SY, q-bio.NC
- URL: http://arxiv.org/abs/2610.10690v1

## One-Sentence Summary
Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to vanishing gradients and limited...

进一步看，论文的核心做法或实验重点可以概括为：To address these limitations, we introduce a second-order recurrent model in which the standard neuron-to-neuron communication is replaced by a spatially evolving field governed by (discretized) partial differential...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG, eess.SY, q-bio.NC

## Abstract Snapshot
Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to vanishing gradients and limited receptive fields. To address these limitations, we introduce a second-order recurrent model in which the standard neuron-to-neuron communication is replaced by a spatially evolving field governed by (discretized) partial differential equations. Drawing inspiration from the role of cortical waves in brain computation, this mechanism allows structured spatiotemporal patterns to serve as an implicit, high-capacity memory. We show that the resulting model is equivalent to a structured infinite-order RNN in which the current state depends explicitly on its entire history of past states, yielding an effectively unbounded receptive field with a fixed number of parameters. We further derive constructive conditions to ensure marginal stability, constraining the gradient spectrum on the unit circle and thereby eliminating vanishing and exploding gradients. Empirically, the proposed architecture outperforms other recurrent models on long-horizon benchmarks while using substantially fewer parameters, demonstrating that spatial dynamics can effectively bridge the gap between efficient inference and long-term memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
