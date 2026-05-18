# SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.15710v1
- Published: 2026-05-15
- Updated: 2026-05-15
- Authors: Huacan Chai, Yukai Wang, Yingxuan Yang, Dan Peng, Yuanyi Song, Zhihui Fu, Weiwen Liu, Jianghao Lin, Jun Wang, Weinan Zhang
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.15710v1

## One-Sentence Summary
Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across independently originated sources.

进一步看，论文的核心做法或实验重点可以概括为：We argue that source-distributed memory composition is an important and under-examined bottleneck in multimodal agent memory, especially when relevant evidence is fragmented across heterogeneous artifacts such as...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across independently originated sources. We argue that source-distributed memory composition is an important and under-examined bottleneck in multimodal agent memory, especially when relevant evidence is fragmented across heterogeneous artifacts such as conversations, profiles, screenshots, tables, images, and documents. To address this gap, we introduce Source-distributed Multimodal Memory Benchmark(SMMBench), which measures whether agents can retrieve, align, and compose multimodal evidence scattered across multiple sources rather than reason within a single curated context. SMMBench evaluates four core capabilities: (1) cross-source multimodal reasoning; (2) conflict resolution; (3) preference reasoning; (4) memory-grounded action prediction. The benchmark contains 1877 samples grounded in 264 sources. Experiments on representative memory-style and retrieval-based baselines show that current systems still struggle on these capabilities, positioning source-distributed multimodal memory as an important and still under-evaluated challenge for multimodal agents. Our data are available at https://huggingface.co/datasets/HuacanChai/SMMBench.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
