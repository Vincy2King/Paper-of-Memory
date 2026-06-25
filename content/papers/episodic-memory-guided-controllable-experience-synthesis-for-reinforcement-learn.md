# Episodic Memory-Guided Controllable Experience Synthesis for Reinforcement Learning

- Source: OpenReview
- Venue: ICML 2026 regular
- Paper ID: openreview:mjYcL7esQO
- Published: 2026-04-30
- Updated: 2026-06-24
- Authors: Xiao Ma, Tian Li, Wu-Jun Li
- Tags: episodic
- Categories: ICML.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=mjYcL7esQO

## One-Sentence Summary
In real-world scenarios, data collection for reinforcement learning (RL) is often constrained by safety concerns and high costs, resulting in limited data availability.

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICML 2026 regular` 这个 venue 相关。

从摘要来看，作者主要关注的是：In real-world scenarios, data collection for reinforcement learning (RL) is often constrained by safety concerns and high costs, resulting in limited data availability.

进一步看，论文的核心做法或实验重点可以概括为：Diffusion models (DMs) have recently demonstrated remarkable capabilities in capturing complex distributions, making data augmentation a promising approach.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICML 2026 regular
- 高亮主题命中：episodic
- 检索关键词命中：episodic memory
- 来源分类信息：ICML.cc/2026/Conference/-/Submission

## Abstract Snapshot
In real-world scenarios, data collection for reinforcement learning (RL) is often constrained by safety concerns and high costs, resulting in limited data availability. Diffusion models (DMs) have recently demonstrated remarkable capabilities in capturing complex distributions, making data augmentation a promising approach. However, existing DM-based data augmentation methods still suffer from the limited quality of synthesized data for downstream RL tasks. To overcome this limitation, we propose a novel method called episodic memory-guided controllable experience synthesizer (EMCES). EMCES incorporates an episodic memory-based controllable DM with informative yet concise conditions constructed by episodic memory (EM). To guide the synthesis toward high-quality data, we propose an EM-prioritized condition sampling strategy that leverages EM-based temporal-difference errors to focus generation on data most helpful for RL. Furthermore, we introduce a hashing-based state representation for EM to improve its efficiency and further boost the quality of synthetic data. To the best of our knowledge, EMCES is the first work to incorporate EM into controllable DMs and to leverage EM for guiding data synthesis in RL. Experimental results across multiple environments demonstrate that EMCES significantly improves the quality of the synthetic data, thereby improving the performance of several state-of-the-art RL algorithms. In particular, the hashing-based state representation can reduce storage cost by about 8000-fold and reduce time cost by 25.5-fold, without degrading the normalized score.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
