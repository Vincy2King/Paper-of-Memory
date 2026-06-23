# DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.22877v1
- Published: 2026-06-22
- Updated: 2026-06-22
- Authors: Wenya Xie, Shengming Zhou, Zelin Li, Pouya Parsa, Shuang Zhou, Xinheng Ding, Chinmay Arvind, Guanchu Wang, Vladimir Braverman, Ali Payani, Yantao Zheng, Zirui Liu
- Tags: agent, benchmark, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.22877v1

## One-Sentence Summary
LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they prefer (preferences), and keep it updated...

进一步看，论文的核心做法或实验重点可以概括为：Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they prefer (preferences), and keep it updated as jobs, routines, and tastes drift. Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. We introduce DynamicMem, a synthetic benchmark that constructs 15 months of activity per user, providing long-term multi-app data that real users' privacy keeps out of reach. It provides user-consistent trajectories averaging 2.2M tokens and 1,772 grounded events per user across 16 applications such as e-commerce, fitness, and social platforms. The profile evolves over this period and is never given explicitly: each attribute, habit, or preference must be inferred from small signals scattered across apps. We evaluate at five quarterly checkpoints to track how systems scale as history grows. Benchmarking five representative systems exposes problems a single accuracy score hides: (i) profile reconstruction degrades with history length while service-task accuracy stays flat, despite both drawing on the same memory; (ii) no system both keeps facts that stay true and replaces facts that change, with errors clustering on preferences and on naming the exact referent; and (iii) over 93% of failures trace to what the memory retrieves, not to the model writing the answer, so the largest room for improvement lies in memory itself. Code: https://wenyaxie023.github.io/DynamicMem/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
