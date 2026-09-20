# Preference-aware memory update for long-term llm agents

- Source: OpenReview
- Venue: ACL26
- Paper ID: openreview:aG2EsikgYl
- Published: 2026-05-04
- Updated: 2026-09-20
- Authors: Haoran Sun, Zekun Zhang, Shaoning Zeng
- Tags: agent, context, conversation, long-term, retrieval
- Categories: OpenReview.net/Archive/-/Direct_Upload
- URL: https://openreview.net/forum?id=aG2EsikgYl

## One-Sentence Summary
One of the key factors influencing the reasoning capabilities of LLM-based agents is their ability to leverage long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL26` 这个 venue 相关。

从摘要来看，作者主要关注的是：One of the key factors influencing the reasoning capabilities of LLM-based agents is their ability to leverage long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Integrating long-term memory mechanisms allows agents to make informed decisions grounded in historical interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL26
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：OpenReview.net/Archive/-/Direct_Upload

## Abstract Snapshot
One of the key factors influencing the reasoning capabilities of LLM-based agents is their ability to leverage long-term memory. Integrating long-term memory mechanisms allows agents to make informed decisions grounded in historical interactions. While recent advances have significantly improved the storage and retrieval components—e.g., by encoding memory into dense vectors for similarity search or organizing memory as structured knowledge graphs—most existing approaches fall short in memory updating. In particular, they lack mechanisms for dynamically refining preference memory representations in response to evolving user behaviors and contexts. To address this gap, we propose a Preference-Aware Memory Update Mechanism (PAMU) that enables dynamic and personalized memory refinement. By integrating sliding window averages (SW) with exponential moving averages (EMA), PAMU constructs a fused preference-aware representation that captures both short-term fluctuations and long-term user tendencies. We conduct experiments on five task scenarios of the LoCoMo dataset, and the results show that our mechanism can significantly improve the output quality of LLM in five baselines, validating its effectiveness in long-term conversations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
