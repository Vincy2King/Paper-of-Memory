# From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21165v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Chaogui Gou
- Tags: agent, benchmark, compression, context, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.21165v1

## One-Sentence Summary
Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-...

进一步看，论文的核心做法或实验重点可以概括为：Existing work on prompt compression, KV-cache management, efficient serving, retrieval augmentation, and agent memory is usually discussed in isolation, leaving the flow of information between storage and computation...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time. Existing work on prompt compression, KV-cache management, efficient serving, retrieval augmentation, and agent memory is usually discussed in isolation, leaving the flow of information between storage and computation insufficiently understood. This survey reframes long-context compression as a memory-management problem for allocating inference-time resources. We distinguish compute-active memory, which directly participates in model computation, from compute-inactive memory, which lies outside the computation path but can be stored, retrieved, updated, or forgotten, and we characterize offloaded KV caches, persistent prefix caches, and precomputed KV states as intermediate states on the activation path. On this basis, we formulate writing, offloading, recall, retrieval-and-injection, materialization, eviction, consolidation, and forgetting as state transitions within an information lifecycle, and introduce a budgeted cost model that places these operations in a single cost account. The resulting framework unifies short-term context compression, long-term memory management, and the transitions between them, and shows that the central challenge is not merely reducing information volume but deciding which information should participate in costly inference, when, and in what form. We further summarize evaluation dimensions, benchmark gaps, and open challenges, and argue that future research should move from static, pointwise compression toward dynamic, governable, lifecycle-aware memory management.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
