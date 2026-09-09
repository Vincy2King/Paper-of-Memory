# What a Deletion Certificate Covers, and Where It Expires: Auditable Removal from a Support-Vector Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.12204v3
- Published: 2026-07-13
- Updated: 2026-09-06
- Authors: Vishwajith Ramesh
- Tags: context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2607.12204v3

## One-Sentence Summary
A dense key--value cache gives an operator no way to verify a deletion: it does not say which stored entries currently contribute nothing to the output, and it offers no...

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A dense key--value cache gives an operator no way to verify a deletion: it does not say which stored entries currently contribute nothing to the output, and it offers no reference state that the edited memory should...

进一步看，论文的核心做法或实验重点可以概括为：We build a context memory whose entries carry explicit weights and ask what a deletion certificate over it can cover and where it expires.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG

## Abstract Snapshot
A dense key--value cache gives an operator no way to verify a deletion: it does not say which stored entries currently contribute nothing to the output, and it offers no reference state that the edited memory should match. We build a context memory whose entries carry explicit weights and ask what a deletion certificate over it can cover and where it expires. A one-class support-vector boundary fit around the keys of a context at test time supplies the coefficients used in the readout, so that each key is active (positive coefficient) or reserve (zero coefficient). Removing a reserve key leaves the readout unchanged without a re-solve, and deleting an active key with a decremental solver reaches the same state as re-solving on the remaining keys at the same coefficient cap. A three-key construction shows the limit of both properties: an inert key can acquire positive weight after one more token is admitted, so reserve status certifies the present solve and does not license permanent pruning. In $1,200$ double-precision trials on Gaussian, near-duplicate, clinical (MIMIC-IV vitals), and learned keys, every trial reached the reference state, all but one through the maintained update, with median gate-score disagreement below $10^{-6}$ in every regime and a worst case of $1.1\times10^{-2}$ associated with numerically near-tied solutions and partition disagreement; maintained deletion ran $24$--$223$ times faster than re-solving. Declaring a minimum-norm tie-break as part of the reference, at a tolerance above the two solvers' disagreement in objective value, brings the worst readout disagreement below $2\%$ of the readout range in every regime and leaves a gate-score disagreement of up to $4.2\times10^{-3}$. A deletion certificate should name its reference state and validity horizon. We show what a system must retain, or refuse to admit, to extend that horizon.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
