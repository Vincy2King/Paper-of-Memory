# CADedup: High-performance Consistency-aware Deduplication Based on Persistent Memory

- Source: OpenReview
- Venue: ICCD 2022
- Paper ID: openreview:skNEA2npnO
- Published: 2022-01-01
- Updated: 2026-05-26
- Authors: Chunlin Song, Xianzhang Chen, Duo Liu, Xiaoliu Feng, Xi Yu, Jiali Li, Yujuan Tan, Ao Ren
- Tags: benchmark
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=skNEA2npnO

## One-Sentence Summary
Block-level data deduplication is prevalent in various-scaled storage systems for saving storage space and improving I/O performance by reducing write operations.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICCD 2022` 这个 venue 相关。

从摘要来看，作者主要关注的是：Block-level data deduplication is prevalent in various-scaled storage systems for saving storage space and improving I/O performance by reducing write operations.

进一步看，论文的核心做法或实验重点可以概括为：However, data deduplication induces additional metadata of blocks, leading to I/O amplification.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICCD 2022
- 高亮主题命中：benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
Block-level data deduplication is prevalent in various-scaled storage systems for saving storage space and improving I/O performance by reducing write operations. However, data deduplication induces additional metadata of blocks, leading to I/O amplification. Furthermore, to ensure the correctness of deduplicated user data, data deduplication systems need to guarantee crash consistency. In this paper, we propose CADedup, to achieve high performance while ensuring crash consistency by using persistent memory. By taking advantage of the byte-addressability and near-DRAM latency of persistent memory, we design an efficient journaling mechanism to manage the deduplication metadata of CADedup. Additionally, we adopt a hybrid storage architecture of DRAM and persistent memory to minimize space costs. We implement CADedup through the device-mapper interface in the Linux kernel. We conduct extensive experiments on Intel Optane PMEM to evaluate CAD-edup with widely-used benchmarks. Experimental results show that compared with the no-deduplication system, CADedup can achieve up to 1×-3× improvement in many workloads of server storage and has negligible throughput drop in the worst case.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
