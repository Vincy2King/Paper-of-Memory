# Supra Cognitive Modes: A Routed Architecture for Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.19096v1
- Published: 2026-07-21
- Updated: 2026-07-21
- Authors: Joshua Tobkin, David Yang
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.19096v1

## One-Sentence Summary
Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories.

进一步看，论文的核心做法或实验重点可以概括为：We describe Supra Cognitive Modes (SCM), an architecture that maps explicit or automatically selected per-query modes to retrieval and synthesis payloads over one shared ingest substrate.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：agent memory, conversational memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories. We describe Supra Cognitive Modes (SCM), an architecture that maps explicit or automatically selected per-query modes to retrieval and synthesis payloads over one shared ingest substrate. A frozen semantic classifier and runtime gates dispatch queries among fused lexical and dense lookup, graph or iterative multi-hop handling, and stratified long-form synthesis. The substrate combines multi-granularity embeddings, extracted triples, fact-version metadata, and optional asynchronous enrichments. We characterize the deployed configuration on three benchmarks: Long-term Conversational Memory (LoCoMo; n = 1,986), MemoryAgentBench (MAB; n = 3,671), and LongMemEval (n = 500). The reference run records 84.87% on LoCoMo factoid categories and 68.61% on adversarial abstention, 61.49% on MAB across two repetitions, and 86.00% on LongMemEval. A repository-backed reproduction produces similar aggregate scores and supports task- and mode-conditioned failure analysis. Raw baseline outputs, aligned end-to-end timing for LoCoMo and LongMemEval, and complete token ledgers are unavailable; stored rows also omit some final runtime decisions. The results characterize one implemented routed configuration and its diagnostic failure patterns, while source inspection verifies the per-query control interface and shared-substrate design. Causal routing effects, efficiency gains, and statistical significance remain outside the available evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
