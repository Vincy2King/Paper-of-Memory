# Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.21768v1
- Published: 2026-05-20
- Updated: 2026-05-20
- Authors: Sikuan Yan, Ahmed Bahloul, Ercong Nie, Susanna Schwarzmann, Riccardo Trivisonno, Volker Tresp, Yunpu Ma
- Tags: agent, context
- Categories: cs.LG, cs.MA
- URL: http://arxiv.org/abs/2605.21768v1

## One-Sentence Summary
Memory-augmented LLM agents enable interactions that extend beyond finite context windows by storing, updating, and reusing information across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented LLM agents enable interactions that extend beyond finite context windows by storing, updating, and reusing information across sessions.

进一步看，论文的核心做法或实验重点可以概括为：However, training such agents with reinforcement learning in multi-session environments is challenging because memory turns the agent's past actions into part of its future environment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.MA

## Abstract Snapshot
Memory-augmented LLM agents enable interactions that extend beyond finite context windows by storing, updating, and reusing information across sessions. However, training such agents with reinforcement learning in multi-session environments is challenging because memory turns the agent's past actions into part of its future environment. Once different rollouts write, update, or delete different memories, they no longer share the same intermediate memory state, making trajectory-level comparisons fundamentally unfair. This violates a key assumption behind group-relative methods such as GRPO, where rollouts are compared as if they were sampled from the same effective environment. Consequently, trajectory-level rewards provide noisy or biased credit signals for long-horizon memory operations. To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents. Its core algorithm, LoGo-GRPO, combines local and global group-relative optimization. The global objective preserves end-to-end learning from long-horizon trajectory-level rewards, while local rerollouts compare different memory-operation outcomes from the same intermediate memory state, yielding fairer group comparisons and more precise supervision for memory construction. Beyond credit assignment, Memory-R2 jointly optimizes memory formation and memory evolution with a shared-parameter co-learning design, where a fact extractor and a memory manager are instantiated from the same LLM backbone through role-specific prompts. To stabilize multi-step RL over long memory horizons, we adopt a progressive curriculum that increases the training horizon from 8 to 16 to 32 sessions. Together, these components provide an effective training paradigm for memory-augmented LLM agents in long-horizon multi-session settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
