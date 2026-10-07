# Memory Depth and Reconstructed Context Width: A Controlled Evaluation of Hierarchical Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.08300v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Michael Andreev
- Tags: context, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.08300v1

## One-Sentence Summary
Long-term conversational memory is becoming an integral component of modern LLM systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational memory is becoming an integral component of modern LLM systems.

进一步看，论文的核心做法或实验重点可以概括为：Proposed architectures group records by topics and events, construct hierarchies and graphs, and connect facts through causal and temporal relations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term conversational memory is becoming an integral component of modern LLM systems. Proposed architectures group records by topics and events, construct hierarchies and graphs, and connect facts through causal and temporal relations. We experimentally study the interaction between two memory parameters: structural depth and the width of context supplied to the answer model. Using EverMemBench, we evaluate depths D1-D4, core budgets of 1,024/2,048/4,096 tokens, and additional Production and Oracle conditions up to the full archive. Increasing width from 1K to 4K improves Accuracy by 10.11-17.98 percentage points, whereas increasing depth provides no monotonic gain. Beyond 8-16K, Production performance reaches a plateau while tokens per correct answer continue to increase; Oracle preserves quality on full archives of 68-71K tokens. These results motivate further investigation of large, coherent context blocks instead of progressively deeper memory structures.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
