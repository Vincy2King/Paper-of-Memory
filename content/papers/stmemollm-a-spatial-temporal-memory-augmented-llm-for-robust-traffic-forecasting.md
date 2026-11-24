# STMemoLLM: A Spatial-Temporal Memory-Augmented LLM for Robust Traffic Forecasting

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.30148v1
- Published: 2026-11-23
- Updated: 2026-11-23
- Authors: Jian Zhou, Binqing Wu, Zongjiang Shang, Wanghui Qiu, Dongliang Cui, Chenxi Jin, Yue Yu, Xinyi Fu, Ling Chen
- Tags: compression, context, long-term
- Categories: cs.LG
- URL: http://arxiv.org/abs/2611.30148v1

## One-Sentence Summary
Traffic forecasting is essential for intelligent transportation systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Traffic forecasting is essential for intelligent transportation systems.

进一步看，论文的核心做法或实验重点可以概括为：However, traditional deep-learning models often rely heavily on high-quality observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context, long-term
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
Traffic forecasting is essential for intelligent transportation systems. However, traditional deep-learning models often rely heavily on high-quality observations. Recent LLM-based approaches incorporate pretrained knowledge to improve forecasting, but they remain sensitive to input perturbations and struggle to preserve long-term patterns. To address this, we propose STMemoLLM, a spatial-temporal memory-augmented LLM for robust traffic forecasting. STMemoLLM introduces memory prototypes to compress inputs into compact summary tokens while extracting reliable dynamics from residual signals, achieving a balance between stability and variability. Specifically, a memory-enhanced tokenizer encodes prototypes and sensor characteristics into attention biases to guide adaptive compression of correlated sensors into semantic summary tokens. A memory-calibrated router further evaluates contextual deviation, compression deficiency, and prototype alignment to identify reliable residual signals, which complement the summaries while suppressing noise. Extensive experiments on eight real-world datasets show that STMemoLLM achieves state-of-the-art performance. Additional experiments examine point masking, additive Gaussian noise, structured missingness, and limited training data, demonstrating strong robustness. Code is available at https://anonymous.4open.science/r/STMemoLLM-70BF.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
