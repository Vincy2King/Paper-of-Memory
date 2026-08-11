# Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.09227v1
- Published: 2026-08-10
- Updated: 2026-08-10
- Authors: Puneet Mathur, Manan Suri, Dinesh Manocha
- Tags: benchmark, compression, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.09227v1

## One-Sentence Summary
Omnimodal language models (OLMs) enable unified audio-visual understanding, but processing long joint token sequences makes inference computationally prohibitive.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Omnimodal language models (OLMs) enable unified audio-visual understanding, but processing long joint token sequences makes inference computationally prohibitive.

进一步看，论文的核心做法或实验重点可以概括为：While recent token compression methods attempt to alleviate this burden, compressing modalities in isolation often destroys the temporal cross-modal anchors necessary for coherent reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, context
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI

## Abstract Snapshot
Omnimodal language models (OLMs) enable unified audio-visual understanding, but processing long joint token sequences makes inference computationally prohibitive. While recent token compression methods attempt to alleviate this burden, compressing modalities in isolation often destroys the temporal cross-modal anchors necessary for coherent reasoning. We introduce Omni2LoRA, a two-stage framework for efficient parametric memory compression via coherence-preserving context distillation that bypasses the token bottleneck entirely. First, a Perceiver hypernetwork processes intermediate representations from a frozen OLM to encode the multimodal context into a full-rank Low-Rank Adaptation (LoRA) adapter in a single forward pass. To prevent the resulting parameter footprint from scaling linearly with recording length, we optimize a discrete rank allocation policy via Group Relative Policy Optimization (GRPO) that uses a modality-ablated counterfactual reward to explicitly penalize the loss of audio-visual coherence, forcing the model to allocate its fixed sub-linear rank budget to synergistic cross-modal anchors rather than isolated visual features. Across three omnimodal backbones, Omni2LoRA operating at a 30% rank budget outperforms direct full-context inference and strong token-compression baselines (OmniZip, OMAC, O-MARC) on four audio-visual question answering benchmarks, improving average accuracy by 8-12% over the strongest baseline and remaining stable under compression ratios as tight as 75%, where token-pruning methods degrade sharply. By converting multimodal memory into a fixed-budget, reusable parameter state, our method drives answer-time multimodal-token load to zero, cutting per-query Time to First Token (TTFT) by up to 12x relative to full-context inference and amortizing to under 0.5s after a handful of queries.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
