# TARIC: Memory-Augmented Traversability-Aware Outdoor VLN under Interrupted Semantic Cues

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.31121v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Tianle Zeng, Hanjing Ye, Jianwei Peng, Jingwen Yu, Hanxuan Chen, Hong Zhang
- Tags: agent
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2605.31121v1

## One-Sentence Summary
Outdoor vision-language navigation (VLN) in long-range, open-world environments is frequently disrupted by semantic-cue interruptions, where informative goal cues become sparse,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Outdoor vision-language navigation (VLN) in long-range, open-world environments is frequently disrupted by semantic-cue interruptions, where informative goal cues become sparse, occluded, or leave the field of view.

进一步看，论文的核心做法或实验重点可以概括为：Once such cues disappear, agents enter a cue-free phase and often degrade into backtracking, oscillatory headings, or aimless exploration.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Outdoor vision-language navigation (VLN) in long-range, open-world environments is frequently disrupted by semantic-cue interruptions, where informative goal cues become sparse, occluded, or leave the field of view. Once such cues disappear, agents enter a cue-free phase and often degrade into backtracking, oscillatory headings, or aimless exploration. While memory-based methods attempt to bridge these gaps, they often fail under traversability-driven detours: the remembered cue direction may be infeasible, forcing detours that prolong cue-free phases and gradually render robot-centric cues stale and implicit histories blurred. This makes traversability a stability condition for maintaining goal-directed guidance, rather than merely a local safety concern. We propose a unified outdoor VLN framework that survives semantic-cue interruptions by maintaining traversability-consistent executable guidance throughout prolonged cue-free phases. Specifically, our method extracts semantic bearings from visibility-gated goal or exploration cues and grounds them into executable headings using a real-time near-field traversability profile, providing goal-consistent feasible guidance beyond reject-only safety filtering. To prevent guidance degradation during detours, we lift intermittent 2D evidence into a world-aligned 3D cue memory with an uncertainty-aware readout mechanism, ensuring guidance remains continuously reachable and stable as the robot moves. We evaluate the framework on quadrupedal and wheeled platforms over 600--1000 m routes. Our method improves simulation success rate by over 10 percentage points over the strongest baseline and achieves a real-world success rate of 40%, compared to 17.5% for the strongest baseline, with substantially higher robustness during prolonged cue-free intervals.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
