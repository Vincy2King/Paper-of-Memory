# TinySAM 2: Extreme Memory Compression for Efficient Track Anything Model

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.18013v1
- Published: 2026-05-18
- Updated: 2026-05-18
- Authors: Zhaoyuan Ding, Yijing Yang, Han Shu, Xinghao Chen
- Tags: compression
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2605.18013v1

## One-Sentence Summary
Segment Anything Model 2 (SAM 2) serves as a core foundation model in the field of video segmentation.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Segment Anything Model 2 (SAM 2) serves as a core foundation model in the field of video segmentation.

进一步看，论文的核心做法或实验重点可以概括为：Building upon the original SAM model, it introduces a memory bank mechanism and demonstrates outstanding performance in tasks such as semi-supervised video object segmentation and tracking anything.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Segment Anything Model 2 (SAM 2) serves as a core foundation model in the field of video segmentation. Building upon the original SAM model, it introduces a memory bank mechanism and demonstrates outstanding performance in tasks such as semi-supervised video object segmentation and tracking anything. However, the complex computational characteristics of SAM 2's multi-stage image encoder and memory module have raised the barrier to the model's deployment in practical applications. To address this issue, we propose TinySAM 2, a lightweight video segmentation model that balances performance and efficiency. First, a memory quality management mechanism is introduced to select and retain high-informative historical frames as the memory. In addition, a joint-spatial-temporal token compression is proposed that reduces the memory storage and computational cost. Specifically, average pooling is employed to first compress redundancy tokens in the spatial domain. In the temporal domain, informative tokens are selected across frames in the memory bank based on token-level similarity measurement. Besides, we take RepViT as the lightweight image encoder, which further reduces the model parameters. Extensive experiments on challenging datasets such as DAVIS and SA-V demonstrate that TinySAM 2 achieves 90% of the performance of SAM 2.1, with only 7% memory tokens and 3% training data. This study effectively alleviates the bottlenecks in parameter count, computational load, and deployment costs associated with SAM 2, providing a resource-efficient solution for the widespread application of video segmentation models on devices.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
