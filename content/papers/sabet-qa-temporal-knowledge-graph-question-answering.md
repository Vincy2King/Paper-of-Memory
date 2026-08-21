# SABET-QA: Temporal Knowledge Graph Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.20083v1
- Published: 2026-08-20
- Updated: 2026-08-20
- Authors: Brahim Touayouch, Mirette Moawad, Dmitry Akulov
- Tags: context
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2608.20083v1

## One-Sentence Summary
Question Answering over Temporal Knowledge Graphs (TKGQA) requires reasoning over time-sensitive facts, yet existing embedding-based methods struggle with multi-step queries due...

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Question Answering over Temporal Knowledge Graphs (TKGQA) requires reasoning over time-sensitive facts, yet existing embedding-based methods struggle with multi-step queries due to single-pass reasoning pipelines.

进一步看，论文的核心做法或实验重点可以概括为：We propose SABET-QA, a framework that iteratively refines reasoning states across multiple hops via a bidirectional entity-temporal scoring mechanism and a slot-aware contextualization module that aligns question...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Question Answering over Temporal Knowledge Graphs (TKGQA) requires reasoning over time-sensitive facts, yet existing embedding-based methods struggle with multi-step queries due to single-pass reasoning pipelines. We propose SABET-QA, a framework that iteratively refines reasoning states across multiple hops via a bidirectional entity-temporal scoring mechanism and a slot-aware contextualization module that aligns question semantics with temporal KG embeddings. A differentiable working memory enables progressive hypothesis refinement, while auxiliary temporal boundaries serve as coarse supervision when available. Experiments on CronQuestions, Complex-CronQuestions, MultiTQ, and TimeQuestions demonstrate consistent improvements over strong baselines, particularly on complex multi-step temporal queries.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
