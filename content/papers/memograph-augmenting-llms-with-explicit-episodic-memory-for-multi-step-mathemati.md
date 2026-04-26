# MemoGraph: Augmenting LLMs with Explicit Episodic Memory for Multi-step Mathematical Reasoning

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents
- Paper ID: openreview:HaCqQlEjCN
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: Yutong Li, Yitian Zhou, Guo Chen, Xudong Wang, Chenghao Li, Chaoning Zhang
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=HaCqQlEjCN

## One-Sentence Summary
Large Language Models (LLMs) fundamentally struggle with complex mathematical reasoning due to the volatility of their implicit parametric memory, which leads to context drift...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) fundamentally struggle with complex mathematical reasoning due to the volatility of their implicit parametric memory, which leads to context drift and hallucination.

进一步看，论文的核心做法或实验重点可以概括为：Existing paradigms, relying on linear generation or static retrieval, fail to maintain a precise, persistent record of the evolving proof state.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
Large Language Models (LLMs) fundamentally struggle with complex mathematical reasoning due to the volatility of their implicit parametric memory, which leads to context drift and hallucination. Existing paradigms, relying on linear generation or static retrieval, fail to maintain a precise, persistent record of the evolving proof state. To address this, we propose \textbf{MemoGraph}, a neuro-symbolic framework that augments LLMs with an explicit episodic memory layer. We formulate reasoning as the dynamic maintenance of a heterogeneous graph, enabling state-aware reading that utilizes graph-structural encoding to retrieve relevant principles from a verified semantic memory. Furthermore, we introduce a write-gating verification module to intercept invalid deductions before they are consolidated into the reasoning context. Empirical evaluations across multiple benchmarks demonstrate that MemoGraph significantly outperforms strong baselines in both accuracy and robustness by ensuring memory integrity, establishing a scalable paradigm for trustworthy reasoning agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
