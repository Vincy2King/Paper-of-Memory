# When Retrieval Is Not Enough: Obsolete Facts in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.36308v1
- Published: 2026-10-26
- Updated: 2026-10-26
- Authors: Oleeviya Babu Poikarayil, Tony Basil Babu, Abdulrahman Nahhas, Het Darshan Mehta, Jawid Ahmad Baktash, Ernesto William De Luca, Klaus Turowski
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.36308v1

## One-Sentence Summary
Memory-agent benchmarks often collapse retrieval and answer generation into one score, making it hard to tell whether a failure comes from missing an update or from not using an...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-agent benchmarks often collapse retrieval and answer generation into one score, making it hard to tell whether a failure comes from missing an update or from not using an update that was already retrieved.

进一步看，论文的核心做法或实验重点可以概括为：We examine this distinction on the single-hop FactConsolidation task of MemoryAgentBench.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-agent benchmarks often collapse retrieval and answer generation into one score, making it hard to tell whether a failure comes from missing an update or from not using an update that was already retrieved. We examine this distinction on the single-hop FactConsolidation task of MemoryAgentBench. With Qwen2.5-7B-Instruct on 6K-history BM25 accuracy drops from 45% to 32% when the retrieved evidence budget grows from 64 to 512 tokens, even though a gold-assisted post-hoc audit finds the newest statement in every retrieved set. Most of the errors occur on questions that also contain an obsolete statement version. Under a frozen prompt and equal four-statement evidence size, replacing one unrelated statement with the obsolete competing statement reduces accuracy from 100% to 44.6% for Qwen2.5 and from 100% to 87.8% for Qwen3-14B, with all 50 harmful paired flips classified as stale. A 32K-history replication likewise favors BM25-64 over BM25-512 (69% versus 58%). These results suggest that retrieving the correct fact is not enough. An obsolete competing statement can be more harmful than an unrelated piece of evidence of the same size.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
