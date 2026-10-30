# Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.40030v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Daniel Strauss, Nikolaos Sotirakis, Zhenshan Bing, Alois Knoll
- Tags: context, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.40030v1

## One-Sentence Summary
Memory in reinforcement learning raises two problems.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory in reinforcement learning raises two problems.

进一步看，论文的核心做法或实验重点可以概括为：Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Memory in reinforcement learning raises two problems. Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits. When a retrieved memory pays off, credit for acquiring it must cross the whole sequence. We argue that both are governed by one quantity, the value of information, and propose to estimate it from archived rollouts with a learned world model. We obtain that, when read at the observation, it yields a provable lower bound on the optimal value of the acquiring action, which floors its TD target and attributes this floor to the observation that earned it. Read at the decision, it defines the optimal retrieval set. A pilot retrieval system, to be trained and improved with this signal, solves a memory task with reduced context.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
