# Memory-Augmented Multimodal Large Language Models for Small Object Understanding in Streaming Aerial Videos

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.19857v1
- Published: 2026-07-22
- Updated: 2026-07-22
- Authors: Penglei Sun, Yehua Huang, Zhuoli Tao, Xiang Li, Runwei Guan, Yaoxian Song, Kaiyong Zhao, Henghui Ding, Bo Han, Yang Yang, Xiaowen Chu
- Tags: compression, context
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2607.19857v1

## One-Sentence Summary
Language-guided aerial perception aims to understand user-specified tiny targets in complex unmanned aerial vehicle (UAV) scenes.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language-guided aerial perception aims to understand user-specified tiny targets in complex unmanned aerial vehicle (UAV) scenes.

进一步看，论文的核心做法或实验重点可以概括为：In real UAV deployment, the UAV must respond while it flies, so such perception runs in an online streaming manner, where frames arrive sequentially and the model responds to each one without access to future frames.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Language-guided aerial perception aims to understand user-specified tiny targets in complex unmanned aerial vehicle (UAV) scenes. In real UAV deployment, the UAV must respond while it flies, so such perception runs in an online streaming manner, where frames arrive sequentially and the model responds to each one without access to future frames. However, applying current Multimodal Large Language Models (MLLMs) to this setting raises two challenges. First, targets viewed from the air are often tiny, yet the visual compression in existing MLLMs treats all regions equally and discards their fine-grained details. Second, understanding a continuous stream requires past-frame context, yet retaining the entire history is infeasible on resource-constrained onboard hardware, whereas discarding it causes the target to drift or disappear. We address the tiny object and streaming challenges from both data and method perspectives. From the data perspective, we present \textbf{DroneEyes}, the \textbf{first} pixel-level and open-vocabulary referring-segmentation dataset for tiny aerial targets, comprising $2,140$ high-definition videos and $176,623$ pairs across Object Description and Referring Expression tasks, with dense per-frame masks. From the method perspective, we propose \textbf{SkyAnchor}, an MLLM with two designs to the above challenges: a Semantics-Aware Token Router that preserves small-target under a reduced visual-token budget, and a Hierarchical Memory Bank that keeps the target consistently understood on streams.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
