# Evaluating Memanto on DolphinBench for AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.28231v1
- Published: 2026-11-20
- Updated: 2026-11-20
- Authors: Suleman Khan, Rasa Rahnema, Tara Khani, Majid Fekri, Fattane Zarrinkalam
- Tags: agent, benchmark, conversation
- Categories: cs.IR, cs.AI
- URL: http://arxiv.org/abs/2611.28231v1

## One-Sentence Summary
Memory benchmarks built on question answering tell an agent which fact to recall.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory benchmarks built on question answering tell an agent which fact to recall.

进一步看，论文的核心做法或实验重点可以概括为：Workplace requests often leave that need implicit: to post an update in the team's channel, an agent must work out which channel from earlier interactions and use it in a tool call.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.IR, cs.AI

## Abstract Snapshot
Memory benchmarks built on question answering tell an agent which fact to recall. Workplace requests often leave that need implicit: to post an update in the team's channel, an agent must work out which channel from earlier interactions and use it in a tool call. We evaluate Memanto, a memory agent that ranks memories with an information-theoretic relevance score, on DolphinBench, which tests memory through 600 simulated workplace tasks, each validated as requiring memory. Running in the Hermes agent harness with GPT-6-Luna and at most 6 iterations per conversation, Memanto completes 503 tasks (83.83%). The strongest configuration reported by the benchmark's authors, Mem0 with GPT-5.6-Luna and up to 60 iterations, completes 424 (70.67%). Memanto's run also has the lowest total cost ($10.86, against $61.48 for the cheapest reported run) and the shortest median task latency (15.32s). Grading uses the benchmark's own judge, but the agent model differs, so these results compare complete systems. The memory system affects both whether an agent completes such tasks and what completion costs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
