# Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.02812v1
- Published: 2026-06-01
- Updated: 2026-06-01
- Authors: Sihang Zeng, Matthew Thompson, Ruth Etzioni, Meliha Yetisgen
- Tags: agent, context, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.02812v1

## One-Sentence Summary
Modeling patient trajectories from longitudinal electronic health records (EHRs) requires reasoning over sparse, noisy, and long-context multimodal sequences.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modeling patient trajectories from longitudinal electronic health records (EHRs) requires reasoning over sparse, noisy, and long-context multimodal sequences.

进一步看，论文的核心做法或实验重点可以概括为：Existing LLM-based multi-agent systems address context length but process patients in isolation, failing to mirror how clinicians leverage accumulated experience from similar prior cases.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Modeling patient trajectories from longitudinal electronic health records (EHRs) requires reasoning over sparse, noisy, and long-context multimodal sequences. Existing LLM-based multi-agent systems address context length but process patients in isolation, failing to mirror how clinicians leverage accumulated experience from similar prior cases. We present Traj-Evolve, a self-evolving multi-agent system with two complementary evolving mechanisms. First, an Experience Pool (ExPool) acts as a non-parametric memory, indexing rejection-sampled reasoning traces to retrieve similar patients as few-shot contexts. Second, multi-agent reinforcement learning (MARL) via reward-ranked fine-tuning parametrically optimizes inter-agent and agent-memory collaboration. A leave-one-out cross-retrieval strategy unifies the two, aligning training- and inference-time behavior under retrieval augmentation. On a lung cancer prediction task utilizing up to five years of multimodal EHRs, Traj-Evolve outperforms 9 strong baselines on the overall population and a challenging never-smoker population. Analysis of the evolving dynamics highlights three key findings: (1) expanding the ExPool shifts optimal retrieval from diverse to specific samples; (2) under MARL, the manager agent's prediction loss converges quickly while the worker agents' temporal reasoning continues to benefit from more verified patients; and (3) the two mechanisms are complementary on the predicted risk, where ExPool improves specificity while MARL improves sensitivity.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
