# Towards Security-Auditable LLM Agents: A Unified Graph Representation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.06812v1
- Published: 2026-05-07
- Updated: 2026-05-07
- Authors: Chaofan Li, Lyuye Zhang, Jintao Zhai, Siyue Feng, Xichun Yang, Huahao Wang, Shihan Dou, Yu Ji, Yutao Hu, Yueming Wu, Yang Liu, Deqing Zou
- Tags: agent, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.06812v1

## One-Sentence Summary
LLM-based agentic systems are rapidly evolving to perform complex autonomous tasks through dynamic tool invocation, stateful memory management, and multi-agent collaboration.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based agentic systems are rapidly evolving to perform complex autonomous tasks through dynamic tool invocation, stateful memory management, and multi-agent collaboration.

进一步看，论文的核心做法或实验重点可以概括为：However, this semantics-driven execution paradigm creates a severe semantic gap between low-level physical events and high-level execution intent, making post-hoc security auditing fundamentally difficult.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM-based agentic systems are rapidly evolving to perform complex autonomous tasks through dynamic tool invocation, stateful memory management, and multi-agent collaboration. However, this semantics-driven execution paradigm creates a severe semantic gap between low-level physical events and high-level execution intent, making post-hoc security auditing fundamentally difficult. Existing representation mechanisms, including static SBOMs and runtime logs, provide only fragmented evidence and fail to capture cognitive-state evolution, capability bindings, persistent memory contamination, and cascading risk propagation across interacting agents. To bridge this gap, we propose Agent-BOM, a unified structural representation for agent security auditing. Agent-BOM models an agentic system as a hierarchical attributed directed graph that separates static capability bases, such as models, tools, and long-term memory, from dynamic runtime semantic states, such as goals, reasoning trajectories, and actions. These layers are connected through semantic edges and security attributes, transforming fragmented execution traces into queryable audit paths. Building on Agent-BOM, we develop a graph-query-based paradigm for path-level risk assessment and instantiate it with the OWASP Agentic Top 10. We further implement an auditing plugin in the OpenClaw environment to construct Agent-BOM from live executions. Evaluation on representative real-world agentic attack scenarios shows that Agent-BOM can reconstruct stealthy attack chains, including cross-session memory poisoning and tool misuse, capability supply-chain hijacking and unexpected code execution, multi-agent ecosystem hijacking, and privilege and trust abuse. These results demonstrate that Agent-BOM provides a unified and auditable foundation for root-cause analysis and security adjudication in complex agentic ecosystems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
