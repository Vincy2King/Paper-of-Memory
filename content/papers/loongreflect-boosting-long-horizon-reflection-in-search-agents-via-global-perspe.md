# LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.11967v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Zhixin Zhang, Xinke Jiang, Zhibang Yang, Weixuan Xu, Guohong Qiu, Xu Chu, Junfeng Zhao, Yasha Wang
- Tags: agent, benchmark, context, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2608.11967v1

## One-Sentence Summary
Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory.

进一步看，论文的核心做法或实验重点可以概括为：A critical capability in such settings is reflection: assessing trajectory progress, identifying missing evidence and unreliable intermediate states, and deciding whether to continue, revise, or abandon the current...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory. A critical capability in such settings is reflection: assessing trajectory progress, identifying missing evidence and unreliable intermediate states, and deciding whether to continue, revise, or abandon the current branch. Learning effective reflection, however, is challenging because reflection is performed locally within the current branch, whereas its utility can only be determined by its contribution to the final trajectory outcome. This local-global mismatch makes outcome-based reinforcement learning provide only local, sparse and delayed supervision for reflective decisions. To solve these, we propose LoongReflect, a training framework that formulates reflection as a memory-control policy. The agent operates over a reversible trajectory tree using explicit reflect and backtrack actions. Reflection consolidates verified facts, missing evidence, and branch-specific risks into working memory, while backtracking removes an unreliable branch from the active context and preserves a concise corrective lesson. To learn this policy, LoongReflect combines two complementary signals through a look-ahead, extragradient-style coordination mechanism. A fast channel distills globally informed reflective behavior from a privileged teacher, with supervision restricted to reflection and backtracking tokens. A slow channel optimizes complete trajectories using outcome-based GRPO, aligning local control decisions with final task success. Experiments on multi-hop retrieval-augmented generation and mathematical reasoning benchmarks demonstrate consistent improvements over outcome-only reinforcement learning and self-distillation baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
