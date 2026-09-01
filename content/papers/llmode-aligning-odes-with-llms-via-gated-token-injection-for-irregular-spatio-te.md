# LLMODE: Aligning ODEs with LLMs via Gated Token Injection for Irregular Spatio-Temporal Forecasting

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.29640v1
- Published: 2026-08-30
- Updated: 2026-08-30
- Authors: Di Zhang, Jingyang Zhang, Ziqian Wang, Chi Zhang, Yikun Ban, Ziwei Zhang, Ruijie Wang
- Tags: benchmark, context
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2608.29640v1

## One-Sentence Summary
Large language models (LLMs) have shown promise for spatio-temporal forecasting, but existing approaches often rely on regularly sampled token sequences and struggle with...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) have shown promise for spatio-temporal forecasting, but existing approaches often rely on regularly sampled token sequences and struggle with irregular observations because of temporal...

进一步看，论文的核心做法或实验重点可以概括为：We propose LLMODE, a token-efficient framework for irregular spatio-temporal forecasting with a frozen LLM backbone.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Large language models (LLMs) have shown promise for spatio-temporal forecasting, but existing approaches often rely on regularly sampled token sequences and struggle with irregular observations because of temporal asynchrony, representation-space misalignment, and limited context windows. We propose LLMODE, a token-efficient framework for irregular spatio-temporal forecasting with a frozen LLM backbone. LLMODE first uses a graph-aware ODE encoder to reconstruct irregular graph observations as a continuous-time latent trajectory. A Fixed-Budget Perceiver Resampler then compresses this variable-length trajectory into a fixed number of dynamic memory tokens. In parallel, compact statistical descriptors are encoded and resampled into context memory tokens. A dual-source gated cross-attention module injects both memories into the frozen LLM, enabling controlled utilization of external spatio-temporal evidence. Experiments on three real-world urban datasets and two physical-dynamics benchmarks show competitive overall performance, with clearer advantages under sparse or dynamically complex irregular sampling. Additional evaluations on unseen urban regions further demonstrate strong zero-shot generalization without adaptation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
