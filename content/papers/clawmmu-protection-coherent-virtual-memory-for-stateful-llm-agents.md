# ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.28093v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique, Lars Henning Klein, Akhil Arora, Ashvin Goel, Laurent Bindschaedler
- Tags: agent, context, long-term
- Categories: cs.CR, cs.AI, cs.OS
- URL: http://arxiv.org/abs/2610.28093v1

## One-Sentence Summary
AI agents keep long-term memory, much of which comes from web pages and tool results.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI agents keep long-term memory, much of which comes from web pages and tool results.

进一步看，论文的核心做法或实验重点可以概括为：Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CR, cs.AI, cs.OS

## Abstract Snapshot
AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose ClawMMU, a protection layer that labels every piece of memory with its owner, scope, origins, and authority. ClawMMU checks these labels whenever content enters the model's context, is written to storage, returns from storage, or drives a tool call. Its central rule is that information may rise in authority, but authority never lifts itself. Because the checks depend on where content came from, not on what it says, memory attacks become classical protection faults that the harness stops even when the model is fooled.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
