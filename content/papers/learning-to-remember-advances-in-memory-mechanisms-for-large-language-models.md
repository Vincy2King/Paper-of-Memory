# Learning to Remember: Advances in Memory Mechanisms for Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.35089v1
- Published: 2026-10-26
- Updated: 2026-10-26
- Authors: Chenye Han, Hongche Yu, Mengyue Wu, Dell Zhang, Jixiang Luo
- Tags: agent, benchmark, context, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2610.35089v1

## One-Sentence Summary
Memory has become a central mechanism for extending large language models (LLMs) beyond fixed context windows, stateless interaction, and static parametric knowledge.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory has become a central mechanism for extending large language models (LLMs) beyond fixed context windows, stateless interaction, and static parametric knowledge.

进一步看，论文的核心做法或实验重点可以概括为：This survey organizes the literature around three complementary dimensions: the life cycle of memory, the storage substrate, and the system role that memory plays in LLM-based agents, while using cognitive-science-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.IR

## Abstract Snapshot
Memory has become a central mechanism for extending large language models (LLMs) beyond fixed context windows, stateless interaction, and static parametric knowledge. This survey organizes the literature around three complementary dimensions: the life cycle of memory, the storage substrate, and the system role that memory plays in LLM-based agents, while using cognitive-science-inspired memory concepts as a lightweight conceptual motivation rather than as a separate technical contribution or implementation family. On this basis, we distinguish three mechanism families: nonparametric memory, where information is stored outside model parameters in text, graph, multimodal, or database-like structures; parametric memory, where information is stored or accessed through activations, key-value caches, learned modules, adapter-based parameterizations, or model weights; and memory for agent evolution, where stored experiences support reinforcement learning, continual learning, procedural reuse, context engineering, and agent harness design. Evaluation is treated as a separate cross-cutting component rather than as a memory mechanism. Unlike surveys that focus primarily on retrieval-augmented generation or long-context modeling, this paper emphasizes the full memory life cycle: construction, maintenance, retrieval, consolidation, forgetting, governance, and evaluation. By aligning conceptual motivations, computational memory mechanisms, benchmarks, and deployment concerns, the survey provides a structured roadmap for designing memory-augmented LLM agents that are persistent, adaptive, auditable, and safe to update over time.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
