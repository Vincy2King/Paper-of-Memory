# MEMORA: A Memory-Enhanced Multimodal Committee Reranking Agent for Reasoning-Intensive Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.25282v1
- Published: 2026-10-18
- Updated: 2026-10-18
- Authors: Mohamed Mahmoud, Mostafa Farouk Senussi, Mahmoud Abdalla, Mahmoud SalahEldin Kasem, Abdelrahman Abdallah, Hyun Soo Kang
- Tags: agent, episodic, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2610.25282v1

## One-Sentence Summary
Reasoning-intensive retrieval is fundamentally challenged when queries demand deep semantic inference and arrive in multimodal form.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Reasoning-intensive retrieval is fundamentally challenged when queries demand deep semantic inference and arrive in multimodal form.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems treat each query in isolation, rely on monolithic rerankers, and lack retrievers trained for cross-modal reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Reasoning-intensive retrieval is fundamentally challenged when queries demand deep semantic inference and arrive in multimodal form. Existing systems treat each query in isolation, rely on monolithic rerankers, and lack retrievers trained for cross-modal reasoning. We introduce MEMORA, a Memory-Enhanced Multimodal Orchestrated Reranking Agent built around three contributions: (1) Collaborative Factor-Committee Reranking, which decomposes queries into intent factors, extracts factor-specific evidence into a structured matrix, and synthesizes judgments via a memory-conditioned meta-verdict model; (2) an Episodic Memory Module that tracks factor outcomes across queries and dynamically adjusts priorities at inference time; and (3) a Reasoning-Aware Dense Retriever fine-tuned with chain-of-thought augmentation on 20k+ reasoning-intensive pairs. Evaluated on MM-BRIGHT across 29 domains, MEMORA achieves nDCG@10 of 41.5 (text-to-text) and 38.9 (multimodal query-to-text), outperforming the strongest agentic text-only baseline by +8.3 points and the strongest agentic multimodal baseline by +7.9 points. Code and data are available at https://github.com/HarnessLab/MEMORA.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
