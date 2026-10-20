# Persistent Memory and Iterative Improvement in an LLM Agent for Chinese-Character Drawing

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.24090v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Peilin Wu, Yi-Zhuang You
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.24090v1

## One-Sentence Summary
Does persistent memory accumulated from previous attempts help an LLM agent solve new problems, and does memory design affect that benefit?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Does persistent memory accumulated from previous attempts help an LLM agent solve new problems, and does memory design affect that benefit?

进一步看，论文的核心做法或实验重点可以概括为：We study programmatic Chinese-character drawing across five agent conditions attempting the same 668 items.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Does persistent memory accumulated from previous attempts help an LLM agent solve new problems, and does memory design affect that benefit? We study programmatic Chinese-character drawing across five agent conditions attempting the same 668 items. Accumulated memory produces modest aggregate gains despite substantial growth in the memory stores: free-form notes improve first-attempt success by 4.6 percentage points, while a design combining free-form memory with reusable code improves it by 2.8 points. The two designs do not differ significantly overall, but the code bank shows a suggestive advantage on later, harder items. A separate post-hoc comparison finds a much larger improvement when the code-bank agent receives privileged, target-specific structural supervision. The agent can therefore exploit highly informative structural guidance, although the privileged per-item information does not establish what could have been learned from experience alone. These results suggest that memory design may affect where accumulated experience becomes useful, even when its average benefit is modest.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
