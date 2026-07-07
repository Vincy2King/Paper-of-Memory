# PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.04089v1
- Published: 2026-07-05
- Updated: 2026-07-05
- Authors: Sukanta Ganguly
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.04089v1

## One-Sentence Summary
Lifelong agents need more than larger context windows and better retrieval.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Lifelong agents need more than larger context windows and better retrieval.

进一步看，论文的核心做法或实验重点可以概括为：They need memories that can persist, evolve, and be corrected without forcing the serving stack to recompute the same history on every turn or silently reuse stale runtime state.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Lifelong agents need more than larger context windows and better retrieval. They need memories that can persist, evolve, and be corrected without forcing the serving stack to recompute the same history on every turn or silently reuse stale runtime state. We present PLACEMEM as a systems position on lifelong-agent memory, instantiated by an executable control-plane prototype. The central claim is that agent memory should be represented as versioned capsules that unify semantics, provenance, validity, and reusable runtime state under one correction-aware identity. In the current prototype, capsules drive prompt-level text retrieval, KV-aware routing, and cascading invalidation over live streamed backends; prospective layer-frontier replay is intentionally framed as a deeper integration agenda rather than a claimed engine feature. We describe a vLLM-first prototype with persistent capsule state, concurrency-safe invalidation, an OpenAI-compatible routing sidecar, a typed metadata contract, and a benchmark harness that measures live first-token latency, reuse, and post-correction behavior. The result is both an executable artifact that demonstrates correction-aware control-plane behavior today and a concrete roadmap for replay-aware serving integration in future lifelong-agent systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
