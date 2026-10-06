# MemTrace: State-Consistent Memory for Long-Horizon Coding Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04838v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Hongming Xu, Le Zhou, ZhongHe Jin, Xiang Zhang, Bo Tang, Zhiyu Li, Xuanhe Zhou, Juncheng Zhang
- Tags: agent, benchmark, compression, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.04838v1

## One-Sentence Summary
As coding agents take on long-horizon software evolution tasks spanning multiple files and stages, longer execution trajectories introduce two coupled challenges: (1)...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As coding agents take on long-horizon software evolution tasks spanning multiple files and stages, longer execution trajectories introduce two coupled challenges: (1) accumulated histories strain context budgets, and...

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches address these challenges through techniques like larger context windows, compression, retrieval, or repository representations, but often fail to reconstruct a consistent task state after a context...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
As coding agents take on long-horizon software evolution tasks spanning multiple files and stages, longer execution trajectories introduce two coupled challenges: (1) accumulated histories strain context budgets, and (2) repository changes can invalidate earlier execution evidence. Existing approaches address these challenges through techniques like larger context windows, compression, retrieval, or repository representations, but often fail to reconstruct a consistent task state after a context refresh or verify whether recalled evidence remains valid. Thus, we introduce MemTrace, a provenance-aware memory system that preserves execution history and aligns its reuse with the evolving task (e.g., iterative cross-file repair) and repository state. MemTrace stores history as immutable Memory Traces anchored to key information (e.g., files, symbols, tests), and organizes their execution order and dependencies in a Memory Trace Graph. When context is constrained, working memory retains only compact Memory Anchors, from which the agent can reconstruct the latest execution state and locate evidence relevant to its next action. Before restoring historical evidence, MemTrace checks its validity against the current repository state and retrieves only what the next action requires. Across three complementary long-horizon coding benchmarks, MemTrace consistently outperforms all fully evaluated baselines under the same backbone and harness, improving DeepSWE pass@1 by 21.2 points, SWE-EVO Resolved Rate by 4.4 points, and SWE-Milestone Score by 17.8 points under Codex CLI.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
