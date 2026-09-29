# MemAgent: Learning to Manage Heterogeneous Memory Providers for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32521v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Yongxian Wei, Yilin Zhao, Runxi Cheng, Xinrui Chen, Chun Yuan, Yaoru Wang, Jiahong Yan, Dian Li
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.32521v1

## One-Sentence Summary
Current agents remain largely stateless across tasks, limiting their ability to continually improve from prior interactions and making memory essential for long-horizon agentic...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Current agents remain largely stateless across tasks, limiting their ability to continually improve from prior interactions and making memory essential for long-horizon agentic behavior.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory methods seek to reuse past experience, but most rely on a single memory representation (e.g., trajectories, reflections, skills, structured knowledge) whose effectiveness varies across task distributions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Current agents remain largely stateless across tasks, limiting their ability to continually improve from prior interactions and making memory essential for long-horizon agentic behavior. Existing memory methods seek to reuse past experience, but most rely on a single memory representation (e.g., trajectories, reflections, skills, structured knowledge) whose effectiveness varies across task distributions. Rethinking this design space, we evaluate 13 memory methods and find that no single method generalizes across benchmarks, revealing the potential of managing heterogeneous memory providers. We formulate agent memory as a routing problem in which a memory agent decides which memory provider to retrieve from, whether to inject short-term memory, and which providers should store the resulting experience. Based on this perspective, we propose MemAgent, featuring a content-aware routing architecture and a training-data synthesis pipeline. The routing architecture combines content-aware probing before retrieval, short-term memory gating during execution, and selective multi-provider storage, while the training pipeline synthesizes phase-specific supervision for routing decisions. Across GAIA, WebWalkerQA, and xBench-DS, MemAgent improves average accuracy by 10.0% and outperforms every individual memory method across all three benchmarks. These gains come with less than 0.3% routing overhead and a 12% reduction in average task steps.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
