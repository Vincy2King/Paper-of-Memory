# EvoMem: Memory-Augmented Evolution for Code Optimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.10795v1
- Published: 2026-08-11
- Updated: 2026-08-11
- Authors: Viktor Volkov, Valentin Khrulkov, Andrey V. Galichin, Danil Sivtsov, Nikita Glazkov, Olga Volkova, Konstantin Pchelin, Iaroslav Bespalov, Dmitry V. Dylov, Petr Anokhin, Ivan Oseledets
- Tags: benchmark, context
- Categories: cs.AI, cs.NE
- URL: http://arxiv.org/abs/2608.10795v1

## One-Sentence Summary
Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks and domains.

进一步看，论文的核心做法或实验重点可以概括为：However, existing LLM-driven evolutionary frameworks largely discard such knowledge, repeatedly rediscovering similar ideas and limiting opportunities for cross-run and cross-task learning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：memory augmented, memory-augmented, persistent memory
- 来源分类信息：cs.AI, cs.NE

## Abstract Snapshot
Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks and domains. However, existing LLM-driven evolutionary frameworks largely discard such knowledge, repeatedly rediscovering similar ideas and limiting opportunities for cross-run and cross-task learning. We introduce EvoMem, a persistent memory architecture for LLM-based evolutionary program search that captures and reuses candidate mutation knowledge. EvoMem converts successful mutation events into structured, task-aware advice for future runs. It operates in two phases: after each run, it extracts and stores promising ideas with provenance, and during subsequent evolution, it retrieves a small set of relevant instructions based on the current task and program context to guide mutation. Across geometric optimization, multi-hop question answering, GPU kernel optimization, and related benchmarks, our experiments show positive average improvements in target metrics or search speed for most evaluated settings, while also revealing variability across tasks. Overall, EvoMem provides evidence that persistent memory can reduce some redundant exploration and improve the reuse and adaptation of successful strategies in LLM-driven evolutionary search.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
