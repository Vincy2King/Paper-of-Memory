# AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04980v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Wanqi Yang, Yuexiao Ma, Alexander Conzelmann, Xiawu Zheng, Michael W. Mahoney, T. Konstantin Rusch, Shiwei Liu
- Tags: compression
- Categories: cs.LG
- URL: http://arxiv.org/abs/2606.04980v1

## One-Sentence Summary
Mixture-of-Experts (MoE) architectures scale model capacity through sparse expert activation, but their deployment remains memory-bound because all expert weights must reside in...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Mixture-of-Experts (MoE) architectures scale model capacity through sparse expert activation, but their deployment remains memory-bound because all expert weights must reside in memory.

进一步看，论文的核心做法或实验重点可以概括为：Mixed-precision quantization can substantially reduce this footprint by assigning different bit-widths to different experts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.LG

## Abstract Snapshot
Mixture-of-Experts (MoE) architectures scale model capacity through sparse expert activation, but their deployment remains memory-bound because all expert weights must reside in memory. Mixed-precision quantization can substantially reduce this footprint by assigning different bit-widths to different experts. Existing approaches, however, typically rely on calibration data to estimate expert importance and determine bit allocation. For frontier MoE LLMs, the original training data, and hence the true training distribution, is proprietary and inaccessible. As a result, calibration sets are inevitably imperfect surrogates, and this can misestimate expert utilization and lead to suboptimal bit allocation. Motivated by the substantial cross-expert quality variability observed in modern MoE models, and by the success of Heavy-Tailed Self-Regularization (HT-SR) theory at predicting neural network model quality without access to training or testing data, we propose AlphaQ, a calibration-free bit-allocation method for MoE quantization. AlphaQ draws on HT-SR theory and follows a simple principle: experts with more heavy-tailed weight spectra are typically better trained and hence should receive higher bit-widths, while experts with weaker heavy-tailed structure can be quantized more aggressively. AlphaQ operationalizes this principle by measuring expert-wise spectral heavy-tailedness and solving a budget-constrained optimization problem that minimizes total quantization error under a global bit-budget constraint. Across several MoE models, AlphaQ consistently outperforms calibration-based baselines under matched bit budgets. Notably, on Qwen1.5-MoE, AlphaQ achieves near full-precision accuracy with an average expert precision of only 3.5 bits, while delivering more than 4$\times$ memory compression. Our code is available at https://github.com/Superone77/AlphaQ.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
