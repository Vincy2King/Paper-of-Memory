# MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.28009v1
- Published: 2026-05-27
- Updated: 2026-05-27
- Authors: Hyeonjeong Ha, Jeonghwan Kim, Cheng Qian, Jiayu Liu, William M. Campbell, Yue Wu, Yuji Zhang, Kathleen McKeown, Dilek Hakkani-Tur, Heng Ji
- Tags: benchmark, context, conversation, episodic, long-term, retrieval
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.28009v1

## One-Sentence Summary
Memory-augmented large language models extend reasoning beyond a fixed context window by maintaining long-term memory across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented large language models extend reasoning beyond a fixed context window by maintaining long-term memory across interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory systems often collapse stable user facts, episodic events, and behavioral rules into a shared space, allowing functionally distinct memories to be retrieved and used as interchangeable evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, episodic, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Memory-augmented large language models extend reasoning beyond a fixed context window by maintaining long-term memory across interactions. However, existing memory systems often collapse stable user facts, episodic events, and behavioral rules into a shared space, allowing functionally distinct memories to be retrieved and used as interchangeable evidence. We identify this failure mode as heterogeneous memory contamination, where context-specific events become overgeneralized claims, or semantically relevant but functionally incompatible memories mislead generation. To this end, we introduce MemGuard, a type-aware memory framework that preserves functional memory boundaries during memory construction and retrieval. It assigns each memory an explicit functional role at write time, maintains relations across type-isolated memories, and selectively composes evidence only from necessary memory types, reducing contamination from irrelevant or functionally incompatible evidence. Across hallucination and long-horizon conversation benchmarks, MemGuard improves memory reliability by up to 28.27% while retrieving up to 5.8x fewer memory tokens than prior methods. These results suggest that reliable long-term reasoning depends on principled organization and selective use of heterogeneous memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
