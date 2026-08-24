# Back to Basics: Let Conversational Agents Remember with Just Retrieval and Generation

- Source: OpenReview
- Venue: COLM 2026
- Paper ID: openreview:BFHdlmY3nL
- Published: 2026-07-08
- Updated: 2026-08-24
- Authors: Yuqian Wu, Wei Chen, Zhengjun Huang, Junle Chen, Qingxiang Liu, Kai Wang, Xiaofang Zhou, Yuxuan Liang
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: colmweb.org/COLM/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=BFHdlmY3nL

## One-Sentence Summary
Existing conversational memory systems rely on complex hierarchical summarization or reinforcement learning to manage long-term dialogue history, yet remain vulnerable to...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `COLM 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Existing conversational memory systems rely on complex hierarchical summarization or reinforcement learning to manage long-term dialogue history, yet remain vulnerable to context dilution as conversations grow.

进一步看，论文的核心做法或实验重点可以概括为：In this work, we offer a different perspective: the primary bottleneck may lie not in memory architecture, but in the Signal Sparsity Effect within the latent knowledge manifold.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：COLM 2026
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：colmweb.org/COLM/2026/Conference/-/Submission

## Abstract Snapshot
Existing conversational memory systems rely on complex hierarchical summarization or reinforcement learning to manage long-term dialogue history, yet remain vulnerable to context dilution as conversations grow. In this work, we offer a different perspective: the primary bottleneck may lie not in memory architecture, but in the Signal Sparsity Effect within the latent knowledge manifold. Through controlled experiments, we identify two key phenomena: Decisive Evidence Sparsity, where relevant signals become increasingly isolated with longer sessions, leading to sharp degradation in aggregation-based methods; and Dual-Level Redundancy, where both intersession interference and intra-session conversational filler introduce large amounts of non-informative content, hindering effective generation. Motivated by these insights, we propose Nano-Memory, a minimalist framework that brings conversational memory back to basics, relying solely on retrieval and generation via Turn Isolation Retrieval (TIR) and Query-Driven Pruning (QDP). TIR replaces global aggregation with a max-activation strategy to capture turn-level signals, while QDP removes redundant sessions and conversational filler to construct a compact, high-density evidence set. Extensive experiments on multiple benchmarks demonstrate that Nano-Memory achieves robust performance across diverse settings, consistently outperforming strong baselines while maintaining high efficiency in tokens and latency, establishing a new minimalist baseline for conversational memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
