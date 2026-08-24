# Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length

- Source: OpenReview
- Venue: COLM 2026
- Paper ID: openreview:7WyNCZXSw7
- Published: 2026-07-08
- Updated: 2026-08-24
- Authors: Chupei Wang, Jiaqiu Vince Sun
- Tags: context, retrieval
- Categories: colmweb.org/COLM/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=7WyNCZXSw7

## One-Sentence Summary
Large language models are often assumed to benefit from longer context windows, yet retrieval from context requires not only locating the target information but also suppressing...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `COLM 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models are often assumed to benefit from longer context windows, yet retrieval from context requires not only locating the target information but also suppressing competing information tied to the same...

进一步看，论文的核心做法或实验重点可以概括为：Inspired by the proactive interference (PI) paradigm in cognitive science, we introduce PI-LLM, an evaluation in which interleaved key-value updates are streamed and models are queried to retrieve only the final value...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：COLM 2026
- 高亮主题命中：context, retrieval
- 检索关键词命中：working memory
- 来源分类信息：colmweb.org/COLM/2026/Conference/-/Submission

## Abstract Snapshot
Large language models are often assumed to benefit from longer context windows, yet retrieval from context requires not only locating the target information but also suppressing competing information tied to the same cue. Inspired by the proactive interference (PI) paradigm in cognitive science, we introduce PI-LLM, an evaluation in which interleaved key-value updates are streamed and models are queried to retrieve only the final value of each key, therefore isolating interference rather than search as the primary variable. Across 35+ models ranging from 0.6B open-weight to frontier-scale proprietary systems, retrieval accuracy declines approximately log-linearly as repeated same-key updates accumulate, with errors dominated by outdated values. Similar log-linear degradation patterns emerge across multiple independent load dimensions, and persist when total input length is held constant, pointing to a working-memory-like bottleneck in maintaining and retrieving the current binding under interference; resistance scales with effective parameter size rather than context window length. This degradation is not alleviated by explicit "forget" instructions or chain-of-thought reasoning, and shows no sign of leveling off within the tested range, in contrast to the plateau observed in human PI studies. Together, these results suggest that LLMs' working-memory-like capacity, though large, is governed by less flexible control than the executive processes that support human resilience to interference.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
