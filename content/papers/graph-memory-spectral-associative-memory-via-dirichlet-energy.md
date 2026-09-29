# Graph Memory: Spectral Associative Memory via Dirichlet Energy

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32365v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Zhaoyang Shi
- Tags: retrieval
- Categories: cs.LG, cs.IR
- URL: http://arxiv.org/abs/2609.32365v1

## One-Sentence Summary
Dense associative memories have traditionally focused on storing and retrieving vector-valued patterns.

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Dense associative memories have traditionally focused on storing and retrieving vector-valued patterns.

进一步看，论文的核心做法或实验重点可以概括为：Many modern machine learning problems, however, are naturally graph-structured, requiring memory mechanisms for relational patterns, graph diffusion geometries, community structures, and graph-based inductive biases.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.LG, cs.IR

## Abstract Snapshot
Dense associative memories have traditionally focused on storing and retrieving vector-valued patterns. Many modern machine learning problems, however, are naturally graph-structured, requiring memory mechanisms for relational patterns, graph diffusion geometries, community structures, and graph-based inductive biases. We propose a spectral dense associative memory for storage and retrieval of graph data, extending the classical vector-valued memories. Retrieval is performed through a log-sum-exp energy induced by Dirichlet energy with spectral norm distances, producing a softmax-weighted average of the stored Laplacians that remains a valid graph Laplacian. We prove exponential storage capacity and exponentially decaying retrieval error. Beyond graph retrieval, we establish theoretical guarantees for spectral quantities central to graph learning, including eigenvalues, eigenspaces, and diffusion operators. Experiments on synthetic graph data, real-world airline network, protein conformation data and wearable sensor data demonstrate robust graph retrieval while preserving the graph geometry of the data. Our framework provides a new associative memory paradigm for graph-structured data and bridges dense associative memory with modern graph learning and generative AI.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
