# Neuro-Symbolic Meta-Policies for Temporal Knowledge-Graph Memory under Partial Observability

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.18368v1
- Published: 2026-07-20
- Updated: 2026-07-20
- Authors: Taewoon Kim, Vincent François-Lavet, Michael Cochez
- Tags: long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.18368v1

## One-Sentence Summary
Partially observable reinforcement learning requires deciding what to retain, retrieve, and forget over time.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Partially observable reinforcement learning requires deciding what to retain, retrieve, and forget over time.

进一步看，论文的核心做法或实验重点可以概括为：We introduce a neuro-symbolic meta-policy that learns which symbolic memory heuristic to apply at each decision point while keeping execution symbolic.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Partially observable reinforcement learning requires deciding what to retain, retrieve, and forget over time. We introduce a neuro-symbolic meta-policy that learns which symbolic memory heuristic to apply at each decision point while keeping execution symbolic. Our setting uses temporal knowledge-graph memory in RoomKG, where hidden state and observations are represented as Resource Description Framework (RDF) graphs and memory is augmented with temporal RDF triple annotations. The model combines knowledge-graph encoding of memory contents with value heads for question answering, exploration, and forgetting, yielding a controller that is both adaptive and inspectable. This gives the work a direct Semantic Web grounding through RDF-based representation, annotation-compatible graph semantics, and graph-based symbolic operations over explicit memory state. On train/test room splits at long-term memory capacity of 512, the qualifier-aware StarE-GNN configuration achieves the best held-out performance among the compared symbolic, neural, and neuro-symbolic systems while preserving step-level traceability of memory-management decisions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
