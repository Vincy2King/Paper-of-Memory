# AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.29537v1
- Published: 2026-08-30
- Updated: 2026-08-30
- Authors: Hongbo Gao, Zeyu Ni, Xin Wen, Siyu Xu, Ruifeng Li
- Tags: agent, benchmark
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2608.29537v1

## One-Sentence Summary
Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or...

进一步看，论文的核心做法或实验重点可以概括为：External memory is a natural remedy, yet it can be harmful when attempted actions are treated as completed progress, turning local execution errors into persistent task-state errors.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or terminate. External memory is a natural remedy, yet it can be harmful when attempted actions are treated as completed progress, turning local execution errors into persistent task-state errors. We propose Achievement-Grounded Memory (AGM), a lightweight closed-loop framework for frozen VLA policies that represents a task as a subgoal sequence with a progress pointer and advances this memory only after the current subgoal is verified by physical evidence. Proprioceptive interaction cues decide when to verify, while coherent point tracking and language-conditioned cross-view comparison, sourced from frozen foundation models through a single 2.43M-parameter verification head, decide what was achieved. AGM thereby converts open-loop execution into a closed loop of execution, verification, and progress, keeping the policy frozen without test-time large-model inference. On the RoboMME Counting benchmark, AGM reaches on PickXTimes and on BinFill, surpassing the strongest memory-augmented baseline by points on average, and the framework yields equally decisive gains on a physical robot. Reliable embodied memory thus depends more on disciplined state updates than on memory capacity.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
