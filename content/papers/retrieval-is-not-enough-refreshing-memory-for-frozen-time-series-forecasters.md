# Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07834v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Chao He, Jianyu Xu, Xinyi Guo, Ruiqi Liu, Haobin Ding, Ruiqi He, Dongqing Song
- Tags: benchmark, context, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.07834v1

## One-Sentence Summary
Retrieval-augmented time-series forecasting uses the continuations of historical segments similar to the current context as references for a forecaster.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented time-series forecasting uses the continuations of historical segments similar to the current context as references for a forecaster.

进一步看，论文的核心做法或实验重点可以概括为：Most existing methods build the retrieval memory once from the training segment, leaving observations revealed after deployment unavailable as references, and generally do not calibrate how much the retrieved...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Retrieval-augmented time-series forecasting uses the continuations of historical segments similar to the current context as references for a forecaster. Most existing methods build the retrieval memory once from the training segment, leaving observations revealed after deployment unavailable as references, and generally do not calibrate how much the retrieved information should influence a frozen forecaster. We identify two key determinants of retrieval utility for a frozen forecaster: whether the history still reflects the current state, and whether the correction it induces aligns with the forecaster's residual errors, an alignment that can shift between validation and deployment when the memory becomes stale. We propose FreshCast, a plug-in retrieval framework that keeps the forecaster frozen, continuously updates a non-parametric memory with new observations, forms a memory forecast through relational kernel regression, and calibrates its weight in closed form on the validation segment. Under a simplified generative model, we characterize the optimal combination gain through the second-order relation between forecaster error and memory correction, and show that a sufficiently long look-back can make periodic memory information redundant. Across seven benchmarks and ten forecasting architectures, FreshCast reduces average MSE for every evaluated forecaster and input length, by 14.6% and 5.6% at input lengths 96 and 720, and achieves lower MSE than the evaluated retrieval-augmented and online baselines in their comparison settings. Ablations show that freezing the memory at the end of training removes most of the gain, identifying post-training observations as a primary source of improvement. For a frozen forecaster, useful historical references must remain timely and provide information that helps correct its remaining errors.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
