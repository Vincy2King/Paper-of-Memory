# Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.02967v1
- Published: 2026-07-03
- Updated: 2026-07-03
- Authors: Joy Bose
- Tags: episodic
- Categories: cs.LG, cs.NE
- URL: http://arxiv.org/abs/2607.02967v1

## One-Sentence Summary
Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory.

进一步看，论文的核心做法或实验重点可以概括为：CALM (Nechesov and Ruponen, 2025) identifies its threshold-binary encoder as an open design question.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic
- 检索关键词命中：episodic memory, memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.NE

## Abstract Snapshot
Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory. CALM (Nechesov and Ruponen, 2025) identifies its threshold-binary encoder as an open design question. This paper evaluates rank-order N-of-M encoding (Furber et al., 2007) as an alternative. We make three contributions. First, a faithful reimplementation validates the published architecture by confirming exact equivalence between WheelSDM and RankOrderSDM (cosine similarity 1.0000 across 10 seeds) and reproducing the documented divergence of RDLIF neurons under interference. Second, multi-seed capacity experiments show RankOrderSDM outperforming StandardSDM by 13.4 percentage points at saturation in the scaled configuration and by 0.8 percentage points at the published architecture scale. Third, BER robustness experiments disentangle representation and learning effects, showing that the large robustness gain arises primarily from the interaction of rank-order encoding with MAX-Hebbian learning, while the encoder alone provides only a small advantage under matched learning conditions. Experiments on GloVe-100 embeddings confirm this small but consistent encoding benefit on real structured data, whereas sentence embeddings exhibit a ceiling effect at low memory load. A secondary analysis shows that idealized rank-order encoding requires half the component-level encoding energy of SpikingMamba's SI-LIF neurons at four-bit precision, although decoder costs dominate overall system energy. These results identify which components of the original rank-order SDM architecture provide measurable benefits for contemporary memory-augmented AI systems, offering practical guidance for architectures such as CALM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
