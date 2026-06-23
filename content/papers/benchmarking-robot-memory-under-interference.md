# Benchmarking Robot Memory Under Interference

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.22338v1
- Published: 2026-06-21
- Updated: 2026-06-21
- Authors: Soumil Rathi
- Tags: benchmark, context
- Categories: cs.RO, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2606.22338v1

## One-Sentence Summary
Robots deployed in realistic settings will accumulate experience across many sessions and tasks over their deployment.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Robots deployed in realistic settings will accumulate experience across many sessions and tasks over their deployment.

进一步看，论文的核心做法或实验重点可以概括为：The robot's tasks may often require it to remember information from multiple sessions ago, making long-context robot memory important for real-world deployments.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：context memory, memory augmented, memory benchmark, memory benchmarks, memory-augmented
- 来源分类信息：cs.RO, cs.AI, cs.LG

## Abstract Snapshot
Robots deployed in realistic settings will accumulate experience across many sessions and tasks over their deployment. The robot's tasks may often require it to remember information from multiple sessions ago, making long-context robot memory important for real-world deployments. However, most robot-memory benchmarks today are based on single episodes or a short context. To measure how current robot memory systems perform on longer sessions with more distractions, we introduce RoboMME-Interference, a cross-session benchmark built on RoboMME. For each query episode, we construct a session history using the query's relevant prior demonstration followed by a controlled number of unrelated sessions, which we provide to the VLA as memory and measure accuracy. Running RoboMME's released memory-augmented $π_{0.5}$ variants unmodified through this benchmark, we find that while perceptual memory variants improve success when given the history without any distractors, they decay strongly and steadily as unrelated sessions accumulate. With this release, we emphasize the importance of long-context memory and robustness to interference and show that current systems largely fail on such capabilities. The project page, videos, code, and data are at https://robotmemorybench.com.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
