# Discovering Effective Agent Memory Designs through Program Evolution

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.17068v1
- Published: 2026-11-12
- Updated: 2026-11-12
- Authors: Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang, Tairan Chen, Wenya Xie, Yu Hou, Rui Zhang, Zirui Liu
- Tags: agent, benchmark, conversation
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2611.17068v1

## One-Sentence Summary
Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness.

进一步看，论文的核心做法或实验重点可以概括为：We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative diagnosis-proposal loop.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness. We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative diagnosis-proposal loop. Experiments on LoCoMo and LongMemEval yield an absolute accuracy gain of up to 12% over manually designed baselines at 35% of the serving cost, with further evaluations supporting transfer across serving backbones and benchmarks. Empirical analyses and ablations identify and validate two recurring design patterns: retaining raw conversations as retrievable evidence preserves details omitted from extracted memories, while composing retrieved evidence according to query intent helps the answering model use it effectively. Transplanting the composition module into five existing memory systems improves accuracy across all five. Beyond these patterns, the search objective shapes where computation goes: optimizing serving cost alongside accuracy shifts computation from LLM-based memory construction to selective processing at query time while retaining competitive accuracy. Together, these findings offer empirical lessons for agent memory design. Code is available at https://github.com/ash-ding/MAPE.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
