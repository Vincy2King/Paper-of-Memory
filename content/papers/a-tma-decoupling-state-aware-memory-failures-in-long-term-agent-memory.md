# A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.01935v1
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Zitong Shi, Yixuan Tang, Anthony Kum Hoe Tung
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.01935v1

## One-Sentence Summary
Long term memory lets LLM agents act as persistent assistants, but user facts change.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long term memory lets LLM agents act as persistent assistants, but user facts change.

进一步看，论文的核心做法或实验重点可以概括为：A useful memory system must know what is true now, what used to be true, and what changed.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long term memory lets LLM agents act as persistent assistants, but user facts change. A useful memory system must know what is true now, what used to be true, and what changed. We study \emph{ghost memory}, a state coordination failure in which old, current, and transition facts coexist in the memory bank, remain mixed during retrieval, and mislead the answer model. We argue that memory systems should be understood and optimized from three levels: bank maintenance, retrieval, and answer time resolution. We propose ATMA, a state aware overlay for existing memory systems. ATMA keeps superseded and transition records in the bank, builds evidence packets for the query's requested state view, and exposes current, historical, and transition labels to QA. We further call for decoupled evaluation of bank, retrieval, and answer level failures, since final QA accuracy can hide where ghost memory occurs. To make this failure measurable, we build LTP (LoCoMo Temporal Plus), a conflict heavy benchmark for ghost memory, and evaluate on LoCoMo for long conversation generalization. On LTP, Graphiti+ATMA improves conflict accuracy by 0.240 absolute over Graphiti. On LoCoMo, Graphiti+ATMA raises temporal F1 from 0.0295 to 0.1705. The gains are host dependent, but they indicate that explicit state roles can reduce memory failures hidden by final QA accuracy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
