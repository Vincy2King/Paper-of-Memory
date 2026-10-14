# Propose, Verify, Commit: Evidence-Grounded Memory for Long-Horizon Multi-Actor Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.23465v2
- Published: 2026-09-20
- Updated: 2026-10-13
- Authors: Zihao Lu, Zhihang Yuan, Litu Ou, Lei Shi
- Tags: agent, benchmark, context, conversation
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.23465v2

## One-Sentence Summary
Memory enables language model agents to use information beyond their context windows, but maintaining and accessing this information reliably remains difficult.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory enables language model agents to use information beyond their context windows, but maintaining and accessing this information reliably remains difficult.

进一步看，论文的核心做法或实验重点可以概括为：Long-horizon conversational memory is especially challenging in multi-actor settings, where relevant evidence is distributed across participants and contexts, and previously established information may later be revised.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Memory enables language model agents to use information beyond their context windows, but maintaining and accessing this information reliably remains difficult. Long-horizon conversational memory is especially challenging in multi-actor settings, where relevant evidence is distributed across participants and contexts, and previously established information may later be revised. We introduce EGMEMORY, a training-free agentic memory framework centered on evidence chains that preserve message-level evidence and provenance while tracking active states and their revision histories. At write time, adaptive memory inspection and an evidence-grounded propose-verify-commit protocol govern state updates. At read time, adaptive evidence navigation iteratively identifies the state and supporting evidence required for a query, using conversational structure to narrow the search space and lexical-semantic relevance to rank candidates. The system operates through prompting and tool use without memory-specific policy training. EGMEMORY achieves 68.2% on GroupMemBench and 77.9% on EverMemBench, outperforming the strongest evaluated baselines by 22.7 and 21.4 percentage points, respectively. It further reaches 73.6% on the dyadic LoCoMo benchmark, supporting its applicability beyond multi-actor conversations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
