# Addressable Memory for Video World Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07408v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Xindi Wu, Sven Elflein, James Lucas, Olga Russakovsky, Laura Leal-Taixé, Despoina Paschalidou, Jonathan Lorraine, Aljoša Ošep
- Tags: benchmark, compression, episodic
- Categories: cs.CV, cs.LG
- URL: http://arxiv.org/abs/2608.07408v1

## One-Sentence Summary
We study visual persistence in interactive video world models.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We study visual persistence in interactive video world models.

进一步看，论文的核心做法或实验重点可以概括为：These models rely on a Key-Value (KV) cache as a growing visual memory to carry forward previously generated frames.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, episodic
- 检索关键词命中：memory compression
- 来源分类信息：cs.CV, cs.LG

## Abstract Snapshot
We study visual persistence in interactive video world models. These models rely on a Key-Value (KV) cache as a growing visual memory to carry forward previously generated frames. However, we find that models can no longer reliably address stored content once rollouts extend beyond the training horizon, because temporal Rotary Positional Embeddings (RoPE) offsets then fall outside the range seen during training and the model struggles to retrieve the relevant visual information through attention. Moreover, naively compressing the cache in the RoPE-rotated space corrupts memory by averaging together incompatible positional phases. To address this, we propose WorldTrace, a training-free memory framework for long-horizon visual persistence. WorldTrace keeps compressed memory addressable by assigning each summary slot a distinct, in-distribution virtual position. Within this addressable cache, we study two memory compression approaches: WorldTrace-Field compresses history for temporal coherence, while WorldTrace-Landmark stores verbatim scene traces at detected transitions for episodic recall. We further introduce LoopBench, a benchmark evaluating whether a compressed cache can reconstruct a previously visited scene after a long detour. WorldTrace-Field improves temporal consistency by +15.5%, and WorldTrace-Landmark improves episodic recall by +19.5% on LoopBench, extending visually persistent generation without retraining.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
