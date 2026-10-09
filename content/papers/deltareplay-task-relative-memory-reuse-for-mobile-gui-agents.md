# DeltaReplay: Task-Relative Memory Reuse for Mobile GUI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11707v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Yudong Bai, Yihong Chen, Quanming Yao, Yaqing Wang
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.11707v1

## One-Sentence Summary
Memory-augmented mobile GUI agents store successful execution trajectories and reuse them in later tasks, but a stored trajectory rarely matches a new task exactly.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented mobile GUI agents store successful execution trajectories and reuse them in later tasks, but a stored trajectory rarely matches a new task exactly.

进一步看，论文的核心做法或实验重点可以概括为：The new task may use different parameters, share only some of its steps with a stored trajectory, or have no relevant record in memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented mobile GUI agents store successful execution trajectories and reuse them in later tasks, but a stored trajectory rarely matches a new task exactly. The new task may use different parameters, share only some of its steps with a stored trajectory, or have no relevant record in memory. Forcing the agent to use irrelevant memory can mislead it, whereas discarding memory that may still be useful deprives it of guidance from past experience. To address this dilemma, we propose DeltaReplay, a step-level memory reuse framework that decides how to use existing memory without modifying it. We observe that the reusable part of a stored record is determined not by the record itself but by its relation to the new task, mainly through two factors: page-level consistency and action-level generality. We therefore store execution trajectories as paths in a transition graph, whose nodes (pages) and edges (actions between pages) capture these two factors. At reuse time, the action on each edge is split into a task-independent operation and task-specific parameters. DeltaReplay then compares each recorded step with the new task and the current screen, and decides whether to follow it, execute it after replacing its parameters, or leave it to the base agent. On AndroidWorld and SPA-Bench, DeltaReplay improves the task success rate over a base agent with the same backbone by up to 10.3 and 25.0 percentage points, respectively. These results indicate that deciding at each step how to use retrieved memory lets agents benefit even from partially matching trajectories.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
