# CoverMem: Coverage-Constrained Visual Memory for Budgeted Embodied Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.32119v1
- Published: 2026-11-24
- Updated: 2026-11-24
- Authors: Ruijie Ma, Haoyue Liu, Mingda Zhang, Dongxu Yue, Xiaoying Tang
- Tags: agent, benchmark, episodic
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.32119v1

## One-Sentence Summary
Episodic-memory embodied question answering enables agents to answer questions based on previously recorded visual observations of the surrounding scenes.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Episodic-memory embodied question answering enables agents to answer questions based on previously recorded visual observations of the surrounding scenes.

进一步看，论文的核心做法或实验重点可以概括为：However, growing observation histories, varying observation quality across viewpoints, and limited computational resources make it challenging to construct and maintain compact visual memories while retrieving...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Episodic-memory embodied question answering enables agents to answer questions based on previously recorded visual observations of the surrounding scenes. However, growing observation histories, varying observation quality across viewpoints, and limited computational resources make it challenging to construct and maintain compact visual memories while retrieving sufficient evidence for question answering. To address these challenges, we introduce CoverMem, which incorporates three key components: (1) a coverage-constrained memory construction method that selects a compact set of informative full frames satisfying object-quality and representative-scene coverage requirements; (2) a coverage-preserving incremental maintenance strategy that locally reselects only the affected frames to satisfy updated coverage requirements as observations arrive; and (3) a budgeted complementary frame selection method that balances question relevance, additional support for question requirements, and redundancy with selected frames within a fixed budget. Experimental results on three benchmarks covering diverse environments and question types demonstrate that CoverMem improves question-answering performance under limited visual budgets.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
