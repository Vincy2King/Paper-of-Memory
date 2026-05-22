# The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.21997v1
- Published: 2026-05-21
- Updated: 2026-05-21
- Authors: Yohei Nakajima
- Tags: agent, conversation, retrieval
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2605.21997v1

## One-Sentence Summary
Most agent frameworks are built around the language model: a conversation loop comes first, then tools, then rules, and finally a logging layer bolted on for observability, with...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Most agent frameworks are built around the language model: a conversation loop comes first, then tools, then rules, and finally a logging layer bolted on for observability, with state persisted as retrievable...

进一步看，论文的核心做法或实验重点可以概括为：The append-only event log is the source of truth; the working graph is a deterministic projection of that log; and behaviors--ordinary functions, classes, LLM-backed routines, or logic attached to typed edges--react...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Most agent frameworks are built around the language model: a conversation loop comes first, then tools, then rules, and finally a logging layer bolted on for observability, with state persisted as retrievable "memory." We describe ActiveGraph, a runtime that inverts this arrangement. The append-only event log is the source of truth; the working graph is a deterministic projection of that log; and behaviors--ordinary functions, classes, LLM-backed routines, or logic attached to typed edges--react to changes in the graph and emit new events. No component instructs another; coordination happens entirely through the shared graph. This single design decision yields three properties that retrieval-and-summarization memory systems do not provide: deterministic replay of any run from its log, cheap forking that branches a run at any event without re-executing the shared prefix, and end-to-end lineage from a high-level goal down to the individual model call that produced each artifact. We present the architecture, a determinism contract that makes replay sound, and a worked diligence example whose full causal structure is reconstructable from the log alone. We discuss--without claiming to demonstrate--why this substrate is unusually well suited to self-improving agents, and how it extends the BabyAGI lineage and prior graph-memory research.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
