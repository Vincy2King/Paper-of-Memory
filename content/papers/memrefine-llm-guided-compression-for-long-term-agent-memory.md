# MemRefine: LLM-Guided Compression for Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.13177v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Minjae Kim, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang
- Tags: agent, benchmark, compression, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2606.13177v1

## One-Sentence Summary
Large language model (LLM) agents are increasingly expected to operate over long-term interactions, where information from past dialogues must be preserved and recalled to...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents are increasingly expected to operate over long-term interactions, where information from past dialogues must be preserved and recalled to support future tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Large language model (LLM) agents are increasingly expected to operate over long-term interactions, where information from past dialogues must be preserved and recalled to support future tasks. However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence. Furthermore, this is especially limiting on resource-constrained platforms with hard memory budgets, motivating us to formulate storage-budgeted memory management, the task of keeping an already constructed memory store within a fixed budget while preserving information useful for future interactions. To this end, we then propose MemRefine, an LLM-guided framework that, since surface similarity poorly reflects factual value, uses similarity only to propose candidate pairs and defers delete, merge, and preserve decisions to an LLM judge based on factual content, iterating until the budget is met. Across multiple memory frameworks and long-term conversation benchmarks, MemRefine consistently meets target budgets while preserving downstream performance and outperforming rule-based baselines under tight budgets.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
