# AdaHOP: Fast and Accurate Low-Precision Training via Outlier-Pattern-Aware Rotation

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.02525v2
- Published: 2026-04-02
- Updated: 2026-05-07
- Authors: Seonggon Kim, Alireza Khodamoradi, Pranathi Vasireddy, Kristof Denolf, Eunhyeok Park
- Tags: compression
- Categories: cs.LG
- URL: http://arxiv.org/abs/2604.02525v2

## One-Sentence Summary
Hadamard transforms have become a key tool for stabilizing low-precision training, but existing methods apply them uniformly across tensors and computation paths.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Hadamard transforms have become a key tool for stabilizing low-precision training, but existing methods apply them uniformly across tensors and computation paths.

进一步看，论文的核心做法或实验重点可以概括为：We show that this one-size-fits-all strategy is inherently limited: Hadamard smoothing reduces quantization error only when its direction is properly aligned with the operand's outlier structure.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.LG

## Abstract Snapshot
Hadamard transforms have become a key tool for stabilizing low-precision training, but existing methods apply them uniformly across tensors and computation paths. We show that this one-size-fits-all strategy is inherently limited: Hadamard smoothing reduces quantization error only when its direction is properly aligned with the operand's outlier structure. Through a systematic study of weights, activations, and gradients in LLM training, we identify three stable outlier patterns, Row-wise, Column-wise, and None, and show that each outlier pattern pair in matrix multiplication requires a distinct transform or outlier-handling strategy. We propose AdaHOP, Adaptive Hadamard transform with Outlier-Pattern-aware strategy, which applies Inner Hadamard Transform (IHT) when inner-dimension mixing properly suppresses the operands' outliers, and selectively applies Outlier Extraction (OE) that extracts dominant outlier rows or columns into a high-precision path when it does not. With fused, hardware-aware Triton kernels, AdaHOP enables training from scratch at MXFP4 precision with BF16-level quality, while achieving up to 3.6X memory compression, 1.46X end-to-end training speedup over BF16.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
