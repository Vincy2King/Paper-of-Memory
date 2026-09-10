# What Should an Agent Forget? Separating What Is Stored from What Is Used

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.10263v1
- Published: 2026-09-09
- Updated: 2026-09-09
- Authors: Yuhang Li, Yuchen Li
- Tags: agent, context, conversation, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.10263v1

## One-Sentence Summary
Persistent language agents need stored experience to remain available across time, while each answer requires evidence suited to a particular question.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent language agents need stored experience to remain available across time, while each answer requires evidence suited to a particular question.

进一步看，论文的核心做法或实验重点可以概括为：A superseded fact can mislead a current-state answer and still be essential for a historical query.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Persistent language agents need stored experience to remain available across time, while each answer requires evidence suited to a particular question. A superseded fact can mislead a current-state answer and still be essential for a historical query. We present RD-Forget, a training-free framework that separates what an agent stores from what it uses. A retained source archive preserves observations, and a query-conditioned memory view controls their influence on the current answer. A frozen language-model curator extracts relevant evidence, groups facts into semantic slots, and preserves the relations needed for multi-hop reasoning. Same-slot replacement links suppress superseded values in current-state contexts, while intent-aware retrieval makes earlier evidence eligible again. A rate-distortion formulation guides construction of the answer-time view within a memory budget. Experiments span conversational memory, knowledge updating, fact consolidation, long-context reasoning, and personalization under a shared answering pipeline. The results associate accurate answers with both query-relevant evidence construction and control over obsolete alternatives. Configurations without forgetting or query conditioning have the largest score deficits, while slot grouping, historical access, and relation preservation contribute complementary functions. Retaining history while selectively controlling its use offers a practical way to accommodate changing facts and future questions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
