# When Stored Evidence Stops Being Usable: Scale-Conditioned Evaluation of Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.07313v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Jiaqi Shao, Yiyi Lu, Yunzhen Zhang, Bing Luo
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.07313v1

## One-Sentence Summary
Memory-agent evaluations report fixed-snapshot accuracy or retrieval quality, but these scores do not show whether evidence remains usable as irrelevant sessions (sessions not...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-agent evaluations report fixed-snapshot accuracy or retrieval quality, but these scores do not show whether evidence remains usable as irrelevant sessions (sessions not annotated as task-relevant evidence for...

进一步看，论文的核心做法或实验重点可以概括为：We present a scale-conditioned evaluation protocol for agent memory under evidence-preserving growth: for each query, task evidence is held fixed while irrelevant sessions are added.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-agent evaluations report fixed-snapshot accuracy or retrieval quality, but these scores do not show whether evidence remains usable as irrelevant sessions (sessions not annotated as task-relevant evidence for the query) accumulate. We present a scale-conditioned evaluation protocol for agent memory under evidence-preserving growth: for each query, task evidence is held fixed while irrelevant sessions are added. The protocol logs agent--memory trajectories and reports four diagnostics: budget-compliant reliability, tail memory-call burden, failure-regime decomposition, and the usable-scale boundary where reliability falls below the target. Applied to LongMemEval and LoCoMo across flat, planar, and hierarchical memory interfaces, the protocol shows reliability loss is not a single phenomenon. On LongMemEval, HippoRAG stays within the two-call budget but loses 16--20 percentage points in budget-compliant reliability as irrelevant sessions are added; LiCoMemory's observed failures depend strongly on the agent, with Qwen3-8B exceeding the budget while Qwen3-32B and Qwen3-235B remain reliable in the tested range. The result supports a framework for making scalable-memory claims conditional on agent, interface, scale range, and interaction budget.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
