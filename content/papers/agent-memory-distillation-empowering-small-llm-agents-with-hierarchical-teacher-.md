# Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07169v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Taeil Kim, Kangsan Kim, Sung Ju Hwang
- Tags: agent, benchmark
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2608.07169v1

## One-Sentence Summary
Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own.

进一步看，论文的核心做法或实验重点可以概括为：We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow memory encodes task-level strategies, Subtask memory provides concrete behavioral examples at an intermediate granularity, and Function memory captures per-function calling conventions and common pitfalls. Workflow and Subtask memories are injected proactively at the start of each task, while Function memory is retrieved reactively upon tool-calling errors. We evaluate AMD on three tool-use benchmarks using four student models (4B-8B parameters) with GPT-5-mini as the teacher, achieving average accuracy gains of 27.2%p, 11.2%p, and 3.4%p on AppWorld, BFCL V3, and ToolSandbox, while consistently outperforming existing memory-based baselines. Further analysis shows that Subtask memory contributes the largest gains, teacher effectiveness depends on both teacher capability and student compatibility, and 4B-sized students benefit most from AMD.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
