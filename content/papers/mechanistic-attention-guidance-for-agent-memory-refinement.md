# Mechanistic Attention Guidance for Agent Memory Refinement

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.17621v1
- Published: 2026-07-20
- Updated: 2026-07-20
- Authors: Yechao Hong, Haiquan Qiu, Yaqing Wang, Quanming Yao
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.17621v1

## One-Sentence Summary
Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections.

进一步看，论文的核心做法或实验重点可以概括为：However, this text-based paradigm rarely incorporates internal mechanistic signals, leaving how retrieved memory is actually utilized during task execution underexplored.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections. However, this text-based paradigm rarely incorporates internal mechanistic signals, leaving how retrieved memory is actually utilized during task execution underexplored. This limitation can lead to unreliable error attribution and hallucinated memory modifications. In this work, we show that retrieval-head attention provides a mechanistic signal for revealing segment-level memory utilization. By aggregating attention over memory segments and decision steps, we construct a context utilization matrix that exposes recurring memory-use patterns and indicates corresponding refinement strategies. Building on this observation, we propose Attention-Guided Memory Refinement (AGMR), a framework that uses utilization patterns revealed by attention to guide targeted segment-level memory updates. AGMR corrects or enhances memory for failed executions, simplifies memory for successful executions, and verifies each update through re-execution. Experiments on interactive decision-making benchmarks show that AGMR improves both task performance and memory efficiency over text-only memory refinement baselines. Code is available at https://anonymous.4open.science/r/AGMR_code-3262/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
