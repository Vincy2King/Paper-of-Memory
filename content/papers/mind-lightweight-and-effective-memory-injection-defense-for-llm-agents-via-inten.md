# MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.28103v1
- Published: 2026-07-30
- Updated: 2026-07-30
- Authors: Dongyi Liu, Haixing He, Xiaobao Wu, Jia Li
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.28103v1

## One-Sentence Summary
Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure.

进一步看，论文的核心做法或实验重点可以概括为：However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. To address these challenges, we propose Memory Intent-Aware Neural Denoising(MIND), a lightweight defense framework for memory injection attack. Our preliminary analysis reveals that benign and poisoned trajectories exhibit distinguishable relationships between the initial user intent and subsequent behavior. Building on this observation, MIND employs an intent-aware Information Bottleneck(IB) to extract compact intent--behavior representations from the initial intent and turn-level behavior. The IB preserves intent-relevant cross-turn attack signals while filtering task-irrelevant and repetitive information, and a lightweight detector identifies malicious memories from the resulting representations. As such, MIND mitigates information redundancy in multi-turn contexts while avoiding the overhead of repeated LLM auditing. Extensive experiments show that MIND reduces attack success rates while preserving task accuracy and inference efficiency. Notably, on ReAct-StrategyQA, MIND reduces mean ASR-r and ASR-a by 55.4% and 55.3%, respectively, while matching the undefended agent in average accuracy and latency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
