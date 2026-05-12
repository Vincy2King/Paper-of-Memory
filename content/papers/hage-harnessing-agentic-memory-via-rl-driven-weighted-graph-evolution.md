# HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09942v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Dongming Jiang, Yi Li, Guanpeng Li, Qiannan Li, Bingzhe Li
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.09942v1

## One-Sentence Summary
Memory retrieval in agentic large language model (LLM) systems is often treated as a static lookup problem, relying on flat vector search or fixed binary relational graphs.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory retrieval in agentic large language model (LLM) systems is often treated as a static lookup problem, relying on flat vector search or fixed binary relational graphs.

进一步看，论文的核心做法或实验重点可以概括为：However, fixed graph structures cannot capture the varying strength, confidence, and query-dependent relevance of relationships between events.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory, memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory retrieval in agentic large language model (LLM) systems is often treated as a static lookup problem, relying on flat vector search or fixed binary relational graphs. However, fixed graph structures cannot capture the varying strength, confidence, and query-dependent relevance of relationships between events. In this paper, we propose HAGE, a weighted multi-relational memory framework that reconceptualizes retrieval as sequential, query-conditioned traversal over a unified relational memory graph. Memory is organized as relation-specific graph views over shared memory nodes, where each edge is associated with a trainable relation feature vector encoding multiple relational signals. Given a query, an LLM-based classifier identifies the relational intent, and a routing network dynamically modulates the corresponding dimensions of the edge embedding. Traversal scores are computed via a learned combination of semantic similarity and these query-conditioned edge representations. This allows memory traversal to prioritize high-utility relational paths while softly suppressing noisy or weakly relevant connections. Beyond adaptive traversal, HAGE further introduces a reinforcement learning-based training framework that jointly optimizes routing behavior and edge representations using downstream tasks. Finally, empirical results demonstrate improved long-horizon reasoning accuracy and a favorable accuracy-efficiency trade-off compared to state-of-the-art agentic memory systems. Our code is available at https://github.com/FredJiang0324/HAGE_MVPReview.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
