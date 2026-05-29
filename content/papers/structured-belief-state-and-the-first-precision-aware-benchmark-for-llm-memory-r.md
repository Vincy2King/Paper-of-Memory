# Structured Belief State and the First Precision-Aware Benchmark for LLM Memory Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.11325v2
- Published: 2026-05-11
- Updated: 2026-05-27
- Authors: Jeffrey Flynt
- Tags: benchmark, retrieval
- Categories: cs.IR, cs.AI
- URL: http://arxiv.org/abs/2605.11325v2

## One-Sentence Summary
Every major benchmark for LLM memory systems, LoCoMo foremost, measures whether a model answered correctly, not whether the memory system retrieved correctly.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Every major benchmark for LLM memory systems, LoCoMo foremost, measures whether a model answered correctly, not whether the memory system retrieved correctly.

进一步看，论文的核心做法或实验重点可以概括为：A system returning its entire belief store achieves recall of 1.0 and passes answer-quality evaluation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.IR, cs.AI

## Abstract Snapshot
Every major benchmark for LLM memory systems, LoCoMo foremost, measures whether a model answered correctly, not whether the memory system retrieved correctly. A system returning its entire belief store achieves recall of 1.0 and passes answer-quality evaluation. This is the difference between a unit test and an integration test: retrieval quality must be measured in isolation from the generative model it feeds into, and no existing benchmark does this. We demonstrate that this failure persists even when entity extraction is entirely faithful. Memory baselines achieve mean retrieval precision of just 0.05 to 0.08 on cases referencing their own extractions. The failure is structural: cosine similarity over a domain-specific corpus cannot discriminate relevant beliefs from semantically proximate ones, an invariance confirmed across a 20x range in embedding model scale. Multi-turn evaluation surfaces a compounding failure; after topic drift, comparison systems allow semantic mass to bleed across turns, yielding high drift scores on re-entry. Single-turn metrics conceal this cost: Hindsight reports sub-700ms single-turn latency but exceeds 2,700ms mean per session turn, with p95 above 6,000ms. Under LLM-as-a-Judge evaluation, these failures remain invisible. We present two contributions: PrecisionMemBench, an 89-case benchmark measuring retrieval precision independently of generative models across diverse scope, mutation, and isolation assertions; and Tenure, a local-first structured belief store using multi-path BM25 with analyzer asymmetry, differential boosting, and hard scope isolation. Tenure passes 89/89 cases with mean precision 1.0 and sub-15ms retrieval latency. Comparison providers perform worse than the raw vector baseline they are built on, with zero active retrieval passes and ingestion costs of 98 to 897 seconds, failures that answer-quality benchmarks cannot detect.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
