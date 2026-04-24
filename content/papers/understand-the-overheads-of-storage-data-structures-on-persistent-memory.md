# Understand the overheads of storage data structures on persistent memory

- Source: OpenReview
- Venue: PPoPP 2020
- Paper ID: openreview:SXC9gIIhta
- Published: 2020-12-31
- Updated: 2026-04-14
- Authors: Abdullah Al Raqibul Islam, Dong Dai
- Tags: benchmark
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=SXC9gIIhta

## One-Sentence Summary
The byte-addressable persistent memory (PMEM) devices have opened new opportunities for building high-performance storage systems.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `PPoPP 2020` 这个 venue 相关。

从摘要来看，作者主要关注的是：The byte-addressable persistent memory (PMEM) devices have opened new opportunities for building high-performance storage systems.

进一步看，论文的核心做法或实验重点可以概括为：With both DRAM and PMEM in the system, it is important to choose the correct storage data structures on each of them to achieve the best overall performance and the needed data persistence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：PPoPP 2020
- 高亮主题命中：benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
The byte-addressable persistent memory (PMEM) devices have opened new opportunities for building high-performance storage systems. With both DRAM and PMEM in the system, it is important to choose the correct storage data structures on each of them to achieve the best overall performance and the needed data persistence. However, this is non-trivial. One reason is the limited understanding of the actual performance characteristic of different data structures on PMEM. In this study, we develop storeds-bench to help developers better understand the overhead they will encounter when using a certain data structure on PMEM. Specifically, storeds-bench is designed as a benchmark suite that leverages YCSB and has various commonly used storage data structures implemented using PMDK (persistent memory develop kit) under different persistent and consistency requirements.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
