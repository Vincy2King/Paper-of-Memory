# PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.09664v1
- Published: 2026-09-09
- Updated: 2026-09-09
- Authors: Hyojeong Yu, Hyukhun Koh, Minsung Kim, Yunah Jang, Kyomin Jung
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.09664v1

## One-Sentence Summary
Large language models (LLMs) are increasingly deployed as personalized assistants that interact with users over extended periods of time.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) are increasingly deployed as personalized assistants that interact with users over extended periods of time.

进一步看，论文的核心做法或实验重点可以概括为：As conversations grow longer, relying on full interaction histories becomes increasingly inefficient and unreliable: long contexts introduce substantial computational overhead, making it difficult for models to...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language models (LLMs) are increasingly deployed as personalized assistants that interact with users over extended periods of time. As conversations grow longer, relying on full interaction histories becomes increasingly inefficient and unreliable: long contexts introduce substantial computational overhead, making it difficult for models to consistently identify and utilize the most relevant information for the current request. These challenges have motivated memory systems that structure and retrieve user-specific information. In realistic interactions, users often seek practical guidance such as recommendations, planning, and decision support. Unlike factual recall tasks, personalized guidance requires models to integrate information across multiple past conversations and reason about changing user preferences and experiences. However, existing conversational memory evaluations mainly focus on retrieval and factual recall. To study this challenge, we introduce PRAGMA, a benchmark for evaluating personalized guidance in long-term conversations. PRGAMA contains curated longitudinal conversation histories, evidence annotations, and guidance scenarios grounded in evolving user contexts and incorrect user assumptions. Experiments across retrieval systems, memory systems, and long-context models reveal that current systems struggle both to recover the appropriate conversational evidence and to effectively use it for personalized guidance. Our results highlight the need for memory architectures that support robust conversational retrieval and memory-grounded reasoning beyond evidence recall.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
