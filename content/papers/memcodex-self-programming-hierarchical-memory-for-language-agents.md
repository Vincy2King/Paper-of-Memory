# MemCodex: Self-Programming Hierarchical Memory for Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.39765v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Xiaoqiang Wang, Bang Liu
- Tags: agent, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.39765v1

## One-Sentence Summary
Agent memory faces heterogeneous access needs: a single-hop question may require one piece of evidence, whereas a multi-hop question must combine evidence from multiple sources.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory faces heterogeneous access needs: a single-hop question may require one piece of evidence, whereas a multi-hop question must combine evidence from multiple sources.

进一步看，论文的核心做法或实验重点可以概括为：Predefined memory workflows cannot adapt to these varying needs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Agent memory faces heterogeneous access needs: a single-hop question may require one piece of evidence, whereas a multi-hop question must combine evidence from multiple sources. Predefined memory workflows cannot adapt to these varying needs. Recent adaptive methods search or learn over memory components and their compositions, but the design space itself remains predefined. We introduce MemCodex, a self-evolving hierarchical memory system that organizes experience into executable memory programs for summaries, relational knowledge, reusable skills, and latent memory. Open-ended program evolution searches the open design space of layer programs by rewriting how each layer is constructed, indexed, retrieved, and routed, thereby adapting both within-layer implementations and cross-layer composition. At query time, reads traverse the hierarchy from coarse to fine and stop once sufficient evidence is found, descending to the original history when needed. We further develop MemArena, a unified runtime that places heterogeneous data and memory systems behind a common interface. MemCodex improves average task success by 10.1% relative to the strongest adaptive-memory baseline, while using 3.4x fewer context tokens and achieving 2.1x faster inference.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
