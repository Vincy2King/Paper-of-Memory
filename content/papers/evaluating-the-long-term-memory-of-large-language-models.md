# Evaluating the Long-Term Memory of Large Language Models

- Source: OpenReview
- Venue: ACL ARR 2024 October Submission
- Paper ID: openreview:6zcelIU9Ei
- Published: 2025-01-09
- Updated: 2026-07-02
- Authors: Unknown
- Tags: conversation, long-term
- Categories: aclweb.org/ACL/ARR/2024/October/-/Submission
- URL: https://openreview.net/forum?id=6zcelIU9Ei

## One-Sentence Summary
Large language models (LLMs) in applications such as dialogue systems, personalized recommendations, and personal assistants need to effectively retain and utilize historical...

## Introduction
这篇论文被纳入仓库，是因为它和 `conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2024 October Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models (LLMs) in applications such as dialogue systems, personalized recommendations, and personal assistants need to effectively retain and utilize historical information to provide more accurate and...

进一步看，论文的核心做法或实验重点可以概括为：Although training can enable LLMs to remember historical information, their effectiveness in long-term tasks requires further exploration.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2024 October Submission
- 高亮主题命中：conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：aclweb.org/ACL/ARR/2024/October/-/Submission

## Abstract Snapshot
Large language models (LLMs) in applications such as dialogue systems, personalized recommendations, and personal assistants need to effectively retain and utilize historical information to provide more accurate and consistent responses. Although training can enable LLMs to remember historical information, their effectiveness in long-term tasks requires further exploration. To this end, we propose a pipeline for constructing long-term dialogue data called Long Conversation Generation (LoCoGen) and develop a dataset named Long-term Chronological Conversations (LOCCO), focusing on studying the long-term memory capabilities of LLMs. We perform supervised fine-tuning (SFT) on LLMs using LOCCO and examine their memory at different time points. Our experiments show that LLMs can remember past interaction information to a certain extent, but their memory diminishes over time. Introducing spaced repetition strategies can enhance the durability of the model's memory. Additionally, models exhibit memory preferences for different categories of information. Our research not only provides a new framework and dataset for evaluating the long-term memory of LLMs but also offers important references for improving their memory durability in the future.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
