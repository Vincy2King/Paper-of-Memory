# Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.24060v1
- Published: 2026-05-22
- Updated: 2026-05-22
- Authors: Sugam Panthi, Rabab Abdelfattah
- Tags: benchmark, conversation, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2605.24060v1

## One-Sentence Summary
Conversational-memory systems increasingly transform dialogue history into facts, summaries, timelines, and other source-linked descendants, so a single source turn can coexist...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational-memory systems increasingly transform dialogue history into facts, summaries, timelines, and other source-linked descendants, so a single source turn can coexist with several derived memories in the...

进一步看，论文的核心做法或实验重点可以概括为：This raises an underspecified evaluation question: which stored form should receive retrieval credit?

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, retrieval
- 检索关键词命中：conversational memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.IR

## Abstract Snapshot
Conversational-memory systems increasingly transform dialogue history into facts, summaries, timelines, and other source-linked descendants, so a single source turn can coexist with several derived memories in the same retrieval index. This raises an underspecified evaluation question: which stored form should receive retrieval credit? We show that this scoring-target choice is often left implicit and can materially change benchmark conclusions. We present TIAP, a fixed-output audit that rescores saved ranked outputs under three targets -- Raw, Source, and Canonical -- without rerunning retrieval. On LoCoMo and LongMemEval-S, switching only the credited target changes nDCG on 83.4--94.0 percent of shared queries, flips target orderings on Mem0 and MemoryOS transfer runs, and reverses parser-density recommendations. A 1,902-case semantic audit further shows that relaxed source-linked credit is fully justified only 29.2 percent of the time, despite high rubric reliability in a validation subset. These results reveal target noninvariance: conclusions about memory architectures can silently flip with a single benchmark-design choice. Conversational-memory papers should therefore define and report the scoring target explicitly.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
