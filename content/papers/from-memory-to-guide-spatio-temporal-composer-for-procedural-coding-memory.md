# From Memory to Guide: Spatio-Temporal Composer for Procedural Coding Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04868v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Zhixuan Tan, Pengjie Gu, Zhao Li, Yihan Hu, Xu He, Dong Li, Jianye Hao
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.04868v1

## One-Sentence Summary
Memory-augmented agents typically integrate procedural knowledge by injecting retrieved skills directly into text prompts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented agents typically integrate procedural knowledge by injecting retrieved skills directly into text prompts.

进一步看，论文的核心做法或实验重点可以概括为：This approach dangerously equates readable text with reliable execution.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented agents typically integrate procedural knowledge by injecting retrieved skills directly into text prompts. This approach dangerously equates readable text with reliable execution. To bridge this gap, we introduce From Memory to Guide, a novel paradigm that transitions procedural memory from passive text delivery to active, inference-time policy adaptation. We instantiate this paradigm through the Spatio-Temporal Composer, an active policy compiler that explicitly manages exactly how and when retrieved knowledge should be applied. Rather than treating skills as plug-and-play modules, Composer dynamically aligns historical knowledge with current environmental constraints (spatial adaptation) and precisely dictates its applicable lifecycle (temporal orchestration). It actively transforms static memories into strictly bounded Runtime Guides---equipping the agent with localized objectives and behavioral guardrails without requiring a single parameter update. Extensive evaluations on 13 demanding, long-horizon software engineering tasks in EngramBench demonstrate the clear advantages of this architecture. Composer not only robustly prevents context mismatch but drives an absolute pass-rate increase of 7.2 percentage points on the most complex tasks, while simultaneously slashing the main agent's token usage by 32.2%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
