# DolphinBench: Mapping the Pareto Frontier of Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.24971v2
- Published: 2026-09-21
- Updated: 2026-09-22
- Authors: Soumil Rathi, Deshraj Yadav, Taranjeet Singh
- Tags: agent, benchmark, context, conversation, long-term
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.24971v2

## One-Sentence Summary
Agents today often take real-world actions that depend on long-term memory and context recall over time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents today often take real-world actions that depend on long-term memory and context recall over time.

进一步看，论文的核心做法或实验重点可以概括为：However, most current memory benchmarks are built for a conversational question-answer format, where the question itself signals that some fact must be retrieved, and often which one.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Agents today often take real-world actions that depend on long-term memory and context recall over time. However, most current memory benchmarks are built for a conversational question-answer format, where the question itself signals that some fact must be retrieved, and often which one. Moreover, benchmarks rarely require anything beyond accuracy from submissions, allowing memory systems to make unreasonable cost/time tradeoffs to achieve higher scores. We present DolphinBench, a benchmark that evaluates memory directly through an agent's task completion. DolphinBench includes three knowledge-work personas with roughly 500k tokens of user messages per persona and evaluates agents on tasks that depend on information from that history. We verify all 200 tasks per persona by running an agent with and without the relevant history, requiring success with it and failure without it. Finally, we require all evaluations to report total cost and latency alongside accuracy, which enables us to evaluate agent memory systems holistically. No existing memory benchmark combines all three. The dataset and evaluation code are available at https://dolphinbench.ai.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
