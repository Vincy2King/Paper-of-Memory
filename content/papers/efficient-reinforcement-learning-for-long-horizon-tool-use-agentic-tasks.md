# Efficient Reinforcement Learning for Long-Horizon Tool-Use Agentic Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.10357v1
- Published: 2026-08-11
- Updated: 2026-08-11
- Authors: Zelei Cheng, Amritansh Mishra, Sambit Sahu, William Campbell
- Tags: agent, benchmark, context
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2608.10357v1

## One-Sentence Summary
Long-horizon tool-using agents must reason over user goals, domain policies, tool calls, simulator state, and delayed verifiable rewards.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon tool-using agents must reason over user goals, domain policies, tool calls, simulator state, and delayed verifiable rewards.

进一步看，论文的核心做法或实验重点可以概括为：Reinforcement learning (RL) is a natural fit for this setting, but multi-turn on-policy rollouts create long contexts, while model-specific attention layers may require custom masks and learned sink normalization.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Long-horizon tool-using agents must reason over user goals, domain policies, tool calls, simulator state, and delayed verifiable rewards. Reinforcement learning (RL) is a natural fit for this setting, but multi-turn on-policy rollouts create long contexts, while model-specific attention layers may require custom masks and learned sink normalization. We present SINKFLEX-RL, a modular training system for RL in dual-control tool-use environments. The system combines a Gymnasium-compatible environment wrapper, a VERL-style rollout dataflow, group-relative policy optimization without a separate value model, and a sink-aware FlexAttention path designed to preserve model-specific sink scaling under causal and sliding-window masks. In a preliminary Tau2Bench retail run, validation reward (mean@1) rises from 0.25 early in training to $0.44$ later in the observed training window, while training-score and trajectory-reward proxies also trend upward. In a fixed-configuration memory benchmark, the optimized attention path reduces peak VRAM from 28.06GB to 22.52GB at 4096 tokens, a $19.7\%$ reduction, and runs the measured 8192-token configuration using $25.53$~GB where the eager baseline runs out of memory. These results illustrate the value of integrating environment interfaces, RL dataflow, and attention-kernel design for memory-feasible long-horizon agent training.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
