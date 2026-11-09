# Decision Context: Persistent Behavioral Learning for AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.08644v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Nima Vahdat, Pashootan Vaezipoor
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.08644v1

## One-Sentence Summary
LLM agents do not learn from corrections across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents do not learn from corrections across sessions.

进一步看，论文的核心做法或实验重点可以概括为：A user fixes the same mistake at the start of every conversation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM agents do not learn from corrections across sessions. A user fixes the same mistake at the start of every conversation. Existing agent memory systems primarily handle facts, such as preferences, entities, and conversational history, rather than procedural knowledge. We present Forge Decision Context (forge_dc), a system that captures behavioral signals from human corrections and self-assessed tool-call failures, compiles them into imperative RULE directives, and injects them at the decision points where they apply. We evaluate forge_dc alongside four predecessor approaches on DC-Bench, a new benchmark of 71 scenarios across nine behavioral dimensions, built from real executed agent traces in a deterministic mocked-tool environment. forge_dc reaches 95% compliance, up from 55% with naive retrieval, while injecting approximately 10 times fewer tokens per query. Across the five-stage progression, the strongest systems represent behavioral memory as explicit directives and deliver it at the decision points where it applies. The results identify representation, activation, and placement as central design choices for persistent behavioral learning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
