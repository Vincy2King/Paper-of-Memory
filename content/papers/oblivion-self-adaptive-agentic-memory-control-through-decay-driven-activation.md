# Oblivion: Self-Adaptive Agentic Memory Control through Decay-Driven Activation

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.00131v2
- Published: 2026-03-31
- Updated: 2026-04-17
- Authors: Ashish Rana, Chia-Chien Hung, Qumeng Sun, Julian Martin Kunkel, Carolin Lawrence
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2604.00131v2

## One-Sentence Summary
Human memory adapts through selective forgetting: experiences become less accessible over time but can be reactivated by reinforcement or contextual cues.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Human memory adapts through selective forgetting: experiences become less accessible over time but can be reactivated by reinforcement or contextual cues.

进一步看，论文的核心做法或实验重点可以概括为：In contrast, memory-augmented LLM agents rely on "always-on" retrieval and "flat" memory storage, causing high interference and latency as histories grow.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Human memory adapts through selective forgetting: experiences become less accessible over time but can be reactivated by reinforcement or contextual cues. In contrast, memory-augmented LLM agents rely on "always-on" retrieval and "flat" memory storage, causing high interference and latency as histories grow. We introduce Oblivion, a memory control framework that casts forgetting as decay-driven reductions in accessibility, not explicit deletion. Oblivion decouples memory control into read and write paths. The read path decides when to consult memory, based on agent uncertainty and memory buffer sufficiency, avoiding redundant always-on access. The write path decides what to strengthen, by reinforcing memories contributing to forming the response. Together, this enables hierarchical memory organization that maintains persistent high-level strategies while dynamically loading details as needed. We evaluate on both static and dynamic long-horizon interaction benchmarks. Results show that Oblivion dynamically adapts memory access and reinforcement, balancing learning and forgetting under shifting contexts, highlighting that memory control is essential for effective LLM-agentic reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
