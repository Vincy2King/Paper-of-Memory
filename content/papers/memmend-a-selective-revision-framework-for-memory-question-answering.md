# MemMend: A Selective Revision Framework for Memory Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.25721v1
- Published: 2026-11-19
- Updated: 2026-11-19
- Authors: Sheng Shi, Geng Li
- Tags: conversation, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.25721v1

## One-Sentence Summary
Revising every answer from a long-term memory can consume substantial inference budget and damage facts that were already correct.

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Revising every answer from a long-term memory can consume substantial inference budget and damage facts that were already correct.

进一步看，论文的核心做法或实验重点可以概括为：We introduce MemMend, a modular selective revision framework that routes potentially incomplete answers to an editor, represents corrections as bounded exact-text replacements, and accepts only edits with resolvable...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Revising every answer from a long-term memory can consume substantial inference budget and damage facts that were already correct. We introduce MemMend, a modular selective revision framework that routes potentially incomplete answers to an editor, represents corrections as bounded exact-text replacements, and accepts only edits with resolvable source coordinates and valid edit operations. The editor preserves the current answer when no legal repair is proposed; accepted edits require no additional semantic-verification call. On 1,986 LoCoMo development questions, MemMend achieves 67.17 conversation-macro F1 and 88.35 mean Judge score, improving over a verified revision chain by 0.82 and 1.24 points while using 62.37% fewer revision calls. Routing uses 54.15% fewer revision calls than ungated local review, with similar F1 but a 0.67-point lower Judge score. Applied directly to native PropMem, Mem0, and SimpleMem answers, the editing interface raises F1 by 3.79, 6.44, and 0.42 points. It outperforms same-gate rewriting and saves 49.85-83.72% of editing calls relative to ungated editing, which retains higher F1 in this adaptation. A source-by-editing factorial supports local editing for F1 but leaves an independent quality benefit from source obligations unresolved. Transfer to 451 LongMemEval-V2 Small questions also favors revision efficiency, while an external PerLTQA dialogue subset reveals a completeness gap. These results support selective editing as a reusable quality-cost operating point.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
