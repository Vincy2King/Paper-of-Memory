# EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents

- Source: OpenReview
- Venue: ACL ARR 2026 January Submission
- Paper ID: openreview:dFQLfagXEK
- Published: 2026-03-20
- Updated: 2026-06-07
- Authors: Unknown
- Tags: agent, benchmark, context, episodic, long-term
- Categories: aclweb.org/ACL/ARR/2026/January/-/Submission
- URL: https://openreview.net/forum?id=dFQLfagXEK

## One-Sentence Summary
We introduce EMemBench, a programmatic benchmark for evaluating long-term memory of agents through interactive games.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 January Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：We introduce EMemBench, a programmatic benchmark for evaluating long-term memory of agents through interactive games.

进一步看，论文的核心做法或实验重点可以概括为：Rather than using a fixed set of questions, EMemBench generates questions from each agent’s own trajectory, covering both text and visual game environments.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 January Submission
- 高亮主题命中：agent, benchmark, context, episodic, long-term
- 检索关键词命中：episodic memory, long-term memory, persistent memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/January/-/Submission

## Abstract Snapshot
We introduce EMemBench, a programmatic benchmark for evaluating long-term memory of agents through interactive games. Rather than using a fixed set of questions, EMemBench generates questions from each agent’s own trajectory, covering both text and visual game environments. Each template computes verifiable ground truth from underlying game signals, with controlled answerability and balanced coverage over memory skills: single/multi-hop recall, induction, temporal, spatial, logical, and adversarial. We evaluate memory agents with strong LMs/VLMs as backbones, using in-context prompting as baselines. Across 15 text games and multiple visual seeds, results are far from saturated: induction and spatial reasoning are persistent bottlenecks, especially in visual setting. Persistent memory yields clear gains for open backbones on text games, but improvements are less consistent for VLM agents, suggesting that visually grounded episodic memory remains an open challenge. A human study further confirms the difficulty of EMemBench.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
