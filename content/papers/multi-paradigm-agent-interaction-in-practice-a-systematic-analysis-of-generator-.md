# Multi-Paradigm Agent Interaction in Practice:A Systematic Analysis of Generator-Evaluator, ReAct Loop,and Adversarial Evaluation in the buddyMe Framework

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.16821v1
- Published: 2026-05-16
- Updated: 2026-05-16
- Authors: Xiaohua Wang, Chao Han, Kai Yu, XiaoLiang Xu, Liang Wang
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.16821v1

## One-Sentence Summary
The rapid evolution of Large Language Model (LLM) agents has produced diverse interaction paradigms, yet few production systems integrate multiple paradigms within a unified...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The rapid evolution of Large Language Model (LLM) agents has produced diverse interaction paradigms, yet few production systems integrate multiple paradigms within a unified architecture.

进一步看，论文的核心做法或实验重点可以概括为：This paper presents a systematic analysis of three principal agent interaction paradigms, including Multi-Agent Orchestration (Generator-Evaluator), ReAct Tool-Use Loops, and Memory-Augmented Interaction, as...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
The rapid evolution of Large Language Model (LLM) agents has produced diverse interaction paradigms, yet few production systems integrate multiple paradigms within a unified architecture. This paper presents a systematic analysis of three principal agent interaction paradigms, including Multi-Agent Orchestration (Generator-Evaluator), ReAct Tool-Use Loops, and Memory-Augmented Interaction, as implemented in buddyMe, an open-source multi-model agent programming framework. We formalize a five-stage processing pipeline: Requirement Pre-Review -> Task Decomposition -> ReAct Execution -> Real-Execution Verification -> Adversarial Evaluation Discussion, and establish a six-dimensional evaluation schema with weighted scoring. Through four empirical case studies drawn from real-world deployment logs covering museum guide generation, scheduled weather tasks, and comprehensive tour planning, we draw three key conclusions. First, Generator-Evaluator pre-review detects requirement omissions in 20 percent of complex tasks, with 80 percent tasks passing initial inspection. Second, the ReAct loop ensures stable subtask execution but leads to around 30 percent redundant tool invocations. Third, adversarial Evaluator-Defender discussions reach consensus within 2-3 rounds for nearly 70 percent of scenarios, functioning mainly for content refinement rather than logical reversal. We additionally provide three Mermaid-based architectural diagrams and conduct cross-paradigm comparisons with CrewAI, AutoGen, LangGraph, MemGPT and A-Mem across six system dimensions. The research outcomes offer practical design guidelines for constructing stable and reliable multi-paradigm agent systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
