# Shared Worlds, Private Minds: Structured Memory for Long-Form Writing as World Creation

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32401v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Qiuyu Tian, Xiaowen Gu, Hang Su, Jianghan Chao, Haojie Yin, Fan Guo, Xin Zhang, Jinjing Shen, Ewing Luo, Youyong Kong, Yingce Xia, Zequn Liu
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.32401v1

## One-Sentence Summary
LLM agents that write long-form fiction need an explicit memory of the evolving storyworld to keep new events consistent with established facts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents that write long-form fiction need an explicit memory of the evolving storyworld to keep new events consistent with established facts.

进一步看，论文的核心做法或实验重点可以概括为：Such memory must keep heterogeneous narrative information distinct, integrate story developments across granularities, and recover dependencies that a writing request leaves implicit.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
LLM agents that write long-form fiction need an explicit memory of the evolving storyworld to keep new events consistent with established facts. Such memory must keep heterogeneous narrative information distinct, integrate story developments across granularities, and recover dependencies that a writing request leaves implicit. We present NarraWorld, a structured memory system for long-form writing that treats memory construction as world creation. From a shared evidence-grounded graph, NarraWorld derives four connected views: world facts, per-character beliefs, open developments, and hypothetical branches (possible-world continuations). Hierarchical aggregation with atomic closure consolidates events into scenes, plotlines, and plots, keeping each higher-level node traceable to its constituent source spans. For retrieval, planned reconstruction infers a query's dependencies from the current narrative situation and a preview of memory, then assembles the relevant records within a token budget. Across three writing benchmarks, NarraWorld achieves the strongest aggregate results. Its memory also transfers to situated role-playing and largely preserves recall on a general-purpose long-term memory benchmark, paving the way for agents that sustain coherent storyworlds across diverse narrative tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
