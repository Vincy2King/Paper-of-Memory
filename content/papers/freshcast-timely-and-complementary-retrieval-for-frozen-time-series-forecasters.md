# FreshCast: Timely and Complementary Retrieval for Frozen Time Series Forecasters

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07834v3
- Published: 2026-10-06
- Updated: 2026-10-17
- Authors: Chao He, Jianyu Xu, Xinyi Guo, Ruiqi Liu, Haobin Ding, Ruiqi He, Yuntong Xie, Dongqing Song
- Tags: context, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.07834v3

## One-Sentence Summary
Retrieval-augmented forecasting for Web and online services supplements a forecaster with the continuations of historical segments that resemble the current context.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented forecasting for Web and online services supplements a forecaster with the continuations of historical segments that resemble the current context.

进一步看，论文的核心做法或实验重点可以概括为：Most existing methods build the retrieval memory once from the training segment, leaving observations revealed after deployment unavailable as references, and generally do not calibrate how much retrieved information...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Retrieval-augmented forecasting for Web and online services supplements a forecaster with the continuations of historical segments that resemble the current context. Most existing methods build the retrieval memory once from the training segment, leaving observations revealed after deployment unavailable as references, and generally do not calibrate how much retrieved information should influence a frozen forecaster. We identify two key determinants of retrieval utility for a frozen forecaster: the timeliness of the retrieved history and its complementarity, i.e., whether the correction it induces aligns with the forecaster's residual errors; this alignment can shift between validation and deployment when the memory becomes stale. We propose FreshCast, a plug-in retrieval framework for frozen forecasters: a non-parametric streaming memory keeps writing in new observations, relational kernel regression weights candidate readouts into a memory forecast, and its correction weight is calibrated in closed form on the validation segment. Under a simplified generative model, we characterize the optimal combination gain through the second-order relation between forecaster error and memory correction, and show that periodic memory information can become redundant once the forecaster captures it. Across seven datasets, ten forecasters, and three input lengths, FreshCast reduces average MSE for every forecaster and input length, by 14.0% and 5.7% at L = 96 and 720, and achieves lower average MSE than the evaluated retrieval-augmented and online updating baselines in their comparison settings. Ablations show that post-training observations are a primary source of the gain: freezing the memory at the end of training removes most of it. For a frozen forecaster, similarity alone is not enough: useful retrieval must stay timely and provide information that the forecaster still misses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
