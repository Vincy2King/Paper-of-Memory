# Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks

- Source: OpenReview
- Venue: ICML 2026 regular
- Paper ID: openreview:JHYmxqS9Jv
- Published: 2026-04-30
- Updated: 2026-06-24
- Authors: Zexue He, Yu Wang, Churan Zhi, Yuanzhe Hu, Tzu-Ping Chen, Lang Yin, Ze Chen, Tong Arthur Wu, Siru Ouyang, Zihan Wang, Jiaxin Pei, Julian McAuley, Yejin Choi, Alex Pentland
- Tags: agent, benchmark, context, conversation, long-term
- Categories: ICML.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=JHYmxqS9Jv

## One-Sentence Summary
Existing evaluations of agents with memory typically assess **memorization** and **action** in isolation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICML 2026 regular` 这个 venue 相关。

从摘要来看，作者主要关注的是：Existing evaluations of agents with memory typically assess **memorization** and **action** in isolation.

进一步看，论文的核心做法或实验重点可以概括为：One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICML 2026 regular
- 高亮主题命中：agent, benchmark, context, conversation, long-term
- 检索关键词命中：agent memory, context memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：ICML.cc/2026/Conference/-/Submission

## Abstract Snapshot
Existing evaluations of agents with memory typically assess **memorization** and **action** in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment, and subsequently rely on that memory to solve future tasks. To capture this setting, we introduce MemoryArena, a unified evaluation gym for benchmarking agent memory in multi-session Memory-Agent-Environment loops. The benchmark consists of human-crafted agentic tasks with explicitly interdependent subtasks, where agents must learn from earlier actions and feedback by distilling experiences into memory, and subsequently use that memory to guide later actions to solve the overall task. MEMORYARENA supports evaluation across web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning, and reveals that agents with near-saturated performance on existing long-context memory benchmarks like LoCoMo perform poorly in our agentic setting, exposing a gap in current evaluations for agents with memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
