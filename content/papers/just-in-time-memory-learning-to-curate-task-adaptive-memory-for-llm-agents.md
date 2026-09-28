# Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.27334v1
- Published: 2026-09-23
- Updated: 2026-09-23
- Authors: Yefan Zhou, Yang Li, Zeyu Leo Liu, Semih Yavuz, Shafiq Joty
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.27334v1

## One-Sentence Summary
Agentic memory systems reuse past experience to improve future performance, yet most existing designs curate memory at write time: once a task is completed, its trajectory is...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic memory systems reuse past experience to improve future performance, yet most existing designs curate memory at write time: once a task is completed, its trajectory is distilled into a fixed artifact, such as a...

进一步看，论文的核心做法或实验重点可以概括为：This forces the system to decide what is worth remembering before the future query is known, irreversibly discarding information and producing a query-independent summary that must serve many possible downstream tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Agentic memory systems reuse past experience to improve future performance, yet most existing designs curate memory at write time: once a task is completed, its trajectory is distilled into a fixed artifact, such as a reflection, workflow, skill, or reasoning strategy, that is later retrieved by similarity. This forces the system to decide what is worth remembering before the future query is known, irreversibly discarding information and producing a query-independent summary that must serve many possible downstream tasks. Learning such a write-time curator is also difficult because the value of a storage decision may only become apparent when a relevant query arrives, potentially many tasks later, creating a long-horizon credit-assignment problem. We instead retain raw trajectories and defer curation until read time, when the current task is known. Given the retrieved traces and the new task, a memory curator synthesizes a compact, task-adaptive payload tailored to the immediate need. Because this payload is consumed on the same task, the curator can be trained directly from immediate task success, avoiding delayed utility signals and the need to artificially group related tasks. Across ALFWorld, WebShop, and $τ^2$-bench, our Just-in-Time Memory (JitMem) consistently outperforms no-memory agents as well as heuristic and learned write-time memory methods, improving over the strongest baseline by 16.2, 16.3, and 3.9 absolute success-rate points, respectively. Notably, even an untrained curator is already competitive with or surpasses these baselines, showing that task-adaptive read-time curation itself is a major source of the gain; training the curator further compounds the improvement.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
