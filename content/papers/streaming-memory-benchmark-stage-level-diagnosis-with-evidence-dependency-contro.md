# Streaming Memory Benchmark: Stage-level Diagnosis with Evidence Dependency Control

- Source: OpenReview
- Venue: LLA 2026 Poster
- Paper ID: openreview:i1gkKNMX0K
- Published: 2026-03-05
- Updated: 2026-04-10
- Authors: Guanming Liu, Haoran Yin, LITIANCHEN, Sikuan Yan, Hongru WANG, Baian Chen, Xiaoteng Ma
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: ICLR.cc/2026/Workshop/LLA/-/Submission
- URL: https://openreview.net/forum?id=i1gkKNMX0K

## One-Sentence Summary
Memory in deployed LLM agents operates under a streaming regime where evidence arrives incrementally, context is bounded, and every pipeline stage incurs recurring latency and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `LLA 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory in deployed LLM agents operates under a streaming regime where evidence arrives incrementally, context is bounded, and every pipeline stage incurs recurring latency and token cost.

进一步看，论文的核心做法或实验重点可以概括为：Yet existing benchmarks evaluate memory statically, providing full history at once and reporting only end-to-end accuracy, making it difficult to (i) attribute failures and costs to specific pipeline stages, and (ii)...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：LLA 2026 Poster
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：memory benchmark
- 来源分类信息：ICLR.cc/2026/Workshop/LLA/-/Submission

## Abstract Snapshot
Memory in deployed LLM agents operates under a streaming regime where evidence arrives incrementally, context is bounded, and every pipeline stage incurs recurring latency and token cost. Yet existing benchmarks evaluate memory statically, providing full history at once and reporting only end-to-end accuracy, making it difficult to (i) attribute failures and costs to specific pipeline stages, and (ii) verify that correct answers truly depend on the memory system rather than in-context extraction or inference shortcuts. We propose a streaming evaluation framework that structures user--agent conversations into streaming episodes with explicit Evidence--Query dependencies and evaluates memory through a four-stage pipeline (Formation, Management, Retrieval, Application) with stage-level accuracy and efficiency metrics. We further show that simply converting existing static benchmarks into a streaming format is insufficient: retrieval and application accuracy can diverge substantially, indicating that some tasks remain solvable without faithfully retrieving the intended evidence. To address this leakage, we construct StreamMemBench, a natively streaming benchmark with per-episode evidence boundaries and evidence-linked distractors that ensure correct answers require the memory pipeline. Across five memory systems and three datasets, we find that formation accuracy saturates while efficiency differs by an order of magnitude, and that retrieval--application divergence serves as a reliable diagnostic signal for evaluation leakage.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
