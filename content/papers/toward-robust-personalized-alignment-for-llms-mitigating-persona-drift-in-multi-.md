# Toward Robust Personalized Alignment for LLMs: Mitigating Persona Drift in Multi-Turn Dialogue

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.12373v1
- Published: 2026-09-11
- Updated: 2026-09-11
- Authors: Youyuan Zhang, Siyuan Li, Fangming Liu, Jing Li
- Tags: benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.12373v1

## One-Sentence Summary
Persona drift remains a central challenge for personalized language models, as user profiles evolve over long interactions rather than remain permanently fixed.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persona drift remains a central challenge for personalized language models, as user profiles evolve over long interactions rather than remain permanently fixed.

进一步看，论文的核心做法或实验重点可以概括为：Models must therefore revise persistent persona states when preferences genuinely change, while avoiding updates driven by transient, ambiguous, or unresolved observations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persona drift remains a central challenge for personalized language models, as user profiles evolve over long interactions rather than remain permanently fixed. Models must therefore revise persistent persona states when preferences genuinely change, while avoiding updates driven by transient, ambiguous, or unresolved observations. We propose CORE, which separates turn-local evidence from persistent persona-state revision and selectively updates grounded user preferences through uncertainty-aware belief revision. We also introduce PERSIST, a held-out post-anchor benchmark for persona-state robustness under sequential interaction stress, covering ambiguity, conflict, and controlled social influence. Across ALOE, PersonaChat, and PERSIST, CORE improves personalized alignment and robustness, with complementary gains in normalized closed-slot state fidelity. Human evaluation and mechanistic controls further support explicit update control beyond stronger generation or persistent memory alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
