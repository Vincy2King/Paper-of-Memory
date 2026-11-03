# Who Schedules Agent Memory? A Sidecar Approach to Long-Horizon Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.00779v1
- Published: 2026-10-31
- Updated: 2026-10-31
- Authors: Qijia Zhuang, Rui Liu, Yuxiang Ren
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.00779v1

## One-Sentence Summary
As large language model agents increasingly undertake complex, long-horizon tasks, memory has become an important component for supporting sustained decision-making and action.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As large language model agents increasingly undertake complex, long-horizon tasks, memory has become an important component for supporting sustained decision-making and action.

进一步看，论文的核心做法或实验重点可以概括为：Existing methods primarily focus on memory storage, updating, and retrieval, but often overlook how memory scheduling affects task execution: the main agent must identify memory needs, initiate retrieval, and wait for...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
As large language model agents increasingly undertake complex, long-horizon tasks, memory has become an important component for supporting sustained decision-making and action. Existing methods primarily focus on memory storage, updating, and retrieval, but often overlook how memory scheduling affects task execution: the main agent must identify memory needs, initiate retrieval, and wait for results while advancing the task, increasing both scheduling burden and execution time. To address this problem, we propose MemSidecar, which decouples memory scheduling from task execution through two independently selectable modes. Hooks directly delivers bound memory to the main agent when execution events match predefined conditions. Foresight uses an independent agent to predict potential queries, retrieve results in parallel, and store them in a cache, delivering matching and valid results when actual requests arrive. Hooks and Foresight achieve scores of 41.23% and 44.34% on MCP-Persona, respectively, while effectively reducing execution costs and latency and improving the efficiency of long-horizon agent execution.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
