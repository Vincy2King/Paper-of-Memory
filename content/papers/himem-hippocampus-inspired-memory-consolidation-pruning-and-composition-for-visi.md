# HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.09355v1
- Published: 2026-11-06
- Updated: 2026-11-06
- Authors: Boran Zhao, Yanbin Hu, Jun Ye, Zhenxian Hu, Yuxin Zhai, Jin Cui, Pengju Ren
- Tags: episodic
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2611.09355v1

## One-Sentence Summary
Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes.

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes.

进一步看，论文的核心做法或实验重点可以概括为：However, existing VLA memory mechanisms suffer from memory noise, particularly in complex 3D scenes, as stored episodic memories contain extensive redundant details about scene layouts, object configurations, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes. However, existing VLA memory mechanisms suffer from memory noise, particularly in complex 3D scenes, as stored episodic memories contain extensive redundant details about scene layouts, object configurations, and robot-specific states, which obscure generalizable manipulation principles and hinder cross-task transfer. To address this challenge, we first introduce a hippocampus-inspired memory consolidation mechanism that synthesizes extensive episodic experiences into a compact set of essential semantic memories, enabling VLA models to derive generalizable principles from practical experience. Second, we propose an episodic memory pruning mechanism that removes redundant episodic memories whose contents are captured by consolidated semantic memories, thereby increasing effective memory capacity and improving long-horizon task execution. Finally, to handle complex task scenarios, we develop a flexible memory composition mechanism that jointly leverages multiple episodic and semantic memories to enhance cross-scenario generalization. Experiments on LIBERO, LIBERO-Plus demonstrate the effectiveness of HiMEM across different VLA backbones, improving the average success rate of pi_0 from 91.88% to 98.20% on LIBERO.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
