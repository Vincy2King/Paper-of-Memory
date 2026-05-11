# ESSENTIAL: Episodic and Semantic Memory Integration for Video Class-Incremental Learning

- Source: OpenReview
- Venue: CoRR 2025
- Paper ID: openreview:qOghLkWng3
- Published: 2025-12-31
- Updated: 2026-05-11
- Authors: Jongseo Lee, Kyungho Bae, Kyle Min, Gyeong-Moon Park, Jinwoo Choi
- Tags: benchmark, episodic, retrieval
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=qOghLkWng3

## One-Sentence Summary
In this work, we tackle the problem of video classincremental learning (VCIL).

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2025` 这个 venue 相关。

从摘要来看，作者主要关注的是：In this work, we tackle the problem of video classincremental learning (VCIL).

进一步看，论文的核心做法或实验重点可以概括为：Many existing VCIL methods mitigate catastrophic forgetting by rehearsal training with a few temporally dense samples stored in episodic memory, which is memory-inefficient.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2025
- 高亮主题命中：benchmark, episodic, retrieval
- 检索关键词命中：episodic memory, memory retrieval
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
In this work, we tackle the problem of video classincremental learning (VCIL). Many existing VCIL methods mitigate catastrophic forgetting by rehearsal training with a few temporally dense samples stored in episodic memory, which is memory-inefficient. Alternatively, some methods store temporally sparse samples, sacrificing essential temporal information and thereby resulting in inferior performance. To address this trade-off between memory-efficiency and performance, we propose EpiSodic and SEmaNTIc memory integrAtion for video class-incremental Learning (ESSENTIAL). ESSENTIAL consists of episodic memory for storing temporally sparse features and semantic memory for storing general knowledge represented by learnable prompts. We introduce a novel memory retrieval (MR) module that integrates episodic memory and semantic prompts through cross-attention, enabling the retrieval of temporally dense features from temporally sparse features. We rigorously validate ESSENTIAL on diverse datasets: UCF-101, HMDB51, and Something-Something-V2 from the TCD benchmark and UCF-101, ActivityNet, and Kinetics-400 from the vCLIMB benchmark. Remarkably, with significantly reduced memory, ESSENTIAL achieves favorable performance on the benchmarks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
