# CoEvo-Mem: Co-Evolving Retrieval Policy and Memory Bank for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01739v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Bowen Ye, Yongchao Xu, Zhijian Li, Xiang Yin, Junkai Ma, Wenzhao Li
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.01739v1

## One-Sentence Summary
As memories accumulate across tasks and sessions, the performance of long-term LLM agents depends jointly on query-specific retrieval and continual memory refinement.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As memories accumulate across tasks and sessions, the performance of long-term LLM agents depends jointly on query-specific retrieval and continual memory refinement.

进一步看，论文的核心做法或实验重点可以概括为：However, existing methods typically optimize either memory access, through iterative query refinement or adaptive retrieval policies, or memory evolution such as structural update.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
As memories accumulate across tasks and sessions, the performance of long-term LLM agents depends jointly on query-specific retrieval and continual memory refinement. However, existing methods typically optimize either memory access, through iterative query refinement or adaptive retrieval policies, or memory evolution such as structural update. This separation overlooks a fundamental feedback loop: retrieval determines which memories receive usage signals, while updated memory bank reshape future retrieval. We propose \textbf{CoEvo-Mem}, a closed-loop framework for co-evolving the retrieval policy and memory bank. For each query, a frozen LLM generates route-specific query rewrites and a routing prior, which a lightweight residual router corrects online. The retrieved context serves as the coupling interface between the two learning processes: task outcomes assign credit to routing decisions, while trajectory-conditioned feedback updates memory values and graph relations. These updates alter how memories are ranked and selected for subsequent queries, thereby closing the feedback loop. To mitigate coupling induced non-stationarity, CoEvo-Mem alternates between updating the router with the memory bank fixed and evolving the memory bank with the retrieval policy fixed. Across seven diverse benchmarks, \textbf{CoEvo-Mem} achieves state-of-the-art performance, demonstrating the importance of retrieval-memory coevolution.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
