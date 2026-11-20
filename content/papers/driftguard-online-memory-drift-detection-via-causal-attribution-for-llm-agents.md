# DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.25583v1
- Published: 2026-11-19
- Updated: 2026-11-19
- Authors: Licheng Pan, Yuzhou Chen, Zhixuan Chu, Yichen Sun, Han Zheng, Zhiyu Wang, Hao Wang, Yan Wang, Bingyu Zhu, Haiwen Hong, Longtao Huang, Kui Ren
- Tags: agent, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.25583v1

## One-Sentence Summary
Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final...

进一步看，论文的核心做法或实验重点可以概括为：In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：persistent memory, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final outcome. In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time. We identify two fundamental challenges. (1) Content-level features are insufficient for causal memory-drift attribution, as perplexity or retrieval relevance alone cannot determine which retrieved memory would change agent behavior if neutralized; (2) Counterfactual attribution is prohibitively expensive for online detection, as it requires replaying downstream agent and tool execution for each candidate memory, exceeding real-time serving budgets. To address these challenges, we propose DriftGuard, a two-stage framework that decouples offline causal supervision from online estimation. Specifically, DriftGuard first constructs causal supervision through repeated paired counterfactual replays, continuing the original and single-memory neutralized trajectory suffixes from a shared pre-action state. The resulting annotations are aggregated by component-wise majority voting into a memory drift score (MDS) that captures action change, attack removal, violation removal, and task recovery. Guided by this supervision, DriftGuard then learns an online risk model that estimates MDS from pre-action information and flags drift-inducing memories via its maximum component risk, without online counterfactual rollouts. Extensive experiments demonstrate that DriftGuard accurately identifies drift-inducing memories and enables efficient online defense. Code is available at https://anonymous.4open.science/r/DriftGuard-7F0B.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
