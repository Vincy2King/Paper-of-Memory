# DYNA : Dynamic Episodic Memory Networks for Augmenting Large Language Models with Temporal Knowledge Graphs in Continuous Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.15778v1
- Published: 2026-06-14
- Updated: 2026-06-14
- Authors: Ali Sarabadani, Mahtab Tajvidiyan
- Tags: episodic, retrieval
- Categories: cs.CL, cs.AI, cs.LG, cs.SI
- URL: http://arxiv.org/abs/2606.15778v1

## One-Sentence Summary
Large Language Models (LLMs) struggle to incorporate new knowledge without forgetting or costly retraining.

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) struggle to incorporate new knowledge without forgetting or costly retraining.

进一步看，论文的核心做法或实验重点可以概括为：We propose DYNA, a lightweight framework that augments a frozen LLM with a temporal knowledge graph where events are nodes and temporal relations are directed, timestamped edges.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.CL, cs.AI, cs.LG, cs.SI

## Abstract Snapshot
Large Language Models (LLMs) struggle to incorporate new knowledge without forgetting or costly retraining. We propose DYNA, a lightweight framework that augments a frozen LLM with a temporal knowledge graph where events are nodes and temporal relations are directed, timestamped edges. The graph serves as an external, updatable memory. At query time, DYNA retrieves relevant nodes via random walks and centrality measures, then augments the LLM's response. Evaluated on three temporal recall tasks, DYNA reduces catastrophic forgetting by ~7% compared to fine-tuning and improves temporal ordering by ~5% over standard RAG. Higher graph clustering coefficients correlate with better retrieval, showing that graph structure matters. Contributions: (1) episodic memory as temporal KG, (2) retraining-free LLM augmentation, (3) graph properties as predictors of retrieval performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
