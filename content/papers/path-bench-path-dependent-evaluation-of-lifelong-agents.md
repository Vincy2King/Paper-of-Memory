# PATH-Bench: Path-Dependent Evaluation of Lifelong Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01149v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Xidong Yang, Xingyi Zhang, Wenhao Li, Wenyan Liu, Junjie Sheng, Yun Hua, Wei Yin, Tao Fang, Chuyun Shen, Xiangfeng Wang
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.01149v1

## One-Sentence Summary
Lifelong LLM agents increasingly adapt through external learning states that store past interactions as retrievable memories or reusable skills, yet existing benchmarks rarely...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Lifelong LLM agents increasingly adapt through external learning states that store past interactions as retrievable memories or reusable skills, yet existing benchmarks rarely account for how the path of accumulated...

进一步看，论文的核心做法或实验重点可以概括为：In this work, we establish PATH-Bench, a benchmark for path-dependent evaluation of lifelong agents.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Lifelong LLM agents increasingly adapt through external learning states that store past interactions as retrievable memories or reusable skills, yet existing benchmarks rarely account for how the path of accumulated experience shapes what agents transfer and retain. In this work, we establish PATH-Bench, a benchmark for path-dependent evaluation of lifelong agents. PATH-Bench estimates directed task relationships via multi-model in-context learning, constructs probe-centered sequences with controlled helpful and interfering histories, and repeatedly evaluates probe tasks to measure average performance, forward transfer, backward transfer, and forgetting. We evaluate eight representative agents on single-turn code generation and multi-turn tool-use tasks under positive- and negative-dominant histories. Benchmark results show that experience utility depends jointly on how experience is represented and on the task's interaction structure, that strong transfer does not ensure retention, and that later experience can reshape gains acquired earlier in the learning path. Based on these findings, we propose Selective Experience Use (SEU), an agent harness that regulates how path-accumulated experience influences each new task, admitting helpful items while filtering out potential interference. SEU consistently reduces forgetting while improving forward transfer in the majority of settings. The PATH-Bench provides both a controlled evaluation framework and actionable guidance for designing more selective and robust lifelong agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
