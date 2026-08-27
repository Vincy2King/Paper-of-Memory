# AWM: Answerable Working Memory for Long-Document VQA Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.25618v1
- Published: 2026-08-26
- Updated: 2026-08-26
- Authors: Dongzhuoran Zhou, Yuqicheng Zhu, Yule Liu, Zhen Yang, Rui Lu, Yuxiao Dong, Jie Tang, Evgeny Kharlamov
- Tags: agent, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.25618v1

## One-Sentence Summary
Long-document visual question answering increasingly relies on VLM agents that retrieve candidate pages, inspect page images, write findings to working memory, and synthesize...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-document visual question answering increasingly relies on VLM agents that retrieve candidate pages, inspect page images, write findings to working memory, and synthesize answers.

进一步看，论文的核心做法或实验重点可以概括为：Working memory should carry answer-supporting evidence across page inspections for later grounded answering, yet existing evaluation mainly checks final-answer correctness and evidence-page access.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-document visual question answering increasingly relies on VLM agents that retrieve candidate pages, inspect page images, write findings to working memory, and synthesize answers. Working memory should carry answer-supporting evidence across page inspections for later grounded answering, yet existing evaluation mainly checks final-answer correctness and evidence-page access. This creates a memory-quality blind spot: an agent may reach the right page and answer correctly while leaving behind memory too generic or incomplete to support answering once page context is removed. We introduce \emph{memory-only answerability}, a diagnostic that asks whether a reader can answer from the question and terminal working memory alone. Building on this diagnostic, \emph{Answerable Working Memory} (AWM) treats terminal working memory as an answerable evidence artifact, and AWM-GRPO incorporates this signal into the GRPO reward while preserving final-answer priority. Under GRPO, this reward assigns higher advantages to answer-correct trajectories whose terminal working memory remains answerable. On \textsc{MMLongBench-Doc}, even when gold evidence pages are provided, 42.5\% of correct answers still cannot be answered from terminal working memory alone. AWM-GRPO improves final-answer accuracy over the RAG baseline by 8.1 and 11.9 points on \textsc{MMLongBench-Doc} and \textsc{LongDocURL} and reduces the memory-missing-correct rate by 2.7 points over answer-only GRPO.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
