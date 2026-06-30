# Self-Evolving World Models for LLM Agent Planning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.30639v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, Yang Deng
- Tags: agent, context, episodic, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.30639v1

## One-Sentence Summary
World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution.

进一步看，论文的核心做法或实验重点可以概括为：However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits real action transitions through retrieval-based simulation; (ii) Semantic Memory, which extracts persistent heuristic rules from prediction-observation mismatches; and (iii) Selective Foresight, which filters low-confidence predictions before integrating them into agent reasoning context. We evaluate WorldEvolver on ALFWorld and ScienceWorld, measuring world model prediction accuracy on Word2World and downstream agent success rate on AgentBoard. Extensive experiments show that WorldEvolver achieves the highest prediction accuracy across three backbones and leads other world model baselines on downstream agent success rate, demonstrating that test-time memory revision enhances both predictive fidelity and planning performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
