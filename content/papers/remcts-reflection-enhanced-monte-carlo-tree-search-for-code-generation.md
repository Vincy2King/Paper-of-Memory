# ReMCTS: Reflection-Enhanced Monte Carlo Tree Search for Code Generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34717v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Huifei Wang, Xinying Huang, Yiheng Sun, Yifan Yuan
- Tags: context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2609.34717v1

## One-Sentence Summary
Open-weight large language models (LLMs) can generate function-level programs from natural-language prompts, but plausible candidates still fail on hidden semantics and repeat...

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Open-weight large language models (LLMs) can generate function-level programs from natural-language prompts, but plausible candidates still fail on hidden semantics and repeat mistakes across repair attempts.

进一步看，论文的核心做法或实验重点可以概括为：We present ReMCTS, an execution-grounded, memory-augmented, LLM-guided MCTS-style search framework.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Open-weight large language models (LLMs) can generate function-level programs from natural-language prompts, but plausible candidates still fail on hidden semantics and repeat mistakes across repair attempts. We present ReMCTS, an execution-grounded, memory-augmented, LLM-guided MCTS-style search framework. It organizes program candidates as tree states, retains branch-local debugging context, retrieves failure experience across branches, and distinguishes failed checks from unavailable evidence. On HumanEval and MBPP-Sanitized, visible-test ReMCTS improves over direct generation in 8 of 10 model-dataset pairs under held-out evaluation, whereas proxy-only search is less stable. Controlled tree-search, sampling, repair, and memory ablations characterize the source and limits of these gains. A 30-task HumanEval-X C++ pilot further demonstrates compatibility with compiler-backed execution, but does not constitute a broad multilingual evaluation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
