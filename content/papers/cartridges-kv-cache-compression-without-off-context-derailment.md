# Cartridges++: KV Cache Compression without Off-Context Derailment

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.35621v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Sonia Laguna, Joao Monteiro, Marco Cuturi, Pierre Ablin, Eleonora Gualdoni
- Tags: compression, context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2609.35621v1

## One-Sentence Summary
Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache...

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache balloons.

进一步看，论文的核心做法或实验重点可以概括为：Compressed KV (CKV) representations aim to mimic the cache of a document and are typically computed once and for all, ahead of inference time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache balloons. Compressed KV (CKV) representations aim to mimic the cache of a document and are typically computed once and for all, ahead of inference time. Methods to obtain CKVs range from drop mechanisms that reduce their number of columns, to learned approaches. Among the latter, Cartridges have emerged as a leading compression method, learning compact KV representations through distillation on relevant Q/A pairs. While existing evaluations focus primarily on whether Cartridges and other CKVs yield approximately similar responses to document-related, on-context queries, we investigate the crucial deployment question of whether they can handle off-context queries, something the native KV representation is particularly good at, thanks to the mechanics of attention. We observe a fundamental trade-off: while Cartridges perform better for on-context queries, heuristic-variants preserve better the original LLM's ability to operate off-context. We measure this through their capability to avoid context contamination in their response, retain general knowledge, and follow instructions. We propose Cartridges++, simple modifications to cartridges that retain off-context abilities at small or negligible cost. The router variant decides at inference time whether the query should use the learned long-context memory, while the data-mixing variant allocates a small fraction of training Q/As to queries outside the reference long document. Our study shows that assessing CKVs on document utility alone can mask substantial degradation in broader model capabilities, yet those issues can be fixed with benign changes to CKV inference or training.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
