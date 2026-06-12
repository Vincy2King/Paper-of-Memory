# How Much Memory Do We Need? Adaptive Memory Gate for Neural Operators

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.13443v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Jihyeon Hur, Yongseok Kwon, Min-Gi Jo, Jeongwhan Choi, Noseong Park
- Tags: memory-augmented
- Categories: cs.LG
- URL: http://arxiv.org/abs/2606.13443v1

## One-Sentence Summary
Neural operators have emerged as a powerful data-driven approach for solving time-dependent PDEs.

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Neural operators have emerged as a powerful data-driven approach for solving time-dependent PDEs.

进一步看，论文的核心做法或实验重点可以概括为：Among recent advances, memory-augmented neural operators explicitly incorporate past states and have achieved remarkable performance under low-resolution observation settings.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
Neural operators have emerged as a powerful data-driven approach for solving time-dependent PDEs. Among recent advances, memory-augmented neural operators explicitly incorporate past states and have achieved remarkable performance under low-resolution observation settings. However, existing approaches apply a fixed memory weight regardless of observation conditions, such as resolution or physical parameters, limiting their adaptability. Our preliminary experiments reveal that optimal memory weight varies with resolution and viscosity, implying that a fixed memory weight cannot simultaneously optimize performance across diverse settings. We propose AMGFNO, which dynamically modulates memory weight through a learnable gate. On the Kuramoto-Sivashinsky and Burgers' equations, AMGFNO achieves 55-79% nRMSE reduction over at low resolution, with the learned gate value automatically decreasing from $\bar{g} \approx 0.7$ to near-zero as resolution increases.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
