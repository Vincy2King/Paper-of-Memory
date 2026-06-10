# Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.10949v1
- Published: 2026-06-09
- Updated: 2026-06-09
- Authors: Shelly Bensal, Axel Magnuson, Aparna Balagopalan, Daniel M. Bikel
- Tags: benchmark, compression, context, conversation
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.10949v1

## One-Sentence Summary
Persistent memory systems promise to make LLMs more helpful by storing user beliefs over time.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory systems promise to make LLMs more helpful by storing user beliefs over time.

进一步看，论文的核心做法或实验重点可以概括为：We show they also make models less correct by systematically amplifying sycophancy, wherein models prioritize agreement with users over accuracy.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, context, conversation
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent memory systems promise to make LLMs more helpful by storing user beliefs over time. We show they also make models less correct by systematically amplifying sycophancy, wherein models prioritize agreement with users over accuracy. We conduct the first systematic evaluation of this effect, introducing MIST: a benchmark of synthetically generated multi-turn conversations where users express plausible misconceptions in scientific, medical, and moral reasoning domains. Testing across three state-of-the-art memory systems and five model families reveals that memory amplifies sycophantic behavior across all conditions, with up to 25x higher sycophancy rates than in-context baselines. Error analyses suggest memory extraction as the primary culprit: lossy compression into discrete snippets encodes user misconceptions while discarding corrective context. Based on these results, we propose two lightweight mitigations that substantially reduce sycophancy while matching or exceeding memory systems at factual recall.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
