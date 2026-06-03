# DELTAMEM: Incremental Experience Memory for LLM Agents via Residual Trees

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.03083v1
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Haoran Tan, Zeyu Zhang, Zhicheng Cao, Rui Li, Xu Chen
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.03083v1

## One-Sentence Summary
Large Language Model (LLM)-based agents increasingly rely on memory to learn from experiences over continual interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM)-based agents increasingly rely on memory to learn from experiences over continual interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, storing experiences as independent, flat units leads to substantial redundancy and retrieval conflicts, as similar episodes repeat overlapping content and subtle scene variations cause retrieved memories to...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large Language Model (LLM)-based agents increasingly rely on memory to learn from experiences over continual interactions. However, storing experiences as independent, flat units leads to substantial redundancy and retrieval conflicts, as similar episodes repeat overlapping content and subtle scene variations cause retrieved memories to offer contradictory guidance. To address this, we introduce residual experience, positing that newly acquired experience is often an incremental variation of existing knowledge. We propose DeltaMem, a framework that organizes experience memory into two independent residual trees, one storing goal-conditioned task experience as reusable skills and another for scene-level environment knowledge. Each tree uses a root node for generalized base experiences and incremental delta nodes for subsequent variations, allowing related experiences to share a common foundation without duplication. For retrieval, a failure-penalized similarity scan locates the best match, reconstructing the full experience via root-to-match chain composition. An autonomous consolidation mechanism distills high-frequency paths into new root nodes, enabling the trees to self-organize from general heuristics to specialized variants. Experiments across diverse interactive environments show that DeltaMem consistently outperforms existing baselines. To facilitate future research, we release the code at https://github.com/import-myself/DeltaMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
