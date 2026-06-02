# CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.00756v1
- Published: 2026-05-30
- Updated: 2026-05-30
- Authors: Yannan Wang, Longli Yang, Zhen Liu, Abhishek Kumar, Carsten Maple
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.00756v1

## One-Sentence Summary
Deploying lightweight Large Language Model (LLM) agents on edge servers can reduce latency and move agentic services closer to users, but resource-constrained edge models often...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deploying lightweight Large Language Model (LLM) agents on edge servers can reduce latency and move agentic services closer to users, but resource-constrained edge models often struggle with long-horizon tasks that...

进一步看，论文的核心做法或实验重点可以概括为：Fine-tuning edge models after deployment is costly and difficult to scale across heterogeneous nodes, while purely local memory leaves agents with isolated experience and growing prompt context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Deploying lightweight Large Language Model (LLM) agents on edge servers can reduce latency and move agentic services closer to users, but resource-constrained edge models often struggle with long-horizon tasks that require persistent memory, subgoal tracking, and reflection. Fine-tuning edge models after deployment is costly and difficult to scale across heterogeneous nodes, while purely local memory leaves agents with isolated experience and growing prompt context. We propose \textsc{CoMIC}, a parameter-update-free cloud-edge framework for Collaborative Memory and Insights Circulation. \textsc{CoMIC} follows a \textit{Centralized Reflection, Decentralized Execution} design: edge agents execute locally using subgoal-oriented hierarchical memory and selective re-expansion of relevant histories, while a cloud-side LLM critic asynchronously evaluates completed trajectories, filters reusable experience, and aggregates cross-agent guidance keyed by semantic subgoal identifiers. Across five long-horizon agent tasks spanning symbolic planning and text interaction, \textsc{CoMIC} improves progress rate and action grounding for weak edge agents and yields task-dependent success-rate gains without updating model parameters.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
