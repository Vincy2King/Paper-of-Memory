# A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.02912v1
- Published: 2026-11-02
- Updated: 2026-11-02
- Authors: Yiqi Wang, Tongyuan Zhao, Jiaqi Zhang, Yiqun Duan, Zhangkai Wu, Mingkai Zheng, Taotao Cai
- Tags: agent, benchmark, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.02912v1

## One-Sentence Summary
Long-lived agents rely on persistent memory of users, tasks and decisions, and this memory must stay consistent with a world that keeps changing.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-lived agents rely on persistent memory of users, tasks and decisions, and this memory must stay consistent with a world that keeps changing.

进一步看，论文的核心做法或实验重点可以概括为：When an upstream fact changes, however, memory systems can revise the contradicted memory itself while the beliefs, plans and actions derived from it remain accepted, even though they have lost their support.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks, persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-lived agents rely on persistent memory of users, tasks and decisions, and this memory must stay consistent with a world that keeps changing. When an upstream fact changes, however, memory systems can revise the contradicted memory itself while the beliefs, plans and actions derived from it remain accepted, even though they have lost their support. We therefore formulate dependency-aware state revision, which asks not only what changed but also which dependent states should no longer be trusted. To address it, StateGraph maintains an evolving state dependency graph whose edges are recovered from interaction histories. Its core design is counterfactual verification: each candidate edge is tested by asking whether the dependent state would survive the loss of its premise, which separates support dependence from semantic relatedness, and revision then invalidates a dependent state only when a strict dependency fails and no independent support path survives. To test this design, we introduce StateChangeBench, a controlled benchmark of 50 author-constructed cases annotated with cascade depth, hard negatives and action consequences. On it, StateGraph's Impact-F1 margin over a CUPMem reimplementation is 6.9 percentage points at depth 1 and 26.0 at depth 3+. On public long-term memory benchmarks, its point estimates are comparable to or higher than those of the evaluated baselines on most datasets. These results provide initial evidence that explicit dependency tracking can improve selective memory revision under changing conditions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
