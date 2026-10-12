# Temporal Evidence Forests for Long-Horizon Multi-Party Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.12874v1
- Published: 2026-10-09
- Updated: 2026-10-09
- Authors: Junyou Guo, Chongyang Tao, Yan He, Yong Wang, Shuai Ma
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.12874v1

## One-Sentence Summary
Long-term memory has been widely adopted in LLM-based agents to support persistent interaction and personalized assistance.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory has been widely adopted in LLM-based agents to support persistent interaction and personalized assistance.

进一步看，论文的核心做法或实验重点可以概括为：Long-term multi-party interactions, however, accumulate substantially more detailed information, with decisions repeatedly updated and states evolving across participants and interaction stages.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory has been widely adopted in LLM-based agents to support persistent interaction and personalized assistance. Long-term multi-party interactions, however, accumulate substantially more detailed information, with decisions repeatedly updated and states evolving across participants and interaction stages. Temporal structure is therefore crucial for tracing such memories: relevant information often appears densely within short intervals, while transitions among different states are anchored by a strict temporal order. Existing temporally aware memory frameworks primarily store time as metadata or use temporal signals to guide retrieval over preconstructed memory structures, without using temporal structure to both recover locally concentrated evidence and reconstruct its complete event progression. To address these limitations, we propose T-Mem, a temporal-structure-based memory framework that preserves interactions and organizes query-relevant evidence through two temporal mechanisms. Temporal Evidence Discovery exploits the local concentration of related messages to recover overlooked evidence, while Temporal Memory Structuring models state transitions and supporting relations over time and compresses low-information spans within the resulting forest. Evidence Forest Linearization then serializes the structured evidence for answer generation. Experiments on two long-term multi-party memory benchmarks demonstrate that T-Mem consistently outperforms competitive memory frameworks across LLMs, parameter settings, domains, and query types.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
