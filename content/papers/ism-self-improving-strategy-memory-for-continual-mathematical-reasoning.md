# ISM:Self-Improving Strategy Memory for Continual Mathematical Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.31191v1
- Published: 2026-06-30
- Updated: 2026-06-30
- Authors: Prakhar Dixit, Tim Oates
- Tags: episodic, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2606.31191v1

## One-Sentence Summary
We propose Intelligent Schema Memory (ISM), a self-evolving memory-augmented system that improves mathematical reasoning for a frozen LLM under continual learning with hard...

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We propose Intelligent Schema Memory (ISM), a self-evolving memory-augmented system that improves mathematical reasoning for a frozen LLM under continual learning with hard episodic resets.

进一步看，论文的核心做法或实验重点可以概括为：ISM maintains a compact, self-refined bank of strategy schemas learned from both successful and failed episodes, with symbolic tools that check intermediate steps and certify answers.Without updating model parameters,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
We propose Intelligent Schema Memory (ISM), a self-evolving memory-augmented system that improves mathematical reasoning for a frozen LLM under continual learning with hard episodic resets. ISM maintains a compact, self-refined bank of strategy schemas learned from both successful and failed episodes, with symbolic tools that check intermediate steps and certify answers.Without updating model parameters, ISM outperforms passive, retrieval, and reflection baselines on MATH-Hard and OlympiadBench, using 64% and 86% fewer schemas respectively than the strongest passive baseline. These results show that small, actively maintained, and verified strategy memories can support reliable continual mathematical reasoning under strict episodic isolation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
