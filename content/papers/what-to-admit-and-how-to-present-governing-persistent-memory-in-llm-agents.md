# What to Admit and How to Present: Governing Persistent Memory in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11188v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Chang Liu, Deliang Ding
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.11188v1

## One-Sentence Summary
Persistent memory can improve personalization in LLM agents but can also induce sycophancy and cross-domain leakage.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory can improve personalization in LLM agents but can also induce sycophancy and cross-domain leakage.

进一步看，论文的核心做法或实验重点可以概括为：We distinguish two governance decisions: admission, which determines what recalled information enters the working context, and presentation, which determines how admitted information is expressed.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory can improve personalization in LLM agents but can also induce sycophancy and cross-domain leakage. We distinguish two governance decisions: admission, which determines what recalled information enters the working context, and presentation, which determines how admitted information is expressed. We implement two inference-time designs without retraining: factor-compiled admission (FC), which assesses whole memory entries, and permission-semantic admission (PS), which decomposes entries into typed units; both translate adjudicated attributes into eligibility decisions via deterministic policies. We evaluate on a four-backbone development suite and an external benchmark with four tasks of 300 samples each. Relative to verbatim injection, FC and PS reduce pooled judge-assessed failure rates on the external benchmark by 6.7 and 8.8 percentage points (p = 2.7e-7 and 4.1e-12), and development-set cross-domain leakage falls by up to 29.5 percentage points. A query-conditioned gating baseline shows no significant change in objective-fact failure or pooled failure. Under matched admission budgets, PS outperforms random and relevance-based selection on external objective-fact judgment after Holm correction. Holding presentation fixed, tightening admission cuts cross-domain failure by a further 17.5 percentage points (p = 1.6e-4); in contrast, no comparison between two renderings of identical adjudicated outputs survives multiple-comparison correction. Both designs increase personalization failures, and PS misses the preregistered improvement and personalization-preservation criteria. These results support evaluating admission and presentation separately: selection quality provides task-specific safety gains, while preserving beneficial memory use remains unresolved.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
