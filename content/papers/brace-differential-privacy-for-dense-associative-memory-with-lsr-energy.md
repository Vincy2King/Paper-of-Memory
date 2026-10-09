# BRACE: Differential Privacy for Dense Associative Memory with LSR Energy

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11218v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Chang Qu, Zhaoyang Shi
- Tags: retrieval
- Categories: cs.CR, cs.LG
- URL: http://arxiv.org/abs/2610.11218v1

## One-Sentence Summary
Dense associative memory (DAM) provides an energy-based framework for memory retrieval with close connections to attention mechanisms in modern artificial intelligence.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Dense associative memory (DAM) provides an energy-based framework for memory retrieval with close connections to attention mechanisms in modern artificial intelligence.

进一步看，论文的核心做法或实验重点可以概括为：Despite growing interest in differential privacy for AI, the privacy of DAM retrieval dynamics remains relatively unexplored.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CR, cs.LG

## Abstract Snapshot
Dense associative memory (DAM) provides an energy-based framework for memory retrieval with close connections to attention mechanisms in modern artificial intelligence. Despite growing interest in differential privacy for AI, the privacy of DAM retrieval dynamics remains relatively unexplored. In this paper, we develop a differential privacy framework for log-sum-ReLU (LSR) dense associative memory, whose finite-support retrieval dynamics pose distinctive challenges for privacy-preserving computation. We propose the Boundary-Responsive Adaptive Correction Evolution (BRACE) algorithm, a differentially private retrieval mechanism for LSR-DAM that adaptively corrects boundary-sensitive perturbations to control their cumulative effect over the retrieval trajectory. In theory, we prove that our method is minimax optimal by deriving dimension-independent terminal and full-trajectory retrieval error rates, with optimal dependence on the inverse temperature and, in the growing-horizon regime, the retrieval horizon. We further establish central limit theorems that enable uncertainty quantification for private retrieval by characterizing its asymptotic distribution and the additional variability introduced by privacy. Numerical experiments compare our proposed method with baseline differential privacy approaches and evaluate its retrieval accuracy. Together, our results provide a theoretical foundation for optimal privacy-preserving retrieval and uncertainty quantification in energy-based associative memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
