# Personalized Turn-Level User Conversation Satisfaction Benchmark

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.29711v1
- Published: 2026-05-28
- Updated: 2026-05-28
- Authors: Zhefan Wang, Zhiqiang Guo, Weizhi Ma, Min Zhang, Quanjia Yan, Hengliang Luo
- Tags: benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.29711v1

## One-Sentence Summary
User satisfaction with AI assistants is highly personalized: the same response may satisfy one user but disappoint another depending on what each user expects and what they have...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：User satisfaction with AI assistants is highly personalized: the same response may satisfy one user but disappoint another depending on what each user expects and what they have asked for before.

进一步看，论文的核心做法或实验重点可以概括为：Existing automatic evaluation methods mostly measure generic response quality, making it difficult to judge whether a response satisfies a user at a specific turn.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
User satisfaction with AI assistants is highly personalized: the same response may satisfy one user but disappoint another depending on what each user expects and what they have asked for before. Existing automatic evaluation methods mostly measure generic response quality, making it difficult to judge whether a response satisfies a user at a specific turn. We study this problem as personalized turn-level user conversation satisfaction evaluation. We build a conversation satisfaction evaluator that combines compact user memories with target-turn context to produce satisfaction scores and dissatisfaction-oriented rationales. Meta-evaluation against human satisfaction annotations shows that personalized memory and post-hoc score calibration improve ordinal agreement and dissatisfied-turn detection over supervised, retrieval-based, and generic LLM-as-a-judge baselines. We further introduce PersTurnBench, a personalized turn-level user conversation satisfaction benchmark that uses the verified evaluator to assess generation models via replay. By holding the replay state fixed, PersTurnBench enables controlled comparison of generic generation models and memory-augmented personalized systems without new human labels for every candidate model. The evaluator and benchmark let researchers compare candidate generation models on personalized satisfaction without collecting new user feedback for every model.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
