# DGAP: Efficient Dynamic Graph Analysis on Persistent Memory

- Source: OpenReview
- Venue: SC 2023
- Paper ID: openreview:7QZI5aArJb
- Published: 2023-12-31
- Updated: 2026-04-14
- Authors: Abdullah Al Raqibul Islam, Dong Dai
- Tags: persistent memory
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=7QZI5aArJb

## One-Sentence Summary
Dynamic graphs, featuring continuously updated vertices and edges, have grown in importance for numerous real-world applications.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `SC 2023` 这个 venue 相关。

从摘要来看，作者主要关注的是：Dynamic graphs, featuring continuously updated vertices and edges, have grown in importance for numerous real-world applications.

进一步看，论文的核心做法或实验重点可以概括为：To accommodate this, graph frameworks, particularly their internal data structures, must support both persistent graph updates and rapid graph analysis simultaneously, leading to complex designs to orchestrate 'fast...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：SC 2023
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
Dynamic graphs, featuring continuously updated vertices and edges, have grown in importance for numerous real-world applications. To accommodate this, graph frameworks, particularly their internal data structures, must support both persistent graph updates and rapid graph analysis simultaneously, leading to complex designs to orchestrate 'fast but volatile' and 'persistent but slow' storage devices. Emerging persistent memory technologies, such as Optane DCPMM, offer a promising alternative to simplify the designs by providing data persistence, low latency, and high IOPS together. In light of this, we propose DGAP, a framework for efficient dynamic graph analysis on persistent memory. Unlike traditional dynamic graph frameworks, which combine multiple graph data structures (e.g., edge list or adjacency list) to achieve the required performance, DGAP utilizes a single mutable Compressed Sparse Row (CSR) graph structure with new designs for persistent memory to construct the framework. Specifically, DGAP introduces a per-section edge log to reduce write amplification on persistent memory; a per-thread undo log to enable high-performance, crash-consistent rebalancing operations; and a data placement schema to minimize in-place updates on persistent memory. Our extensive evaluation results demonstrate that DGAP can achieve up to 3.2× better graph update performance and up to 3.77× better graph analysis performance compared to state-of-the-art dynamic graph frameworks for persistent memory, such as XPGraph, LLAMA, and GraphOne.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
