# D-ACR: Dialogue-Aware Context Retrieval for Long-Term Conversational Memory

- Source: OpenReview
- Venue: ACL ARR 2026 August Submission
- Paper ID: openreview:LJTjY3nUJm
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Unknown
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/August/-/Submission
- URL: https://openreview.net/forum?id=LJTjY3nUJm

## One-Sentence Summary
AI assistants now accumulate conversation history spanning days, months, or years, making retrieval of past context essential for grounded responses.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 August Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：AI assistants now accumulate conversation history spanning days, months, or years, making retrieval of past context essential for grounded responses.

进一步看，论文的核心做法或实验重点可以概括为：Users may seek specific details from prior interactions, either explicitly through history search or implicitly during ongoing conversations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 August Submission
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory, memory benchmark, memory benchmarks
- 来源分类信息：aclweb.org/ACL/ARR/2026/August/-/Submission

## Abstract Snapshot
AI assistants now accumulate conversation history spanning days, months, or years, making retrieval of past context essential for grounded responses. Users may seek specific details from prior interactions, either explicitly through history search or implicitly during ongoing conversations. Unlike typical document retrieval in RAG settings, dialogue history forms a coherent sequential discourse in which the meaning of an utterance depends on its surrounding context. Existing approaches construct dialogue retrieval units through segmentation, summarization, or hybrid memory construction, but these units are constructed offline and therefore cannot adapt to the information needs expressed by the current query. We propose D-ACR (Dialogue-Aware Context Retrieval), which dynamically identifies relevant segments at query time via KadaneDial, our adaptation of Kadane's maximum-subarray algorithm to the dialogue domain. Across four conversational memory benchmarks and four backbone LLMs, D-ACR achieves the highest retrieval hit and recall while retrieving fewer turns than other strong methods, and maintains stable performance regardless of the backbone LLM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
