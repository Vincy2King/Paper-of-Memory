# CMDO: A Cognitive Memory-Driven Optimization Algorithm for Adaptive Population-Based Search

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.35657v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Mohammed Yusuf Mujawar, Shahram Rahimi, Noorbakhsh Amiri Golilarz
- Tags: benchmark, context, episodic
- Categories: cs.NE, cs.AI
- URL: http://arxiv.org/abs/2609.35657v1

## One-Sentence Summary
Population-based optimization methods often use previous search information through successful solutions, parameter adaptation, or operator performance, but they rarely retain...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Population-based optimization methods often use previous search information through successful solutions, parameter adaptation, or operator performance, but they rarely retain the context in which a search behavior...

进一步看，论文的核心做法或实验重点可以概括为：We introduce Cognitive Memory-Driven Optimization (CMDO), a derivative-free population-based optimizer that represents experience as the relationship between search context, search behavior, and observed outcome.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, episodic
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.NE, cs.AI

## Abstract Snapshot
Population-based optimization methods often use previous search information through successful solutions, parameter adaptation, or operator performance, but they rarely retain the context in which a search behavior succeeded or failed. We introduce Cognitive Memory-Driven Optimization (CMDO), a derivative-free population-based optimizer that represents experience as the relationship between search context, search behavior, and observed outcome. CMDO organizes these experiences across working, episodic, and consolidated memory, retrieves them according to similarity with the current search state, and uses both positive and negative evidence to guide subsequent search. Retrieved experience does not replay previous candidate locations; instead, it selects search recipes that are reconstructed from the current population through exploratory, directed, and local search behaviors with adaptive search geometry. We evaluate CMDO on selected Blackbox Optimization Benchmarking test suite on COCO (BBOB/COCO) and Congress on Evolutionary Computation 2017 (CEC2017) problems against DE, CMA-ES, SHADE, GWO, HHO, and ORCA, and further study its application to seven-parameter photovoltaic model estimation using measured current--voltage data. The results show problem-dependent but competitive optimization performance, including the lowest median error among the compared methods on CEC2017 F10. More importantly, analysis of the search traces shows that context-dependent recall changes the distribution of executed search behaviors, while unsuccessful experiences remain available as negative evidence for later decisions, showing that accumulated experience directly influences subsequent search behavior. These results support the use of explicit context--behavior--outcome memory as an active mechanism for controlling population-based search.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
