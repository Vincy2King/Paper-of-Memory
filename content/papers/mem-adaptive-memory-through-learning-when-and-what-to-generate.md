# Mem-$π$: Adaptive Memory through Learning When and What to Generate

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.21463v1
- Published: 2026-05-20
- Updated: 2026-05-20
- Authors: Xiaoqiang Wang, Chao Wang, Hadi Nekoei, Christopher Pal, Alexandre Lacoste, Spandana Gella, Bang Liu, Perouz Taslakian
- Tags: agent, benchmark, context, episodic, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.21463v1

## One-Sentence Summary
We present Mem-$π$, a framework for adaptive memory in large language model (LLM) agents, where useful guidance is generated on demand rather than retrieved from external memory...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We present Mem-$π$, a framework for adaptive memory in large language model (LLM) agents, where useful guidance is generated on demand rather than retrieved from external memory stores.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory-augmented agents typically rely on similarity-based retrieval from episodic memory banks or skill libraries, returning static entries that often misalign with the current context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic, retrieval
- 检索关键词命中：episodic memory, memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
We present Mem-$π$, a framework for adaptive memory in large language model (LLM) agents, where useful guidance is generated on demand rather than retrieved from external memory stores. Existing memory-augmented agents typically rely on similarity-based retrieval from episodic memory banks or skill libraries, returning static entries that often misalign with the current context. In contrast, Mem-$π$ uses a dedicated language or vision-language model with its own parameters, separate from the downstream agent, to generate context-specific guidance for complex tasks. Conditioned on the current agent context, the model jointly decides when to produce guidance and what guidance to produce. We train it with a decision-content decoupled reinforcement learning (RL) objective, enabling it to abstain when generation would not help and otherwise produce concise, useful guidance. Across diverse agentic benchmarks spanning web navigation, terminal-based tool use, and text-based embodied interaction, Mem-$π$ consistently outperforms retrieval-based and prior RL-optimized memory baselines, achieving over 30% relative improvement on web navigation tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
