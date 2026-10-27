# Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34251v1
- Published: 2026-10-25
- Updated: 2026-10-25
- Authors: Xinyu Liu, Daiying Tian, Chenwei Tang, Ruyang Han, Chengyang Zhang, Qingyu Zeng, Wei Ju, Liangli Zhen, Jiancheng Lv
- Tags: benchmark, compression, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.34251v1

## One-Sentence Summary
Vision-Language-Action (VLA) models have shown remarkable success in robotic manipulation, yet their ability to execute long-horizon tasks remains limited by insufficient long-...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-Language-Action (VLA) models have shown remarkable success in robotic manipulation, yet their ability to execute long-horizon tasks remains limited by insufficient long- term memory modeling.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods either rely on implicit temporal representations within policy networks, where historical information can be gradually diluted, or maintain explicit memory buffers that suffer from redundancy, noise...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Vision-Language-Action (VLA) models have shown remarkable success in robotic manipulation, yet their ability to execute long-horizon tasks remains limited by insufficient long- term memory modeling. Existing methods either rely on implicit temporal representations within policy networks, where historical information can be gradually diluted, or maintain explicit memory buffers that suffer from redundancy, noise accumulation, and inefficient retrieval. In this paper, we propose CogMemory, a novel variational cognitive memory framework that enables VLA systems to selectively preserve and reuse task-relevant historical information. Our approach encodes multimodal trajectories into compact latent memory representations through a selective state- space memory encoder, multi-slot temporal abstraction, and variational information compression. During action generation, dynamic cross-attention retrieval with gated fusion adaptively incorporates relevant memories into policy prediction. With merely 3.45M additional parameters, CogMemory stays lightweight and seamlessly fits both early- and intermediate-fusion VLA backbones. Extensive experiments on long-horizon robotic manipulation benchmarks demonstrate consistent improvements across diverse VLA backbones.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
