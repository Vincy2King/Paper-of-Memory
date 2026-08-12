# MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.10108v1
- Published: 2026-08-10
- Updated: 2026-08-10
- Authors: Beidi Zhao, Yaoqi Chen, Yuru Feng, Menghao Li, Qianxi Zhang, Baotong Lu, Jianan Lu, Zhirui Wang, Xinjiang Wang, Shusen Xu, Zengzhong Li, Xiaoxiao Li, Qi Chen
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.10108v1

## One-Sentence Summary
Long-horizon agents accumulate trajectories spanning hundreds of interleaved reasoning, action, and observation steps, where answering a query may depend on evidence buried far...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon agents accumulate trajectories spanning hundreds of interleaved reasoning, action, and observation steps, where answering a query may depend on evidence buried far back in the history.

进一步看，论文的核心做法或实验重点可以概括为：External memory stores such trajectories as structured representations, yet each structure provides a distinct and incomplete view.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon agents accumulate trajectories spanning hundreds of interleaved reasoning, action, and observation steps, where answering a query may depend on evidence buried far back in the history. External memory stores such trajectories as structured representations, yet each structure provides a distinct and incomplete view. Existing multi-memory systems either read a fixed set of structures for every query, inflating context and introducing noise, or route each query to a single structure, preventing the composition of complementary evidence. A controlled analysis on AMA-Bench shows that the optimal memory configuration is typically neither a single structure nor the full union, but a tailored composition of multiple structural memories that varies with query and task demands. Motivated by these findings, we formulate structure-level dynamic selection: selecting and fusing a query-adaptive subset from a library of specialized memory structures. We propose MESA (a Multi-structure Evidence Selection framework for long-horizon Agent), which builds five complementary structure views of each trajectory and learns from end-to-end answer-level feedback to select and fuse a query-specific subset for a frozen answer model. To learn under this weak supervision, MESA employs harness optimization with prior-guided search and UCB-guided scheduling to balance exploration and exploitation. On AMA-Bench, MESA outperforms the strongest baseline by 8.5% while using 41% fewer evidence tokens than the all-structure alternative.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
