# Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.12476v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Guodong Xu
- Tags: agent, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.12476v1

## One-Sentence Summary
Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim.

进一步看，论文的核心做法或实验重点可以概括为：We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release. Five executable clauses cover ledger integrity, source binding, conflict isolation, non-revival after retraction or deletion, and exact claim closure over a fresh view at one verified head. On a prespecified hash-frozen 3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of three intentionally simple complete policies matches 1,800/3,600 and makes unmatched releases on 50% of violation cases. A separate sealed end-to-end service evaluation exercises real ingestion and release across eight query families. In its publicly disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400 for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over Chinese- and English-command arms, with generation-date pinning and no post-freeze reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent finite model explores 331,776 semantic and 1,990,656 query states without a full-contract counterexample, and a 100,000-trace three-engine differential yields zero mismatches. These are bounded contract and implementation results, not open-world model accuracy or evidence of world truth. Governed answers in the sealed service evaluation are deterministic service outputs; the 7B result is the ungoverned comparison, not a claim that a language model itself became perfectly accurate.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
