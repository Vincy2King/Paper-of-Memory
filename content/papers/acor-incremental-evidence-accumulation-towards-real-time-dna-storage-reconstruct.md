# ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.36500v1
- Published: 2026-10-27
- Updated: 2026-10-27
- Authors: Linxuan Han, Huaming Wu, Shi Jia, Guanjin Qu
- Tags: benchmark, context
- Categories: cs.IR, q-bio.GN
- URL: http://arxiv.org/abs/2610.36500v1

## One-Sentence Summary
DNA offers high-density, durable storage by encoding digital information into synthetic strands and retrieving it through sequencing.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：DNA offers high-density, durable storage by encoding digital information into synthetic strands and retrieving it through sequencing.

进一步看，论文的核心做法或实验重点可以概括为：Sequence reconstruction combines noisy copies of each strand before downstream decoding.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：context memory
- 来源分类信息：cs.IR, q-bio.GN

## Abstract Snapshot
DNA offers high-density, durable storage by encoding digital information into synthetic strands and retrieving it through sequencing. Sequence reconstruction combines noisy copies of each strand before downstream decoding. Conventional offline methods typically reconstruct completed read clusters, separating reconstruction from ongoing read collection. Streaming reconstruction offers a way to overlap evidence processing with sequencing and reduce the computation remaining before downstream decoding. We present ACOR, a streaming consensus reconstruction method that records $k$-mer transitions and boundary support in a persistent ledger, then decodes through length-constrained beam search and priority-based selection at cluster closure. Evaluation on real and simulated DNA-storage datasets showed competitive recovery. On our own short-read next-generation sequencing (NGS) wet-lab library, ACOR combined near-complete recovery with second-scale reconstruction of more than ten million reads. A smaller public benchmark was completed in a fraction of a second. Parallel ACOR achieved speedups of tens to over a thousand-fold relative to the tested serial baseline configurations. Sparse storage reduced high-context memory requirements, while parallel execution accelerated reconstruction computation. ACOR is designed for streaming readout pipelines that process assigned reads while sequencing continues.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
