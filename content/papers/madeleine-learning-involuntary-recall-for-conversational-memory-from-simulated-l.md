# Madeleine: Learning Involuntary Recall for Conversational Memory from Simulated Lives

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.01118v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Zhiyun Shi
- Tags: context, conversation, long-term
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2610.01118v1

## One-Sentence Summary
A long-term conversational assistant must recall the right memory at the right moment, yet the memory that matters most is often not similar to what the user says now.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A long-term conversational assistant must recall the right memory at the right moment, yet the memory that matters most is often not similar to what the user says now.

进一步看，论文的核心做法或实验重点可以概括为：Current systems recover such associations by letting an LLM reason at write or read time, at a cost of hundreds to over a thousand LLM calls per memory bank and up to several thousand context tokens per query.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, long-term
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
A long-term conversational assistant must recall the right memory at the right moment, yet the memory that matters most is often not similar to what the user says now. Current systems recover such associations by letting an LLM reason at write or read time, at a cost of hundreds to over a thousand LLM calls per memory bank and up to several thousand context tokens per query. We argue that association is a learnable relevance: the pointwise mutual information of memories under how human lives unfold. We introduce Madeleine, which learns amortized association: offline, an LLM life simulator writes simulated lives, whose cue-trigger pairs teach a query encoder a residual association on top of frozen similarity; online, it calls no LLM and plugs into any vector memory by replacing only the query encoder. On LoCoMo-Plus under the official protocol, Madeleine (I) reaches 66.6 when plugged into HyperMem, the highest among all systems evaluated under this protocol; (II) used alone, reaches the score of HyperMem as released (52.4 vs. 52.9) with zero LLM calls and about 1/21 of its answer context; and (III) lifts T-Mem by 26.2 points, significantly outperforms the same untrained backbone inside both systems, and leaves ordinary QA intact on the 4B backbone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
