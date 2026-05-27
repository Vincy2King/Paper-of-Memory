# Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.26256v1
- Published: 2026-05-25
- Updated: 2026-05-25
- Authors: Jeongeun Lee, Chanyoung Park, Dongha Lee
- Tags: agent, context, episodic, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.26256v1

## One-Sentence Summary
Multimodal large language model (MLLM)-based embodied agents have shown strong potential for solving complex tasks in physical environments.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal large language model (MLLM)-based embodied agents have shown strong potential for solving complex tasks in physical environments.

进一步看，论文的核心做法或实验重点可以概括为：However, personalized assistance requires more than following generic instruction or recognizing object categories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, long-term
- 检索关键词命中：episodic memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Multimodal large language model (MLLM)-based embodied agents have shown strong potential for solving complex tasks in physical environments. However, personalized assistance requires more than following generic instruction or recognizing object categories. In real-world scenarios, the intended target is often specified only implicitly through prior interactions, requiring agents to leverage personalized context accumulated over time. In this work, we propose POLAR, a multiomodal memory-augmented framework for personalized embodied agents over long-term user interactions. POLAR organizes prior interactions into a multimodal knowledge graph that captures semantic memory for personalized context and visual concepts, and episodic memory for embodied experiences such as agent trajectories. To execute embodied tasks, POLAR retrieves relevant memories to interpret the current request and guide task execution. We evaluate POLAR across multiple MLLM backbones and diverse evaluation scenarios to study the role of memory in long-term personalization. Results show that the proposed memory mechanism consistently improves performance by enabling more effective use of information accumulated over prior interactions. The gains are especially pronounced when the agents are required to reason across multiple interactions, perform multi-hop inference, or tracking updates in user-specific context over time.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
