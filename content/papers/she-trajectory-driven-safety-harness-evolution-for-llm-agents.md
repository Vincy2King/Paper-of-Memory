# SHE: Trajectory-driven Safety Harness Evolution for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.09885v1
- Published: 2026-08-10
- Updated: 2026-08-10
- Authors: Wanying Qu, Qinghua Mao, Yu Li, Jiyao Liu, Xin Zhang, Dadi Guo, Yanxu Zhu, Qingyu Liu, Leitao Yuan, Xi Lin, Shanfeng Zhu, Yanwei Fu, Jing Shao, Xia Hu, Dongrui Liu
- Tags: agent, benchmark, context
- Categories: cs.AI, cs.CV
- URL: http://arxiv.org/abs/2608.09885v1

## One-Sentence Summary
The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control.

进一步看，论文的核心做法或实验重点可以概括为：Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：context memory
- 来源分类信息：cs.AI, cs.CV

## Abstract Snapshot
The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. Moreover, coupled functions across harness components obscure safety responsibility attribution, making localized evolution difficult. We propose Safety Harness Evolution (SHE), a framework that learns evolving safe boundaries from rollout trajectories. SHE decomposes the harness into four artifacts with explicit safety responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy, defining clear functional boundaries for localized evolution. Based on this decomposition, SHE introduces an attribution-guided evolution loop that converts trajectory failures into structured diagnoses, learns artifact-specific boundary refinements, and selects evolved harnesses through safety-utility validation. Experiments on Agent-SafetyBench demonstrate that SHE effectively enhances safety through harness evolution, achieving a 3.1x ASR reduction compared with static SafeHarness, while also improving benign utility. The evolved harness further generalizes to unseen risks on the held-out AgentHarm benchmark and transfers across agent models without additional evolution.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
