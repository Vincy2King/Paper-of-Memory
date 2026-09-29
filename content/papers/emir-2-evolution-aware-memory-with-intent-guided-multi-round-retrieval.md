# EMIR$^2$: Evolution-Aware Memory with Intent-Guided Multi-Round Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32584v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Jinlan Liu, Hongliang Sun, Yong Wang, Bolin Zhang, Dinabo Sui, Dianhui Chu, Zhiying Tu
- Tags: agent, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.32584v1

## One-Sentence Summary
Long-term memory enables large language model (LLM) agents to leverage historical interactions for future tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables large language model (LLM) agents to leverage historical interactions for future tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory systems struggle to utilize continuously evolving historical information, as they often rely on static memory representations and single-round retrieval strategies, failing to track factual...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory enables large language model (LLM) agents to leverage historical interactions for future tasks. However, existing memory systems struggle to utilize continuously evolving historical information, as they often rely on static memory representations and single-round retrieval strategies, failing to track factual changes or integrate distributed evidence across long-term interactions. To address these challenges, we propose \textsc{EMIR}$^{2}$, an \textbf{E}volution-Aware \textbf{M}emory framework with \textbf{I}ntent-Guided Multi-\textbf{R}ound \textbf{R}etrieval, enabling LLM agents to maintain evolving historical knowledge and adaptively retrieve relevant evidence. Specifically, \textsc{EMIR}$^{2}$ constructs a State-Evolving Memory Graph (SEMG) that represents long-term memory as evolving knowledge states supported by temporal event trajectories and evidential associations. By maintaining semantic states through evidence-based updates, SEMG preserves historical evolution and enables evidence tracing under complex and conflicting scenarios. Building upon this, we introduce an intent-guided multi-round retrieval mechanism that iteratively identifies missing evidence and expands retrieval based on accumulated information. Experiments on LoCoMo and MemConflict demonstrate that \textsc{EMIR}$^{2}$ improves long-term memory utilization, dynamic and static conflict handling, and complex retrieval performance, achieving relative improvements of more than 12\% in certain categories. These results highlight the effectiveness of jointly modeling memory evolution and adaptive evidence acquisition for long-term agent interactions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
