# From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.20006v1
- Published: 2026-04-21
- Updated: 2026-04-21
- Authors: Md Nayem Uddin, Kumar Shubham, Eduardo Blanco, Chitta Baral, Gengyu Wang
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2604.20006v1

## One-Sentence Summary
Personalized agents that interact with users over long periods must maintain persistent memory across sessions and update it as circumstances change.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized agents that interact with users over long periods must maintain persistent memory across sessions and update it as circumstances change.

进一步看，论文的核心做法或实验重点可以概括为：However, existing benchmarks predominantly frame long-term memory evaluation as fact retrieval from past conversations, providing limited insight into agents' ability to consolidate memory over time or handle frequent...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks, persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Personalized agents that interact with users over long periods must maintain persistent memory across sessions and update it as circumstances change. However, existing benchmarks predominantly frame long-term memory evaluation as fact retrieval from past conversations, providing limited insight into agents' ability to consolidate memory over time or handle frequent knowledge updates. We introduce Memora, a long-term memory benchmark spanning weeks to months long user conversations. The benchmark evaluates three memory-grounded tasks: remembering, reasoning, and recommending. To ensure data quality, we employ automated memory-grounding checks and human evaluation. We further introduce Forgetting-Aware Memory Accuracy (FAMA), a metric that penalizes reliance on obsolete or invalidated memory when evaluating long-term memory. Evaluations of four LLMs and six memory agents reveal frequent reuse of invalid memories and failures to reconcile evolving memories. Memory agents offer marginal improvements, exposing shortcomings in long-term memory for personalized agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
