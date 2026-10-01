# Simple Agentic Memory for Generalist Robot Policies

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36595v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Yuyou Zhang, Yunbei Zhang, Miao Li, Janet Wang, Zijian Jin, Shilong Liu, Ding Zhao
- Tags: agent, benchmark
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2609.36595v1

## One-Sentence Summary
Visual-memory systems commonly retain or compress past observations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Visual-memory systems commonly retain or compress past observations.

进一步看，论文的核心做法或实验重点可以概括为：Robot control additionally requires interaction-derived state that no individual frame may explicitly represent, such as persistent identity relations, accumulated progress, or ordered procedures.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Visual-memory systems commonly retain or compress past observations. Robot control additionally requires interaction-derived state that no individual frame may explicitly represent, such as persistent identity relations, accumulated progress, or ordered procedures. We introduce Simple Agentic Robot Memory (SimpleARM), a training-free memory layer for frozen generalist robot policies. From the task instruction, SimpleARM specifies what to monitor; frozen perceptual tools maintain compact typed state online; structured access retrieves that state only when a proposed subgoal depends on history; and current-view grounding resolves recalled entities before execution. We evaluate SimpleARM on RoboMME, a benchmark of memory-dependent robot manipulation tasks that require history information no longer available in the current observation. Across all 16 tasks and three policy seeds, SimpleARM achieves 67.17% mean success, compared with 44.51% for the strongest non-oracle baseline. Matched ablations show mechanism specificity: removing relation, reference, progress, or route state produces large losses where the affected state is retrieved for control, while largely sparing other tasks. These results support a state-based view of robot memory: effective memory for control is not simply retained visual history, but compact task-relevant state derived from the interaction history.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
