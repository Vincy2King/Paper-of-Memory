# Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.09900v1
- Published: 2026-06-05
- Updated: 2026-06-05
- Authors: Liuyin Wang
- Tags: agent, benchmark, context, long-term
- Categories: cs.CL, cs.AI, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2606.09900v1

## One-Sentence Summary
Long-term memory is the missing layer for LLM agents: across sessions they forget, and the common workaround -- replaying the whole history into the prompt -- is expensive,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is the missing layer for LLM agents: across sessions they forget, and the common workaround -- replaying the whole history into the prompt -- is expensive, slow, and, as distractors accumulate, less...

进一步看，论文的核心做法或实验重点可以概括为：Most memory systems win on cost or latency but still lose to the full-context baseline on accuracy, and benchmark numbers are reported on inconsistent, non-reproducible harnesses, so one system appears at wildly...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI, cs.IR, cs.LG

## Abstract Snapshot
Long-term memory is the missing layer for LLM agents: across sessions they forget, and the common workaround -- replaying the whole history into the prompt -- is expensive, slow, and, as distractors accumulate, less accurate. Most memory systems win on cost or latency but still lose to the full-context baseline on accuracy, and benchmark numbers are reported on inconsistent, non-reproducible harnesses, so one system appears at wildly different scores across sources. We present Engram, an open-source, dual-process memory engine on a bi-temporal data model. A fast write path appends lossless episodes with no LLM on the critical path; an asynchronous path extracts atomic (subject, predicate, object) facts, builds a bi-temporal knowledge graph, and resolves contradictions without an LLM call per fact -- invalidating, never deleting, so every fact keeps provenance and a supersession chain. A hybrid read path fuses dense, lexical, graph, and recency/salience signals, applies a point-in-time ("as-of") filter, and assembles a compact, provenance-tagged context. On the full 500-question LongMemEval_S, graded by the official category-specific judge, Engram's lean configuration -- answering from a ~9.6k-token retrieved slice, never the full history -- scores 83.6% vs. 73.2% for full-context (+10.4 points, McNemar p < 10^-6) at ~8x fewer tokens (9.6k vs. 79k), with 0/500 errored. The gain needs a hybrid read path: facts alone lose recall, while facts plus retrieved chunks recover detail. We also contribute a neutral, in-repo evaluation harness with the official judge baked in and the full-context baseline in every table, publish the raw per-question logs, and document the measurement-integrity pitfalls (truncation, home-grown judges, full-history leaks) that silently distort memory benchmarks. Every number ships with a command to reproduce it.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
