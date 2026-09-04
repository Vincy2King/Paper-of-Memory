# TRACE: Spatiotemporal Contact Memory Graph Network Simulator for Granular Dynamics

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.02991v1
- Published: 2026-09-02
- Updated: 2026-09-02
- Authors: Changjian Zhou, Negin Yousefpour, Jie Qi, Junfeng Fang, Guillermo A. Narsilio, Hans Petter Jostad
- Tags: benchmark
- Categories: cs.LG, math.NA, stat.ML
- URL: http://arxiv.org/abs/2609.02991v1

## One-Sentence Summary
Learned graph simulators provide an efficient alternative to high-fidelity solvers for granular dynamics.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Learned graph simulators provide an efficient alternative to high-fidelity solvers for granular dynamics.

进一步看，论文的核心做法或实验重点可以概括为：However, granular motion depends strongly on inter-granular contact history, which is difficult to preserve when particle contacts form, break, and rearrange.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, math.NA, stat.ML

## Abstract Snapshot
Learned graph simulators provide an efficient alternative to high-fidelity solvers for granular dynamics. However, granular motion depends strongly on inter-granular contact history, which is difficult to preserve when particle contacts form, break, and rearrange. Existing simulators mainly store temporal information in node features or node-level memory. Here we introduce TRACE, a graph-network simulator that stores interaction history directly on contact edges. Each edge maintains a persistent memory updated by attention-based message passing and a gated recurrent unit, while an edge-identity dictionary preserves this memory as the contact graph changes. A physics-structured decoder predicts inter-granular normal and tangential contact forces, enforces the Coulomb friction limit, and applies equal-and-opposite internal forces. The model is trained with single-step pretraining followed by autoregressive rollout fine-tuning. We evaluate TRACE on 2D and 3D granular column-collapse benchmarks. In both cases, TRACE produces stable, physically consistent long-horizon rollouts, closely reproducing the final deposit geometry and the kinetic energy released during collapse. Compared with graph network simulator (GNS) and node-memory graph neural simulator (NMGNS), TRACE reduces long-rollout position error by 31-62% and final-deposit error by 58-89% across the two benchmarks, while using fewer parameters and maintaining near-zero particle interpenetration. TRACE also achieves 12.2$\times$ and 8.9$\times$ speedups over the material point method (MPM) reference solver in 2D and 3D, respectively. Our code is available at https://github.com/Data-Driven-Computational-Geotechnics/TRACE.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
