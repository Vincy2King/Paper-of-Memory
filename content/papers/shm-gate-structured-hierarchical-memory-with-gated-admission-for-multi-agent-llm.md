# SHM-GATE: Structured Hierarchical Memory with Gated Admission for Multi-Agent LLM Hallucination Containment

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:B4JBE7ZfwQ
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Unknown
- Tags: agent, benchmark, conversation, episodic, long-term
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=B4JBE7ZfwQ

## One-Sentence Summary
Multi-agent LLM systems increasingly share a long-term memory, yet most designs commit every candidate write to a single flat store.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Multi-agent LLM systems increasingly share a long-term memory, yet most designs commit every candidate write to a single flat store.

进一步看，论文的核心做法或实验重点可以概括为：We show that this design choice drives hallucination propagation: a speculative, stale, or private statement entered by one agent can be retrieved by another, restated with confidence, and laundered into the shared...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, conversation, episodic, long-term
- 检索关键词命中：episodic memory, long-term memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Multi-agent LLM systems increasingly share a long-term memory, yet most designs commit every candidate write to a single flat store. We show that this design choice drives hallucination propagation: a speculative, stale, or private statement entered by one agent can be retrieved by another, restated with confidence, and laundered into the shared substrate that downstream agents treat as fact. We propose SHM-GATE, a training-free framework that combines three primitives: atomic-claim structurisation of every candidate write, an explicit admission gate that rejects speculation and shadows contradicted facts, and a three-tier hierarchical memory consisting of private episodic memory, a shared semantic graph, and frozen invariants read in trust order. A lightweight evidence-driven correction loop verifies answer claims, counterfactually edits retrieved evidence, and rolls back unsupported claims. We evaluate SHM-GATE on MA-MEMCONFLICT, a 250-sample multi-agent benchmark covering five labelled conflict types, together with scale-stress extensions, LoCoMo long-conversation transfer, a simulated user study, and a gpt-4o backbone-sensitivity run. SHM-GATE is statistically tied with the best-accuracy answerers, including Flat-RAG, while improving Memory Consistency Score by 14 absolute points over Flat-RAG. Under scale stress, baselines degrade substantially at high distractor density, while SHM-GATE retains perfect accuracy across all configurations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
