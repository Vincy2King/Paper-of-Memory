# HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.16487v1
- Published: 2026-11-12
- Updated: 2026-11-12
- Authors: Saehun Chun, Wonje Choi, Jinwoo Jang, Taeyoon Kwack, Honguk Woo
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.16487v1

## One-Sentence Summary
Embodied agents make decisions by combining information from heterogeneous memory modules, including declarative memory for explicit knowledge, procedural memory for learned...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Embodied agents make decisions by combining information from heterogeneous memory modules, including declarative memory for explicit knowledge, procedural memory for learned routines, and working memory for current...

进一步看，论文的核心做法或实验重点可以概括为：During interaction, the memory contents required for decision making change with the agent's state, goal, and task progress, while many contents remain shared across consecutive decisions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Embodied agents make decisions by combining information from heterogeneous memory modules, including declarative memory for explicit knowledge, procedural memory for learned routines, and working memory for current observations. During interaction, the memory contents required for decision making change with the agent's state, goal, and task progress, while many contents remain shared across consecutive decisions. However, existing memory modules are typically accessed through separate interfaces, so each updated memory context is often processed as a new input to the foundation model. This prevents selective key-value (KV) cache reuse for unchanged memory contents and forces full KV cache recomputation even when much of the memory context remains valid. We introduce HeMeR, an inference framework that performs KV reconciliation between dynamically updated memory contexts and reusable KV states. HeMeR tracks declarative, procedural, and working memory contents across action decisions, preserves KV states for unchanged contents, and reconciles only the KV states affected by memory-content updates. This enables efficient and stable inference as memory contents evolve during interaction. We evaluate HeMeR on ALFWorld, Habitat, and real-world robotic deployments requiring coordinated use of heterogeneous memory contents. In the real-world setting, HeMeR achieves 83.20% task success and reduces per-step inference time from 2.94 to 1.87 seconds compared with MemRL, while preserving compatible KV states as task progress updates the memory context.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
