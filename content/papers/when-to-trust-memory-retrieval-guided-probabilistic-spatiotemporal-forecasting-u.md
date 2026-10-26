# When to Trust Memory: Retrieval-Guided Probabilistic Spatiotemporal Forecasting under Distribution Shift

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.32329v1
- Published: 2026-10-23
- Updated: 2026-10-23
- Authors: Haochen Lv, Jianhao Zhang, Zhichen Lei, Yang Jiang, Xiaowei Mao, Shengnan Guo, Youfang Lin, Huaiyu Wan
- Tags: retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.32329v1

## One-Sentence Summary
Spatiotemporal forecasting plays an important role in real-world applications, where probabilistic approaches provide uncertainty estimates for decision-making.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Spatiotemporal forecasting plays an important role in real-world applications, where probabilistic approaches provide uncertainty estimates for decision-making.

进一步看，论文的核心做法或实验重点可以概括为：Real-world systems are inherently non-stationary, leading to distribution shifts between training and test data.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.LG

## Abstract Snapshot
Spatiotemporal forecasting plays an important role in real-world applications, where probabilistic approaches provide uncertainty estimates for decision-making. Real-world systems are inherently non-stationary, leading to distribution shifts between training and test data. However, existing probabilistic methods mainly focus on modeling data distributions under standard settings, while distribution shift methods often handle such shifts in a coarse manner, failing to characterize shift degree and adapt prediction strategy accordingly. As a result, they often produce miscalibrated and unreliable forecasts. To address this issue, we propose REMIND, a retrieval-guided probabilistic framework for spatiotemporal forecasting under distribution shift. REMIND leverages retrieval to estimate how well current observation are supported by historical patterns, enabling adaptive prediction under different shift regimes. It employs spatiotemporal retrieval to construct a memory bank and introduces a dual branch architecture, combining a memory-calibrated probabilistic branch for mild shifts with a deviation-aware probabilistic branch for severe shifts. A shift-adaptive gate, guided by retrieval similarity and memory dispersion, balances the two branches according to shift degree. We further design a hierarchical Gaussian mixture to capture heterogeneous uncertainty over the dual branch predictions, and introduce a memory perturbation training scheme to improve generalization. Experiments on real-world datasets with distribution shifts demonstrate that REMIND consistently outperforms state-of-the-art methods in both forecasting accuracy and probabilistic prediction quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
