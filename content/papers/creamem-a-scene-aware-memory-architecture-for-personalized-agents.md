# CreaMem: A Scene-Aware Memory Architecture for Personalized Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.08550v1
- Published: 2026-09-08
- Updated: 2026-09-08
- Authors: Qixuan Sun, Yue Que, Bowei He, Jin Guo, Dihang Yang, Wenchang Situ, Chen Ma
- Tags: agent, benchmark, episodic, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.08550v1

## One-Sentence Summary
Long-term memory is a core capability for personalized LLM agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is a core capability for personalized LLM agents.

进一步看，论文的核心做法或实验重点可以概括为：To support it, existing memory systems organize information using various criteria such as topic segments or summary hierarchies.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory is a core capability for personalized LLM agents. To support it, existing memory systems organize information using various criteria such as topic segments or summary hierarchies. However, we identify two major limitations in these designs. First, they lack scene awareness: memories from unrelated life scenes share the same retrieval space, which inflates the search space and introduces cross-scene interference. Second, they encode each memory from a single perspective, making it difficult to retrieve complementary views of the same event. In this paper, we propose the CreaMem architecture, which enables scene-aware memory organization by partitioning memory into several Life Scene Memories to reduce cross-scene interference at retrieval. To go beyond the single perspective and achieve cross-memory synergy, entries are dual-coded from both episodic and trait-based perspectives within each memory. We further devise a permemory balanced sampling strategy at retrieval time. Extensive experiments on two long-term memory benchmarks show that CreaMem improves QA accuracy across all evaluation metrics, with particularly large gains on multi-hop reasoning performance, validating scene-aware partitioning and cross-memory synergy. To enhance reproducibility, we release our code in a public GitHub repository.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
