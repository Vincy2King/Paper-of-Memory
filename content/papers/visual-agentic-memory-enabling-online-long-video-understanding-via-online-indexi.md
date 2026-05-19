# Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.16481v1
- Published: 2026-05-15
- Updated: 2026-05-15
- Authors: Aiden Yiliu Li, Nels Numan, Anthony Steed
- Tags: agent, context, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2605.16481v1

## One-Sentence Summary
Long video understanding requires more than large context windows.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long video understanding requires more than large context windows.

进一步看，论文的核心做法或实验重点可以概括为：It also needs a memory mechanism that decides what visual evidence to retain, keeps it searchable over long horizons, and grounds later reasoning in recoverable observations rather than compressed latent state alone.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Long video understanding requires more than large context windows. It also needs a memory mechanism that decides what visual evidence to retain, keeps it searchable over long horizons, and grounds later reasoning in recoverable observations rather than compressed latent state alone. We propose Visual Agentic Memory (VAM), a training-free framework with three components. Online Indexing supports selective evidence retention under streaming constraints. Hierarchical Memory organises retained evidence in a Parallel Representation that aligns temporal context with spatial observations. Agentic Retrieval searches, inspects, and verifies candidate evidence before producing a grounded answer. On OVO-Bench, VAM achieves the highest RT+BT average (68.41) across all reported baselines, improving over end-to-end use of the same underlying MLLM (Gemini 3 Flash, 67.46). On the month-scale split of MM-Lifelong train@month (105.6 hours over 51 days), VAM reaches 17.11%, second only to ReMA with GPT-5 (17.62%). These results suggest that long-horizon video understanding benefits from treating visual memory as an explicit, inspectable, and queryable substrate. Code is available at https://github.com/yiliu-li/Visual-Agentic-Memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
