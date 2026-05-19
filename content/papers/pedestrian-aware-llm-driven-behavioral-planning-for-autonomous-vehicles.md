# Pedestrian-Aware LLM-Driven Behavioral Planning for Autonomous Vehicles

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.16858v1
- Published: 2026-05-16
- Updated: 2026-05-16
- Authors: Aidana Baimbetova, Haruki Yonekura, Hamada Rizk, Hirozumi Yamaguchi
- Tags: agent, episodic
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2605.16858v1

## One-Sentence Summary
Autonomous Vehicles (AVs) must make reliable decisions in dense urban environments where pedestrian behavior is variable, sometimes abnormal, and often unseen during training.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Autonomous Vehicles (AVs) must make reliable decisions in dense urban environments where pedestrian behavior is variable, sometimes abnormal, and often unseen during training.

进一步看，论文的核心做法或实验重点可以概括为：Reinforcement learning (RL)-based AV control systems perform well in structured traffic but struggle to generalize to unpredictable pedestrian interactions and out-of-distribution scenarios.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic
- 检索关键词命中：episodic memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Autonomous Vehicles (AVs) must make reliable decisions in dense urban environments where pedestrian behavior is variable, sometimes abnormal, and often unseen during training. Reinforcement learning (RL)-based AV control systems perform well in structured traffic but struggle to generalize to unpredictable pedestrian interactions and out-of-distribution scenarios. Their reliance on handcrafted rewards and opaque decisions further limits their suitability for safety-critical, pedestrian-rich environments. To address these limitations, we introduce a Large Language Model (LLM)-based decision-making framework for pedestrian-aware behavioral planning. The system converts structured scene observations into natural-language reasoning prompts, enabling the LLM to infer pedestrian intent, anticipate risk, and generate cautious tactical driving decisions. These decisions are executed by a motion planner that ensures smooth, kinematically feasible control. We evaluate the framework in SUMO across multiple pedestrian-interaction scenarios, including unexpected jaywalking, turn-back crossing, hesitation, and bidirectional crossing. In zero-shot evaluation, the LLM-based agent achieves a 68% collision-free success rate, substantially outperforming deep RL baselines (17.7%). With few-shot episodic memory in a single-pedestrian scenario, performance increases to 96.0%, exceeding a custom DQN controller (82.0%). Cross-behavior evaluation further shows that memory derived from turn-back interactions transfers to unseen hesitation and bidirectional crossing scenarios, achieving 82.0% and 90.0% success, respectively. The system consistently initiates earlier responses, maintains wider safety buffers, and produces interpretable, human-aligned decisions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
