# MINDSET: Energy-based Memory Evolution for Long Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.08586v2
- Published: 2026-10-06
- Updated: 2026-11-03
- Authors: Sujato Dutta, Sreekruthy Tummala, Shashank Vanga, Ayushmi Pavani, Neeraj Choudhary
- Tags: agent, context, conversation, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.08586v2

## One-Sentence Summary
In conversational memory, a later statement may replace an earlier fact, describe a different context, or be an isolated contradiction.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In conversational memory, a later statement may replace an earlier fact, describe a different context, or be an isolated contradiction.

进一步看，论文的核心做法或实验重点可以概括为：Thus, agentic memory must track what changed over time without erasing what was true before.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI

## Abstract Snapshot
In conversational memory, a later statement may replace an earlier fact, describe a different context, or be an isolated contradiction. Thus, agentic memory must track what changed over time without erasing what was true before. We introduce MINDSET, a memory controller that makes this distinction through explicit state transitions. It preserves original dialogue episodes and organizes them into versioned schemas. For each new episode, it chooses whether to reinforce a schema, supersede its current state, create a contextual branch, or start a new schema. A local energy score balances coherence, contradiction, historical preservation and fragmentation. Stability rules prevent isolated conflicts from immediately replacing established memory. On a frozen 700-question LoCoMo subset, MINDSET achieves the highest observed answer F1 among six evaluated systems and significantly improves retrieval ranking over LightMem. Without retuning, it obtains 69.23% judge accuracy on all LongMemEval knowledge-update cases, compared with 64.10% for Vector RAG. Two additional answer model backbones using Gemma-4-31B and GLM-4.7 provide further qualified evidence of generalization. These findings support explicit memory-state management as a useful approach to changing conversational knowledge.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
