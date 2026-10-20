# Reasoning with Context Management and External Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.24187v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Man-Ling Sung, William Hartmann, Jiangying Zhou
- Tags: context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.24187v1

## One-Sentence Summary
Reasoning models maintain information about the status of their reasoning process through in-context memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Reasoning models maintain information about the status of their reasoning process through in-context memory.

进一步看，论文的核心做法或实验重点可以概括为：Complex problems require larger context windows and memory requirements.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Reasoning models maintain information about the status of their reasoning process through in-context memory. Complex problems require larger context windows and memory requirements. In this scenario, context management without caching risks discarding useful information for reasoning. We propose RCMEM, an approach that extends context management with an external memory to maintain additional information without burdening the reasoning model with additional context. RCMEM significantly reduces computation time on problems that require repeated computation of intermediate steps, while achieving better performance on complex problems. We demonstrate our approach on a few mathematics problems using model sizes ranging from 0.4 to 25 million parameters, and GPT-2.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
