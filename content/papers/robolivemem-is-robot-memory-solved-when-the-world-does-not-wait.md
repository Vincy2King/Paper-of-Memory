# RoboLiveMem: Is Robot Memory Solved When the World Does Not Wait?

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.30047v1
- Published: 2026-11-23
- Updated: 2026-11-23
- Authors: Yunbei Zhang, Yuyou Zhang, Janet Wang, Ming Liu, Yijiang Li, Yikai Wang, Weirui Ye, Ding Zhao, Jihun Hamm
- Tags: agent, benchmark
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2611.30047v1

## One-Sentence Summary
Robot agents built on frontier vision-language models now solve most robot memory benchmarks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Robot agents built on frontier vision-language models now solve most robot memory benchmarks.

进一步看，论文的核心做法或实验重点可以概括为：Does this mean they can remember what they need in a home, where people and machines keep moving things?

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Robot agents built on frontier vision-language models now solve most robot memory benchmarks. Does this mean they can remember what they need in a home, where people and machines keep moving things? Existing memory benchmarks cannot answer this question, because they pause the simulator while the model thinks: nothing can change during a decision, so whatever the robot remembers is still true when it acts. We introduce RoboLiveMem, a benchmark that runs the same memory tasks twice, once with the world paused while the model thinks and once with the world running. It contains 29 task families in three tiers, from 16 realistic BEHAVIOR-1K scenes of homes, workshops and a restaurant to controlled ManiSkill tasks. Every task mixes real changes with harmless look-alikes and runs without any change, so that no fixed strategy succeeds, and most tasks have a twin that keeps the change in view, which separates forgetting from acting too late. Testing 16 models on 34,176 episodes, we find three surprises. (1) Paused results hide the problem: when a remembered object changes in a realistic scene, the 8 Claude and GPT models succeed in 97% of episodes on average with the world paused, but in only 50% with the world running, and their ranking changes: Claude Opus 5.5, which never fails when paused, succeeds in 44%. (2) Speed is not the fix: slower models do no worse, and models given only 2 s per decision still fall at least 36 points below their paused success. (3) Models see the change but act on camera frames from before it ended. Looking again just before acting closes most of the realistic gap, yet when identical objects are swapped several times, all nine models we test still lose points to memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
