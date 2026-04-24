# Temporal Representations for Exploration: Learning Complex Exploratory Behavior without Extrinsic Rewards

- Source: arXiv
- Venue: N/A
- Paper ID: 2603.02008v2
- Published: 2026-03-02
- Updated: 2026-04-19
- Authors: Faisal Mohamed, Catherine Ji, Benjamin Eysenbach, Glen Berseth
- Tags: agent, episodic
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2603.02008v2

## One-Sentence Summary
Effective exploration in reinforcement learning requires not only tracking where an agent has been, but also understanding how the agent perceives and represents the world.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Effective exploration in reinforcement learning requires not only tracking where an agent has been, but also understanding how the agent perceives and represents the world.

进一步看，论文的核心做法或实验重点可以概括为：To learn powerful representations, an agent should actively explore states that contribute to its knowledge of the environment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Effective exploration in reinforcement learning requires not only tracking where an agent has been, but also understanding how the agent perceives and represents the world. To learn powerful representations, an agent should actively explore states that contribute to its knowledge of the environment. Temporal representations can capture the information necessary to solve a wide range of potential tasks while avoiding the computational cost associated with full state reconstruction. In this paper, we propose an exploration method that leverages temporal contrastive representations to guide exploration, prioritizing states with unpredictable future outcomes. We demonstrate that such representations can enable the learning of complex exploratory x in locomotion, manipulation, and embodied-AI tasks, revealing capabilities and behaviors that traditionally require extrinsic rewards. Unlike approaches that rely on explicit distance learning or episodic memory mechanisms (e.g., quasimetric-based methods), our method builds directly on temporal similarities, yielding a simpler yet effective strategy for exploration.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
