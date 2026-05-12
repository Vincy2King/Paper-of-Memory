# MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.10268v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
- Tags: agent, context, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.10268v1

## One-Sentence Summary
To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when...

进一步看，论文的核心做法或实验重点可以概括为：To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
