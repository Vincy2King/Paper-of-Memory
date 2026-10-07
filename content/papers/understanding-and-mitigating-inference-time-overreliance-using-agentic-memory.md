# Understanding and Mitigating Inference-Time Overreliance Using Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07311v1
- Published: 2026-10-05
- Updated: 2026-10-05
- Authors: Luoxi Tang, Yuqiao Meng, Nilesh Auradkar, Muchao Ye, Dazheng Zhang, Zhaohan Xi
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.07311v1

## One-Sentence Summary
Agentic memory allows LLM agents to reuse past experience, yet retrieved memories can also distort inference even when they are benign, correctly stored, and appropriately...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic memory allows LLM agents to reuse past experience, yet retrieved memories can also distort inference even when they are benign, correctly stored, and appropriately retrieved.

进一步看，论文的核心做法或实验重点可以概括为：We study this failure mode, which we call memory over-reliance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Agentic memory allows LLM agents to reuse past experience, yet retrieved memories can also distort inference even when they are benign, correctly stored, and appropriately retrieved. We study this failure mode, which we call memory over-reliance. Across benchmarks and memory architectures, we find that memory is useful when past experience transfers to the current task, but can become misleading when only part of the evidence transfers. Failures are strongest under partial query-memory overlap, a pattern further confirmed by controlled experiments thatvary the amount of overlapping evidence. Motivated by this finding, we propose MEMTRIM, a plug-and-play framework that indexes memory evidence at write time and controls its reuse at read time. MEMTRIM removes repeated or conflicting evidence while preserving useful memory-specific information, requires no retraining, and applies to both embedding-based and structured memory systems.Experiments show that MEMTRIM reduces memory overreliance while preserving the benefits of useful memory across models and memory settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
