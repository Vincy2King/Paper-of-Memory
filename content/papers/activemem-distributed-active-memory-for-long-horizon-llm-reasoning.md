# ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.10532v1
- Published: 2026-06-09
- Updated: 2026-06-09
- Authors: Yunhan Jiang, Wenbin Duan, Shasha Guo, Liang Pang, Xiaoqian Sun, Huawei Shen
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.10532v1

## One-Sentence Summary
Memory is essential for enabling large language model (LLM) agents to handle long-horizon reasoning tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is essential for enabling large language model (LLM) agents to handle long-horizon reasoning tasks.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory mechanisms are largely centralized, typically organizing retrieved information and interaction history within a single model context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory is essential for enabling large language model (LLM) agents to handle long-horizon reasoning tasks. Existing memory mechanisms are largely centralized, typically organizing retrieved information and interaction history within a single model context. This design imposes a fundamental trade-off: scaling reasoning trajectories risks context overload, whereas aggressive content pruning may result in irreversible information loss. Seeking a better trade-off, we draw inspiration from human cognitive systems, especially the functional complementarity between the prefrontal cortex (executive control) and the hippocampus (memory management), suggesting that such a trade-off need not be inherent, but may instead stem from centralized memory organization. To this end, we propose ActiveMem, a heterogeneous framework that decouples agent memory from the core reasoning process. Specifically, a high-level Planner utilizes distilled semantic gists to execute reasoning, while a lightweight, distributed memory system operates in parallel to actively accumulate and consolidate these gists throughout the task. Experiments on BrowseComp-Plus and GAIA show that ActiveMem achieves state-of-the-art accuracy with significantly reduced overhead, demonstrating the effectiveness of distributed active memory for long-horizon reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
