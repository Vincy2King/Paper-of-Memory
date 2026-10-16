# TEM: Temporal State Tracking Memory for Large Language Model Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21900v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Pengfeng Song, Yunkai Zhuang, Liye Shi
- Tags: agent, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.21900v1

## One-Sentence Summary
An agent's memory must remain useful as information changes across conversations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An agent's memory must remain useful as information changes across conversations.

进一步看，论文的核心做法或实验重点可以概括为：A new fact may replace an earlier value without making that value irrelevant to a later question.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
An agent's memory must remain useful as information changes across conversations. A new fact may replace an earlier value without making that value irrelevant to a later question. We present Temporal State Tracking Memory (TEM), a training-free framework for tracking these changes. TEM stores facts as versioned records linked to their sources. It retrieves relevant versions, places them in source order and labels historical records before passing the evidence to the answer model. Event memory and original dialogue turns provide details missing from structured facts. We evaluated TEM on 420 questions drawn from 600 sessions involving 60 personas. Across four open-weight models, key-entity hit rates reached 75.71-97.62% overall and 96.67-100.00% on the historical-residence subset. Adding historical labels to otherwise identical, source-ordered facts increased overall hit rates by 17.14-55.95 percentage points. The evidence was compact: 94-118 tokens per answer, or 48.75-56.73% less than session-aware retrieval-augmented generation (RAG). A further evaluation on 1,540 LoCoMo questions tested hybrid memory under a fixed evidence budget. TEM exceeded session-aware RAG with both backbones; conservative score differences were 7.92 and 10.58 percentage points. The results support preserving fact versions and exposing their temporal status to the generator when answering questions about repeatedly updated information.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
