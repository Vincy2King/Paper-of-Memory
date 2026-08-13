# Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.11879v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Natchanon Pollertlam, Witchayut Kornsuwannawit
- Tags: agent, benchmark, conversation
- Categories: cs.CL, cs.IR
- URL: http://arxiv.org/abs/2608.11879v1

## One-Sentence Summary
Long-running conversational agents increasingly rely on a memory system to avoid resending the whole conversation each turn, yet how much that costs to serve has received little...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running conversational agents increasingly rely on a memory system to avoid resending the whole conversation each turn, yet how much that costs to serve has received little systematic benchmarking.

进一步看，论文的核心做法或实验重点可以概括为：We compare three memory systems (Mem0, Hindsight, and Mastra Observational Memory) against two reference strategies -- a fixed-size rolling window and resubmitting the full transcript -- across two backbones and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.IR

## Abstract Snapshot
Long-running conversational agents increasingly rely on a memory system to avoid resending the whole conversation each turn, yet how much that costs to serve has received little systematic benchmarking. We compare three memory systems (Mem0, Hindsight, and Mastra Observational Memory) against two reference strategies -- a fixed-size rolling window and resubmitting the full transcript -- across two backbones and conversations of up to 400 turns, pairing every cost measurement with answer accuracy on 665 LoCoMo questions. First, a memory system's serving cost cannot be predicted from conversation length and message size alone: a regression that tracks the two reference strategies closely misses the memory systems by 18-69%, their cost driven instead by internal memory behavior. Second, a break-even analysis shows that whether -- and when -- a memory system becomes cheaper to serve than the full transcript is highly sensitive to the system and the backbone, from the first tens of turns for the cheapest to never within 400 turns for the most expensive. Third, no system wins on both axes: accuracy spans 21-54%, and the backbone choice drives cost as much as the memory system does.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
