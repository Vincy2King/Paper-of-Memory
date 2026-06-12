# WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.12852v1
- Published: 2026-06-11
- Updated: 2026-06-11
- Authors: Renmin Cheng, Changhao Chen
- Tags: agent, episodic, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.12852v1

## One-Sentence Summary
Rapid advances have been made in developing general-purpose embodied agent in environments like Minecraft through the adoption of LLM-augmented hierarchical approaches.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Rapid advances have been made in developing general-purpose embodied agent in environments like Minecraft through the adoption of LLM-augmented hierarchical approaches.

进一步看，论文的核心做法或实验重点可以概括为：Despite their promise, low-level controllers often become performance bottlenecks due to repeated execution failures.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Rapid advances have been made in developing general-purpose embodied agent in environments like Minecraft through the adoption of LLM-augmented hierarchical approaches. Despite their promise, low-level controllers often become performance bottlenecks due to repeated execution failures. We argue that a key limitation is not only the lack of episodic memory, but also the decoupling of \textit{what-where-when} memory from \textit{which-why} reasoning. To address this, we propose \textbf{WISE} (Which-Why Informed Semantic Explorer), a long-horizon agent framework with an enhanced low-level controller equipped with a Causal Event Graph that augments episodic memory with explicit causal structure linking observations to task relevance. Unlike prior work such as MrSteve, which relies on feature similarity for retrieval, WISE enables robust recall under viewpoint changes and supports opportunistic task reordering through causal reasoning. Building on this memory, we propose an Opportunistic Task Scheduler that dynamically re-prioritizes subtasks when causally relevant opportunities are detected. We further equip WISE with a multi-scale progressive exploration strategy to provide spatially comprehensive observations for downstream reasoning. Experiments show that WISE largely improves task success and efficiency on long-horizon sparse tasks, particularly in settings requiring adaptive decision-making.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
