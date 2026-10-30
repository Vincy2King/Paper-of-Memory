# The Cost of Working Memory in Streaming Mean Estimation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.39540v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Zeyu Wu, Zihao Wang, Minghua Deng
- Tags: compression
- Categories: stat.ML, cs.LG
- URL: http://arxiv.org/abs/2610.39540v1

## One-Sentence Summary
A streaming estimator must compute from the evidence that fits in memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A streaming estimator must compute from the evidence that fits in memory.

进一步看，论文的核心做法或实验重点可以概括为：We determine when storing an accurate mean is easier than computing it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression
- 检索关键词命中：working memory
- 来源分类信息：stat.ML, cs.LG

## Abstract Snapshot
A streaming estimator must compute from the evidence that fits in memory. We determine when storing an accurate mean is easier than computing it. For Gaussian mean estimation over the Euclidean unit ball in $\mathbb{R}^d$, we establish the minimax rate under squared error with $K$ persistent states, a known horizon, and a public time index: $\min\{1, K^{-2/d}+\frac{d}{n} (1+\frac{\log(ed)}{1+(\log K)/d})\}$. Unrestricted computation followed by $K$-level encoding has rate $\min\{1,d/n+K^{-2/d}\}$. At a fixed sufficiently small error, statistically optimal sample size therefore requires order $d\log d$ working bits, while order $d$ bits suffice to store the answer. The lower bound tracks repeated state compression through an entropy potential obtained by Gaussian smoothing. A matching construction combines a multiscale modular counter with workspace reused across coordinate groups. In one dimension, it attains the terminal rate $n^{-1}+K^{-2}$. Any fixed confidence requirement that the realized loss not exceed the zero baseline preserves these rates. Increasing confidence creates a further memory requirement: at fixed nontrivial risk in every fixed dimension, failure probability $e^{-γn}$ requires and permits order $\log n$ working states for sufficiently small fixed $γ>0$. In the scalar problem, a fixed terminal alphabet suffices under the same protection. These bounds separate the memory needed to represent an answer from the memory needed to accumulate evidence and validate a decision.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
