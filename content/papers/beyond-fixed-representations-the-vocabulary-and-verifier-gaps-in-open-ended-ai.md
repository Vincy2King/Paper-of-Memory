# Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.09560v1
- Published: 2026-07-10
- Updated: 2026-07-10
- Authors: Yuan Cao, Haiqian Yang
- Tags: persistent memory
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2607.09560v1

## One-Sentence Summary
Modern AI systems are increasingly being evaluated for their ability to reason, code, prove theorems, use tools, and long-horizon research tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modern AI systems are increasingly being evaluated for their ability to reason, code, prove theorems, use tools, and long-horizon research tasks.

进一步看，论文的核心做法或实验重点可以概括为：These are powerful capabilities, but they share a structural limitation: the representational frame within which the model operates, including its conceptual vocabulary, the space of admissible solutions it can...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Modern AI systems are increasingly being evaluated for their ability to reason, code, prove theorems, use tools, and long-horizon research tasks. These are powerful capabilities, but they share a structural limitation: the representational frame within which the model operates, including its conceptual vocabulary, the space of admissible solutions it can search, and the criteria by which success is evaluated, is typically fixed and supplied in advance. This paper argues that building stronger intelligent systems capable of open-ended innovation requires additional classes of operations: the creation, stabilization, and reuse of new representational primitives, which alter the space being searched rather than simply searching within it. We characterize the distance between current AI systems and genuinely open-ended intelligence through two gaps. The first is the vocabulary gap, the difficulty of inventing and stabilizing new representational primitives rather than merely recombining existing ones. The second is the verifier gap, the difficulty of judging the value of a new primitive when its full payoff may be visible only after future reuse. We interpret both gaps through a unified framework of intelligence as cognitive discrepancy reduction. By viewing intelligent behaviors as a sequence of cognitive transformations, we distinguish intra-space transformations which operate within a fixed representational frame, from generative transformations which may modify the frame itself. On this basis, we propose a ladder of innovation autonomy and outline several directions for advancing open-ended AI, including objectives that reward useful representational change, persistent memory architectures for invented primitives, and adaptive verification mechanisms capable of evolving alongside the representations they evaluate.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
