# QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.26425v2
- Published: 2026-09-22
- Updated: 2026-09-23
- Authors: Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan
- Tags: benchmark, compression
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2609.26425v2

## One-Sentence Summary
KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency.

进一步看，论文的核心做法或实验重点可以概括为：Existing 2-bit KV cache quantization methods can achieve nearly lossless performance on video benchmarks such as VBench, however, we find that they still cause severe temporal flickering and visual degradation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency. Existing 2-bit KV cache quantization methods can achieve nearly lossless performance on video benchmarks such as VBench, however, we find that they still cause severe temporal flickering and visual degradation. Meanwhile, deeper investigates show that Key quantization produces smaller reconstruction errors than Value, but surprisingly leads to much larger output degradation. We trace this discrepancy to attention: small Key perturbations can change the attention logits, i.e., QK^\top, and shift the temporal-spatial tokens selected by Queries. These observations motivate us to explicitly preserve attention logits and temporal-spatial token selection during KV cache quantization to alleviate the visual degradation problem. To address this issue, we present QuantWM, a training-free and strictly causal 2-bit KV cache quantization framework. QuantWM introduces two complementary techniques to mitigate the attention shifts. Firstly, quantization-sensitivity-aware clustering (QSAC) jointly considers historical Query sensitivity and residual ranges to select INT2-friendly Key centroids, which reduces quantization errors in channels that are more critical to attention. In addition, principal-subspace attention compensation (PSAC) restores the remaining Key errors along the dominant Query subspace using low-rank projections, which provides a direct and efficient correction to stabilize attention logits. Extensive experiments on Causal-Forcing, LingBot-World-v2, HY-World 1.5, Matrix-Game-2 and Longcat-Video demonstrate that QuantWM significantly improves visual quality and temporal consistency, while outperforming existing methods across image and video quality metrics with up to 6.20x KV cache memory compression and limited additional overhead.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
