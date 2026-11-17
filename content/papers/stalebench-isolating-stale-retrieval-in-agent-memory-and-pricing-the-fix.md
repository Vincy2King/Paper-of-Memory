# StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.19752v1
- Published: 2026-11-15
- Updated: 2026-11-15
- Authors: S M Mahbub Murshed
- Tags: agent, retrieval
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2611.19752v1

## One-Sentence Summary
An agent that stores facts over time eventually stores several versions of the same fact.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An agent that stores facts over time eventually stores several versions of the same fact.

进一步看，论文的核心做法或实验重点可以概括为：Asked a value-agnostic question - "which team does X play for now?" - a similarity retriever cannot prefer the current version, because every version matches the entity the query names.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
An agent that stores facts over time eventually stores several versions of the same fact. Asked a value-agnostic question - "which team does X play for now?" - a similarity retriever cannot prefer the current version, because every version matches the entity the query names. StaleBench isolates this stale-retrieval failure on 892 real updating facts, with currency labels from the source (Wikidata validity years via TempLAMA), never from a retrieval score. Our central result is that retrieval metrics can rank memory policies backwards: a retention policy and its retain-everything control return the identical statement at rank 1 for every test query, yet differ by 29.5 and 65.6 points in reader accuracy on two readers when no date is shown. Contamination@5, the metric we add, ranks them correctly where current@1 and current@5 do not. Withdrawing the lexical anchor that statements carry costs deployed keying mechanisms tens of points of freshness; entity resolution on both the write path and the query recovers most of the loss. Three deployed systems (Mem0, Graphiti, LangMem) and a reimplemented ERASE each handle supersession differently, and no single scoring convention describes all four. We release the data, a frozen evaluator, and reference baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
