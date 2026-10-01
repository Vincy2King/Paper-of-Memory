# Authority Before Utility: Non-Compensatory Control for Persistent LLM Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.37474v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Wesley Shu
- Tags: retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.37474v1

## One-Sentence Summary
Persistent memory creates a control problem that retrieval relevance alone does not solve: a memory can remain highly useful after an update, deletion, or revocation makes it...

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory creates a control problem that retrieval relevance alone does not solve: a memory can remain highly useful after an update, deletion, or revocation makes it inadmissible for the current answer.

进一步看，论文的核心做法或实验重点可以概括为：We formalize this as a separation between utility and authority.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory creates a control problem that retrieval relevance alone does not solve: a memory can remain highly useful after an update, deletion, or revocation makes it inadmissible for the current answer. We formalize this as a separation between utility and authority. A fixed finite penalty applied to an unnormalized utility score cannot guarantee exclusion under arbitrary positive-affine reparameterization of that score; by contrast, rank-normalized compensation is scale-invariant and therefore forms a stronger empirical comparator. Our prospectively frozen TIDE/LongMemEval primary was quarantined before a valid HELDOUT comparison because the materialized TIDE adapter conflated historical age with query-relative inadmissibility and the aligned LongMemEval split left no DEV set for the predeclared penalty selection. We therefore report a post-primary replacement diagnostic on Memora Remembering, where update/delete operations provide item-level forgetting state. On Qwen3-8B, DEV selected lambda = 0.6 from a ten-point normalized SOFT family. Across 185 HELDOUT units in 28 dependency clusters, HARD exclusion yields 4.04% balanced construct error versus 19.66% for locked SOFT, a paired difference of 15.61 points with a 20,000-replicate cluster-bootstrap 95% interval of [13.07, 18.76]. The effect is driven primarily by forgotten-value leakage while current-value recall is preserved. This is same-Q operator-comparison evidence, not a universal claim that scalar control fails, not an evaluation of learned authority inference, and not an independent downstream-harm endpoint.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
