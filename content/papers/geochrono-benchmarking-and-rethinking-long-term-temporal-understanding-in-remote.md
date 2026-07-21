# GeoChrono: Benchmarking and Rethinking Long-Term Temporal Understanding in Remote Sensing

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.15768v1
- Published: 2026-07-17
- Updated: 2026-07-17
- Authors: Yujie Li, Jiancheng Pan, Zhiwei Wei, Jiuniu Wang, Mugen Peng, Wenjia Xu
- Tags: benchmark, long-term
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2607.15768v1

## One-Sentence Summary
Remote sensing offers an unparalleled vantage point for observing the Earth's long-term surface evolution, yet it demands that a model not only perceive land cover at isolated...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Remote sensing offers an unparalleled vantage point for observing the Earth's long-term surface evolution, yet it demands that a model not only perceive land cover at isolated moments, but also track changes, memorize...

进一步看，论文的核心做法或实验重点可以概括为：However, existing studies lack a systematic evaluation that dissects these distinct competencies.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Remote sensing offers an unparalleled vantage point for observing the Earth's long-term surface evolution, yet it demands that a model not only perceive land cover at isolated moments, but also track changes, memorize evolution histories, and reason across time and space. However, existing studies lack a systematic evaluation that dissects these distinct competencies. To fill this gap, we introduce ChronoBench, a multidimensional benchmark that decomposes this task into four progressive cognitive levels (i.e., Land Cover Perception, Temporal Recognition, Long-Term Memory, and Spatio-Temporal Reasoning). The ChronoBench comprises 12 sub-tasks and 17,689 rigorously validated QA (Question-Answer) pairs. Extensive evaluations reveal that mainstream MLLMs fall drastically behind human experts, with Long-Term Memory emerging as the most critical bottleneck. Motivated by this finding, we further propose GeoChrono, an MLLM with enhanced capabilities for tracing, memorizing, and reasoning about long-term geographic evolution. Leveraging the physical prior that geographic parcels remain spatially fixed while their semantics evolve, we design a Temporal Trajectory Encoder~(TempEnc) that constructs per-location temporal trajectories for dedicated land cover evolution modeling, and we introduce a Coarse-to-Fine Token Compressor~(C2FComp) that adaptively preserves dynamic regions while compressing the static background. To support training, we also construct ChronoInstruct, a 104K-sample instruction-tuning dataset spanning all competency levels for training. GeoChrono achieves state-of-the-art performance on ChronoBench, surpassing the leading commercial MLLMs by over 20%, while C2FComp reduces visual tokens by over 56% while retaining GeoChrono's 94.6% performance. The code and data will be available at https://github.com/IntelliSensing/GeoChrono

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
