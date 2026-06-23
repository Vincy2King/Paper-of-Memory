# AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.21144v1
- Published: 2026-06-19
- Updated: 2026-06-19
- Authors: Xingyu Chen, Rui Wang, Zhaopeng Tu, Liefeng Bo
- Tags: agent, benchmark, context, long-term
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.21144v1

## One-Sentence Summary
Long-term memory systems for Large Language Model (LLM) agents typically try to \emph{remember everything}, extracting memories uniformly to retain as many facts as possible.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory systems for Large Language Model (LLM) agents typically try to \emph{remember everything}, extracting memories uniformly to retain as many facts as possible.

进一步看，论文的核心做法或实验重点可以概括为：In production, however, inference cost and finite context budgets make this untenable: beyond consolidating raw dialogue into memory, an agent must exert \emph{write control}, efficiently keeping only the information...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term memory systems for Large Language Model (LLM) agents typically try to \emph{remember everything}, extracting memories uniformly to retain as many facts as possible. In production, however, inference cost and finite context budgets make this untenable: beyond consolidating raw dialogue into memory, an agent must exert \emph{write control}, efficiently keeping only the information each user actually cares about. Otherwise, long-horizon personalized interactions suffer \emph{memory bloat}, where irrelevant trivia crowds out useful information and steadily erodes question-answering (QA) accuracy. We argue that what is worth remembering is role-dependent, and propose \textbf{AdaMem} (Adaptive Memory), a method that \emph{learns what to remember} for each user from feedback. AdaMem maintains a structured, role-specific Memory Policy and refines it from weekly QA feedback through a lightweight, patch-style self-reflection step with failure rollback. To study this setting, we build \textbf{AdaMem-Bench}, a benchmark that simulates weeks of interaction with week-by-week QA. Across two extraction models and two feedback modes, AdaMem improves QA accuracy by up to \textbf{+9.0\%} over the uniform Mem0 baseline while shrinking memory volume by \textbf{9\%}.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
