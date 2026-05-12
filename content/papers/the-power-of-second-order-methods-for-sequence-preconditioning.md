# The Power of Second Order Methods for Sequence Preconditioning

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.08390v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Annie Marsden, Elad Hazan
- Tags: compression
- Categories: cs.LG
- URL: http://arxiv.org/abs/2605.08390v1

## One-Sentence Summary
Sequence prediction methods for dynamical systems with long memory, i.e. marginally stable systems, typically achieve regret that grows polynomially with the hidden dimension of...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Sequence prediction methods for dynamical systems with long memory, i.e. marginally stable systems, typically achieve regret that grows polynomially with the hidden dimension of the underlying generative model.

进一步看，论文的核心做法或实验重点可以概括为：Universal Sequence Preconditioning (USP) is a method that compresses any sequence which comes from a linear dynamical system into a "preconditioned" sequence which requires exponentially shorter memory for accurate...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.LG

## Abstract Snapshot
Sequence prediction methods for dynamical systems with long memory, i.e. marginally stable systems, typically achieve regret that grows polynomially with the hidden dimension of the underlying generative model. Universal Sequence Preconditioning (USP) is a method that compresses any sequence which comes from a linear dynamical system into a "preconditioned" sequence which requires exponentially shorter memory for accurate prediction. However, the preconditioned sequence yields exponentially larger diameters and gradients, hindering USP from unlocking optimal regret bounds. Inspired by the minimum description length principle, we show that the Vovk-Azoury-Warmuth (VAW) algorithm is naturally matched to the USP regime. Indeed, it takes advantage of the memory compression while remaining robust to the exponential explosion of the diameter. We prove that combining USP with VAW achieves astoundingly strong results: for any marginally-stable linear dynamical system, this algorithm achieves polylogarithmic regret $O \left( \log^3 T \right)$ even in the presence of asymmetric hidden transition matrices. Finally, we extend the applicability of USP beyond bounded-spectrum systems by providing new complex-analytic bounds on Chebyshev polynomials, allowing for systems with constant complex arguments.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
