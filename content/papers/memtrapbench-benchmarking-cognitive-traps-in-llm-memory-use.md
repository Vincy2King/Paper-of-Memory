# MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.20202v1
- Published: 2026-08-20
- Updated: 2026-08-20
- Authors: Mengru Wang, Haozhe Luo, Zhenqian Xu, Zhixiang Cui, Haoming Xu, Qu Yang, Jizhan Fang, Junfeng Fang, Ningyu Zhang
- Tags: benchmark, long-term
- Categories: cs.AI, cs.CL, cs.CY, cs.DB, cs.LG
- URL: http://arxiv.org/abs/2608.20202v1

## One-Sentence Summary
Memory has become a key component of large language models, enabling them to retain information and learn from long-term interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory has become a key component of large language models, enabling them to retain information and learn from long-term interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory benchmarks mainly evaluate whether information is correctly extracted, stored, and retrieved, while largely overlooking how retrieved memories reshape model reasoning and affect performance on...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term
- 检索关键词命中：memory benchmark, memory benchmarks, retrieval memory
- 来源分类信息：cs.AI, cs.CL, cs.CY, cs.DB

## Abstract Snapshot
Memory has become a key component of large language models, enabling them to retain information and learn from long-term interactions. However, existing memory benchmarks mainly evaluate whether information is correctly extracted, stored, and retrieved, while largely overlooking how retrieved memories reshape model reasoning and affect performance on the current task. We identify memory-induced cognitive traps: even faithfully recorded and semantically relevant memories can distort model reasoning or beliefs and degrade current task performance. To systematically evaluate these failure modes, we introduce MemTrapBench, which covers two forms of cognitive traps: Reasoning Fixation and Belief Distortion. Experiments across two model families and five representative memory frameworks show that MemTrapBench is challenging: all evaluated memory strategies underperform the no-memory setting, with even the strongest methods suffering drops of more than 10%. To mitigate these cognitive traps, we propose AdaptiveMem, a simple yet effective inference-time method that instructs LLMs to avoid memory traps. AdaptiveMem mitigates cognitive traps on MemTrapBench while preserving or improving performance on standard memory benchmarks across diverse memory frameworks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
