# Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.31166v1
- Published: 2026-10-22
- Updated: 2026-10-22
- Authors: Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
- Tags: benchmark
- Categories: cs.RO, cs.CV, cs.LG
- URL: http://arxiv.org/abs/2610.31166v1

## One-Sentence Summary
Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only...

进一步看，论文的核心做法或实验重点可以概括为：We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.RO, cs.CV, cs.LG

## Abstract Snapshot
Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
