# Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.30485v1
- Published: 2026-10-21
- Updated: 2026-10-21
- Authors: Jialin Li, Zhenhao Chen, Hanjun Luo, Hanan Salam
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2610.30485v1

## One-Sentence Summary
Personal intelligence systems are taking on increasingly complex everyday tasks, yet repeated questions, unnecessary confirmations, and unwanted outreach can turn capable...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal intelligence systems are taking on increasingly complex everyday tasks, yet repeated questions, unnecessary confirmations, and unwanted outreach can turn capable assistance into interaction burden.

进一步看，论文的核心做法或实验重点可以概括为：Reducing this burden requires agents to remember how users want to be assisted.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Personal intelligence systems are taking on increasingly complex everyday tasks, yet repeated questions, unnecessary confirmations, and unwanted outreach can turn capable assistance into interaction burden. Reducing this burden requires agents to remember how users want to be assisted. However, existing memory benchmarks focus on factual recall and personalized answers and rarely test how agents learn and act on interaction preferences. We introduce MemPABench, an interactive environment for on-policy evaluation of memory in personal agents. MemPABench poses long-horizon tasks requiring agents to decide when to clarify, confirm, or act autonomously. Four grounded simulated users hold 14 preferences across work and personal contexts. Their feedback spans 99 sessions over four months, with five event-driven changes per user testing memory updates. We evaluate preference selection, delivered behavior, and sensitivity to context and preference change. Evaluating four memory systems across four LLM backbones, we find that current memory brings limited gains in preference selection. Retrieval-based systems (i.e. Mem0, MemOS, simple RAG) do not outperform No Memory, while File-based memory improves accuracy but applies preferences beyond relevant contexts. Our analysis shows that current memory struggles to retrieve interaction preferences and adapt to preference changes. Even with the correct preference available, overriding the agent's default interaction habits remains challenging. The environment and dataset are available at https://mempabench.com.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
