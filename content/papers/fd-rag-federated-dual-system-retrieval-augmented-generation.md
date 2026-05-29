# FD-RAG: Federated Dual-System Retrieval-Augmented Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.27432v1
- Published: 2026-05-22
- Updated: 2026-05-22
- Authors: Tianhao Gao, Kai Yang, Yiyang Li
- Tags: benchmark, retrieval
- Categories: cs.IR, cs.AI
- URL: http://arxiv.org/abs/2605.27432v1

## One-Sentence Summary
Retrieval-augmented generation (RAG) has emerged as a paradigm for grounding large language models in external knowledge, yet most existing RAG systems assume centralized...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented generation (RAG) has emerged as a paradigm for grounding large language models in external knowledge, yet most existing RAG systems assume centralized knowledge access and ample computation.

进一步看，论文的核心做法或实验重点可以概括为：These assumptions break down in edge environments, where knowledge is fragmented across devices, raw data cannot be shared, and repeated LLM calls are prohibitively expensive.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.IR, cs.AI

## Abstract Snapshot
Retrieval-augmented generation (RAG) has emerged as a paradigm for grounding large language models in external knowledge, yet most existing RAG systems assume centralized knowledge access and ample computation. These assumptions break down in edge environments, where knowledge is fragmented across devices, raw data cannot be shared, and repeated LLM calls are prohibitively expensive. We propose FD-RAG, a federated dual-system RAG framework that decouples lightweight memory access from on-demand LLM reasoning for decentralized deployment. Specifically, FD-RAG learns semantic-aware adaptive hypergraphs over local corpora and distills them into compact QA memories. At inference time, it answers well-covered queries via direct memory matching and invokes LLM-based reasoning only when necessary, while tracing retrieved memories to hypergraph-grounded evidence. To mitigate cross-device knowledge fragmentation, FD-RAG aggregates anonymized memories across devices without exposing raw documents. Experiments on QA benchmarks show that FD-RAG improves accuracy by up to 7.8\% while reducing latency by 8.4$\times$ compared with strong local and federated baselines. We also provide theoretical analysis establishing an $\mathcal{O}(1/ε^{2})$ convergence rate for the proposed hypergraph learning, supporting its tractable deployment in edge settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
