# The Trap of Trajectory: Towards Understanding and Mitigating Spurious Correlations in Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.09330v1
- Published: 2026-05-10
- Updated: 2026-05-10
- Authors: Luoxi Tang, Rupali Rajendra Vaje, Yuqiao Meng, Sakshi Sunil Narkar, Weicheng Ma, Zeyu Ding, Dazheng Zhang, Zhaohan Xi
- Tags: agent, benchmark, context, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2605.09330v1

## One-Sentence Summary
Agentic memory enables LLMs to persist information beyond a single context window and reuse it in later decisions, but it also introduces a new vulnerability: spurious...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic memory enables LLMs to persist information beyond a single context window and reuse it in later decisions, but it also introduces a new vulnerability: spurious correlations, where retrieved memory carries...

进一步看，论文的核心做法或实验重点可以概括为：Despite the widespread use of agentic memory, this risk remains largely underexplored.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Agentic memory enables LLMs to persist information beyond a single context window and reuse it in later decisions, but it also introduces a new vulnerability: spurious correlations, where retrieved memory carries miscorrelated evidence and propagates erroneous reasoning into downstream decisions. Despite the widespread use of agentic memory, this risk remains largely underexplored. We address it from two aspects. First, we benchmark several canonical types of spurious patterns identified through causal structure and record them across trajectory-level memory. Diagnosing agentic memory systems on this benchmark reveals that memory improves reasoning on clean inputs but amplifies reliance on spurious patterns when they are present. Second, we propose CAMEL, a plug-and-play calibration method that operates across diverse memory architectures at both write and retrieval time. CAMEL consistently reduces reliance on spurious patterns across all three types while preserving or improving performance on clean inputs and staying robust under adaptive attacks targeting the calibration. Overall, CAMEL offers a principled and lightweight solution toward more reliable agentic memory deployment.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
