# MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.27366v1
- Published: 2026-05-26
- Updated: 2026-05-26
- Authors: Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang
- Tags: agent, long-term
- Categories: cs.AI, cs.CL, cs.LG, cs.MA
- URL: http://arxiv.org/abs/2605.27366v1

## One-Sentence Summary
Large language model (LLM) agents rely on reusable skills to solve complex tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents rely on reusable skills to solve complex tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, existing skill creation approaches treat skills as isolated and static artifacts, limiting their reusability, reliability, and long-term improvement.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CL, cs.LG, cs.MA

## Abstract Snapshot
Large language model (LLM) agents rely on reusable skills to solve complex tasks. However, existing skill creation approaches treat skills as isolated and static artifacts, limiting their reusability, reliability, and long-term improvement. We propose MUSE-Autoskill Agent (Memory-Utilizing Skill Evolution), a skill-centric agent framework that lets agents continuously improve their task-solving capability by creating, reusing, and refining skills under a unified lifecycle (creation, memory, management, evaluation, and refinement). Our framework enables agents to create skills on demand, store and reuse them across tasks, organize and select them efficiently, and evaluate them through unit tests and runtime feedback for continuous refinement. We further introduce skill-level memory that accumulates experience for each skill across tasks, enabling more effective reuse and adaptation over time. Experiments on SkillsBench provide initial evidence that lifecycle-managed skills can improve task success, efficiency, reuse, and cross-agent transfer, highlighting the importance of treating skills as long-lived, experience-aware, and testable assets.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
