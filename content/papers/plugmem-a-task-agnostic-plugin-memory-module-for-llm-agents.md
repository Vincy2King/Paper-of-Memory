# PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents

- Source: OpenReview
- Venue: LLA 2026 Poster
- Paper ID: openreview:LE664kai2e
- Published: 2026-03-02
- Updated: 2026-04-10
- Authors: Ke Yang, Zixi Chen, Xuan He, Jize Jiang, Michel Galley, Chenglong Wang, Jianfeng Gao, Jiawei Han, ChengXiang Zhai
- Tags: agent, benchmark, context, conversation, episodic, long-term, retrieval
- Categories: ICLR.cc/2026/Workshop/LLA/-/Submission
- URL: https://openreview.net/forum?id=LE664kai2e

## One-Sentence Summary
Long-term memory is essential for large language model (LLM) agents operating in complex environments, yet existing memory designs are either task-specific and non-transferable,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `LLA 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory is essential for large language model (LLM) agents operating in complex environments, yet existing memory designs are either task-specific and non-transferable, or task-agnostic but less effective due...

进一步看，论文的核心做法或实验重点可以概括为：We propose PlugMem, a task-agnostic plugin memory module that can be attached to arbitrary LLM agents without task-specific redesign.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：LLA 2026 Poster
- 高亮主题命中：agent, benchmark, context, conversation, episodic, long-term
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：ICLR.cc/2026/Workshop/LLA/-/Submission

## Abstract Snapshot
Long-term memory is essential for large language model (LLM) agents operating in complex environments, yet existing memory designs are either task-specific and non-transferable, or task-agnostic but less effective due to low task-relevance and context explosion from raw memory retrieval. We propose PlugMem, a task-agnostic plugin memory module that can be attached to arbitrary LLM agents without task-specific redesign. Motivated by the fact that decision-relevant information is concentrated as abstract knowledge rather than raw experience, we draw on cognitive science to structure episodic memories into a compact, extensible knowledge-centric memory graph that explicitly represents propositional and prescriptive knowledge. This representation enables efficient memory retrieval and reasoning over task-relevant knowledge, rather than verbose raw trajectories, and departs from other graph-based methods like GraphRAG by treating knowledge as the unit of memory access and organization instead of entities or text chunks. We evaluate PlugMem unchanged across three heterogeneous benchmarks (long-horizon conversational question answering, multi-hop knowledge retrieval, and web agent tasks). The results show that PlugMem consistently outperforms task-agnostic baselines and exceeds task-specific memory designs, while also achieving the highest information density under a unified information-theoretic analysis.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
