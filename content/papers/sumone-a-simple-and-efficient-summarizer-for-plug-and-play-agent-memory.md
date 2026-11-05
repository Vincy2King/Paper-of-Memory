# SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.06445v1
- Published: 2026-11-04
- Updated: 2026-11-04
- Authors: Jizhe Zhang, Ang Li, Chenheng Zhang, Yisen Wang
- Tags: agent, compression, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.06445v1

## One-Sentence Summary
Long-horizon language-model agents accumulate increasingly large interaction histories, making context compaction essential for efficient execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon language-model agents accumulate increasingly large interaction histories, making context compaction essential for efficient execution.

进一步看，论文的核心做法或实验重点可以概括为：Existing learned compaction methods often rely on downstream task outcomes or solver behavior, coupling training to specific tasks or agents.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon language-model agents accumulate increasingly large interaction histories, making context compaction essential for efficient execution. Existing learned compaction methods often rely on downstream task outcomes or solver behavior, coupling training to specific tasks or agents. We introduce SumOne, a standalone summarizer trained to preserve information in agent histories through masked reconstruction. Given a summary of the expired history, a frozen reconstructor recovers randomly masked portions of the original trajectory; reconstruction quality, combined with a length penalty, provides a task-agnostic reward for optimizing the summarizer with GRPO. This yields self-supervision directly from raw trajectories, without reference summaries or downstream task execution. At inference time, only the lightweight summarizer is retained, enabling plug-and-play context compression for otherwise unchanged agents. We conduct a systematic evaluation of SumOne in long-horizon search and software-engineering tasks. SumOne reduces estimated inference cost by approximately 78\% on DeepSearchQA and 75\% on SWE-bench Verified relative to operating with full context, with absolute decreases of 0.04. The same checkpoint also transfers across downstream models and agent harnesses without additional fine-tuning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
