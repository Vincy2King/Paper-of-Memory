# Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.17879v1
- Published: 2026-07-20
- Updated: 2026-07-20
- Authors: Ganesh Senrayan, Moyuru Yamada, Ishan Jindal, Kiran Purohit
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.17879v1

## One-Sentence Summary
LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory retrieval methods often lack adaptability and sample efficiency, and struggle to retrieve the right mixture of memories from heterogeneous stores.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning. However, existing memory retrieval methods often lack adaptability and sample efficiency, and struggle to retrieve the right mixture of memories from heterogeneous stores. We propose Exploratory-Assimilating Reflection (EAR), a framework for high initial retrieval performance and sample-efficient adaptation. EAR combines two mechanisms: Exploratory Reflection, which performs iterative search to bootstrap retrieval and collect useful experiences for each query, and Assimilating Reflection, which replays these experiences from an Experience Buffer to refine a global reranker more efficiently than methods relying only on immediate rewards. Experiments show that EAR improves retrieval by up to 17.9% over the baseline retriever on two long-term dialogue benchmarks. We also show that EAR is highly sample-efficient and robust to noisy feedback.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
