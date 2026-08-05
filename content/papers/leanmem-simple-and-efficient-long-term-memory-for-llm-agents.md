# LeanMem: Simple and Efficient Long-Term Memory for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.03463v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Yuxin Liao, Le Wu, Min Hou, Hao Liu, Han Wu, Zishu Wang
- Tags: agent, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.03463v1

## One-Sentence Summary
Long-term memory is essential for LLM-based agents to sustain interactions and reliably leverage distant history.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for LLM-based agents to sustain interactions and reliably leverage distant history.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory systems typically process heterogeneous dialogue content through a uniform summarization and retrieval pipeline, leading to either excessive token consumption or irreversible loss of fine-...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory is essential for LLM-based agents to sustain interactions and reliably leverage distant history. However, existing memory systems typically process heterogeneous dialogue content through a uniform summarization and retrieval pipeline, leading to either excessive token consumption or irreversible loss of fine-grained evidence. We argue that historical dialogue content should be handled differently according to its compressibility, temporal dynamics, and fidelity requirements. Based on this insight, we propose LeanMem, a lightweight long-term memory framework. LeanMem first filters out low-value content, then stores informative segments as compact profile memory, temporally structured event memory, or source-grounded record memory, depending on the nature of the information. During maintenance, only dynamically evolving event memories are selectively updated, avoiding redundant consolidation of stable profiles and immutable records. During inference, LeanMem dynamically selects memory types and allocates retrieval budgets according to query-specific evidence demands, assembling relevant evidence on demand. On LoCoMo and LongMemEval-S with GPT-4.1-mini and Qwen3-8B, LeanMem improves accuracy over the strongest memory-based baseline in every setting, by up to 15.1 points, at the lowest or near-lowest construction cost, inference tokens, and latency. The code and datasets are included in the supplementary materials.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
