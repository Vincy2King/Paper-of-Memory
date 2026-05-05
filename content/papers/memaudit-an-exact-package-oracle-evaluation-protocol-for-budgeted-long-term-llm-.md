# MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.02199v1
- Published: 2026-05-04
- Updated: 2026-05-04
- Authors: Nishant Bhargava, Rodrigo Sobral Barrento
- Tags: agent, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.02199v1

## One-Sentence Summary
Long-term LLM agents must compress streams of past interactions into persistent memory before future queries are known.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term LLM agents must compress streams of past interactions into persistent memory before future queries are known.

进一步看，论文的核心做法或实验重点可以概括为：Existing evaluations usually measure final question-answering accuracy, which entangles memory writing with retrieval, prompting, and reader reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term LLM agents must compress streams of past interactions into persistent memory before future queries are known. Existing evaluations usually measure final question-answering accuracy, which entangles memory writing with retrieval, prompting, and reader reasoning. We introduce MEMAUDIT, an exact packageoracle evaluation protocol for budgeted long-term memory writing. A MEMAUDIT package fixes an experience stream, candidate memory representations, storage costs, semantic evidence units, future-query requirements, and a budget, turning write-time memory selection into a finite auditable optimization problem with a certified denominator. We instantiate this protocol with a concave-over-modular semantic coverage objective under storage and one-representation-per-experience constraints, and compute exact package optima using branch-and-bound with MILP certification. Across controlled exact packages, validity-heavy stress tests, human-audited natural support slices, and exported Mem0, A-Mem, and Letta stores, MEMAUDIT separates representation quality, validity-state preservation, and budget-aware selection effects that end-to-end QA cannot localize. The resulting artifact provides reusable package generators, certified solvers, natural package exports, external-system scorers, and cached reproducibility metadata for evaluating what memory writers actually preserve under fixed storage budgets.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
