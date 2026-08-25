# Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.21693v1
- Published: 2026-08-22
- Updated: 2026-08-22
- Authors: Afsara Benazir, Chen Chen, Rongxiao Qu, Jiabo Huang, Jingtao Li, Lingjuan Lyu
- Tags: benchmark, compression, context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2608.21693v1

## One-Sentence Summary
Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-cache growth make deployment difficult on...

进一步看，论文的核心做法或实验重点可以概括为：Practical deployment often requires stacking multiple compression techniques: expert pruning removes redundant experts, weight quantization lowers model memory footprint, and KV-cache compression reduces long-context...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-cache growth make deployment difficult on commodity hardware. Practical deployment often requires stacking multiple compression techniques: expert pruning removes redundant experts, weight quantization lowers model memory footprint, and KV-cache compression reduces long-context memory pressure. However, these techniques are typically evaluated in isolation, leaving open how they interact when applied together in realistic deployment pipelines. In this work, we present MoEXBench, a systematic benchmark for evaluating composable MoE compression as an end-to-end deployment workflow. MoEXBench studies 10 MoE models ranging from 30B to 235B total parameters across standard-attention, hybrid linear-attention, and sliding window attention architectures. It evaluates 20%-50% expert pruning rates, 1 to 16 bit weight-quantization schemes, and multiple KV-cache precision settings, applied both individually and in combination. MoEXBench introduces an eight-module evaluation suite that jointly measures composable-compression quality, workload and architecture robustness, pruning/quantization/KV cache sensitivity, and deployment efficiency on commodity hardware. Our results reveal non-trivial interactions among compression methods: composable compression cannot be predicted from standalone techniques, compression rate alone does not reliably predict quality loss or runtime gain, expert pruning is the dominant degradation source, and average quality can hide workload and architecture-specific failures. By releasing normalized module scores, compressed artifacts, and reproducible scripts, MoEXBench enables practical accuracy-memory-latency comparison across MoE families and hardware backends.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
