# Topology Survives Shuffling: Robust Long-Context Memory Access Prediction for Graph Analytics

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.39477v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Dongyan Sun, Neelesh Gupta, Rajgopal Kannan, Viktor K. Prasanna
- Tags: context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.39477v1

## One-Sentence Summary
Graph analytics generates irregular, topology-dependent memory-access streams via indirect traversals, limiting data prefetching.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Graph analytics generates irregular, topology-dependent memory-access streams via indirect traversals, limiting data prefetching.

进一步看，论文的核心做法或实验重点可以概括为：Accurate prediction enables timely prefetches that hide memory latency.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Graph analytics generates irregular, topology-dependent memory-access streams via indirect traversals, limiting data prefetching. Accurate prediction enables timely prefetches that hide memory latency. However, ML predictors couple short histories with fixed horizons, fitting the training trace's node layout rather than learning transferable graph patterns. We propose LoCoMAP, a long-context representation-learning framework for memory-access prediction with independently controlled observation history and prediction horizon. We evaluate Connected Components (CC), PageRank (PR), and Single-Source Shortest Paths (SSSP) on six synthetic graph families, with Erdos-Renyi (ER) and Grid as random and deterministic controls. We test two interventions: same-family regeneration changes connectivity, while node shuffling disrupts layout but preserves connectivity. Across 18 graph-workload pairs, extending history from 8 to 128 accesses improves F1 by 7.8%, while extending prediction horizon from 8 to 512 improves F1 by 88.3%. For CC, regeneration is less disruptive than shuffling: without retraining, long context retains 95.4% of original F1 and outperforms short context in six families. Under full shuffle, long context improves CC F1 by 33.6% across ER, Barabasi-Albert, Copying Model, and Stochastic Block Model (SBM), with a 2.06x gain on SBM, but not on Watts-Strogatz or Grid, where near-zero delta mass shifts into heavy tails beyond the predictor's range. Long context outperforms short context on six real-world CC graphs. At full shuffle, long-context PR retains 57.6% of original F1 and averages 11.0% above short context. Both SSSP models retain about 30% of original F1 under full shuffle as distance updates access vertex data in a new order. Within these bounds, long-context predictors are robust across related graphs and layouts without retraining, enabling a generalizable graph prefetcher.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
