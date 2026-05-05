# Recurrent Deep Reinforcement Learning for Chemotherapy Control under Partial Observability

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.02552v1
- Published: 2026-05-04
- Updated: 2026-05-04
- Authors: Firas Mohamed Elamine Kiram, Imane Youkana, Rachida Saouli, Gian Antonio Susto, Laid Kahloul
- Tags: benchmark
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2605.02552v1

## One-Sentence Summary
Chemotherapy dose optimization can be formulated as a dynamic treatment regime, requiring sequential decisions under uncertainty that must balance tumor suppression against...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Chemotherapy dose optimization can be formulated as a dynamic treatment regime, requiring sequential decisions under uncertainty that must balance tumor suppression against toxicity.

进一步看，论文的核心做法或实验重点可以概括为：However, most reinforcement learning approaches assume full observability of the patient state, a condition rarely met in clinical practice.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Chemotherapy dose optimization can be formulated as a dynamic treatment regime, requiring sequential decisions under uncertainty that must balance tumor suppression against toxicity. However, most reinforcement learning approaches assume full observability of the patient state, a condition rarely met in clinical practice. We investigate whether memory-augmented policies can improve chemotherapy control under partial observability. To this end, we employ a recurrent TD3-based approach with separate LSTM actor-critic networks and evaluate it on the AhnChemoEnv benchmark from DTR-Bench, considering both off-policy and on-policy recurrent architectures against feed-forward TD3 and Soft Actor-Critic. Pharmacokinetic and pharmacodynamic variability are held fixed to isolate hidden-state uncertainty and observation noise and to avoid confounding effects from inter-patient variability. Across ten random seeds, recurrence yields modest benefit under full observability but substantially stronger and more stable performance under partial observability, with more consistent tumor suppression and improved normal-cell preservation. These findings indicate that memory-based policies are particularly beneficial when clinically relevant state information is incomplete or noisy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
