# CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17926v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Xiaoxue Wu, Xinyu Gao, Fang Yu, Yu Qiao, Xinyuan Chen
- Tags: context, long-term, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2610.17926v1

## One-Sentence Summary
Autoregressive video generation relies on memory retrieval to model long-range dependencies.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Autoregressive video generation relies on memory retrieval to model long-range dependencies.

进一步看，论文的核心做法或实验重点可以概括为：This capability becomes particularly critical for multi-shot generation, where models must reconcile substantial visual changes across shot transitions with persistent semantic continuity.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Autoregressive video generation relies on memory retrieval to model long-range dependencies. This capability becomes particularly critical for multi-shot generation, where models must reconcile substantial visual changes across shot transitions with persistent semantic continuity. Existing methods tend to perform memory retrieval at the frame level and share the same historical context across all query tokens, overlooking the heterogeneous information needs and leading to redundant retrieval and inefficient use of historical memory. To bridge this gap, we introduce CineMem, an attention-aligned fine-grained memory retrieval framework that combines online memory organization with query-adaptive retrieval for autoregressive multi-shot video generation. Specifically, guided by intrinsic memory-access patterns revealed through attention analysis, we propose an online-clustered KV cache as a memory organization strategy over all historical tokens, enabling semantic-aware memory grouping and more precise retrieval. In addition, we introduce a query-level retrieval mechanism that provides broader access to historical information under a fixed retrieval budget, thereby improving long-term memory utilization. Together, these designs enable the multi-shot video generator to preserve long-range consistency across shot transitions, particularly in revisitation scenarios, while approximating full-memory access under a constrained memory budget. To facilitate evaluation, we further introduce a suite of task-specific, VLM-assisted metrics for faithful inter-shot consistency assessment. Extensive experiments demonstrate the effectiveness of our framework.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
