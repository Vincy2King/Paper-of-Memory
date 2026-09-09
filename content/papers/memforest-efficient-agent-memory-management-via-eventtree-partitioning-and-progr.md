# MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.08273v1
- Published: 2026-09-08
- Updated: 2026-09-08
- Authors: Junxi Wang, Te Sun, Jiayi Zhu, Chen Zhang, Siyuan Li, Xuyang Liu, Zichen Wen, Xiaobing Tu, Jinkui Ren, Xiantao Zhang, Ziqi Yuan, Linfeng Zhang
- Tags: agent, benchmark, compression, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.08273v1

## One-Sentence Summary
Agent memory systems have demonstrated significant potential in long-term dialogue, personalized assistants, and video understanding.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory systems have demonstrated significant potential in long-term dialogue, personalized assistants, and video understanding.

进一步看，论文的核心做法或实验重点可以概括为：However, continuously accumulated memory introduces substantial storage and retrieval costs during inference.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, long-term, retrieval
- 检索关键词命中：agent memory, memory compression
- 来源分类信息：cs.AI

## Abstract Snapshot
Agent memory systems have demonstrated significant potential in long-term dialogue, personalized assistants, and video understanding. However, continuously accumulated memory introduces substantial storage and retrieval costs during inference. To address this issue, we propose \textbf{MemForest}, a general memory compression framework adaptable to various agent memory systems. Specifically, MemForest partitions historical memory into event-centric units by leveraging global semantic similarity and local temporal continuity. For each unit, it constructs a maximum spanning tree, termed an EventTree, and progressively merges redundant memory nodes by selecting high-weight edges, reducing storage overhead. Furthermore, we introduce an anchor-guided propagation retrieval mechanism that retrieves relevant memory nodes from the temporal neighborhoods of key nodes, improving retrieval accuracy. Extensive experiments demonstrate the effectiveness of MemForest. Under the unimodal Mem0 framework, MemForest retains \textbf{97.1%} of the original performance while compressing \textbf{50%} of historical memory across three benchmarks (LoCoMo, LongMemEval, and PersonaMem), achieving a \textbf{1.89x} retrieval speedup. Under the multimodal M3-Agent framework, it preserves \textbf{99.7%} of the original performance with a \textbf{50%} compression ratio across two benchmarks (M3-Bench-robot and M3-Bench-web), achieving a \textbf{2.24x} retrieval speedup. \textcolor{RoyalBlue}{\textit{Our code is available at [https://github.com/Celina-love-sweet/MemForest.}}](https://github.com/Celina-love-sweet/MemForest.}})

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
