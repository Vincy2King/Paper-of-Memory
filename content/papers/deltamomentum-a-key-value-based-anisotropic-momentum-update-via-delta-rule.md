# DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.19491v1
- Published: 2026-08-19
- Updated: 2026-08-19
- Authors: Euijin Hong, Guannan Qu
- Tags: persistent memory
- Categories: cs.LG, cs.CL, math.OC, stat.ML
- URL: http://arxiv.org/abs/2608.19491v1

## One-Sentence Summary
Most modern optimizers form their momentum as an exponential moving average (EMA) of past gradients, forgetting every direction at one fixed rate.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Most modern optimizers form their momentum as an exponential moving average (EMA) of past gradients, forgetting every direction at one fixed rate.

进一步看，论文的核心做法或实验重点可以概括为：However, the inputs a deep network sees during training can be highly anisotropic, with a few directions queried frequently while most are seen rarely.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, cs.CL, math.OC, stat.ML

## Abstract Snapshot
Most modern optimizers form their momentum as an exponential moving average (EMA) of past gradients, forgetting every direction at one fixed rate. However, the inputs a deep network sees during training can be highly anisotropic, with a few directions queried frequently while most are seen rarely. Recent methods address this anisotropy by wrapping extra processing around this buffer, leaving the momentum update itself unchanged. We propose DeltaMomentum, which builds direction-awareness into the momentum update rule. The main observation is that the gradient of a linear layer splits into an input that acts as a key and an output-side error that acts as a value. Exploiting the key-value structure, DeltaMomentum updates the momentum buffer by the canonical delta rule, so each direction is forgotten at a rate set by how often it appears. We prove that it is a valid momentum, that it applies the input-side curvature correction without matrix inversion, and that it clears stale directions faster than EMA under both a fixed and a drifting optimum. It is a drop-in replacement for the momentum buffer of any optimizer, its coefficient transfers across widths under $μ$P, and its extra compute stays between $22.2\%$ and $25.0\%$ of a gated-MLP block's linear cost with no persistent memory. In FineWeb-Edu pretraining, AdamW with DeltaMomentum (DeltaAdamW) reaches AdamW's validation loss in up to $46.39 \pm 4.32\%$ fewer steps at 67M and $22.12 \pm 0.80\%$ at 370M over three seeds, and the gain persists at 1B on a Chinchilla-optimal budget. A Muon baseline tuned under the same protocol sits above DeltaAdamW at both language-model scales, and the gain holds for SGD, ResNet-18, and ViT-Tiny on CIFAR-10. Training-time diagnostics confirm the predicted mechanism, better gradient tracking and healthier input directions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
