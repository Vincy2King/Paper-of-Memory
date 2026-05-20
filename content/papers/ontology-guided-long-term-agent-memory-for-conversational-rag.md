# Ontology-Guided Long-Term Agent Memory for Conversational RAG

- Source: OpenReview
- Venue: MLSys 2026
- Paper ID: openreview:wpZHLPz4N0
- Published: 2026-03-19
- Updated: 2026-05-20
- Authors: Shuang Cao, Rui Li
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: MLSys.org/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=wpZHLPz4N0

## One-Sentence Summary
Retrieval-augmented generation (RAG) enables LLMs to ground responses in external knowledge, but long-term, multi-session conversations still suffer from implicit recall...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `MLSys 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Retrieval-augmented generation (RAG) enables LLMs to ground responses in external knowledge, but long-term, multi-session conversations still suffer from implicit recall failures: when current user queries lack...

进一步看，论文的核心做法或实验重点可以概括为：We present a dialogue-aware RAG system that jointly addresses what to store and how to retrieve under constraints.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：MLSys 2026
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：MLSys.org/2026/Conference/-/Submission

## Abstract Snapshot
Retrieval-augmented generation (RAG) enables LLMs to ground responses in external knowledge, but long-term, multi-session conversations still suffer from implicit recall failures: when current user queries lack lexical overlap with earlier facts (e.g., preferences), standard dense retrieval and long-context prompting often miss the most relevant memories. We present a dialogue-aware RAG system that jointly addresses what to store and how to retrieve under constraints. Our design extracts durable user facts into a lightweight memory graph, enriches queries with conversational cues, performs hybrid retrieval, and uses a budget-aware router to balance quality and serving cost. On our Implicit Preference Recall benchmark, the system lifts Recall@10 to 0.70 (vs. 0.58 for dense-only) and improves nDCG@10 from 0.41 to 0.51. The system also reduces cross-modality disagreement by 47% and achieves a 81% cost reduction compared to long-context methods.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
