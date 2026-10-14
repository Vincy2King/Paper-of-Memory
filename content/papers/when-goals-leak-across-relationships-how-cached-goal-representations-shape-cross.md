# When Goals Leak Across Relationships: How Cached Goal Representations Shape Cross-Client Decisions

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17365v1
- Published: 2026-10-12
- Updated: 2026-10-12
- Authors: Saloni Gupta, Sébastien Krier, Glenn Matlin
- Tags: agent, conversation
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.17365v1

## One-Sentence Summary
As LLM agents take on more autonomous roles, they may interact with multiple clients and counterparties whose goals and incentives conflict.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As LLM agents take on more autonomous roles, they may interact with multiple clients and counterparties whose goals and incentives conflict.

进一步看，论文的核心做法或实验重点可以概括为：If an agent maintains shared inference state across these interactions, information associated with one relationship may influence decisions made for another.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI

## Abstract Snapshot
As LLM agents take on more autonomous roles, they may interact with multiple clients and counterparties whose goals and incentives conflict. If an agent maintains shared inference state across these interactions, information associated with one relationship may influence decisions made for another. We test OLMo-3-7B-Instruct in a controlled two-client environment with 20 market scenarios, where each client is assigned an opposing objective. With shared conversational memory, the model deviates from the current client's objective in 22% of eligible decisions. We then investigate how these goals are represented in the KV cache. Linear probes show that client-goal ownership becomes highly recoverable in middle layers and is concentrated in particular attention heads. We use these results to identify where to intervene in the cache and test whether these representations affect the model's decisions. Ablating the competitor's cached goal representations at these locations shifts the model toward the current client. The effect is larger for heads identified by probing than for randomly selected heads, and larger when ablating goal tokens than matched non-goal tokens from the same client. Our results show that client-specific goal representations persist in the KV cache and can causally influence decisions made for other clients, highlighting the importance of relationship-specific state isolation in persistent LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
