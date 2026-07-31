# Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.27919v1
- Published: 2026-07-30
- Updated: 2026-07-30
- Authors: Rubin Wei, Jiaqi Cao, Jiarui Wang, Junming Zhang, Qipeng Guo, Bowen Zhou, Zhouhan Lin
- Tags: benchmark, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2607.27919v1

## One-Sentence Summary
Decoder-only language models entangle long-term memory and reasoning in a single parameter set, making it difficult to scale memory capacity independently.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Decoder-only language models entangle long-term memory and reasoning in a single parameter set, making it difficult to scale memory capacity independently.

进一步看，论文的核心做法或实验重点可以概括为：Memory Decoder introduces a parametric long-term memory module but only studies it at a relatively small scale.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Decoder-only language models entangle long-term memory and reasoning in a single parameter set, making it difficult to scale memory capacity independently. Memory Decoder introduces a parametric long-term memory module but only studies it at a relatively small scale. In this work, we present Memory Decoder at Scale, scaling memory models up to 6.9B parameters and pretraining them on 300B tokens. At this data scale, the combined cost of indexing and search makes a standard Faiss pipeline infeasible. We address this bottleneck with a distributed pipeline for Faiss indexing and retrieval, together with sparse, batch-wise loading of kNN distributions. Across model scales, we find that allocating more parameters to memory yields a better parameter-performance tradeoff than scaling the base model alone. On 17 benchmarks, pairing a 6.9B general memory with Pythia-410M raises its average score from 29.86 to 37.34, surpassing Pythia-12B (37.24) with 39% fewer total parameters. For Qwen3 Base models ranging from 0.6B to 14B, 1.7B domain memories improve the average score across the three domains by more than 9 points at every scale. Overall, our results demonstrate that independently scaling pretrained memory offers a more parameter efficient path to improving language model performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
