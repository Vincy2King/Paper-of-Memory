# TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory

- Source: OpenReview
- Venue: COLM 2026
- Paper ID: openreview:svKCa4itcd
- Published: 2026-07-08
- Updated: 2026-08-24
- Authors: Qiming Zhu, Shunian Chen, Rui Yu, Zhehao Wu, Benyou Wang
- Tags: agent, benchmark
- Categories: colmweb.org/COLM/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=svKCa4itcd

## One-Sentence Summary
Long-horizon agents must preserve past experience before knowing what future queries will require.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `COLM 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-horizon agents must preserve past experience before knowing what future queries will require.

进一步看，论文的核心做法或实验重点可以概括为：Compact memory makes growing histories efficient to reuse by distilling experience into reusable abstractions, while raw history preserves fine-grained evidence for faithful grounding.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：COLM 2026
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：colmweb.org/COLM/2026/Conference/-/Submission

## Abstract Snapshot
Long-horizon agents must preserve past experience before knowing what future queries will require. Compact memory makes growing histories efficient to reuse by distilling experience into reusable abstractions, while raw history preserves fine-grained evidence for faithful grounding. Because future queries require different levels of detail, the appropriate memory granularity cannot be reliably fixed when memory is written. We therefore argue that memory granularity should be determined when the future information need becomes known. We introduce \textbf{TierMem}, a provenance-linked two-tier memory framework that allocates memory granularity according to evidence sufficiency. TierMem retrieves compact memory by default, uses a learned router to identify when finer-grained evidence is required, and follows provenance links to recover relevant raw evidence. Recovered evidence can be consolidated into compact memory for future reuse. Across two long-horizon memory benchmarks, TierMem recovers much of the quality enabled by raw evidence while substantially reducing inference cost. Further analyses show that provenance improves evidence recovery and that consolidation progressively increases the share of queries served by compact memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
