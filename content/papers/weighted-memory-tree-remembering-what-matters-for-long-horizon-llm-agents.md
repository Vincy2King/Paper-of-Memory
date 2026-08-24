# Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.20631v1
- Published: 2026-08-21
- Updated: 2026-08-21
- Authors: Quang Dao, Purvi Kathalkar, Kenneth Eaton
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.20631v1

## One-Sentence Summary
Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and...

进一步看，论文的核心做法或实验重点可以概括为：Existing memory approaches organize or compress execution histories but provide limited mechanisms for deciding which memories remain active.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and expose reasoning to outdated, irrelevant, or misleading information, potentially degrading reasoning quality. Existing memory approaches organize or compress execution histories but provide limited mechanisms for deciding which memories remain active. We introduce the, a hierarchical memory system that organizes execution into tasks, subtasks, and actions while assigning each memory a dynamic retention score. Event-based updates and selection-based decay revise these scores, allowing WMT to preserve useful information, fold completed trajectories, suppress low-utility content, and retain access to folded context. We evaluate WMT on GAIA-Text using Qwen3-8B, Gemma 4 E4B, and Llama-3.1-8B, with ablations and memory-poisoning experiments. Relative to linear memory, WMT improves accuracy by an average of 9.97 percentage points while reducing prompt-token usage by 32.8%. Memory-poisoning experiments show that WMT limits the persistence and propagation of unreliable information. Our results suggest that effective long-horizon agent memory depends less on storing more information than on deciding which information should remain active.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
