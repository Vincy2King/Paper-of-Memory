# Towards Faithful Simulation of Human Shopping Behavior

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.20707v1
- Published: 2026-08-21
- Updated: 2026-08-21
- Authors: Jiakai Tang, Yan Mi, Jing Yu, Yang Zhang, See-Kiong Ng, Qi Cao, Fei Sun, Xu Chen, Wen Chen, Jian Wu, Han Zhu, Bo Zheng
- Tags: agent, benchmark, context, episodic
- Categories: cs.IR
- URL: http://arxiv.org/abs/2608.20707v1

## One-Sentence Summary
Simulating realistic user shopping behavior underpins offline evaluation and reinforcement learning in e-commerce scenarios.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Simulating realistic user shopping behavior underpins offline evaluation and reinforcement learning in e-commerce scenarios.

进一步看，论文的核心做法或实验重点可以概括为：While recent LLM- and VLM-based simulators have made encouraging progress, reproducing a real browsing session remains difficult for two reasons. (i) Memory Challenge: a shopping session spans dozens of pages, yet...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, episodic
- 检索关键词命中：episodic memory, working memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Simulating realistic user shopping behavior underpins offline evaluation and reinforcement learning in e-commerce scenarios. While recent LLM- and VLM-based simulators have made encouraging progress, reproducing a real browsing session remains difficult for two reasons. (i) Memory Challenge: a shopping session spans dozens of pages, yet existing agents either discard long-range observation histories, losing the evolving user state, or naively concatenate them, overwhelming the context window and even degrading simulation quality. (ii) Optimization Challenge: current user simulators are typically supervised to match each logged action via imitation or step-level rewards; the resulting sessions often display unrealistic patterns, such as over-exploration or excessive passivity, which per-step supervision can neither detect nor correct. To address the above challenges, we present RecVerse, a GUI-grounded simulation agent that perceives pages through screenshots and produces faithful multi-turn trajectories. For the memory challenge, RecVerse adopts a cognitive-inspired hierarchical memory: Working Memory for short-term focus, Episodic Memory for in-session traces, and Preference Memory for high-level intent, with memory updates treated as actions so that the agent adaptively learns when and what to memorize. For the optimization challenge, RecVerse is optimized with a trajectory-level RL objective that scores entire sessions, aligning both macro-level action-type distributions and micro-level shopping intent with real users. We further release USB (User Simulation Benchmark), an interactive e-commerce GUI trajectory dataset for multi-turn user simulation. Experiments show that RecVerse significantly outperforms existing baselines in both behavioral fidelity and intent consistency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
