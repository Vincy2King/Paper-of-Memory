# Prompt-Adapter Context Routing for Parameter-Efficient Multi-Shot Long Video Extrapolation

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.06481v1
- Published: 2026-07-07
- Updated: 2026-07-07
- Authors: Anna Córdoba, Adam Puente Tercero, Nerea Angulo Hijo, Mar Linares Tercero, Julia Barrientos, Ainhoa Miranda, Jesús Olivera
- Tags: benchmark, context
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2607.06481v1

## One-Sentence Summary
We present PACR-Video, a parameter-efficient framework for multi-shot long video extrapolation that preserves recurring entities, scene structure, visual style, and causal...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present PACR-Video, a parameter-efficient framework for multi-shot long video extrapolation that preserves recurring entities, scene structure, visual style, and causal progression without full generator fine-tuning.

进一步看，论文的核心做法或实验重点可以概括为：PACR-Video keeps a text-to-video diffusion transformer frozen and augments it with low-rank temporal adapters conditioned by learned shot-role prompt tokens.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
We present PACR-Video, a parameter-efficient framework for multi-shot long video extrapolation that preserves recurring entities, scene structure, visual style, and causal progression without full generator fine-tuning. PACR-Video keeps a text-to-video diffusion transformer frozen and augments it with low-rank temporal adapters conditioned by learned shot-role prompt tokens. To maintain long-horizon coherence, it builds a recursive prompt bank that stores compact entity, location, action, and style prompts from previous shots, then routes them through adapter gates according to predicted narrative dependencies. A Shot-Local/Story-Global tuning objective combines next-shot reconstruction, cross-shot identity contrast, and prompt sparsity regularization, while an adapter composition schedule balances early-shot visual consistency with later-shot event progression and viewpoint change. Across six multi-shot and long-video benchmarks, PACR-Video outperforms text-to-video, tuning-based, memory-augmented, streaming, and recursive-context baselines on distributional quality, semantic alignment, identity consistency, temporal smoothness, motion stability, transition coherence, and human preference. These results show that compact prompt routing and lightweight temporal adaptation provide sufficient controllable capacity for stable long video extrapolation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
