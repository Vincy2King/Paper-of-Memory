# Long-Memory Reservoir Computing for Data-Scarce Dengue Forecasting

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.11272v1
- Published: 2026-07-13
- Updated: 2026-07-13
- Authors: Rahul Goswami, Shinjini Paul, Palash Ghosh, Tanujit Chakraborty
- Tags: long-term
- Categories: stat.ML, cs.LG
- URL: http://arxiv.org/abs/2607.11272v1

## One-Sentence Summary
Accurate dengue forecasting is crucial for public health planning, but remains challenging because incidence series are often short, noisy, non-stationary, nonlinear, and often...

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Accurate dengue forecasting is crucial for public health planning, but remains challenging because incidence series are often short, noisy, non-stationary, nonlinear, and often affected by long-range temporal dependence.

进一步看，论文的核心做法或实验重点可以概括为：Fractional differencing in Autoregressive Fractionally Integrated Moving Average (ARFIMA) helps balance non-stationarity and persistence, but its linear structure limits its ability to capture nonlinear dynamics.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory
- 来源分类信息：stat.ML, cs.LG

## Abstract Snapshot
Accurate dengue forecasting is crucial for public health planning, but remains challenging because incidence series are often short, noisy, non-stationary, nonlinear, and often affected by long-range temporal dependence. Fractional differencing in Autoregressive Fractionally Integrated Moving Average (ARFIMA) helps balance non-stationarity and persistence, but its linear structure limits its ability to capture nonlinear dynamics. Deep neural networks can model nonlinear patterns, but usually require large training samples and do not explicitly encode statistical long memory. Echo State Networks (ESNs), a widely used reservoir computing framework, are attractive in this setting because they retain nonlinear recurrent dynamics while training only a simple readout, making them suitable for data-scarce scenarios. However, standard ESNs lack long-term memory from a time-series perspective. This study proposes a long-memory reservoir computing framework that integrates dedicated long-memory and short-memory ESN reservoirs with a ridge-regression readout. We introduce two variants: Fractional ESN (fESN), which incorporates fractional-differencing dynamics into the reservoir to encode long-range dependence directly, and Wavelet ESN (wESN), which extracts stable low-frequency components through wavelet smoothing before modeling them with a memory-aware reservoir. We establish theoretical guarantees for closed-loop reservoir dynamics, showing that standard ESNs induce short-memory processes under mild conditions, whereas the proposed long-memory reservoirs generate polynomially decaying dependence consistent with statistical long memory. Across multiple dengue datasets and forecasting horizons, fESN and wESN outperform statistical and deep learning baselines. Combining conformal prediction with fESN and wESN provides distribution-free calibrated uncertainty intervals.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
