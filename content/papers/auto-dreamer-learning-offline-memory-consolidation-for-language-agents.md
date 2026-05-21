# Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.20616v1
- Published: 2026-05-20
- Updated: 2026-05-20
- Authors: Chongrui Ye, Yuxiang Liu, Yu Wang, Haofei Yu, Yining Zhao, Ge Liu, Julian McAuley, Jiaxuan You
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.20616v1

## One-Sentence Summary
Language agents increasingly operate over streams of related tasks, yet existing memory systems struggle to convert accumulated experience into reusable knowledge.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language agents increasingly operate over streams of related tasks, yet existing memory systems struggle to convert accumulated experience into reusable knowledge.

进一步看，论文的核心做法或实验重点可以概括为：Retrieval-augmented and structured memory methods record per-session observations effectively, but often couple acquisition and consolidation into a single online process, leaving the agent without a global view...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Language agents increasingly operate over streams of related tasks, yet existing memory systems struggle to convert accumulated experience into reusable knowledge. Retrieval-augmented and structured memory methods record per-session observations effectively, but often couple acquisition and consolidation into a single online process, leaving the agent without a global view across sessions to discover recurring patterns, abstract shared procedures, or prune redundant entries. Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory. Auto-Dreamer decouples fast per-session memory acquisition from slow cross-session consolidation. Given a selected working region of a typed memory bank, the consolidator treats the region as read-only evidence, performs bounded tool-use to inspect entries and provenance-linked source trajectories, and synthesizes a fresh compact replacement set that abstracts across sessions and supersedes the original region. We train Auto-Dreamer via GRPO, using end-to-end agent performance as the reward signal to learn how to consolidate memories acquired through fast online experience. Trained on ScienceWorld trajectories alone, Auto-Dreamer outperforms fixed, RL-trained, and prompted memory baselines on ScienceWorld by 7 points while using an active memory bank 12$\times$ smaller than the strongest baseline, and continues to lead on held-out ALFWorld and WebArena without retraining -- using 6$\times$ less memory than the strongest baseline on ALFWorld.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
