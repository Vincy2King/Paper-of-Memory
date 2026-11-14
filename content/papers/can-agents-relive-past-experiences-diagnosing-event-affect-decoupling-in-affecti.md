# Can Agents Relive Past Experiences? Diagnosing Event-Affect Decoupling in Affective-Episodic Retrospection

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.15655v1
- Published: 2026-11-11
- Updated: 2026-11-11
- Authors: Tingna Xie, Ming Wang, Shi Feng, Yongkang Liu
- Tags: agent, benchmark, episodic, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.15655v1

## One-Sentence Summary
As memory-augmented agents increasingly support long-term and personalized interactions, reliable recall of emotional experiences while preserving their associated affect...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As memory-augmented agents increasingly support long-term and personalized interactions, reliable recall of emotional experiences while preserving their associated affect becomes necessary.

进一步看，论文的核心做法或实验重点可以概括为：However, existing evaluations usually assess emotion accuracy and factual memory grounding separately, overlooking event-affect correspondence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, long-term, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
As memory-augmented agents increasingly support long-term and personalized interactions, reliable recall of emotional experiences while preserving their associated affect becomes necessary. However, existing evaluations usually assess emotion accuracy and factual memory grounding separately, overlooking event-affect correspondence. In this work, we formulate Affective-Episodic Retrospection (AER) as a task that explicitly evaluates the recovery of past events, associated affects, and their correspondence, and define Event-Affect Decoupling as a failure mode where the correct emotion is recalled but associated with the wrong episode. To diagnose Event-Affect Decoupling, we propose EM-TRACE, a stage-wise framework that decomposes AER into retrieval, affect recovery, and realization. On a controlled GoEmotions-based benchmark, Emotion-only retrieval achieves 28.65% affect recovery but retrieves the target episode for only 4.44% of queries, yielding a UAR of 24.21%. Further analysis reveals that event retrieval and affect assignment introduce distinct binding failures. These findings show that reliable AER requires grounded recall of emotional experiences, where episode retrieval, affect recovery, event-affect binding, and generation quality should be evaluated jointly. Our code is available at https://anonymous.4open.science/r/A412/.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
