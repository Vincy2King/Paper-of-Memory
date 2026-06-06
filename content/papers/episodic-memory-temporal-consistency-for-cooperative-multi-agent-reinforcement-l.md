# Episodic Memory Temporal Consistency for Cooperative Multi-Agent Reinforcement Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04492v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Zicheng Zhao, Yu Lan, Chengzhengxu Li, Zhaohan Zhang, Xiaoming Liu
- Tags: agent, benchmark, episodic, retrieval
- Categories: cs.LG, cs.GT
- URL: http://arxiv.org/abs/2606.04492v1

## One-Sentence Summary
Cooperative Multi-Agent Reinforcement Learning (MARL) frequently suffers from severe reward sparsity and exploration bottlenecks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Cooperative Multi-Agent Reinforcement Learning (MARL) frequently suffers from severe reward sparsity and exploration bottlenecks.

进一步看，论文的核心做法或实验重点可以概括为：While episodic memory mechanisms mitigate these issues by reusing high-return trajectories, they often trap agents in local optima due to unconstrained incentive distribution and semantic representation collapse.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, retrieval
- 检索关键词命中：episodic memory, memory retrieval
- 来源分类信息：cs.LG, cs.GT

## Abstract Snapshot
Cooperative Multi-Agent Reinforcement Learning (MARL) frequently suffers from severe reward sparsity and exploration bottlenecks. While episodic memory mechanisms mitigate these issues by reusing high-return trajectories, they often trap agents in local optima due to unconstrained incentive distribution and semantic representation collapse. To address this, we propose Episodic Memory Temporal Consistency (EMTC), a framework that robustly constructs and selectively leverages historical experiences. EMTC introduces two synergistic components: (1) a Temporally Consistent Semantic Embedder that integrates contrastive learning with time-conditioned state reconstruction, preventing representation collapse and enabling precise memory retrieval; and (2) a Temporal Consistency Gating Mechanism that dynamically modulates episodic incentives based on temporal consistency error. This adaptive gate filters misleading signals from pseudo-successful trajectories, effectively mitigating Q-value overestimation. We provide theoretical guarantees, establishing a strict error bound that directly links the observable temporal consistency error to the underlying trajectory optimality and representation quality. Extensive evaluations on the SMAC and GRF benchmarks demonstrate that EMTC consistently outperforms state-of-the-art baselines. Notably, compared to the strongest episodic baseline, EMTC achieves absolute win-rate improvements of up to 24% in super-hard SMAC scenarios and an average improvement of 28% across GRF tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
