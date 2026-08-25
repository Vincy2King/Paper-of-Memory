# HERO: Human-profile Enhanced Retrieval Optimization Framework for Long-term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.22310v1
- Published: 2026-08-23
- Updated: 2026-08-23
- Authors: Yuanhua Lin, Yile Li, Zhiyuan Zhao, Jing Shang, Jian Sun
- Tags: agent, benchmark, compression, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.22310v1

## One-Sentence Summary
Long-term memory is crucial for personalized responses and long-horizon agent interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is crucial for personalized responses and long-horizon agent interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods often rely on LLMs to compress or rewrite dialogue histories and use the transformed memories as retrieval evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory is crucial for personalized responses and long-horizon agent interactions. Existing methods often rely on LLMs to compress or rewrite dialogue histories and use the transformed memories as retrieval evidence. Despite the progress in organizing fragmented contexts, two major drawbacks persist: (1) information loss from compression, which discards fine-grained but later useful details, and (2) semantic drift from rewriting, which erodes the original tone and situated context. In this work, we propose a novel Human-profile Enhanced Retrieval Optimization framework for long-term agent memory (HERO). Specifically, HERO converts the dialogue history into a traceable heterogeneous memory graph that preserves raw dialogue text as evidence for reasoning, thereby mitigating information loss. For retrieval, HERO extracts initial anchors from the current query and incorporates human profiles via an iterative graph traversal; these anchors and profiles provide guidance signals that adaptively activate the most informative regions of the graph. Experiments on two benchmark datasets show that HERO outperforms strong baselines on both factual and personalized reasoning, while providing more faithful access to raw dialogue evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
