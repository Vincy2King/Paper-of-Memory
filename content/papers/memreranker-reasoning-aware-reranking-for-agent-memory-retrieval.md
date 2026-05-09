# MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.06132v1
- Published: 2026-05-07
- Updated: 2026-05-07
- Authors: Chunyu Li, Jingyi Kang, Ding Chen, Mengyuan Zhang, Jiajun Shen, Bo Tang, Xuanhe Zhou, Feiyu Xiong, Zhiyu Li
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.06132v1

## One-Sentence Summary
In agent memory systems, the reranking model serves as the critical bridge connecting user queries with long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In agent memory systems, the reranking model serves as the critical bridge connecting user queries with long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Most systems adopt the "retrieve-then-rerank" two-stage paradigm, but generic reranking models rely on semantic similarity matching and lack genuine reasoning capabilities, leading to a problem where recalled results...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
In agent memory systems, the reranking model serves as the critical bridge connecting user queries with long-term memory. Most systems adopt the "retrieve-then-rerank" two-stage paradigm, but generic reranking models rely on semantic similarity matching and lack genuine reasoning capabilities, leading to a problem where recalled results are semantically highly relevant yet do not contain the key information needed to answer the question. This deficiency manifests in memory scenarios as three specific problems. First, relevance scores are miscalibrated, making threshold-based filtering difficult. Second, ranking degrades when facing temporal constraints, causal reasoning, and other complex queries. Third, the model cannot leverage dialogue context for semantic disambiguation. This report introduces MemReranker, a reranking model family (0.6B/4B) built on Qwen3-Reranker through multi-stage LLM knowledge distillation. Multi-teacher pairwise comparisons generate calibrated soft labels, BCE pointwise distillation establishes well-distributed scores, and InfoNCE contrastive learning enhances hard-sample discrimination. Training data combines general corpora with memory-specific multi-turn dialogue data covering temporal constraints, causal reasoning, and coreference resolution. On the memory retrieval benchmark, MemReranker-0.6B substantially outperforms BGE-Reranker and matches open-source 4B/8B models as well as GPT-4o-mini on key metrics. MemReranker-4B further achieves 0.737 MAP, with several metrics on par with Gemini-3-Flash, while maintaining inference latency at only 10--20\% of large models. On finance and healthcare vertical-domain benchmarks, the models preserve generalization capabilities on par with mainstream large-parameter rerankers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
