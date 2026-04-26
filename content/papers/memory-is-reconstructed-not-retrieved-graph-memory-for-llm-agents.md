# MEMORY IS RECONSTRUCTED, NOT RETRIEVED: GRAPH MEMORY FOR LLM AGENTS

- Source: OpenReview
- Venue: ICLR 2026 Workshop MemAgents
- Paper ID: openreview:YPoHy6lgKP
- Published: 2026-03-03
- Updated: 2026-04-25
- Authors: Shuo Ji, Yibo Li, Bryan Hooi
- Tags: agent, benchmark, context, retrieval
- Categories: ICLR.cc/2026/Workshop/MemAgent/-/Submission
- URL: https://openreview.net/forum?id=YPoHy6lgKP

## One-Sentence Summary
Despite recent progress, LLM agents still struggle with reasoning over long interaction histories.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Workshop MemAgents` 这个 venue 相关。

从摘要来看，作者主要关注的是：Despite recent progress, LLM agents still struggle with reasoning over long interaction histories.

进一步看，论文的核心做法或实验重点可以概括为：While current memory-augmented agents rely on a static ``retrieve-then-reason'' paradigm, this rigid pipeline design prevents them from dynamically adapting memory access to intermediate evidence discovered during...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Workshop MemAgents
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory reasoning, memory retrieval, memory-augmented
- 来源分类信息：ICLR.cc/2026/Workshop/MemAgent/-/Submission

## Abstract Snapshot
Despite recent progress, LLM agents still struggle with reasoning over long interaction histories. While current memory-augmented agents rely on a static ``retrieve-then-reason'' paradigm, this rigid pipeline design prevents them from dynamically adapting memory access to intermediate evidence discovered during inference. To bridge this gap, we propose MRAgent, a framework that combines an associative memory graph with an active reconstruction mechanism. We represent memory as a Cue–Tag–Content graph, where associative tags serve as semantic bridges connecting fine-grained cues to memory contents. Operating on this structure, our active reconstruction mechanism integrates LLM reasoning directly into memory access, allowing the agent to iteratively explore and prune retrieval paths based on accumulated evidence. This ensures that memory retrieval is dynamically adapted to the reasoning context while avoiding combinatorial explosion caused by unconstrained expansion. Experiments on the LoCoMo benchmark and LongMemEval benchmark demonstrate significant improvements over strong baselines (up to $23\%$), while substantially reducing token and runtime cost, highlighting the effectiveness of active and associative reconstruction for long-horizon memory reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
