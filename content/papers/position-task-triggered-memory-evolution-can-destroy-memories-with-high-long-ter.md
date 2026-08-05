# Position: Task-Triggered Memory Evolution Can Destroy Memories with High Long-Term Utility

- Source: OpenReview
- Venue: CBW Poster
- Paper ID: openreview:yVsPr3C0Th
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Afrin Dange, Rahul Rahaman, Deepak Gupta, Sankalp Dayal
- Tags: agent, episodic, long-term
- Categories: colmweb.org/COLM/2026/Workshop/CBW/-/Submission
- URL: https://openreview.net/forum?id=yVsPr3C0Th

## One-Sentence Summary
Memory-augmented agents increasingly operate over long-term tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CBW Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory-augmented agents increasingly operate over long-term tasks.

进一步看，论文的核心做法或实验重点可以概括为：These agents rely on persistent memory that evolves through update and delete operations on stored content.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CBW Poster
- 高亮主题命中：agent, episodic, long-term
- 检索关键词命中：memory-augmented, persistent memory
- 来源分类信息：colmweb.org/COLM/2026/Workshop/CBW/-/Submission

## Abstract Snapshot
Memory-augmented agents increasingly operate over long-term tasks. These agents rely on persistent memory that evolves through update and delete operations on stored content. Many existing memory architectures execute these irreversible operations within the task execution loop, treating task feedback as a proxy for memory utility. This position paper argues that task-triggered evolution of memory content can destroy memories with high long-term utility. We introduce a taxonomy of memory-augmented agents organized by the trigger and target of their evolution operations. We present per-operation evidence from nine architectures across procedural and episodic-memory settings. We show that task-triggered update and delete operations precede a substantial share of downstream failures, while methods that defer evolution or restrict evolution to auxiliary content exhibit far fewer. We call on the community to (i) discipline memory operations separately for episodic and procedural memory, and (ii) adopt stage-level diagnostic tools that attribute failures to specific pipeline stages rather than report aggregate accuracy alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
