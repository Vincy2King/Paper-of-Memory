# Fast and Scalable Caputo Fractional Gradient Descent via Perturbation-Preserving Memory Compression

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.15505v1
- Published: 2026-07-16
- Updated: 2026-07-16
- Authors: Hwanseo Lee, Junseo Lee, Hyunju Kim
- Tags: compression
- Categories: math.OC, cs.LG, cs.NE, math.NA
- URL: http://arxiv.org/abs/2607.15505v1

## One-Sentence Summary
Fractional gradient descent (FGD) incorporates long-range memory through Caputo-type operators and has been shown to improve stability in ill-conditioned and nonconvex...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Fractional gradient descent (FGD) incorporates long-range memory through Caputo-type operators and has been shown to improve stability in ill-conditioned and nonconvex optimization problems.

进一步看，论文的核心做法或实验重点可以概括为：Despite these advantages, its practical use remains limited, mainly due to the high computational cost of evaluating history-dependent convolutions, which scales quadratically with the number of iterations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：memory compression
- 来源分类信息：math.OC, cs.LG, cs.NE, math.NA

## Abstract Snapshot
Fractional gradient descent (FGD) incorporates long-range memory through Caputo-type operators and has been shown to improve stability in ill-conditioned and nonconvex optimization problems. Despite these advantages, its practical use remains limited, mainly due to the high computational cost of evaluating history-dependent convolutions, which scales quadratically with the number of iterations. In this paper, we focus on making Caputo-based optimization computationally viable without sacrificing its intrinsic memory structure. We begin by expressing the fractional descent direction as a discrete convolution over past gradients, which provides a unified view of the method. Based on this formulation, we introduce two complementary mechanisms to reduce the cost of the memory term. The first uses a sum-of-exponentials (SOE) approximation of the power-law kernel, leading to efficient recursive updates. The second approach, newly proposed in this paper as dyadic hierarchical discrete convolution (DHDC), compresses the gradient history through a multiscale aggregation strategy. Rather than treating these approximations as purely numerical accelerations, we interpret them as perturbations of the ideal Caputo operator. This viewpoint allows us to analyze how the compressed memory affects the optimization dynamics. Under standard $μ$-strong convexity and $L$-smoothness assumptions, we show that the resulting method still exhibits monotone descent and linear convergence, provided that the approximation error remains controlled.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
