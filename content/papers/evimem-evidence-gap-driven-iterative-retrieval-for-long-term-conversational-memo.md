# EviMem: Evidence-Gap-Driven Iterative Retrieval for Long-Term Conversational Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.27695v1
- Published: 2026-04-30
- Updated: 2026-04-30
- Authors: Yuyang Li, Yime He, Zeyu Zhang, Dong Gong
- Tags: conversation, long-term, retrieval
- Categories: cs.CV, cs.CL
- URL: http://arxiv.org/abs/2604.27695v1

## One-Sentence Summary
Long-term conversational memory requires retrieving evidence scattered across multiple sessions, yet single-pass retrieval fails on temporal and multi-hop questions.

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational memory requires retrieving evidence scattered across multiple sessions, yet single-pass retrieval fails on temporal and multi-hop questions.

进一步看，论文的核心做法或实验重点可以概括为：Existing iterative methods refine queries via generated content or document-level signals, but none explicitly diagnoses the evidence gap, namely what is missing from the accumulated retrieval set, leaving query...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CV, cs.CL

## Abstract Snapshot
Long-term conversational memory requires retrieving evidence scattered across multiple sessions, yet single-pass retrieval fails on temporal and multi-hop questions. Existing iterative methods refine queries via generated content or document-level signals, but none explicitly diagnoses the evidence gap, namely what is missing from the accumulated retrieval set, leaving query refinement untargeted. We present EviMem, combining IRIS (Iterative Retrieval via Insufficiency Signals), a closed-loop framework that detects evidence gaps through sufficiency evaluation, diagnoses what is missing, and drives targeted query refinement, with LaceMem (Layered Architecture for Conversational Evidence Memory), a coarse-to-fine memory hierarchy supporting fine-grained gap diagnosis. On LoCoMo, EviMem improves Judge Accuracy over MIRIX on temporal (73.3% to 81.6%) and multi-hop (65.9% to 85.2%) questions at 4.5x lower latency. Code: https://github.com/AIGeeksGroup/EviMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
