# Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.17545v1
- Published: 2026-07-20
- Updated: 2026-07-20
- Authors: Qingcan Kang, Mingyang Liu, Shixiong Kai, Kaichao Liang, Zhentao Tang, Yuqi Cui, Tao Zhong, Mingxuan Yuan
- Tags: agent, benchmark, compression, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.17545v1

## One-Sentence Summary
Language agents depend on memory across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language agents depend on memory across interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, the limited context windows of large language models (LLMs) and their inference costs constrain how much memory can be used at once.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Language agents depend on memory across interactions. However, the limited context windows of large language models (LLMs) and their inference costs constrain how much memory can be used at once. Existing systems mainly follow two strategies: memory retention and memory consolidation. Retention keeps raw records and preserves exact details, but relevant evidence may not fit under a tight budget; consolidation compresses and combines records, improving coverage per token but risking the loss of query-critical details. Neither strategy is universally preferable. This raises two central questions: when should consolidation replace retention, and which operator -- Merge, Abstract, or Rewrite -- should be selected? We formalize this decision by decomposing each operator's utility into a coverage effect on evidence omitted by retention and a signed replacement effect on raw evidence that already fits. Their balance explains why the preferred action changes with relative budget pressure. We implement this mechanism with Offline Abstraction-Safety (OAS), a lightweight learner that estimates action utilities from pre-generation features with held-out harm calibration. The public LongMemEval and LoCoMo benchmarks show the same budget-dependent pattern. On LongMemEval, consolidation improves absolute accuracy by up to 48% under tight budgets, whereas retention is preferable under loose budgets; LoCoMo replicates this crossover at a smaller budget, consistent with its shorter evidence. On both datasets, cross-note abstraction and merging generally outperform local rewriting when compression is necessary.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
