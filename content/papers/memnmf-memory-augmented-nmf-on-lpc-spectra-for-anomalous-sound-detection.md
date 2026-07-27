# MemNMF: Memory-Augmented NMF on LPC Spectra for Anomalous Sound Detection

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.22086v1
- Published: 2026-07-24
- Updated: 2026-07-24
- Authors: Phurich Saengthong, Takahiro Shinozaki
- Tags: memory-augmented
- Categories: cs.SD, cs.LG
- URL: http://arxiv.org/abs/2607.22086v1

## One-Sentence Summary
Autoencoder-based anomalous sound detection is attractive for machine condition monitoring because it can be trained using only normal recordings and yields an interpretable...

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Autoencoder-based anomalous sound detection is attractive for machine condition monitoring because it can be trained using only normal recordings and yields an interpretable anomaly score from reconstruction error.

进一步看，论文的核心做法或实验重点可以概括为：Most prior work uses spectrogram autoencoders, but reconstructing detailed time--frequency patterns is sensitive to noise and transients, and models can reconstruct some anomalous inputs well, weakening normal--...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.SD, cs.LG

## Abstract Snapshot
Autoencoder-based anomalous sound detection is attractive for machine condition monitoring because it can be trained using only normal recordings and yields an interpretable anomaly score from reconstruction error. Most prior work uses spectrogram autoencoders, but reconstructing detailed time--frequency patterns is sensitive to noise and transients, and models can reconstruct some anomalous inputs well, weakening normal--anomaly separation. We propose MemNMF, a constrained reconstruction method that operates on the Linear Predictive Coding spectrum, a compact estimate of the spectral envelope. MemNMF initializes a memory module from an NMF dictionary learned on normal LPC spectra and reconstructs each input as an attention-weighted combination of prototypical normal spectral patterns. Experiments on MIMII and DCASE 2020 Task 2 across multiple machine types and operating conditions show that LPC-spectrum inputs improve a standard autoencoder baseline and that MemNMF yields further gains, with especially strong robustness under noisy, non-stationary settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
