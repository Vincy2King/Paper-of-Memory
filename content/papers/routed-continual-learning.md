# Routed Continual Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.38796v1
- Published: 2026-10-28
- Updated: 2026-10-28
- Authors: Michael Philip, Mahesh Balakrishnan, David Geraghty, David Mao, Vidhya Venkat, Ilya Mironov
- Tags: agent, context
- Categories: cs.LG, cs.MA
- URL: http://arxiv.org/abs/2610.38796v1

## One-Sentence Summary
Agents deployed at scale repeatedly encounter related problems, and it is natural to let them learn from each other's experience rather than starting over each time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents deployed at scale repeatedly encounter related problems, and it is natural to let them learn from each other's experience rather than starting over each time.

进一步看，论文的核心做法或实验重点可以概括为：Unfortunately, there is no single way to retain that experience that works well across settings, and no way to know in advance which future problems a given experience will help with.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG, cs.MA

## Abstract Snapshot
Agents deployed at scale repeatedly encounter related problems, and it is natural to let them learn from each other's experience rather than starting over each time. Unfortunately, there is no single way to retain that experience that works well across settings, and no way to know in advance which future problems a given experience will help with. A global history preserves every detail but becomes expensive and mixes together experience that may not belong together; compressing that history into one fixed representation limits the cost but can throw away valuable details. We introduce Routed Continual Learning (Routed CL), an architecture that decides how to partition and retain experience. Past trajectories are grouped into clusters, each of which maintains state using one memory system from a fixed library. Before each run, an LLM-based router either reuses an existing cluster or creates a new one, basing its decision on the problem statement, memory system descriptions, and cluster summaries. We also introduce Context Memory Adapter, which mediates between the memory system and the agentic loop. We evaluate the architecture on a heterogeneous stream that interleaves 301 instances from the six CL-Bench tasks with 97 banking instances from $τ^3$-Bench. Across four language models and five matched rollouts, Routed Continual Learning raises normalized reward over a single global in-context learning (ICL) history by 15-30% of the maximum attainable normalized reward, achieves higher mean normalized reward than ICL-only clustering, and reduces estimated API cost by 65-72% relative to Global ICL. These results support approaching continual learning as a routing problem that chooses both a learning mechanism and a state cluster rather than committing to one representation globally.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
