# Episodic Memory from Compression Boundaries in Latent Representation Space

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents Oral
- Paper ID: openreview:En9aRT4uz8
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: David Oneil Campos Ferreira, Priscila Rocha Maia Freitas Ribeiro, EMANUEL BORGES PASSINATO, Diogo Fernandes Costa Silva, Arlindo Rodrigues Galvão Filho
- Tags: agent, compression, context, episodic, long-term
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=En9aRT4uz8

## One-Sentence Summary
Long-term memory in Large Language Model (LLM) agents requires selective persistence: only a subset of interactions should be consolidated beyond the current context window.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents Oral` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory in Large Language Model (LLM) agents requires selective persistence: only a subset of interactions should be consolidated beyond the current context window.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems rely on heuristic importance rules or similarity-based novelty, which remain external to the model’s internal computation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents Oral
- 高亮主题命中：agent, compression, context, episodic, long-term
- 检索关键词命中：episodic memory, long-term memory
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
Long-term memory in Large Language Model (LLM) agents requires selective persistence: only a subset of interactions should be consolidated beyond the current context window. Existing memory systems rely on heuristic importance rules or similarity-based novelty, which remain external to the model’s internal computation. We propose a geometric principle for memory formation: episodic memory can emerge from compression failure in latent representation space. We approximate the manifold of routine LLM activations using Sparse Autoencoders (SAEs) and define representational surprise as reconstruction error relative to this learned manifold. Deviations from routine structure yield elevated residuals, providing an unsupervised, model-internal signal for memory writing. We demonstrate this principle through ReSuME, a surprise-gated memory mechanism that commits turns to memory only when normalized reconstruction error exceeds a calibrated threshold. In long-horizon multi-turn dialogue settings, representational surprise separates routine, critical, and out-of-distribution states, and achieves a superior performance–memory trade-off compared to heuristic and similarity-based baselines under fixed budgets. Covariance-aware normalization further enables robust cross-domain calibration. These results suggest that episodic memory gating in neural agents can be grounded in intrinsic latent geometry rather than externally engineered rules.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
