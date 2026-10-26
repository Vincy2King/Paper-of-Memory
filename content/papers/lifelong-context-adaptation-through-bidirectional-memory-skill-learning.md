# Lifelong Context Adaptation through Bidirectional Memory-Skill Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.32295v1
- Published: 2026-10-23
- Updated: 2026-10-23
- Authors: Tianyi Xu, Huazheng Wang
- Tags: agent, context, conversation, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.32295v1

## One-Sentence Summary
Lifelong LLM agents must learn from an expanding history of interactions while making each decision within a bounded context window.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Lifelong LLM agents must learn from an expanding history of interactions while making each decision within a bounded context window.

进一步看，论文的核心做法或实验重点可以概括为：Memory makes past experience available, but the agent may still need to infer how to solve each new task from the retrieved records.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Lifelong LLM agents must learn from an expanding history of interactions while making each decision within a bounded context window. Memory makes past experience available, but the agent may still need to infer how to solve each new task from the retrieved records. Skills provide reusable procedures, yet may omit the task-specific facts needed to apply them. Because retrieved memory and skills shape the agent's behavior, they also influence the experience available for future learning. We introduce MemCryst, a framework for lifelong context adaptation through bidirectional learning of memory and skills with a frozen language model. Recurring episodes stored in memory support skill creation and revision, and the interactions guided by those skills supply new memory for subsequent learning. Facts retrieved from memory and learned skills jointly form the agent's context, while task outcomes adjust the future retrieval influence of the records actually served without rewriting their content. Across ten settings spanning embodied control, long-document reading, conversation, mathematics, and code, MemCryst leads seven reported comparisons. On ALFWorld, joint serving achieves 63.17% success, compared with 59.83% for memory-only and 50.50% for skill-only serving. Code is available at https://github.com/tianyi0216/Memcryst.git

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
