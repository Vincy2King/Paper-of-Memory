# MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.06830v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Haozhen Zhang, Haodong Yue, Quanyu Long, Jianzhu Bao, Qingyuan Liu, Tao Feng, Bohan Liu, Weida Liang, Wenya Wang
- Tags: agent, benchmark
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.06830v1

## One-Sentence Summary
Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performance, cost, and latency largely underexplored. To address this challenge, we present \textbf{MemPilot}, a flexible framework that orchestrates on-demand memory curation under different performance--cost--latency preferences. Specifically, we optimize a multi-step LLM policy via reinforcement learning to iteratively choose between retrieving from query-agnostic memory and delegating query-specific curation of raw multimodal history to heterogeneous LLMs and VLMs. The policy jointly controls evidence amount, curation instructions, model selection, and visual access, enabling fine-grained allocation of runtime computation. To optimize this policy under competing objectives, we adapt objective-wise advantage decoupling by separately estimating each objective's advantage before aggregation. Moreover, we introduce prefix-based marginal utility estimation for fine-grained credit assignment across multi-step rollouts. Experiments on five multimodal agent-memory benchmarks demonstrate favorable performance--cost--latency trade-offs across optimization preferences, with preference sweeps yielding broader frontiers than existing trade-off-aware baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
