# AtomRec: Evolving Atomic Memory for Agentic Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.04882v1
- Published: 2026-09-04
- Updated: 2026-09-04
- Authors: Peiyu Hu, Weihai Lu, Siying Gu, Zhuodong Liu, Zhaokai Luo, Yuean Niu, Zhiyong Wang, Jia Wang
- Tags: agent, benchmark
- Categories: cs.IR
- URL: http://arxiv.org/abs/2609.04882v1

## One-Sentence Summary
Agentic recommender systems use large language models to maintain semantic memory and support evidence-aware recommendation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic recommender systems use large language models to maintain semantic memory and support evidence-aware recommendation.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory mechanisms often compress user and item information into coarse summaries and connect them with scalar collaborative links, making it difficult to preserve fine-grained preference stages or...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.IR

## Abstract Snapshot
Agentic recommender systems use large language models to maintain semantic memory and support evidence-aware recommendation. However, existing memory mechanisms often compress user and item information into coarse summaries and connect them with scalar collaborative links, making it difficult to preserve fine-grained preference stages or retrieve interpretable evidence as user interests evolve. We propose \textsc{AtomRec}, an agentic recommender with evolving atomic collaborative memory. \textsc{AtomRec} represents user and item memories as structured atomic units, builds semantic links across related memories, and evolves related historical fields when new interactions arrive. During recommendation, it retrieves linked memories as multi-hop evidence paths rather than isolated neighbor summaries, allowing collaborative signals to support grounded ranking. Experiments on four public benchmarks show that \textsc{AtomRec} consistently outperforms state-of-the-art agentic and memory-augmented baselines, with around 8.5\% average relative improvement across metrics.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
