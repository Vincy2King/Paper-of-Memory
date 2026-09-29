# ARSM: Auto-Regressive State Machine for Agentic Reasoning Compression

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32852v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Xiafeng Man, Siyuan Ye, Xiaosong Ma
- Tags: agent, compression, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.32852v1

## One-Sentence Summary
While Large Language Model (LLM)-based agents demonstrate strong capabilities in long-horizon tasks by interleaving reasoning with external environment interactions, the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While Large Language Model (LLM)-based agents demonstrate strong capabilities in long-horizon tasks by interleaving reasoning with external environment interactions, the continuous accumulation of context rapidly...

进一步看，论文的核心做法或实验重点可以概括为：Existing memory compression methods rely on task-specific optimization or external auxiliary models, introducing significant computational overhead.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context
- 检索关键词命中：memory compression
- 来源分类信息：cs.CL

## Abstract Snapshot
While Large Language Model (LLM)-based agents demonstrate strong capabilities in long-horizon tasks by interleaving reasoning with external environment interactions, the continuous accumulation of context rapidly creates a critical memory bottleneck. Existing memory compression methods rely on task-specific optimization or external auxiliary models, introducing significant computational overhead. Furthermore, the resulting compressed representations tend to lose structured relationships, leading to information dilution, attention collapse, and degraded decision consistency. To address these limitations, we propose Auto-Regressive State Machine (ARSM), a lightweight training-free framework that enables in-situ reasoning compression through structured state evolution. ARSM introduces two key components: (i) a trajectory abstraction mechanism that reorganizes interaction histories into compact Hypothesis-Action-Result (HAR) micro-chains; (ii) a dynamic state machine that regulates hierarchical memory through atomic operations and a compression-control parameter. These components are unified within an auto-regressive, self-compressive generation space, where each model output jointly performs external action execution and internal state updates. We evaluate ARSM on Webshop, Multi-Objective Multi-Hop QA, and SWE-Bench Lite datasets. Experimental results show that ARSM maintains the task performance while simultaneously reducing token consumption, offering a practical, cost-effective route toward scalable autonomous agents for long-horizon tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
