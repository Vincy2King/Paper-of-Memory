# Invalidation Contracts for Cross-Episode Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.00243v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Michael Wu, Arquimedes Canedo
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.00243v1

## One-Sentence Summary
LLM agents that cache recovery suggestions from API errors can skip re-derivation in later episodes, spending fewer tokens and fewer model calls on constraints they have already...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents that cache recovery suggestions from API errors can skip re-derivation in later episodes, spending fewer tokens and fewer model calls on constraints they have already learned.

进一步看，论文的核心做法或实验重点可以概括为：Server-side data drift turns those cached fixes into silent failures, and the usual remedy, re-deriving on every episode, gives the savings back.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM agents that cache recovery suggestions from API errors can skip re-derivation in later episodes, spending fewer tokens and fewer model calls on constraints they have already learned. Server-side data drift turns those cached fixes into silent failures, and the usual remedy, re-deriving on every episode, gives the savings back. We introduce invalidation contracts, a protocol layer that attaches version stamps and cacheability hints to every recovery suggestion so the client can evict stale entries without trial and error, and keep the rest. The contract decomposes realized savings into two independent factors: validity, the fraction of cached suggestions that remain correct after a drift event, and compliance, the fraction the planner applies on the first attempt. Validity depends only on the protocol and is vendor-independent. Compliance depends on the planner model: identical wire bytes yield 100% first-try compliance on Claude Haiku 4.5 and 11% or below on Claude Sonnet 5, which exhibits input-schema conservatism, refusing fixes that add fields the original request did not contain. We evaluate across seven models, three serving paths, two domains, and approximately 9,400 episodes. Row-level invalidation raises compliance by 0 to 66.7 percentage points across the seven models, 55.6 to 66.7 on three, and recovers 29-33% of baseline token cost on four of seven models, while table-level invalidation destroys co-located entries and drops post-drift first-try rates to 0% on five of seven. Eviction precision is 1.00 at row granularity on every model under the row-level oracle of Section 4.1. The contract adds 15% to response payload. Version-stamp validity is deterministic by construction and produced identical results across every model and serving path, with zero contract failures in the entire evaluation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
