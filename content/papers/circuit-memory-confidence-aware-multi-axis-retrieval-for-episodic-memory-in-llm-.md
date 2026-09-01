# CIRCUIT Memory: Confidence-Aware Multi-Axis Retrieval for Episodic Memory in LLM Agents

- Source: OpenReview
- Venue: ACL ARR 2026 August Submission
- Paper ID: openreview:yLpeuklQK4
- Published: 2026-08-04
- Updated: 2026-09-01
- Authors: Unknown
- Tags: agent, episodic, retrieval
- Categories: aclweb.org/ACL/ARR/2026/August/-/Submission
- URL: https://openreview.net/forum?id=yLpeuklQK4

## One-Sentence Summary
Episodic memory retrieval for LLM agents, whether via dense vector similarity or structured multi-axis indexing, generally assumes every extracted query cue is equally reliable,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 August Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Episodic memory retrieval for LLM agents, whether via dense vector similarity or structured multi-axis indexing, generally assumes every extracted query cue is equally reliable, so an incomplete or ambiguous cue can...

进一步看，论文的核心做法或实验重点可以概括为：We introduce CIRCUIT Memory, a two-tier structured episodic memory architecture that instead separates query-cue confidence (how reliably a cue was extracted) from evidence matching (how well a memory satisfies it),...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 August Submission
- 高亮主题命中：agent, episodic, retrieval
- 检索关键词命中：episodic memory, memory retrieval
- 来源分类信息：aclweb.org/ACL/ARR/2026/August/-/Submission

## Abstract Snapshot
Episodic memory retrieval for LLM agents, whether via dense vector similarity or structured multi-axis indexing, generally assumes every extracted query cue is equally reliable, so an incomplete or ambiguous cue can eliminate relevant memories under rigid intersection. We introduce CIRCUIT Memory, a two-tier structured episodic memory architecture that instead separates query-cue confidence (how reliably a cue was extracted) from evidence matching (how well a memory satisfies it), letting retrieval down-weight unreliable cues rather than enforcing hard intersection across axes. On EPBench, replacing hard multi-axis intersection with this confidence-weighted aggregate, using per-axis held-out calibrated confidence, nearly eliminates zero-retrieval failures (61.1% to 1.0%) and is the most robust rule across two books; on LoCoMo, the same additive form, with per-axis confidence calibrated under held-out cross-validation, reaches 81.2% QA accuracy while scanning 41.6% fewer candidates than flat-scan retrieval. We report these gains alongside a candid analysis of where fixed structured strategies, and confidence-weighting itself, still fall short.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
