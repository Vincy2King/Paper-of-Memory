# ASH: Agents that Self-Hone via Embodied Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.14211v1
- Published: 2026-05-14
- Updated: 2026-05-14
- Authors: Benjamin Schneider, Xavier Schneider, Victor Zhong, Sun Sun
- Tags: agent, long-term, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.14211v1

## One-Sentence Summary
Long-horizon embodied tasks remain a fundamental challenge in AI, as current methods rely on hand-engineered rewards or action-labeled demonstrations, neither of which scales.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon embodied tasks remain a fundamental challenge in AI, as current methods rely on hand-engineered rewards or action-labeled demonstrations, neither of which scales.

进一步看，论文的核心做法或实验重点可以概括为：We introduce ASH, an agentic system that learns an embodied policy from unlabeled, noisy internet video, without reward shaping or expert annotation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Long-horizon embodied tasks remain a fundamental challenge in AI, as current methods rely on hand-engineered rewards or action-labeled demonstrations, neither of which scales. We introduce ASH, an agentic system that learns an embodied policy from unlabeled, noisy internet video, without reward shaping or expert annotation. ASH follows a self-improvement loop; when it gets stuck, ASH learns an Inverse Dynamics Model (IDM) from its own trajectories, and uses its IDM to extract supervision from relevant internet video. ASH uses unsupervised learning to identify key moments from large-scale internet video and retains them as long-term memory -- allowing it to tackle long-horizon problems. We evaluate ASH on two complementary environments demanding multi-hour planning: Pokemon Emerald, a turn-based RPG, and The Legend of Zelda: The Minish Cap, a real-time action-adventure game. In both games, behavioral cloning, retrieval-augmented and zero-shot foundation-model baselines plateau, while ASH sustains progression across our 8-hour evaluation. ASH reaches an average of $11.2/12$ milestones in Pokemon Emerald and $9.9/12$ in Legend of Zelda, while the strongest baseline gets stuck in both environments at an average of $6.5/12$ and $6.0/12$ milestones, respectively. We demonstrate that self-improving agents are a scalable recipe for long-horizon embodied learning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
