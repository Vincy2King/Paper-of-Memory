# RecMem: Recurrent Memory Compression for Long-Sequence Generative Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.17921v1
- Published: 2026-11-13
- Updated: 2026-11-13
- Authors: Haoyi Hu, Gaoyang Guo, Yunjia Xi, Wen Chen, Weiwen Liu, Jian Wu, Yuning Jiang, Weinan Zhang
- Tags: compression, context, retrieval
- Categories: cs.AI, cs.IR
- URL: http://arxiv.org/abs/2611.17921v1

## One-Sentence Summary
Generative recommendation benefits from long interaction histories, but the cost of processing them directly grows with history length.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Generative recommendation benefits from long interaction histories, but the cost of processing them directly grows with history length.

进一步看，论文的核心做法或实验重点可以概括为：We propose RecMem, a recurrent memory compression framework guided by three desiderata: space invariance, semantic fidelity, and lifelong evolvability.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context, retrieval
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI, cs.IR

## Abstract Snapshot
Generative recommendation benefits from long interaction histories, but the cost of processing them directly grows with history length. We propose RecMem, a recurrent memory compression framework guided by three desiderata: space invariance, semantic fidelity, and lifelong evolvability. RecMem compresses historical segments into a fixed set of memory slots using a bifurcated encoder-decoder with shared lower layers and slot-wise forget-gated updates. Recommendation supervision trains the memory to preserve predictive information, while stream-consistency training aligns predictions from sequential and packed processing. By construction, the memory state and decoder context are independent of history length; under contraction and approximate semigroup consistency, we further derive a horizon-independent bound on the state discrepancy between these two processing orders. On MerRec, RecMem uses 16 memory slots and a 216-token decoder context, compared with 1,200 tokens for HSTU-1200, while retaining 87.9% of HSTU-1200's Recall@10 and 97.0% of its Recall@200. It outperforms PHSTU and the evaluated recent-only and retrieval baselines, and analyses of distant history show that archived interactions contribute predictive signal.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
