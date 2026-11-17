# When Facts Change, Which Decisions Break? Dependency-Aware Context Graphs for Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.19859v1
- Published: 2026-11-15
- Updated: 2026-11-15
- Authors: Paul Deepakraj Retinraj
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.19859v1

## One-Sentence Summary
When an observed fact changes, an agent must identify and repair the decisions that depend on it while preserving unaffected outputs.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：When an observed fact changes, an agent must identify and repair the decisions that depend on it while preserving unaffected outputs.

进一步看，论文的核心做法或实验重点可以概括为：We investigate the reliability-cost trade-off of field-level dependency graphs extracted from actual agent read traces.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
When an observed fact changes, an agent must identify and repair the decisions that depend on it while preserving unaffected outputs. We investigate the reliability-cost trade-off of field-level dependency graphs extracted from actual agent read traces. A controlled benchmark spans three executable workflow domains and four successive updates, with independent imperative and expression-based references. Across 120 workflows, two models and two repeated runs, we compare full recomputation, rolling summary memory, lexical retrieval, trace-extracted dependencies and verified dependency upper bounds. Trace-derived graphs reduce reviewed decisions and estimated total cost, but omitted alternative supports and missing repair context can reduce complete-plan correctness. Paired ablations isolate the effects of edge deletion, spurious edges, transitive propagation and context scope. An exploratory enhancement supplies the existing record ID/field directory during extraction without revealing unread values or reference edges. We evaluate this enhancement on 60 fresh workflows with two repeats per model. On this fresh set, the directory-aware graph matches observed full-context complete-plan correctness for gpt-6.1-sol (100%) with an estimated 4.0% total-cost reduction, but reaches only 84.8% versus 99.6% for gpt-6-luna. The results distinguish potential dependency impact from actual decision invalidity and show why selective repair must be evaluated with both executable correctness and full memory-processing cost. The evidence concerns explicit procedural workflows; broad real-world agent-memory generalization remains untested.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
