# NEAR: Neighborhood-Aware Residuals for Memory Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.13314v1
- Published: 2026-10-09
- Updated: 2026-10-09
- Authors: Han Luo, Zhan Zhuang, Xu He, Jujia Zhao, Yu Li, Suqin Yuan, Dong Li, Lei Feng
- Tags: benchmark, context, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2610.13314v1

## One-Sentence Summary
Memory retrieval aims to identify evidence from stored records to answer a query.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory retrieval aims to identify evidence from stored records to answer a query.

进一步看，论文的核心做法或实验重点可以概括为：Stored records with different factual details may share topics, entities, or events.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.IR

## Abstract Snapshot
Memory retrieval aims to identify evidence from stored records to answer a query. Stored records with different factual details may share topics, entities, or events. Such shared contents would make records without the required evidence more likely to receive high similarity scores and outrank the correct evidence. In this paper, we use the information shared by these records to construct local references for query-memory matching. We propose NEighborhood-Aware Residuals (NEAR), a training-free framework that uses these references to construct residual representations that complement the original embeddings. Specifically, each memory derives a reference direction from its neighbors, and each query obtains its reference from a precomputed table. Using these references, NEAR constructs projection residuals for both queries and memories. These residuals are combined with the original embeddings for a single approximate nearest-neighbor search over a fixed memory index. Experiments on eight long-context retrieval benchmarks show consistent improvements across nine embedding models. Downstream evaluations show that NEAR improves question-answering performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
