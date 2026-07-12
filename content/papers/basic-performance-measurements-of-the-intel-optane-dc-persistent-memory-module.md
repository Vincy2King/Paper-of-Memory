# Basic Performance Measurements of the Intel Optane DC Persistent Memory Module

- Source: OpenReview
- Venue: CoRR 2019
- Paper ID: openreview:nj36rMxssk
- Published: 2019-01-01
- Updated: 2026-07-11
- Authors: Joseph Izraelevitz, Jian Yang, Lu Zhang, Juno Kim, Xiao Liu, Amir Saman Memaripour, Yun Joon Soh, Zixuan Wang, Yi Xu, Subramanya R. Dulloor, Jishen Zhao, Steven Swanson
- Tags: benchmark
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=nj36rMxssk

## One-Sentence Summary
Scalable nonvolatile memory DIMMs will finally be commercially available with the release of the Intel Optane DC Persistent Memory Module (or just "Optane DC PMM").

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2019` 这个 venue 相关。

从摘要来看，作者主要关注的是：Scalable nonvolatile memory DIMMs will finally be commercially available with the release of the Intel Optane DC Persistent Memory Module (or just "Optane DC PMM").

进一步看，论文的核心做法或实验重点可以概括为：This new nonvolatile DIMM supports byte-granularity accesses with access times on the order of DRAM, while also providing data storage that survives power outages.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2019
- 高亮主题命中：benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
Scalable nonvolatile memory DIMMs will finally be commercially available with the release of the Intel Optane DC Persistent Memory Module (or just "Optane DC PMM"). This new nonvolatile DIMM supports byte-granularity accesses with access times on the order of DRAM, while also providing data storage that survives power outages. This work comprises the first in-depth, scholarly, performance review of Intel's Optane DC PMM, exploring its capabilities as a main memory device, and as persistent, byte-addressable memory exposed to user-space applications. This report details the technologies performance under a number of modes and scenarios, and across a wide variety of macro-scale benchmarks. Optane DC PMMs can be used as large memory devices with a DRAM cache to hide their lower bandwidth and higher latency. When used in this Memory (or cached) mode, Optane DC memory has little impact on applications with small memory footprints. Applications with larger memory footprints may experience some slow-down relative to DRAM, but are now able to keep much more data in memory. When used under a file system, Optane DC PMMs can result in significant performance gains, especially when the file system is optimized to use the load/store interface of the Optane DC PMM and the application uses many small, persistent writes. For instance, using the NOVA-relaxed NVMM file system, we can improve the performance of Kyoto Cabinet by almost 2x. Optane DC PMMs can also enable user-space persistence where the application explicitly controls its writes into persistent Optane DC media. In our experiments, modified applications that used user-space Optane DC persistence generally outperformed their file system counterparts. For instance, the persistent version of RocksDB performed almost 2x faster than the equivalent program utilizing an NVMM-aware file system.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
