# Coding Agent Memory Post-training: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via Reinforcement Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34422v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Lirui Luo, Kelong Mao, Heming Xia, Rongqing Li, Xinwei Yang, Luyu Chen, Kieran Wong, Yudong Guo, Xinrui Wang, Jiayin Zhu, Simiu Gu, Sulong Xu, Cong Fang
- Tags: agent, context
- Categories: cs.LG, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.34422v1

## One-Sentence Summary
Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context.

进一步看，论文的核心做法或实验重点可以概括为：Recent work has begun to use reinforcement learning to make memory control part of the policy, often relying on predefined memory tools within domain-specific training environments of relatively short horizons.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG, cs.AI, cs.CL

## Abstract Snapshot
Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. Recent work has begun to use reinforcement learning to make memory control part of the policy, often relying on predefined memory tools within domain-specific training environments of relatively short horizons. This setup ties learned memory behavior to environment-specific interfaces that lie outside the base model's pre-training and must be learned from scratch, so even after post-training, agents struggle to use memory in long-horizon tasks. To address these limitations, we introduce Coding Agent Memory Gym (CAMG), a suite of long-horizon agentic-RL environments spanning Shop, Coding, DeepResearch, and AutoResearch. Alongside each environment's native task interface, CAMG provides executable shell access and an episode-persistent workspace, enabling agents to create, revise, search, and reuse files as memory throughout an episode. We also introduce CAMG-RL, which trains a single policy jointly across all four environments with fully asynchronous PPO, learning this file-based memory behavior directly from downstream task reward, and we train CAMG-RL-4B and CAMG-RL-9B from Qwen3.5 models of matching size. On SWE-bench Verified and MLE-bench Lite, CAMG-RL-4B and CAMG-RL-9B are competitive with Qwen3.5-35B-A3B and Qwen3.5-122B-A10B, respectively.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
