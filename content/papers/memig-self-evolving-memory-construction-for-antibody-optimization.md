# MEMIG: Self-evolving Memory Construction for Antibody Optimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.41245v1
- Published: 2026-10-30
- Updated: 2026-10-30
- Authors: Yunhui Jang, Zach Wang, Jai Doshi, Kangway Chuang, Sidney Lisanza, Taylor Joren
- Tags: agent, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.41245v1

## One-Sentence Summary
Memory has become central to self-evolving LLM agents, which store and retrieve experience from past rollouts to guide future decisions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory has become central to self-evolving LLM agents, which store and retrieve experience from past rollouts to guide future decisions.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems represent this experience as free-form natural language and maintain it by rewriting, which fits tasks whose experience is narratable.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory has become central to self-evolving LLM agents, which store and retrieve experience from past rollouts to guide future decisions. Existing systems represent this experience as free-form natural language and maintain it by rewriting, which fits tasks whose experience is narratable. However, in scientific discovery and optimization, experience is often a quantity measured by an oracle under a specific context. Rewriting it as text leaves no index for where a record should be, replaces a measurement with a description, and cannot express how interventions interact. To address this, we argue that agent memory for biomolecule optimization should instead be indexable, quantitative, and structured, and we introduce MEMIG. This memory construction framework realizes these three properties. In detail, MEMIG addresses each insight with a domain-grounded identifier and accumulates the quantitative effect measured by a property oracle, so that updates remain local and retrieval becomes an exact lookup. Next, MEMIG connects insights whose interventions are applied together and measures their epistasis by decomposing each evaluated set. Our results show that MEMIG improves performance in most settings across in silico antibody optimization tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
