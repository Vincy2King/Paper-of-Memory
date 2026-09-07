# Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.05339v1
- Published: 2026-09-04
- Updated: 2026-09-04
- Authors: Ankit Goyal, Jaideep Ray
- Tags: agent, context, retrieval
- Categories: cs.AI, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2609.05339v1

## One-Sentence Summary
Model upgrades are routine; memory migrations are not.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Model upgrades are routine; memory migrations are not.

进一步看，论文的核心做法或实验重点可以概括为：An agent can keep the same memory store and still forget: a new model may interpret old notes differently, mixed embedding versions may break retrieval, and repair may fail without the original evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Model upgrades are routine; memory migrations are not. An agent can keep the same memory store and still forget: a new model may interpret old notes differently, mixed embedding versions may break retrieval, and repair may fail without the original evidence. We compare memory as the same history is preserved verbatim for long-context reading (LC-RAW), divided into chunks for retrieval-augmented generation (RAG), compressed by a model into natural-language notes (NOTES), or normalized into a fixed-schema knowledge graph (KG-fixed). The study uses 48 synthetic histories with randomized answer codes, exact scoring, and two open-weight models with sub 10 billion parameters. Our measurements show that fixed-schema structures transfer reliably, with KG-fixed accuracy changing by only $+0.0004 \pm 0.0020$ following a writer swap. Conversely, compressed NOTES exhibit high model coupling, with accuracy shifting asymmetrically by $+9.91$ or $-13.28$ percentage points depending on the specific migration direction. In RAG systems, partial embedding migrations using a 50/50 mixed index capture only a 4.96-point accuracy improvement, forfeiting the majority of the 11.90-point gain achieved through full re-embedding. Diagnostic decomposition attributes 80% ($0.467 \pm 0.014$) of the NOTES accuracy deficit to information lost during initial construction, whereas retrieval failures drive 81% ($0.364 \pm 0.012$) of the RAG deficit. Finally, store-only repair of NOTES fails to reach a 90% performance recovery target in all 48 test cases, whereas retaining the raw source history enables successful recovery in 34 of 48 cases for one tested direction. These findings highlight the necessity of direction-specific migration testing, strict embedding space isolation, and the retention of source histories for memory repair.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
