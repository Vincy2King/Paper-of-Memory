# Self-Review Reinforcement Learning (SRRL) with Cross-Episode Memory and Policy Distillation

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.05541v1
- Published: 2026-07-06
- Updated: 2026-07-06
- Authors: Muhammad Zain Amin, Kibele Sebnem Yildirim
- Tags: benchmark
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2607.05541v1

## One-Sentence Summary
Reinforcement Learning is commonly used to train large language models using environmental feedback.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Reinforcement Learning is commonly used to train large language models using environmental feedback.

进一步看，论文的核心做法或实验重点可以概括为：In applied settings, the environment usually provides sparse or delayed feedback.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：episodic memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Reinforcement Learning is commonly used to train large language models using environmental feedback. In applied settings, the environment usually provides sparse or delayed feedback. This makes it difficult for the model to pinpoint which actions in its reasoning led to success or failure. So, learning effectively from these signals is hard because the model must determine how each failure should inform meaningful behavioral corrections in subsequent iterations. We introduce a training framework, Self-Review Reinforcement Learning, that embeds an explicit self-review step into each RL episode. When a first-pass response fails, the model generates a self-review to identify what went wrong, which conditions an improved second attempt. Unlike inference-time reflection approaches, such as Reflexion, the framework optimizes self-review with policy gradients and internalizes improvements into the base policy via selective distillation, ensuring they persist across future episodes. A cross-episode memory keeps successful self-reviews for reuse when encountering similar tasks in future episodes during training. We evaluate SRRL against a standard RLVR baseline using the GRPO optimizer across two language models, Qwen 3-4B and OLMo-3- 7B, on GSM8K benchmark. SRRL consistently outperforms the RLVR in final reward performance and achieves greater learning efficiency by successfully transforming feedback into behavioral improvement.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
