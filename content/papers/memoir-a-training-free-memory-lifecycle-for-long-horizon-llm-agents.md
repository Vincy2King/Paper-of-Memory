# MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.07631v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Mayank Anand, Subham Raj, Aman Vaibhav Jha, Sriparna Saha
- Tags: agent, compression, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2611.07631v1

## One-Sentence Summary
Long-horizon LLM agents require memory systems that preserve useful information across sessions and retrieve it when needed.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon LLM agents require memory systems that preserve useful information across sessions and retrieve it when needed.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems treat these as separate problems: memories are written prospectively with static importance scores that are never revised after use.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Long-horizon LLM agents require memory systems that preserve useful information across sessions and retrieve it when needed. Existing systems treat these as separate problems: memories are written prospectively with static importance scores that are never revised after use. This creates two coupled failure modes: consolidation can silently destroy evidence that future queries require, while retrieval continues to favor stale memories. We propose MEMOIR (Memory Evidence via Merge-certified, Online Importance Revision), a training-free memory lifecycle that unifies judge-gated consolidation with retrospective attribution. Before compressing memory, screening gates test whether answer-relevant evidence is preserved. After each query, attribution estimates which retrieved memories supported the answer and updates their retrieval priority. A UCB-style exploration bonus additionally encourages retrieval of under-exposed memories, reducing the risk that frequently retrieved memories crowd out useful but less-seen evidence. On 1,905 deduplicated LoCoMo QA pairs, the full retrieval stack improves evidence recall@5 by 11.92 percentage points over bare cosine, with confidence-gated feedback adding 1.50 points overall without reference answers or reranker training; a deployment-unavailable oracle adds 1.84 points overall and 8.05 points on multi-hop. Judge-gated merge changes the recall of text-based evidence from 58.82% to 59.08%, reduces the active store by 1.42%, and incurs 0 observed losses in 100 independently audited merges, with a one-sided 95% upper loss-rate bound of 2.95%. Together, these results outline a practical deployment path: no additional LLM call on the online write path, with merge screening confined to periodic offline consolidation. The lifecycle reduces to one principle: attribute usefulness after use, and screen for preservation before compression.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
