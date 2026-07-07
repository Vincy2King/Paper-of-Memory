# HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.03449v1
- Published: 2026-07-03
- Updated: 2026-07-03
- Authors: Li Ji, Siyin Wang, Pengfang Qian, Xiaopeng Yu, Yihai Tian, Zhaoye Fei, Jingjing Gong, Xipeng Qiu
- Tags: long-term
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2607.03449v1

## One-Sentence Summary
Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their...

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate observations.

进一步看，论文的核心做法或实验重点可以概括为：Existing solutions face a ''frequency-competence paradox,'' where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory, working memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate observations. Existing solutions face a ''frequency-competence paradox,'' where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities. To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, and a Planner for long-term strategy. We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through ''Add, Update, and Delete'' operations. This hierarchical design effectively balances the conflict between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks. Experiments demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to self-correct its internal knowledge based on human preferences.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
