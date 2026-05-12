# Bias by Necessity: Impossibility Theorems for Sequential Processing with Convergent AI and Human Validation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.08716v1
- Published: 2026-05-09
- Updated: 2026-05-09
- Authors: Jikun Wu, Dongxin Guo, Siu-Ming Yiu
- Tags: working memory
- Categories: cs.AI, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2605.08716v1

## One-Sentence Summary
Are certain cognitive biases mathematically inevitable consequences of sequential information processing?

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Are certain cognitive biases mathematically inevitable consequences of sequential information processing?

进一步看，论文的核心做法或实验重点可以概括为：We prove that primacy effects, anchoring, and order-dependence are architecturally necessary in autoregressive language models due to causal masking constraints.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.CL, cs.LG

## Abstract Snapshot
Are certain cognitive biases mathematically inevitable consequences of sequential information processing? We prove that primacy effects, anchoring, and order-dependence are architecturally necessary in autoregressive language models due to causal masking constraints. Our three impossibility theorems establish: (1) primacy bias arises from asymmetric attention accumulation; (2) anchoring emerges from sequential conditioning with provable information bounds; and (3) exact debiasing by permutation marginalization requires factorial-time computation, with Monte Carlo approximation feasible at constant per-tolerance overhead. We validate these bounds across 12 frontier LLMs ($R^2 = 0.89$; $Δ$BIC $= 16.6$ vs. next-best alternative). We then derive quantitative predictions from the framework and test them in two pre-registered human experiments ($N = 464$ analyzed). Study 1 confirms anchor position modulates anchoring magnitude ($d = 0.52$, BF$_{10} = 847$). Study 2 shows working memory load amplifies primacy bias ($d = 0.41$, BF$_{10} = 156$), with WM capacity predicting bias reduction ($r = -.38$). These convergent findings reframe cognitive biases as resource-rational responses to sequential processing.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
