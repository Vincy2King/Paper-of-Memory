# Memory-Augmented Online Test-Time Adaptation for EEG Motor Imagery via Perturbation Consistency and Confidence Calibration

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.30422v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Kunkun Zhang, Kehao Wu, Zhitao Chen, Haigen Hu, Qianwei Zhou
- Tags: memory-augmented
- Categories: cs.LG, eess.SP
- URL: http://arxiv.org/abs/2610.30422v1

## One-Sentence Summary
Recently, electroencephalography (EEG)-based brain--computer interfaces (BCIs) have gained traction as portable neural measurement systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recently, electroencephalography (EEG)-based brain--computer interfaces (BCIs) have gained traction as portable neural measurement systems.

进一步看，论文的核心做法或实验重点可以概括为：However, the practical deployment of these instruments is often hindered by nonstationarity and cross-subject distribution shifts, which lead to significant intersubject inconsistency.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, eess.SP

## Abstract Snapshot
Recently, electroencephalography (EEG)-based brain--computer interfaces (BCIs) have gained traction as portable neural measurement systems. However, the practical deployment of these instruments is often hindered by nonstationarity and cross-subject distribution shifts, which lead to significant intersubject inconsistency. Existing adaptation methods remain impractical for real-time measurement scenarios, as they typically require offline access to source or aggregated target data. To address these challenges, this article proposes memory-augmented online test-time adaptation (OTTA) with perturbation consistency and confidence calibration (MOPC), a source-free framework designed to enhance the reliability of BCI instrumentation. MOPC enables the measurement system to update its decoding parameters on the fly during the inference stage, facilitating single-pass adaptation without accessing sensitive source data. We introduce random-mask perturbations to enforce prediction consistency against inherent EEG signal noise and acquisition artifacts. Furthermore, a confidence-calibrated reweighting loss is designed to integrate feature-space similarity, effectively mitigating unreliable pseudolabels and class imbalance during continuous signal acquisition. To ensure system stability and prevent the catastrophic forgetting of established neural patterns, a lightweight memory module is incorporated to regularize parameter updates within a tight latency budget. Evaluated on the BCI IV IIb and OpenBMI datasets, MOPC achieves state-of-the-art performance, outperforming prior methods by 2.22~\% and 3.67~\%, respectively, while keeping the per-trial adaptation latency to approximately 40--60 ms. This study provides a robust, recalibration-free solution for real-time EEG decoding, marking a significant advancement in the precision and usability of practical BCI measurement instruments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
