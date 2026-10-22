# MemoryTax: The Bitter Lesson of Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.29823v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Zedong Peng
- Tags: agent, context, conversation
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2610.29823v1

## One-Sentence Summary
Agent memory systems such as Mem0 and Zep decide what to keep before any question arrives; coding agents keep the raw history and let the model search it with its own tools.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory systems such as Mem0 and Zep decide what to keep before any question arrives; coding agents keep the raw history and let the model search it with its own tools.

进一步看，论文的核心做法或实验重点可以概括为：We ask whether designed memory still helps once the model is strong enough to search for itself.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Agent memory systems such as Mem0 and Zep decide what to keep before any question arrives; coding agents keep the raw history and let the model search it with its own tools. We ask whether designed memory still helps once the model is strong enough to search for itself. On one LoCoMo conversation (419 turns, 152 questions), we run four memory methods (full context, BM25, Mem0, Zep) and three coding agents (Pi, Codex, Claude Code), each with GPT-4o-mini, GPT-6 Luna and Claude Opus 5.5, and record what every rollout costs. This is a short empirical study, with one conversation and one run per cell. Agent memory is a costly patch for a weak model: Mem0 beats full context only with GPT-4o-mini, and its build alone costs more than a whole full-context rollout. Agent memory also has a ceiling, set by the model that writes it: a stronger reader does not recover what a weaker writer left out. With Claude Opus 5.5, Pi tops the cost-accuracy frontier, scoring 99% for less than half the cost of full context; its one miss is a wrong answer key. Part of that lead comes from photo captions that only the agents could read: on the 88 questions whose evidence has no photo, Pi and full context differ by one answer.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
