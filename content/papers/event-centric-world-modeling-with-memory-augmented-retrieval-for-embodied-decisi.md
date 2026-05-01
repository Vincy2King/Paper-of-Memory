# Event-Centric World Modeling with Memory-Augmented Retrieval for Embodied Decision-Making

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.07392v2
- Published: 2026-04-08
- Updated: 2026-04-30
- Authors: Zhaowen Fan, Rongchao Zhang
- Tags: agent, retrieval
- Categories: cs.LG, cs.IR, cs.RO
- URL: http://arxiv.org/abs/2604.07392v2

## One-Sentence Summary
Autonomous agents operating in dynamic and safety-critical environments require decision-making frameworks that are both computationally efficient and physically grounded.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Autonomous agents operating in dynamic and safety-critical environments require decision-making frameworks that are both computationally efficient and physically grounded.

进一步看，论文的核心做法或实验重点可以概括为：However, many existing approaches rely on end-to-end learning, which often lacks interpretability and explicit mechanisms for ensuring consistency with physical constraints.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.IR, cs.RO

## Abstract Snapshot
Autonomous agents operating in dynamic and safety-critical environments require decision-making frameworks that are both computationally efficient and physically grounded. However, many existing approaches rely on end-to-end learning, which often lacks interpretability and explicit mechanisms for ensuring consistency with physical constraints. In this work, we propose an event-centric world modeling framework with memory-augmented retrieval for embodied decision-making. The framework represents the environment as a structured set of semantic events, which are encoded into a permutation-invariant latent representation. Decision-making is performed via retrieval over a knowledge bank of prior experiences, where each entry associates an event representation with a corresponding maneuver. The final action is computed as a weighted combination of retrieved solutions, providing a transparent link between decision and stored experiences. The proposed design enables structured abstraction of dynamic environments and supports interpretable decision-making through case-based reasoning. In addition, incorporating physics-informed knowledge into the retrieval process encourages the selection of maneuvers that are consistent with observed system dynamics. Experimental evaluation in UAV flight scenarios demonstrates that the framework operates within real-time control constraints while maintaining interpretable and consistent behavior.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
