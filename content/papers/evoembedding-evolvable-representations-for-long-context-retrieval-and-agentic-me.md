# EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.21649v1
- Published: 2026-06-19
- Updated: 2026-06-19
- Authors: Chang Nie, Chaoyou Fu, Junlan Feng, Caifeng Shan
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.21649v1

## One-Sentence Summary
Existing embedding models are inherently static: they encode text segments in isolation, ignoring their surrounding context and temporal order.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing embedding models are inherently static: they encode text segments in isolation, ignoring their surrounding context and temporal order.

进一步看，论文的核心做法或实验重点可以概括为：This paper introduces EvoEmbedding, a novel embedding model that generates evolvable representations for retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Existing embedding models are inherently static: they encode text segments in isolation, ignoring their surrounding context and temporal order. This paper introduces EvoEmbedding, a novel embedding model that generates evolvable representations for retrieval. It is tailored for long-context scenarios, where information is dynamic, sequential, and requires continuous state tracking. Our design is simple: EvoEmbedding maintains a continuously updated latent memory as it sequentially processes inputs, and uses it alongside the raw content to jointly generate evolvable embeddings. Consequently, for the same query, our model adapts its representation to retrieve distinct targets based on the evolving context, going beyond static semantic search. To equip the model with this capability, we construct EvoTrain-180K, a diverse dataset for the joint optimization of latent memory and retrieval. Furthermore, we introduce a memory queue to prevent representation collapse during recurrent encoding, alongside segment-batching techniques that tackle significant length variance and accelerate training by 3.8$\times$. Extensive experiments show that our model not only outperforms larger-scale specialists (e.g., Qwen3-Embedding-8B and KaLM-Embedding-Gemma3-12B) across a range of long-context retrieval benchmarks, but also generalizes well to downstream tasks (e.g., personalization) with contexts 10$\times$ longer than its training window. Notably, EvoEmbedding seamlessly integrates into agentic workflows to boost performance. For instance, a naive RAG pipeline equipped with our model surpasses dedicated agentic memory systems. Project Page: https://clare-nie.github.io/EvoEmbedding.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
