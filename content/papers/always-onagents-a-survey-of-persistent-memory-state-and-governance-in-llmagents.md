# Always-OnAgents:A Survey of Persistent Memory, State, and Governance in LLMAgents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.30306v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang
- Tags: agent
- Categories: cs.MA, cs.AI
- URL: http://arxiv.org/abs/2606.30306v1

## One-Sentence Summary
Always-on agents are systems whose future behavior depends on durable state accumulated across earlier interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Always-on agents are systems whose future behavior depends on durable state accumulated across earlier interactions.

进一步看，论文的核心做法或实验重点可以概括为：We treat them as persistent-state systems: the operative system includes retrievable memories, but also task ledgers, permissions, credentials, commitments, provenance and audit records, shared state, trigger...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory, retrieval memory
- 来源分类信息：cs.MA, cs.AI

## Abstract Snapshot
Always-on agents are systems whose future behavior depends on durable state accumulated across earlier interactions. We treat them as persistent-state systems: the operative system includes retrievable memories, but also task ledgers, permissions, credentials, commitments, provenance and audit records, shared state, trigger conditions, and externally committed effects linked to those records. The survey reads the literature through six diagnostic axes for each state item, authority, scope, mutability, provenance, recoverability, and actionability, and through a lifecycle in which state is written, validated, organized, retrieved, acted upon, updated, forgotten, audited, and sometimes rolled back. Across a 435-work coded corpus, treated as a scoped map rather than an exhaustive census, the literature concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it. We therefore introduce the Always-On Evaluation Protocol (AOEP-v0), a pilot evaluation contract that makes these governance requirements concrete by scoring state mutation and recovery obligations rather than answer quality alone. The resulting agenda connects always-on agents to databases, distributed systems, formal methods, capability security, and machine unlearning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
