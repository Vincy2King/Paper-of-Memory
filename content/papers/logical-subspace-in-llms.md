# Logical subspace in LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32907v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Hope Kean, Enric Boix-Adsera
- Tags: working memory
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.32907v1

## One-Sentence Summary
Recent work has identified a human brain network specialized for abstract formal reasoning (Kean et al., 2025).

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent work has identified a human brain network specialized for abstract formal reasoning (Kean et al., 2025).

进一步看，论文的核心做法或实验重点可以概括为：Does the same hold true in language models?

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Recent work has identified a human brain network specialized for abstract formal reasoning (Kean et al., 2025). Does the same hold true in language models? To answer this question, we introduce the minimal viable subspace (MVS) method, which searches for the lowest-rank activation subspace at a layer that preserves task performance when everything outside that subspace is ablated. Using MVS, we demonstrate low-rank subspaces supporting logical inference on Gemma and Qwen models. Furthermore, these subspaces exhibit a clear dissociation from model capacities on other tasks, such that retaining these late logic subspaces preserves inference while impairing factual knowledge, working memory, cognitive control, and arithmetic. Conversely, ablating them reduces logical inference accuracy to chance while largely sparing these other capacities. Our results suggest a functionally localizable core machinery for logic akin to that in the human brain.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
