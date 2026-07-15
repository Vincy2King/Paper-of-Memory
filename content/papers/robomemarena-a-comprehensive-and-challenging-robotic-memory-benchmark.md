# RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:gZ90mjAw1k
- Published: 2026-12-31
- Updated: 2026-07-15
- Authors: {'fullname': 'Huashuo Lei', 'username': ''}, {'fullname': 'Wenxuan Song', 'username': ''}, {'fullname': 'Huarui Zhang', 'username': ''}, {'fullname': 'Jieyuan Pei', 'username': ''}, {'fullname': 'Jiayi Chen', 'username': ''}, {'fullname': 'Haodong Yan', 'username': ''}, {'fullname': 'Han Zhao', 'username': ''}, {'fullname': 'Pengxiang Ding', 'username': ''}, {'fullname': 'Zhipeng Zhang', 'username': '~Zhipeng_Zhang2'}, {'fullname': 'Lida Huang', 'username': ''}, {'fullname': 'Donglin Wang', 'username': ''}, {'fullname': 'Yan Wang', 'username': ''}, {'fullname': 'Haoang Li', 'username': ''}
- Tags: benchmark
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=gZ90mjAw1k

## One-Sentence Summary
Memory is a critical component of robotic intelligence, as robots must rely on past observations and actions to accomplish long-horizon tasks in partially observable environments.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory is a critical component of robotic intelligence, as robots must rely on past observations and actions to accomplish long-horizon tasks in partially observable environments.

进一步看，论文的核心做法或实验重点可以概括为：However, existing robotic memory benchmarks still lack multimodal annotations for memory formation, provide limited task coverage and structural complexity, and remain restricted to simulation without real-world...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：benchmark
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
Memory is a critical component of robotic intelligence, as robots must rely on past observations and actions to accomplish long-horizon tasks in partially observable environments. However, existing robotic memory benchmarks still lack multimodal annotations for memory formation, provide limited task coverage and structural complexity, and remain restricted to simulation without real-world evaluation. We address this gap with RoboMemArena, a large-scale benchmark of 26 tasks, with average trajectory lengths exceeding 1,000 steps per task and 68.9% of subtasks being memory-dependent. The generation pipeline leverages a vision-language model (VLM) to design and compose subtasks, generates full trajectories through atomic functions, and provides memory-related annotations, including subtask instructions and native keyframe annotations, while paired real-world memory tasks support physical evaluation. We further design PrediMem, a dual-system VLA in which a high-level VLM planner manages a memory bank with recent and keyframe buffers and uses a predictive coding head to improve sensitivity to task dynamics. Extensive experiments on RoboMemArena show that PrediMem outperforms all baselines and provides insights into memory management, model architecture, and scaling laws for complex memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
