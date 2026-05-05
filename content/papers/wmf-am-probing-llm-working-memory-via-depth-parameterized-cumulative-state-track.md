# WMF-AM: Probing LLM Working Memory via Depth-Parameterized Cumulative State Tracking

- Source: arXiv
- Venue: N/A
- Paper ID: 2603.27343v2
- Published: 2026-03-28
- Updated: 2026-05-03
- Authors: Dengzhe Hou, Lingyu Jiang, Deng Li, Zirui Li, Fangzhou Lin, Kazunori D Yamada
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2603.27343v2

## One-Sentence Summary
Existing large language models (LLMs) evaluations use fixed-difficulty benchmarks that cannot adapt as models improve, and rarely isolate specific cognitive processes.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing large language models (LLMs) evaluations use fixed-difficulty benchmarks that cannot adapt as models improve, and rarely isolate specific cognitive processes.

进一步看，论文的核心做法或实验重点可以概括为：We introduce Working Memory Fidelity-Active Manipulation (WMF-AM), a probe of cumulative state tracking, the ability to maintain and update intermediate results across K sequential operations within a single query,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Existing large language models (LLMs) evaluations use fixed-difficulty benchmarks that cannot adapt as models improve, and rarely isolate specific cognitive processes. We introduce Working Memory Fidelity-Active Manipulation (WMF-AM), a probe of cumulative state tracking, the ability to maintain and update intermediate results across K sequential operations within a single query, without a scratchpad. Unlike multi-step agent benchmarks that stress task orchestration, WMF-AM isolates within-pass cumulative load by parameterizing depth K. The core probe uses arithmetic accumulation on 28 models from 12 families (0.5B to frontier); a matched non-arithmetic extension (permissions, schedules, inventories) confirms the design generalizes beyond arithmetic. Three construct-isolation ablations confirm that cumulative load, not arithmetic skill or entity tracking, drives difficulty. We release WMF-AM as a lightweight, recalibratable diagnostic for characterizing where models degrade under cumulative load. Code and data can be accessed at https://github.com/dengzhe-hou/WMF-AM

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
