# Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.23195v1
- Published: 2026-06-22
- Updated: 2026-06-22
- Authors: Zewen Liu
- Tags: agent, long-term
- Categories: cs.LG, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.23195v1

## One-Sentence Summary
Large Language Model (LLM) agents increasingly rely on memory systems to maintain long-term coherence.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM) agents increasingly rely on memory systems to maintain long-term coherence.

进一步看，论文的核心做法或实验重点可以概括为：Recent work shows that agent memories degrade during continuous consolidation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG, cs.AI, cs.CL

## Abstract Snapshot
Large Language Model (LLM) agents increasingly rely on memory systems to maintain long-term coherence. Recent work shows that agent memories degrade during continuous consolidation. However, existing research assumes memories are derived from unbiased experiences. In this work, we identify and formalize a novel phenomenon: Memory Contagion -- the cross-temporal propagation of evaluator bias through agent memory. We show that when agents are trained or guided by biased evaluators, their experiences become biased; when these trajectories are stored and consolidated into memory, the bias propagates to future agents retrieving from the same memory store, even when consolidation is perfect (oracle). Across two bias types (length preference, authority bias) and four experimental phases, we demonstrate: (1) Memory Contagion occurs even with perfect consolidation (oracle condition), proving that biased input is a sufficient cause of contagion; (2) Consolidation has opposite effects depending on bias type -- robustly attenuating length bias while preliminarily amplifying authority bias (single-run estimate), suggesting a bias-type-dependent interaction; (3) No observed safe threshold: bias propagation is detected at contamination rates as low as p=0.2. Our findings expose a critical vulnerability in current agent memory designs and provide formal tools for measuring cross-temporal bias propagation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
