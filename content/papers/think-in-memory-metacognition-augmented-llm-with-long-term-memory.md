# Think-in-Memory: Metacognition-Augmented LLM with Long-Term Memory

- Source: OpenReview
- Venue: ACL ARR 2025 February Submission
- Paper ID: openreview:xWMKJbmgeF
- Published: 2025-05-09
- Updated: 2026-07-02
- Authors: Unknown
- Tags: agent, context, conversation, long-term
- Categories: aclweb.org/ACL/ARR/2025/February/-/Submission
- URL: https://openreview.net/forum?id=xWMKJbmgeF

## One-Sentence Summary
Memory-augmented Large Language Models (LLMs) can utilize past contexts via recall-reason steps, which may produce biased thoughts, i.e., inconsistent reasoning paths over the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2025 February Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Memory-augmented Large Language Models (LLMs) can utilize past contexts via recall-reason steps, which may produce biased thoughts, i.e., inconsistent reasoning paths over the same recalled contexts.

进一步看，论文的核心做法或实验重点可以概括为：Motivated by that humans only memorize the metacognition thoughts rather than all details, we propose a self-organizing memory-augmented mechanism called Think-in-Memory (TiM) to flexibly utilize the historical...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2025 February Submission
- 高亮主题命中：agent, context, conversation, long-term
- 检索关键词命中：long-term memory, memory-augmented
- 来源分类信息：aclweb.org/ACL/ARR/2025/February/-/Submission

## Abstract Snapshot
Memory-augmented Large Language Models (LLMs) can utilize past contexts via recall-reason steps, which may produce biased thoughts, i.e., inconsistent reasoning paths over the same recalled contexts. Motivated by that humans only memorize the metacognition thoughts rather than all details, we propose a self-organizing memory-augmented mechanism called Think-in-Memory (TiM) to flexibly utilize the historical context, which is equipped with a metacognition space and stationary operation actions. Concretely, TiM can imitate human-level self-organization to memorize and update history context in a plug-and-play paradigm without suffering from reasoning inconsistency. The self-organization is formulated as a role-playing LLM agent pipeline to achieve stationary operation actions, i.e., thought generator, retriever, and organizer. Clinical diagnosis is adopted as the evaluation task: (1) we formulate a role-play simulator to simulate long-term interactions between the doctor and patient. (2) we collect a multi-turn medical consultations dataset from the real-world hospitals. Besides, two daily conversation datasets are also involved. Experiments demonstrate that our method achieves remarkable improvements on memory-augmented long-term dialogues about both daily and medical topics.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
