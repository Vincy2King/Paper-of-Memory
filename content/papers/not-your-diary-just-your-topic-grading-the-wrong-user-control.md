# Not Your Diary, Just Your Topic: Grading the Wrong-User Control

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.09609v1
- Published: 2026-11-06
- Updated: 2026-11-06
- Authors: Karina Romanova, Igor Kiselev, Vladimir Platonov, Viliana Devbunova, Gregory Leleytner, Adeliya Leleytner, Lina Veltman, Aleksandr Nikolich
- Tags: memory
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.09609v1

## One-Sentence Summary
A common test of personalization replaces a user's history with someone else's and measures the drop in accuracy.

## Introduction
这篇论文被纳入仓库，是因为它和 `memory research` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A common test of personalization replaces a user's history with someone else's and measures the drop in accuracy.

进一步看，论文的核心做法或实验重点可以概括为：But this swap also changes the topics in the history, so the drop may reflect topic mismatch.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
A common test of personalization replaces a user's history with someone else's and measures the drop in accuracy. But this swap also changes the topics in the history, so the drop may reflect topic mismatch. We examine this problem with a frozen language model on LaMP-2 news categorization, using histories from similar users and synthetic histories assembled from other users' articles. The user's own history improves accuracy by 2.3 percentage points over a model trained without history. Removing history only at evaluation makes this gain appear larger, at 4.8 points. Category labels alone reproduce 86% of the accuracy gap between the user's own history and a random user's history. With synthetic histories matched on labels and text similarity, the gap falls to 0.9 points. Across two user splits and three training seeds, the advantage over a similar user's history is 3.2 points for users seen during training and 0.65 points for unseen users, where the evidence for an advantage remains inconclusive. A small movie-tagging experiment with one training seed also finds no advantage over other users' histories. These findings show why personalization should be evaluated on unseen users, with histories of similar content and a model trained without history as comparisons. We also find that adding gated cross-attention improves on a prefix-only model under our training setup; whether this holds more broadly remains open.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
