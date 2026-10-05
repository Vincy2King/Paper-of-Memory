# Interpreting at Write Time: A Policy Ablation for Multi-Goal Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.02897v1
- Published: 2026-10-02
- Updated: 2026-10-02
- Authors: Albert Sadowski, Jarosław A. Chudziak
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.02897v1

## One-Sentence Summary
A long-running assistant cannot keep everything it has seen, so it summarises.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A long-running assistant cannot keep everything it has seen, so it summarises.

进一步看，论文的核心做法或实验重点可以概括为：Summarising is not neutral: what is kept is chosen against some notion of what the record is for, and that choice is made once, before anyone knows which of the user's standing goals will ask.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
A long-running assistant cannot keep everything it has seen, so it summarises. Summarising is not neutral: what is kept is chosen against some notion of what the record is for, and that choice is made once, before anyone knows which of the user's standing goals will ask. Goals rarely disagree about what happened. They disagree about which parts of it were worth the space. Once the history is too long to re-read, the summary replaces the stream, and whatever it left out is gone. We ask what a memory should summarise for when it serves several standing goals at once. Three policies answer differently: summarise with no goal in view, write one summary covering every goal, or write one summary per goal and read them together. We compare them across several models and event streams, holding the read step fixed so that only the write differs. The goals do pull apart: summaries written for different goals overlap each other less than a summary overlaps a rewrite of itself. Per-goal summaries win on relevance, completeness and accuracy, and the all-goal summary loses even to the neutral one written at a fraction of its budget. Interpreting at write pays off, but only for the goal that later asks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
