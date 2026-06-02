# Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.00832v1
- Published: 2026-05-30
- Updated: 2026-05-30
- Authors: Adril Putra Merin, David Anugraha, Ayu Purwarianti, Genta Indra Winata
- Tags: agent, benchmark, context, conversation
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.00832v1

## One-Sentence Summary
Recent advances in agentic AI have enabled agents to complete complex tasks through tool use, reasoning, and multi-step planning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in agentic AI have enabled agents to complete complex tasks through tool use, reasoning, and multi-step planning.

进一步看，论文的核心做法或实验重点可以概括为：Yet existing benchmarks evaluate agents within a single session, ignoring past actions, stated preferences, and prior decisions that agents must integrate to fulfill personalized user goals.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Recent advances in agentic AI have enabled agents to complete complex tasks through tool use, reasoning, and multi-step planning. Yet existing benchmarks evaluate agents within a single session, ignoring past actions, stated preferences, and prior decisions that agents must integrate to fulfill personalized user goals. We introduce Momento, a benchmark for persistent agentic task completion in multi-session service environments, requiring agents to take consequential, tool-mediated actions while resolving temporal dependencies and evolving user goals across sessions. Experimental results reveal that current agents fail primarily through misestimation of user state, treating prior session history as a reliable proxy for current context rather than stale information requiring re-validation, highlighting a substantial gap between current agent capabilities and realistic long-horizon human-agent interaction.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
