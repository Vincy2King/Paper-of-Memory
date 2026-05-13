# Automated Reformulation of Robust Optimization via Memory-Augmented Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.11813v1
- Published: 2026-05-12
- Updated: 2026-05-12
- Authors: Jinbiao Chen, Shuang Jin, Guoyun Zhang, Junyu Zhang, Guanyi Wang, Hanzhang Qin
- Tags: benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.11813v1

## One-Sentence Summary
Robust optimization (RO) provides a principled framework for decision-making under uncertainty, but its practical use is often limited by the need to manually reformulate...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Robust optimization (RO) provides a principled framework for decision-making under uncertainty, but its practical use is often limited by the need to manually reformulate uncertain optimization models into tractable...

进一步看，论文的核心做法或实验重点可以概括为：Recent large language models (LLMs) have been shown promising for automating optimization formulation, yet RO reformulation remains challenging because it requires precise multi-step reasoning and mathematically...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Robust optimization (RO) provides a principled framework for decision-making under uncertainty, but its practical use is often limited by the need to manually reformulate uncertain optimization models into tractable deterministic counterparts. Recent large language models (LLMs) have been shown promising for automating optimization formulation, yet RO reformulation remains challenging because it requires precise multi-step reasoning and mathematically consistent transformations. To facilitate systematic evaluation of LLM-based reformulation, for which no dedicated benchmark currently exists, we develop AutoRO-Bench, a benchmark featuring an automated data generation pipeline for the core RO reformulation task and a curated dataset for the RO application task. To address the reformulation challenge, we propose Automated Reformulation with Experience Memory (AutoREM), a tuning-free memory-augmented framework that autonomously builds a structured textual experience memory by reflecting on past failed trajectories through a tailored offline adaptation procedure. AutoREM requires neither domain-specific expert knowledge nor parameter updates, and the resulting memory readily transfers across different base LLMs. Experimental results show that AutoREM consistently improves the accuracy and efficiency of RO reformulation across in-distribution datasets, out-of-distribution datasets, and diverse base LLMs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
