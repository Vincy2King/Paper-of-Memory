# When Correct Memory Goes Wrong: Fuzzing Persistent Memory Use in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.38275v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Yuqiao Meng, Luoxi Tang, Yingxue Zhang, Yuchen Yang, Zhaohan Xi
- Tags: agent, retrieval
- Categories: cs.DC, cs.AI
- URL: http://arxiv.org/abs/2609.38275v1

## One-Sentence Summary
Persistent memory helps LLM agents carry information across long interactions, but correct memory can still be used incorrectly when queries change or memory states evolve.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory helps LLM agents carry information across long interactions, but correct memory can still be used incorrectly when queries change or memory states evolve.

进一步看，论文的核心做法或实验重点可以概括为：Existing work mainly studies memory content errors or evaluates fixed test cases, leaving memory-use failures hard to discover systematically.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory retrieval, persistent memory
- 来源分类信息：cs.DC, cs.AI

## Abstract Snapshot
Persistent memory helps LLM agents carry information across long interactions, but correct memory can still be used incorrectly when queries change or memory states evolve. Existing work mainly studies memory content errors or evaluates fixed test cases, leaving memory-use failures hard to discover systematically. We formulate this issue as a fuzzing problem and categorize such failures into query-related and memory-state failures. We then develop U-Fuzz, which starts from memory checkpoints as test seeds, mutates queries or memory states under explicit mutation obligations, validates each mutant, and uses observed memory behavior to guide iterative testing while keeping failure labels outside the search. We evaluate U-Fuzz across several memory systems against diverse fuzzing baselines, and further test an output-only setting with API-based LLMs where memory retrieval is hidden. Across these settings, U-Fuzz consistently uncovers more confirmed memory-use failures, showing that its search remains effective across different memory architectures and even when only final responses are observable.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
