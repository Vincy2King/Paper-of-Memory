# EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.18421v1
- Published: 2026-05-18
- Updated: 2026-05-18
- Authors: Yuyao Wang, Zhongjian Zhang, Mo Chi, Kaichi Yu, Yuhan Li, Miao Peng, Bing Tong, Chen Zhang, Yan Zhou, Jia Li
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.18421v1

## One-Sentence Summary
Recent benchmarks for Large Language Model (LLM) agents mainly evaluate reasoning, planning, and execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent benchmarks for Large Language Model (LLM) agents mainly evaluate reasoning, planning, and execution.

进一步看，论文的核心做法或实验重点可以概括为：However, memory is also essential for agents, as it enables them to store, update, and retrieve information over time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Recent benchmarks for Large Language Model (LLM) agents mainly evaluate reasoning, planning, and execution. However, memory is also essential for agents, as it enables them to store, update, and retrieve information over time. This ability remains under-evaluated, largely because existing benchmarks do not provide a systematic way to assess memory mechanisms. In this paper, we study agent memory from a self-evolving perspective and introduce EvoMemBench, a unified benchmark organized along two axes: memory scope (in-episode vs. cross-episode) and memory content (knowledge-oriented vs. execution-oriented). We compare 15 representative memory methods with strong long-context baselines under a standardized protocol. Results show that current memory systems are still far from a general solution: long-context baselines remain highly competitive, memory helps most when the current context is insufficient or tasks are difficult, and no single memory form works consistently across all settings. Retrieval-based methods remain strong for knowledge-intensive settings, whereas procedural and long-term memory methods are more effective for execution-oriented tasks when their stored experience matches the task structure. We hope EvoMemBench facilitates future research on more effective memory systems for LLM-based agents. Our code is available at https://github.com/DSAIL-Memory/EvoMemBench.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
