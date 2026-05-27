# Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark and Empirical Study

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.26394v1
- Published: 2026-05-25
- Updated: 2026-05-25
- Authors: Ravi Kumar Tummalapenta, Suman Addanki
- Tags: agent, benchmark, episodic, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.26394v1

## One-Sentence Summary
Multi-turn Text-to-SQL is central to enterprise analytics yet remains predominantly evaluated in single-turn settings.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-turn Text-to-SQL is central to enterprise analytics yet remains predominantly evaluated in single-turn settings.

进一步看，论文的核心做法或实验重点可以概括为：We introduce EnterpriseMem-Bench, a multi-turn Text-to-SQL benchmark of 300 sessions and 1,400 turns built programmatically from three enterprise domains (BIRD financial, SEC EDGAR, Northwind), with deterministic...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Multi-turn Text-to-SQL is central to enterprise analytics yet remains predominantly evaluated in single-turn settings. We introduce EnterpriseMem-Bench, a multi-turn Text-to-SQL benchmark of 300 sessions and 1,400 turns built programmatically from three enterprise domains (BIRD financial, SEC EDGAR, Northwind), with deterministic ground truth and per-turn memory-critical annotation. We evaluate five frontier models -- GPT-5 mini, GPT-5.2, Claude Sonnet 4.5, Sonnet 4.6, and Opus 4.6 -- across five memory conditions enabling a three-way ablation isolating working-memory window size, episodic retrieval, and semantic augmentation as independent effects. All Claude models are evaluated with extended thinking enabled to maintain parity with GPT reasoning models. We introduce the Memory Benefit Score (MBS) as a per-turn diagnostic metric. Four findings emerge: (1) stateless multi-turn Text-to-SQL collapses to zero execution accuracy by Turn 3 across all five models, even under reasoning; (2) memory-architecture complexity does not monotonically improve accuracy -- working memory dominates, and additional components produce model- and dataset-dependent effects from +14 to -16 percentage points; (3) Claude Sonnet 4.6 underperforms Sonnet 4.5 by 17-33pp on SEC EDGAR across conditions, a generational regression persisting under reasoning; (4) under reasoning, Claude error distributions become mono-modal -- every non-correct turn is a wrong-result error. We release the benchmark, agent, and evaluation code.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
