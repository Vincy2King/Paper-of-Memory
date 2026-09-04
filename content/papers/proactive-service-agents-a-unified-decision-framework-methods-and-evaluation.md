# Proactive Service Agents: A Unified Decision Framework, Methods, and Evaluation

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.03727v1
- Published: 2026-09-03
- Updated: 2026-09-03
- Authors: Yan Tang, Tingyu Cao, Yuanbo Tang, Huaze Tang, Keer Hu
- Tags: agent, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.03727v1

## One-Sentence Summary
Large language model agents can plan, invoke tools, and modify external states, yet most systems still take an explicit user instruction as a fixed starting point.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents can plan, invoke tools, and modify external states, yet most systems still take an explicit user instruction as a fixed starting point.

进一步看，论文的核心做法或实验重点可以概括为：Proactive service moves the decision upstream: an agent must infer service opportunities from incomplete environmental and user signals, choose among remaining silent, asking, assisting, and acting, and account for...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model agents can plan, invoke tools, and modify external states, yet most systems still take an explicit user instruction as a fixed starting point. Proactive service moves the decision upstream: an agent must infer service opportunities from incomplete environmental and user signals, choose among remaining silent, asking, assisting, and acting, and account for interruption, misunderstanding, overreach, and privacy costs. This survey gives an operational definition centered on initiative and formulates the problem as a partially observable sequential decision process constrained by authorization and risk. The formulation represents timing, content, and delivery within one structured action, while making explicit the option value of waiting, the decision value of questions, and feedback-induced state changes. On this basis, we organize existing methods along one decision pipeline (state and need estimation, intervention gating, action construction, and feedback adaptation) and describe prescribed, predictive, model based, and return optimizing mechanisms as nonexclusive policy-construction components. We further normalize decision units and three-axis evidence descriptors across streaming dialogue, screen, video, software-engineering, and human-agent collaboration resources, and formalize metrics for triggering, timing, calibration, user burden, safety, and policy value. The synthesis shows why offline classification performance alone does not predict deployment benefit and why long-term memory is not a defining condition of proactivity. Reliable proactive service instead requires calibrated incremental intervention value, verifiable authorization, recoverable execution, and counterfactual evidence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
