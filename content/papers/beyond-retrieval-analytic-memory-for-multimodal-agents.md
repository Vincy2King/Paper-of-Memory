# Beyond Retrieval: Analytic Memory for Multimodal Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.29440v1
- Published: 2026-07-31
- Updated: 2026-07-31
- Authors: Zhoujin Tian, Yao Tian, Hao Zhang, Cheng Chen, Yakun Li, Lei Zhang, Xiaofang Zhou
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.29440v1

## One-Sentence Summary
Long-term multimodal memory must support not only retrieving relevant information but also computing over observations accumulated across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term multimodal memory must support not only retrieving relevant information but also computing over observations accumulated across interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems largely emphasize \emph{retrieval memory}, organizing interaction histories through summaries and indexes to return query-relevant information at multiple granularities, from high-level abstractions...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term multimodal memory must support not only retrieving relevant information but also computing over observations accumulated across interactions. Existing systems largely emphasize \emph{retrieval memory}, organizing interaction histories through summaries and indexes to return query-relevant information at multiple granularities, from high-level abstractions to underlying records. In this paper, we formulate \emph{analytic memory} as a complementary abstraction that organizes recurring multimodal observations into queryable structures supporting filtering, aggregation, ranking, and temporal comparison. We present AdaMM, a framework that jointly supports retrieval and analytic memory. Rather than relying on application-defined schemas, AdaMM extracts provenance-linked attribute-value observations from dialogue, images, and contextual metadata, discovers recurring field structures, and materializes them for analytical access. At inference time, a memory-aware planner decomposes queries into retrieval and analytic operations and routes each operation to the appropriate tools. Experiments on two long-term multimodal memory benchmarks, MemEye and MemGallery, show that AdaMM improves performance by up to 11.3\% and 7.3\%, respectively.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
