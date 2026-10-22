# ChronoSynth: Constraint-Aware Question Synthesis over Temporal Knowledge Graphs

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.29339v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Feng Liang, Weixin Zeng, Runhao Zhao, Mingjun Zhou, Shaoshi Yang, Xiang Zhao
- Tags: memory-augmented
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2610.29339v1

## One-Sentence Summary
Knowledge graph question generation (KGQG) generates natural-language questions from structured graph evidence and a target answer.

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Knowledge graph question generation (KGQG) generates natural-language questions from structured graph evidence and a target answer.

进一步看，论文的核心做法或实验重点可以概括为：When the input graph is temporal, a valid question must also preserve the answer field, time condition, reference event, and temporal order that determine the answer set.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Knowledge graph question generation (KGQG) generates natural-language questions from structured graph evidence and a target answer. When the input graph is temporal, a valid question must also preserve the answer field, time condition, reference event, and temporal order that determine the answer set. Existing KGQG methods and prompting baselines can produce fluent questions that alter these conditions, causing temporal semantic drift. This paper studies temporal KGQG as a constraint-preserving graph-to-question problem and proposes ChronoSynth, a memory-augmented and constraint-aware generation framework. ChronoSynth first constructs a Temporal Intent State to make the intended question semantics explicit. It then retrieves compatible typed question patterns from an indexed pattern memory, adapts them to the input graph, and validates the generated question. Validation feedback guides revisions when a supported inconsistency is detected. Experiments on CRONQUESTIONS and MultiTQ demonstrate state-of-the-art generation performance, with ablations supporting the contributions of its components.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
