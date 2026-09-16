# LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.14138v1
- Published: 2026-09-12
- Updated: 2026-09-12
- Authors: Siddharth Sharma, Nilesh Prasad Pandey, Onat Gungor, Tajana Rosing
- Tags: agent, retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2609.14138v1

## One-Sentence Summary
As LLM agents become integrated into increasingly complex workflows, they must continually acquire new capabilities while retaining competence on previously learned tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As LLM agents become integrated into increasingly complex workflows, they must continually acquire new capabilities while retaining competence on previously learned tasks.

进一步看，论文的核心做法或实验重点可以概括为：Lifelong agents address this through experience replay, injecting past interactions into the prompt to leverage prior experience during inference.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
As LLM agents become integrated into increasingly complex workflows, they must continually acquire new capabilities while retaining competence on previously learned tasks. Lifelong agents address this through experience replay, injecting past interactions into the prompt to leverage prior experience during inference. However, replay is not free: every replayed trajectory competes with retrieval, reasoning, tool use, and verification for the same limited prompt and compute budget, making effective resource allocation essential. Existing approaches allocate these resources using fixed replay policies, regardless of whether replay is beneficial for the current task. We identify this as inference-time memory allocation, a distinct problem class for lifelong agents, and introduce LIMBO: the first online framework to our knowledge that treats memory as a controllable inference-time resource and jointly optimizes memory strategy and inference budget for each incoming task. Unlike prior approaches that fix the replay policy or require model weights, teacher supervision, or offline retraining, LIMBO learns this allocation online in a single pass, explicitly balancing task performance and inference cost without modifying the underlying agent. Across three LLM backbones on LifelongAgentBench, LIMBO achieves better cost-accuracy tradeoffs than state-of-the-art memory-augmented baselines and nearly matches all strongest such baselines at up to ~83% lower inference cost (~53% on average). LIMBO adapts its policy across models and environments without retraining, demonstrating that effective allocation can be learned online rather than manually specified.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
