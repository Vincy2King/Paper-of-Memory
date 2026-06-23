# MemoryVLN: Memory-Augmented Vision-Language Navigation

- Source: OpenReview
- Venue: Under review for TMLR
- Paper ID: openreview:vHb61DlKTh
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Unknown
- Tags: agent, benchmark, context, long-term
- Categories: TMLR/-/Submission
- URL: https://openreview.net/forum?id=vHb61DlKTh

## One-Sentence Summary
Vision-Language Navigation (VLN) requires embodied agents to interpret natural language instructions and navigate through previously unseen complex environments.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `Under review for TMLR` 这个 venue 相关。

从摘要来看，作者主要关注的是：Vision-Language Navigation (VLN) requires embodied agents to interpret natural language instructions and navigate through previously unseen complex environments.

进一步看，论文的核心做法或实验重点可以概括为：Despite recent progress with large-scale pretraining and multimodal foundation models, current VLN systems remain limited by shallow temporal modeling and insufficient spatial understanding, often processing only...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：Under review for TMLR
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：memory-augmented
- 来源分类信息：TMLR/-/Submission

## Abstract Snapshot
Vision-Language Navigation (VLN) requires embodied agents to interpret natural language instructions and navigate through previously unseen complex environments. Despite recent progress with large-scale pretraining and multimodal foundation models, current VLN systems remain limited by shallow temporal modeling and insufficient spatial understanding, often processing only short observation sequences and lacking structured memory. Such deficiency severely hinders them from capturing critical information from earlier observations and building detailed representations with structured spatial contexts, unable to make reliable decisions. In this work, we present MemoryVLN, a memory-augmented VLN framework that explicitly models temporal, spatial, and trajectory information to enable long-horizon reasoning and comprehensive spatial understanding. It includes a temporal reasoning memory to adaptively distinguish short-term dynamics and long-term context through selective frame retention, a spatial intelligence memory to build detailed scene graphs with object entities and relationships, and a trajectory memory to visualize historical actions as top-down trajectory maps to encode holistic motion history. With information-intensive memory features, MemoryVLN demonstrates new state-of-the-art performance on R2R-CE and RxR-CE benchmarks by outperforming previous methods by 5%-10%, while simultaneously achieving high computing efficiency by consuming far fewer input tokens. It even largely outperforms previous models with panoramic observations by using RGB observations only. Moreover, experiments on cross-dataset generalization and enhanced spatial reasoning further validate the effectiveness of MemoryVLN in capturing long-term temporal dependencies and 3D scene understanding for embodied navigation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
