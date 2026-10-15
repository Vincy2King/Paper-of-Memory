# EGCForest: Structured Agent Memory Organization for Enterprise Group Chats

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.19836v1
- Published: 2026-10-14
- Updated: 2026-10-14
- Authors: Lingxi Cui, Jinhao Ruan, Wenqing Wei, Guo Yi, Li Rao, Ke Chen, Lidan Shou
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.19836v1

## One-Sentence Summary
Enterprise group chats record project progress, decisions, task ownership, and other organizational information valuable to enterprise agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Enterprise group chats record project progress, decisions, task ownership, and other organizational information valuable to enterprise agents.

进一步看，论文的核心做法或实验重点可以概括为：Reliable retrieval is challenging because evidence spans interleaved threads, channels, and time, with meaning and authority conditioned on the speaker.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Enterprise group chats record project progress, decisions, task ownership, and other organizational information valuable to enterprise agents. Reliable retrieval is challenging because evidence spans interleaved threads, channels, and time, with meaning and authority conditioned on the speaker. Neither RAG's independent chunk retrieval nor memory systems' summary-based consolidation can reliably recover such distributed evidence. We present EGCForest, a novel multi-view hierarchical memory framework for enterprise group chats. EGCForest organizes an immutable message log into three complementary forests: a Channel forest for temporal workflows, an Actor forest for speaker-conditioned context, and an Artifact forest for deliverable lifecycles. Cross-view connections are enabled by a Placement Map and sparse structural bridges. Built on this memory backbone, EGCForest retrieves and assembles evidence by jointly leveraging message-level relevance, hierarchical context from forest summaries, and cross-view links, recovering distributed evidence. Experiments on three enterprise-chat benchmarks show that EGCForest consistently outperforms RAG and memory-system baselines, improving answer accuracy by up to 20.85 points over MemOS while supporting efficient online retrieval.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
