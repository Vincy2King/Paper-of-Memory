# Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.12213v1
- Published: 2026-05-12
- Updated: 2026-05-12
- Authors: Jiazhou Liang, Armin Toroghi, Yifan Simon Liu, Faeze Moradi Kalarde, Liam Gallagher, Scott Sanner
- Tags: agent, context, conversation, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.12213v1

## One-Sentence Summary
LLM-based conversational AI agents struggle to maintain coherent behavior over long horizons due to limited context.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based conversational AI agents struggle to maintain coherent behavior over long horizons due to limited context.

进一步看，论文的核心做法或实验重点可以概括为：While RAG-based approaches are increasingly adopted to overcome this limitation by storing interactions in external memory modules and performing retrieval from them, their effectiveness in answering challenging...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：agent memory, memory retrieval, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM-based conversational AI agents struggle to maintain coherent behavior over long horizons due to limited context. While RAG-based approaches are increasingly adopted to overcome this limitation by storing interactions in external memory modules and performing retrieval from them, their effectiveness in answering challenging questions (e.g., multi-hop, commonsense) ultimately depends on the agent's ability to reason over the retrieved information. However, existing methods typically retrieve memory based on semantic similarity to the raw user utterance, which lacks explicit reasoning about missing intermediate facts and often returns evidence that is irrelevant or insufficient for grounded reasoning. In this work, we introduce Goal-Mem, a goal-oriented reasoning framework for RAG-based agentic memory that performs explicit backward chaining from the user's utterance as a goal. Rather than progressively expanding from retrieved context, Goal-Mem decomposes each goal into atomic subgoals, performs targeted memory retrieval to satisfy each subgoal, and iteratively identifies what information from memory should be retrieved when intermediate goals cannot be resolved. We formalize this process in Natural Language Logic, a logical system that combines the verifiability of reasoning provided by FOL with the expressivity of natural language. Through extensive experiments on two datasets and comparing to nine strong memory baselines, we show that Goal-Mem consistently improves performance, particularly on tasks requiring multi-hop reasoning and implicit inference.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
