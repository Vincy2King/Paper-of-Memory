# Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.25179v1
- Published: 2026-10-18
- Updated: 2026-10-18
- Authors: Chen-Fang Hu, Hong-Han Shuai, Woan-Shiuan Chien
- Tags: agent
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2610.25179v1

## One-Sentence Summary
Persistent memory turns prior interactions into durable agent state, but existing systems provide limited control over whether that state remains valid and whether it should...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory turns prior interactions into durable agent state, but existing systems provide limited control over whether that state remains valid and whether it should influence a later query.

进一步看，论文的核心做法或实验重点可以概括为：We argue that reliable memory requires governance over both state formation and query-time influence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Persistent memory turns prior interactions into durable agent state, but existing systems provide limited control over whether that state remains valid and whether it should influence a later query. We argue that reliable memory requires governance over both state formation and query-time influence. We introduce PLACE, a factorized governance layer that adds write-side state certification and read-side authorization to a memory backend. A factorial evaluation on Mem0 with Qwen2.5-3B and Qwen2.5-7B isolates the contribution of each mechanism. Results show that write-side governance substantially improves lifecycle state correctness, while read-side governance eliminates measured causal leakage from ineligible memory in the state-correct setting. Their combination achieves the strongest joint performance while preserving query-relevant support. These findings show that reliable persistent memory requires explicit control over both maintained state and query-time information influence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
