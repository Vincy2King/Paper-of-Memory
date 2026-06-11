# Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.11853v1
- Published: 2026-06-10
- Updated: 2026-06-10
- Authors: Zhirui Chen, Ziwei Chen, Ling Shao
- Tags: compression, context, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2606.11853v1

## One-Sentence Summary
Multi-modal large language models (MLLMs) depend on in-context learning (ICL) for rapid task adaptation, but their scalability is severely limited by finite context windows and...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-modal large language models (MLLMs) depend on in-context learning (ICL) for rapid task adaptation, but their scalability is severely limited by finite context windows and the growing cost of key-value (KV)...

进一步看，论文的核心做法或实验重点可以概括为：Existing memory compression approaches typically rely on rigid token removal or sample-dependent importance estimation, which introduces bias, disrupts semantic structure, particularly for visual representations, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context, retrieval
- 检索关键词命中：memory compression
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Multi-modal large language models (MLLMs) depend on in-context learning (ICL) for rapid task adaptation, but their scalability is severely limited by finite context windows and the growing cost of key-value (KV) caches in long multi-modal sequences. Existing memory compression approaches typically rely on rigid token removal or sample-dependent importance estimation, which introduces bias, disrupts semantic structure, particularly for visual representations, and yields static memories that cannot adapt to new queries. We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction. TASM employs task-vector guided compression to replace sample-specific signals with a task-level direction that captures shared relevance across demonstrations. To preserve the underlying manifold, it applies semantics-aware token merging via bipartite graph matching, aggregating tokens without destructive pruning. Finally, TASM structures memory into a hierarchy comprising a compact Core Memory and a Latent Bank, facilitating query-adaptive dynamic retrieval. Evaluations confirm TASM maintains high performance under heavy compression, effectively balancing efficiency with adaptability.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
