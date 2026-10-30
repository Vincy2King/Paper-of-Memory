# FIRME: Registry-Anchored Memory Graphs for Evolving, Heterogeneous Investor Knowledge

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.40482v1
- Published: 2026-10-29
- Updated: 2026-10-29
- Authors: Yunbai Zhang, Yunyi Gao, Han-Tai Shiao
- Tags: context
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2610.40482v1

## One-Sentence Summary
Financial AI workflows that reuse investor knowledge need persistent memory that integrates observations across sources and periods without losing identity or provenance.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Financial AI workflows that reuse investor knowledge need persistent memory that integrates observations across sources and periods without losing identity or provenance.

进一步看，论文的核心做法或实验重点可以概括为：In a knowledge graph, recurring observations may use different surface forms, fragmenting relationship histories and preventing evidence from accumulating.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Financial AI workflows that reuse investor knowledge need persistent memory that integrates observations across sources and periods without losing identity or provenance. In a knowledge graph, recurring observations may use different surface forms, fragmenting relationship histories and preventing evidence from accumulating. We introduce Fusion and Identity Registry for Memory Evolution (FIRME), a registry-anchored memory graph that reconciles incoming observations to persistent canonical relationships and retains their source, time, and context. Within periods, rule-based fusion links investor-call discussions to portfolio cash-flow signals, directly or through a fixed product-topic ontology. Across periods, canonical identities and persistent aliases direct recurring observations to the same relationship history; deterministic updates summarize reinforcement, inactivity, and reactivation. We evaluate FIRME on proprietary investor-call and cash-flow records and on S&P 500 earnings-call transcripts. Compared with a historical registry that retains canonical identities and semantic fallback but omits alias memory, FIRME increases final-period Correct Match Rate by 7.8-12.1 percentage points across four dataset-backend settings under a fixed-judge and fallback-review protocol. A blinded human audit of 200 incoming observations per setting finds Correct Match Rate gains of 9.0-16.5 points and reattachment-recall gains of 22.5-29.0 points, with higher observed merge precision in all four samples. A separate audit finds valid evidence paths for 293 of 300 outputs from full within-period fusion in the investor-call setting. Extraction-faithfulness and round-trip diagnostics assess source grounding and preservation of extractor-derived graph content.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
