# Contextual Memory-Enhanced Source Coding for Low-SNR Communications

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.04400v1
- Published: 2026-05-06
- Updated: 2026-05-06
- Authors: Ziqiong Wang, Rongpeng Li
- Tags: context
- Categories: cs.IT, cs.LG
- URL: http://arxiv.org/abs/2605.04400v1

## One-Sentence Summary
While Separate Source-Channel Coding (SSCC) retains the practical benefits of modular system design, its effectiveness in noisy text transmission is fundamentally constrained by...

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While Separate Source-Channel Coding (SSCC) retains the practical benefits of modular system design, its effectiveness in noisy text transmission is fundamentally constrained by the fragility of autoregressive source...

进一步看，论文的核心做法或实验重点可以概括为：In low-SNR regimes, even a small number of residual bit errors after channel decoding may derail the subsequent lossless reconstruction process, especially when Arithmetic Coding (AC) relies on Large Language Model...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.IT, cs.LG

## Abstract Snapshot
While Separate Source-Channel Coding (SSCC) retains the practical benefits of modular system design, its effectiveness in noisy text transmission is fundamentally constrained by the fragility of autoregressive source decoding. In low-SNR regimes, even a small number of residual bit errors after channel decoding may derail the subsequent lossless reconstruction process, especially when Arithmetic Coding (AC) relies on Large Language Model (LLM)-based probability estimation. Existing remedies either strengthen channel decoding based solely on channel observations or introduce contextual information only at the receiver for post-hoc correction, yet neither fully addresses the fragility of source probability modeling under residual channel errors. To this end, this paper proposes a Memory-Augmented Source Coding (MASC) scheme for robust SSCC-based transmission. Rather than treating context as external side information, MASC internalizes contextual patterns into a source model shared by both the transmitter-side source encoder and the receiver-side source decoder. Specifically, MASC employs a shared Parameterized Contextual Memory (PCM) to encode multi-order $n$-gram patterns, and further introduces a Mixture-of-Memory-Experts Router (MMER) to perform sparse, hidden-state-dependent routing over memory experts during autoregressive source modeling. By adaptively activating only the most relevant memories at each coding step, MASC refines source probability estimation, shortens average codelength, and mitigates the sensitivity of source decoding to residual channel errors. Extensive experiments over Rayleigh fading and AWGN channels demonstrate the effectiveness of the proposed scheme compared with state-of-the-art methods.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
