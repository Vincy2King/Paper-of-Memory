# RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22179v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Jingyu Liu, Zongze Li, Zach Xu, Zhanhui Zhou, Tahseen Rabbani, Dawn Song, Ce Zhang
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.22179v1

## One-Sentence Summary
Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation.

进一步看，论文的核心做法或实验重点可以概括为：However, we found that almost none of those primitives earn their cost in our tested memory benchmarks: we show this with BRIDGE, a deliberately minimal RAG memory with chained observation notes, hybrid BM25 with...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our tested memory benchmarks: we show this with BRIDGE, a deliberately minimal RAG memory with chained observation notes, hybrid BM25 with cosine retrieval, and chronological rendering, which reaches parity within bootstrap CI with the prior SOTA on LongMemEval-S and BEAM, and beats the best memory baseline on EverMemBench by 5.7-6.3 points at matched reader. It runs at ~5-7K reader-prompt tokens per query, using a single LLM call for each ingestion or query. We argue that this parity is itself the result: standard benchmarks score what memory retrieves, not what memory enables when the agent acts. To test the latter, we introduce five adversarial probes (Rule Application +-, Pattern Induction Style / Procedural, Dynamic Multiturn) judged at generation time by a cross vendor verification chain, where each query can only be solved by applying a remembered rule or pattern it never mentions. Across 5 probes x 20 scenarios, no architecture wins universally: atomic fact extractors (LangMem) win rule application, while BRIDGE's block-summary memory wins pattern induction. This result holds across four domains, three graders, and three reader families. Each design fails where the other wins, for reasons a recall benchmark cannot see: atomic-fact extractors discard the form a demonstrated pattern takes, while block-summary memory retrieves the rule but the reader does not act on it, a gap that presenting the rule more prominently largely closes. What separates memory designs is not what they retrieve but what they enable an agent to do, and that is what agentic memory should be evaluated on.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
