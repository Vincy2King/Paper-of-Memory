# NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.17596v1
- Published: 2026-05-17
- Updated: 2026-05-17
- Authors: Mujahid Sultan, Sri Thuraisamy, Daya Rajaratnam
- Tags: agent, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.17596v1

## One-Sentence Summary
We present NeuSymMS, an adaptive memory system that enables large language model (LLM) agents to learn, remember, and reason about users across sessions via a hybrid neuro-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present NeuSymMS, an adaptive memory system that enables large language model (LLM) agents to learn, remember, and reason about users across sessions via a hybrid neuro-symbolic architecture.

进一步看，论文的核心做法或实验重点可以概括为：NeuSymMS couples neural fact extraction from unstructured dialogue with a CLIPS-based expert system that classifies, deduplicates, and reconciles facts under explicit lifecycle rules.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
We present NeuSymMS, an adaptive memory system that enables large language model (LLM) agents to learn, remember, and reason about users across sessions via a hybrid neuro-symbolic architecture. NeuSymMS couples neural fact extraction from unstructured dialogue with a CLIPS-based expert system that classifies, deduplicates, and reconciles facts under explicit lifecycle rules. The system represents knowledge as subject-relation-value triples stored in relational database management system, supports user/agents/agent-to-agents scoping, and implements a dual-horizon short-term/long-term memory model with access-based promotion and time-based pruning. NeuSymMS maintains continuity of memory while avoiding context-window bloat and cross-entity contamination. We argue that this architecture offers a practical path to trustworthy, auditable memory for production agentic systems and discuss its novelty relative to log retrieval, summarization, and key-value approaches.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
