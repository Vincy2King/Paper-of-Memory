# Reasoning as Attractor Dynamics: Latent Memory Retrieval via Gibbs-Weighted Energy Minimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.24543v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Kanishk Awadhiya
- Tags: retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2606.24543v1

## One-Sentence Summary
Large Language Models (LLMs) are traditionally viewed as autoregressive generators.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) are traditionally viewed as autoregressive generators.

进一步看，论文的核心做法或实验重点可以概括为：However, from the perspective of collective computation, they function as high-dimensional Dense Associative Memories that store complex reasoning patterns as latent attractors.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.LG

## Abstract Snapshot
Large Language Models (LLMs) are traditionally viewed as autoregressive generators. However, from the perspective of collective computation, they function as high-dimensional Dense Associative Memories that store complex reasoning patterns as latent attractors. In this work, we investigate the energy landscape of mathematical reasoning. We posit that correct reasoning chains correspond to deep, wide attractor basins ("flat minima") in the model's output distribution, whereas hallucinations manifest as sharp, unstable local minima. To exploit this geometry, we introduce a retrieval mechanism based on a Gibbs measure of the trajectory's spectral entropy. By sampling multiple reasoning paths and weighting them by their inverse energy ($P \propto e^{-βE}$), we approximate the equilibrium distribution of the associative memory, effectively ``relaxing'' the system into a robust solution. Empirically, this physics-inspired mechanism improves Microsoft Phi-3.5 performance on GSM8K by 5.38\% (84.7\% $\to$ 90.1\%), demonstrating that inference is better modeled as a dynamic settling process into an attractor basin rather than greedy next-token prediction.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
