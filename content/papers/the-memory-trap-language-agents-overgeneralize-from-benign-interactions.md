# The Memory Trap: Language Agents Overgeneralize from Benign Interactions

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.07554v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Kaiqu Liang, Jaime Fernández Fisac, Thomas L. Griffiths, Andrew Lampinen
- Tags: agent
- Categories: cs.CL, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2611.07554v1

## One-Sentence Summary
Language agents increasingly use persistent memory to record user preferences and procedures across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language agents increasingly use persistent memory to record user preferences and procedures across sessions.

进一步看，论文的核心做法或实验重点可以概括为：We show that memory from benign interactions can cause unsafe or unreliable behavior on later tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL, cs.AI, cs.LG

## Abstract Snapshot
Language agents increasingly use persistent memory to record user preferences and procedures across sessions. We show that memory from benign interactions can cause unsafe or unreliable behavior on later tasks. We call this failure the memory trap. To study this issue, we compare behavior in sessions with and without memory across six frontier models (including Claude Sonnet, Opus, and Fable models and GPT-5.6). We evaluate these models in a range of settings. First, in autonomy experiments, we find that requests to skip confirmation during low-stakes coding chores lead agents to skip confirmation and verification on simulated high-stakes tasks in both coding and everyday life. We next study memories formed when users seek emotional support, or describe harm from uncritical feedback, and find these memories bias later judgments of mathematical work, arguments, and poems toward sycophancy or over-critique (respectively). Memory notes written during legitimate stale-test repairs lead agents to weaken correct tests that catch broken safeguards; these memories also increase cheating on ImpossibleBench, with larger increases for stronger Sonnet and Opus models. We show that memory traps can arise both from overgeneralizations in memory writing, and when acting on memory. These findings demonstrate that even benign interactions can lead to serious risks from memory systems, and thus motivate the need for new research into ensuring that agents preserve the scope of their memories.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
