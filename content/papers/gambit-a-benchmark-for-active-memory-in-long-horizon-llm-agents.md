# GAMBIT: A Benchmark for Active Memory in Long-Horizon LLM Agents

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:qGMh6l7hRw
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Unknown
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=qGMh6l7hRw

## One-Sentence Summary
Long-horizon LLM agents must maintain, update, and revise task state over time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-horizon LLM agents must maintain, update, and revise task state over time.

进一步看，论文的核心做法或实验重点可以概括为：Yet current memory benchmarks mostly test passive retrieval, asking whether a model can find information in a fixed context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Long-horizon LLM agents must maintain, update, and revise task state over time. Yet current memory benchmarks mostly test passive retrieval, asking whether a model can find information in a fixed context. Active memory remains undermeasured, especially how models use changing task state across multi-step interactions. We introduce GAMBIT, a benchmark that uses deterministic game episodes to test active memory in LLM agents. It tests online updating, ordered recall, interference resistance, visuospatial tracking, episodic binding, and hypothesis revision. GAMBIT reveals that the passive-to-active memory gap persists across model families and scales. Models with near-perfect scores on passive retrieval benchmarks such as Needle-in-a-Haystack still fail when they must update state, resist interference, reconstruct episodic routes, or maintain hypotheses across feedback. These results show that reliable long-horizon agents require more than retrieval and need active control over changing state.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
