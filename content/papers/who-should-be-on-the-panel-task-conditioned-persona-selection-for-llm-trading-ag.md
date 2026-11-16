# Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.18150v1
- Published: 2026-11-13
- Updated: 2026-11-13
- Authors: Boming Yang, Yuquan Wang, Jiaxian Guo, Yusuke Iwasawa, Yutaka Matsuo
- Tags: agent
- Categories: q-fin.TR, cs.AI
- URL: http://arxiv.org/abs/2611.18150v1

## One-Sentence Summary
Multi-agent LLM systems are built by fixing a cast of roles and then designing how the cast coordinates.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent LLM systems are built by fixing a cast of roles and then designing how the cast coordinates.

进一步看，论文的核心做法或实验重点可以概括为：Which agents should make up the group for a given task is left to the designer, and the same cast is reused for every task.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：q-fin.TR, cs.AI

## Abstract Snapshot
Multi-agent LLM systems are built by fixing a cast of roles and then designing how the cast coordinates. Which agents should make up the group for a given task is left to the designer, and the same cast is reused for every task. Financial trading makes the cost of that choice visible: stocks trade differently, and the trading styles suited to one need not suit another. We study task-conditioned persona selection, composing the group from the characteristics of the task it will face, and instantiate it with FinPanel, an LLM multi-agent trading system in which a recruiter selects a panel of named trader personas for each stock from a direction-blind statistical sketch of how the stock trades, each persona gives an independent daily call in its own style, and a manager commits the trade after reading the panel's arguments and their desk-kept, hierarchical track records. Because nothing is returned to the traders, the panel stays the panel that was selected, and it can trade a new stock from an empty record. On eight US stocks over the out-of-knowledge year 2025, against three prior LLM trading agents re-implemented in the same framework and against rule-based, predictive and reinforcement-learning baselines, the selected panel is ahead of a fixed panel of the same size and of the prior agents run as their papers prescribe, with a shallower drawdown than buy-and-hold on every stock; it keeps its performance with no warm-up and with no record at all, whereas the memory-augmented agents' returns swing with their warm-up; and neither more seats nor the manager's reading of the arguments substitutes for selecting the right ones. Who is in the group is a design decision to be made per task, before how the group coordinates.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
