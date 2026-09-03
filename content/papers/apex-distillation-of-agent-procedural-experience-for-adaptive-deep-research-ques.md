# APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.02253v1
- Published: 2026-09-02
- Updated: 2026-09-02
- Authors: Jie Ding, Rui Sun, Xinyuan Zhang, Zeyu Zhang, Xin Liu
- Tags: agent, benchmark
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.02253v1

## One-Sentence Summary
Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning.

进一步看，论文的核心做法或实验重点可以概括为：Learning from prior experience is crucial for continual improvement, yet existing methods either retrieve verbose task-specific traces that burden decision-making, or distill procedural skills that remain decoupled...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning. Learning from prior experience is crucial for continual improvement, yet existing methods either retrieve verbose task-specific traces that burden decision-making, or distill procedural skills that remain decoupled from downstream policy adaptation. We propose APEx, a hierarchical experience utilization framework that organizes interaction history into instance-level trajectory memories and category-level procedural skills, and couples them through a closed-loop architecture of Executor, Distiller, and Planner. The three modules are optimized via a three-stage alternating GRPO training paradigm, enabling reward-guided skill distillation rather than fixed-prompt generation. At test time, distilled skills serve as procedural priors for online Planner adaptation through skill-guided test-time reinforcement learning, allowing ground-truth-free self-improvement with skill-alignment regularization to prevent policy drift. Experiments on 7 benchmarks demonstrate that APEx achieves state-of-the-art performance, surpassing GPT-5.4 by 14.7 points and the strongest memory-augmented baseline by 3.0 points.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
