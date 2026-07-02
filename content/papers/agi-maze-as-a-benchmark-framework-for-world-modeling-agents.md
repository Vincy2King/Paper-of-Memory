# AGI Maze as a Benchmark Framework for World-Modeling Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.00627v1
- Published: 2026-07-01
- Updated: 2026-07-01
- Authors: Alexey Potapov
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.00627v1

## One-Sentence Summary
Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably produce persistent, manipulable...

进一步看，论文的核心做法或实验重点可以概括为：Many tasks that look like "reasoning" in text become substantially harder once the environment is partially observable, stateful, and requires memory and structured hypotheses about hidden state.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably produce persistent, manipulable representations of an external world. Many tasks that look like "reasoning" in text become substantially harder once the environment is partially observable, stateful, and requires memory and structured hypotheses about hidden state. AGI Maze is a lightweight framework for building such environments without requiring high-dimensional sensory inputs. It provides a family of grid-based maze tasks with a clean API and multiple difficulty regimes. The goal is to create benchmarks where agents must learn and use world state representations, not just infer a local rule over readily provided observations. We provide an initial evaluation of several vanilla LLMs on simple mazes showing that they fail to represent mazes internally at LLM inference time. We also introduce a baseline agent, which is allowed to use its message history as a working memory to construct descriptions of observations at agentic runtime. Although this can improve performance, it is still insufficient for an LLM agent to reliably solve even small mazes within a step budget that is more than enough for humans.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
