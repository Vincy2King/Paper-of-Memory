# R-APS: Compositional Reasoning and In-Context Meta-Learning for Constrained Design via Reflective Adversarial Pareto Search

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04823v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: João Pedro Gandarela, Thiago Rios, Stefan Menzel, André Freitas
- Tags: agent, context
- Categories: cs.AI, cs.CL, cs.MA
- URL: http://arxiv.org/abs/2606.04823v1

## One-Sentence Summary
Large language models (LLMs) are fluent on open-ended tasks, yet in agentic settings, where a system must plan, use tools, and act over extended horizons, fluency does not...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) are fluent on open-ended tasks, yet in agentic settings, where a system must plan, use tools, and act over extended horizons, fluency does not ensure reliable delivery.

进一步看，论文的核心做法或实验重点可以概括为：We trace this gap to three coupled structural failures: errors propagate without localization, worst-case perturbations go unevaluated, and accumulated knowledge is never invalidated.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL, cs.MA

## Abstract Snapshot
Large language models (LLMs) are fluent on open-ended tasks, yet in agentic settings, where a system must plan, use tools, and act over extended horizons, fluency does not ensure reliable delivery. We trace this gap to three coupled structural failures: errors propagate without localization, worst-case perturbations go unevaluated, and accumulated knowledge is never invalidated. We argue these share a root cause: abductive, counterfactual, meta-inductive, corrective, and inductive reasoning pull a shared context in incompatible directions. We introduce Reflective Adversarial Pareto Search (R-APS), to our knowledge the first method addressing all three failures jointly via reasoning-mode decomposition, allocating each reasoning mode its own context and orchestrating interaction across three timescales: staged compositional reasoning with a typed validation critic (failure localization), sensitivity-guided counterfactual stress-testing as a first-class Pareto objective (robustness), and meta-inductive rule extraction with explicit invalidation (persistent memory). R-APS requires no fine-tuning and operates on a frozen LLM purely via structured protocol design. We evaluate on planar mechanism synthesis (robotics, prosthetics, mechanical design), with every candidate checked by a kinematic solver. On 32 target trajectories, R-APS delivers robustness certificates 3.5x tighter than uniform-perturbation baselines, 46% faster iterations-to-first-admission, and 2.1x Chamfer-distance reduction over Enum+GA while jointly controlling bar-count and worst-case robustness. Small 4B reasoning-specialized models prove competitive with general-purpose 70B backbones inside the protocol, suggesting structured protocols can partially offset model scale.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
