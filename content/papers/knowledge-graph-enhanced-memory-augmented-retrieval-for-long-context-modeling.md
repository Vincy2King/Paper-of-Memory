# Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling

- Source: OpenReview
- Venue: ACL ARR 2026 March Submission
- Paper ID: openreview:qCI2vlnLSI
- Published: 2026-06-07
- Updated: 2026-06-07
- Authors: Unknown
- Tags: context, retrieval
- Categories: aclweb.org/ACL/ARR/2026/March/-/Submission
- URL: https://openreview.net/forum?id=qCI2vlnLSI

## One-Sentence Summary
Long-context language modeling requires not only extending context windows but maintaining coherent understanding of entity states and relationships across thousands of tokens...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 March Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-context language modeling requires not only extending context windows but maintaining coherent understanding of entity states and relationships across thousands of tokens---a challenge that semantic similarity...

进一步看，论文的核心做法或实验重点可以概括为：KGERMAR addresses this by constructing dynamic, context-specific knowledge graphs from input text during inference, enabling domain-adaptive retrieval that leverages both semantic similarity and explicit entity...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 March Submission
- 高亮主题命中：context, retrieval
- 检索关键词命中：memory-augmented
- 来源分类信息：aclweb.org/ACL/ARR/2026/March/-/Submission

## Abstract Snapshot
Long-context language modeling requires not only extending context windows but maintaining coherent understanding of entity states and relationships across thousands of tokens---a challenge that semantic similarity alone cannot address. KGERMAR addresses this by constructing dynamic, context-specific knowledge graphs from input text during inference, enabling domain-adaptive retrieval that leverages both semantic similarity and explicit entity relationships. The framework performs real-time entity and relation extraction to build contextual knowledge graphs, then integrates graph-structural embeddings with textual semantics through a multi-component memory architecture. Three memory banks---contextual, semantic, and structural---are maintained with retrieval signals fused via learned weights to capture both surface-level semantics and deeper relational patterns. Evaluated on SlimPajama (84.7K training examples), WikiText-103 (4,358 examples), PG-19 (100 examples), and Proof-pile (46.3K examples), KGERMAR achieves up to 8.5\% lower perplexity and 2--2.5x better memory efficiency than memory-augmented baselines across context lengths from 1K to 32K tokens, with superior in-context learning performance across five NLU tasks. The dynamic knowledge graph construction approach advances memory-augmented language modeling by enabling domain-specific knowledge representation that adapts to input contexts rather than relying on fixed knowledge bases.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
