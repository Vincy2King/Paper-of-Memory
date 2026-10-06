# SEER: Self-Evolving Event Reasoning and Retrieval for Time Series Forecasting

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04109v1
- Published: 2026-10-02
- Updated: 2026-10-02
- Authors: Mingtian Tan, Palash Goyal, Mihir Parmar, Sarkar Snigdha Sarathi Das, Chun-Liang Li, Nanyun Peng, Thomas Hartvigsen, Jinsung Yoon, Tomas Pfister
- Tags: benchmark, retrieval
- Categories: cs.LG, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2610.04109v1

## One-Sentence Summary
Real-world time series are frequently driven by exogenous events and structural shifts, rendering conventional forecasting based solely on historical numerical observations...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Real-world time series are frequently driven by exogenous events and structural shifts, rendering conventional forecasting based solely on historical numerical observations insufficient.

进一步看，论文的核心做法或实验重点可以概括为：While language models can retrieve external news, standard retrieval-augmented approaches struggle with high noise, missing signals, and an inability to reason causally about event impacts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.LG, cs.AI, cs.CL

## Abstract Snapshot
Real-world time series are frequently driven by exogenous events and structural shifts, rendering conventional forecasting based solely on historical numerical observations insufficient. While language models can retrieve external news, standard retrieval-augmented approaches struggle with high noise, missing signals, and an inability to reason causally about event impacts. We propose SEER (Self-Evolving Event Reasoning and Retrieval), a closed-loop framework that dynamically optimizes event conditioning for time series forecasting. SEER translates prediction errors into two decoupled feedback mechanisms: (i) a reflective retrieval memory that refines subsequent search queries and filters spurious noise, and (ii) a persistent causal knowledge base that distills transferable domain dynamics. SEER enforces strict chronological boundaries across both event retrieval and reflection, preventing look-ahead bias and data leakage. Across six volatile time-series benchmarks, SEER consistently outperforms state-of-the-art time series foundation models and language model baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
