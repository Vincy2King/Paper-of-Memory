# I see artifacts: ICA-based EEG artifact removal does not improve deep network decoding across three BCI tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.06018v1
- Published: 2026-05-07
- Updated: 2026-05-07
- Authors: Taeho Kang, Yiyu Chen, Christian Wallraven
- Tags: long-term
- Categories: cs.HC
- URL: http://arxiv.org/abs/2605.06018v1

## One-Sentence Summary
In this paper, we conduct a detailed investigation on the effect of independent component (IC)-based noise rejection methods in neural network classifier-based decoding of...

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In this paper, we conduct a detailed investigation on the effect of independent component (IC)-based noise rejection methods in neural network classifier-based decoding of electroencephalography (EEG) data in...

进一步看，论文的核心做法或实验重点可以概括为：We apply a pipeline matrix of two popular different independent component (IC) decomposition methods (Infomax and Adaptive Mixture Independent Component Analysis (AMICA)) with three different component rejection...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.HC

## Abstract Snapshot
In this paper, we conduct a detailed investigation on the effect of independent component (IC)-based noise rejection methods in neural network classifier-based decoding of electroencephalography (EEG) data in different task datasets. We apply a pipeline matrix of two popular different independent component (IC) decomposition methods (Infomax and Adaptive Mixture Independent Component Analysis (AMICA)) with three different component rejection strategies (none, ICLabel, and multiple artifact rejection algorithm [MARA]) on three different EEG datasets (motor imagery, long-term memory formation, and visual memory). We cross-validate processed data from each pipeline with three architectures commonly used for EEG classification (two convolutional neural networks and one long short-term memory-based model. We compare decoding performances on within-participant and within-dataset levels.Our results show that the benefit from using IC-based noise rejection for decoding analyses is at best minor, as component-rejected data did not show consistently better performance than data without rejections; especially given the significant computational resources required for independent component analysis (ICA) computations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
