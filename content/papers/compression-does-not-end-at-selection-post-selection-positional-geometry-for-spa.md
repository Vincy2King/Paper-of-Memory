# Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21126v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Wanyang Hong, Zhaoning Zhang
- Tags: compression, context, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.21126v1

## One-Sentence Summary
Sparse KV compression reduces long-context inference costs by retaining selected historical states, yet these states typically keep their coordinates from the full history.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Sparse KV compression reduces long-context inference costs by retaining selected historical states, yet these states typically keep their coordinates from the full history.

进一步看，论文的核心做法或实验重点可以概括为：Under Rotary Position Embedding (RoPE), gaps left by evicted tokens continue to affect query-key matching, potentially limiting the use of retained evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Sparse KV compression reduces long-context inference costs by retaining selected historical states, yet these states typically keep their coordinates from the full history. Under Rotary Position Embedding (RoPE), gaps left by evicted tokens continue to affect query-key matching, potentially limiting the use of retained evidence. We study post-selection positional geometry on a fixed selector-produced cache, examining how positional organization affects the use of retained information and which coordinate and continuation rules improve answer quality. To reorganize this geometry, we propose RoPERelay, which assigns compact, order-preserving RoPE coordinates, relocates cached key phases through inverse rotation and re-rotation, and synchronizes the current query and subsequent generation. It reuses existing K/V without renewed selection, historical re-prefill, or additional cache budget. Across 36 comparisons spanning two models, six sparse selectors, and three long-term memory tasks, RoPERelay improves answer quality in 32 cases. For Llama-3.1-8B-Instruct with BM25 on LongMemEval-S, accuracy increases from 23.6% to 35.4%. Measured complete-request time overhead is approximately 1%-3% in the evaluated configurations. These findings establish positional organization as a distinct optimization dimension for sparse KV caches after content selection.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
