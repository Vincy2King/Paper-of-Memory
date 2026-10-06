# Decoupling Memory from Context: Structured Memory for Token-Efficient Test-Time Continual Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.02687v1
- Published: 2026-10-02
- Updated: 2026-10-02
- Authors: Yehya Farhat, Michael Desmond, Anastasios Kyrillidis
- Tags: agent, context, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.02687v1

## One-Sentence Summary
Large language models (LLMs) are increasingly deployed in enterprise, scientific, and medical applications, where agents must incorporate domain-specific knowledge and adapt...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) are increasingly deployed in enterprise, scientific, and medical applications, where agents must incorporate domain-specific knowledge and adapt from experience.

进一步看，论文的核心做法或实验重点可以概括为：Context engineering offers a practical alternative to weight updates by improving model behavior through instructions, strategies, and evidence supplied at inference time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Large language models (LLMs) are increasingly deployed in enterprise, scientific, and medical applications, where agents must incorporate domain-specific knowledge and adapt from experience. Context engineering offers a practical alternative to weight updates by improving model behavior through instructions, strategies, and evidence supplied at inference time. However, adapting context online typically requires a costly trial-and-error process, while queries are often processed independently, preventing useful experience from carrying forward. Memory systems address this limitation by retaining information across interactions, but approaches that continually append information to a shared context face increasing token costs, context-window limits, and performance degradation as the context expands. We introduce a unified formulation of context optimization and show that an agent memory system update can be interpreted as an optimization update procedure over the model's context. This perspective attempts to provide a principled framework for studying memory design and its efficiency. We then propose GraphMemory, a lightweight graph-based memory that accumulates, refines, organizes, and connects reusable strategies. For each query, GraphMemory retrieves only the relevant subgraph, enabling online context adaptation without exposing the model to the entire memory. Under bounded retrieval, the amount of retrieved memory remains constant as the number of processed examples grows. Experiments show that GraphMemory achieves competitive downstream performance while using approximately 81-85% fewer memory-construction tokens than our baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
