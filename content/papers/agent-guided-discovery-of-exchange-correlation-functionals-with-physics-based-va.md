# Agent-Guided Discovery of Exchange-Correlation Functionals with Physics-based Validation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.13329v1
- Published: 2026-11-09
- Updated: 2026-11-09
- Authors: Achuth Chandrasekhar, Amir Barati Farimani
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.13329v1

## One-Sentence Summary
Accurate, compact exchange--correlation functionals are central to predictive density functional theory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Accurate, compact exchange--correlation functionals are central to predictive density functional theory.

进一步看，论文的核心做法或实验重点可以概括为：Symbolic search and language-model agents can propose new functional forms, but it remains unclear whether their gains survive self-consistency and external evaluation, whether the new terms carry physical content,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Accurate, compact exchange--correlation functionals are central to predictive density functional theory. Symbolic search and language-model agents can propose new functional forms, but it remains unclear whether their gains survive self-consistency and external evaluation, whether the new terms carry physical content, whether agents outperform evolutionary search, and how language-model backbones compare. We connect frontier LLM agents to a GPU evaluator through the Model Context Protocol, with training-only fitting, persistent memory, and self-consistent and external evaluation. Opus-5.5 agents passed the screening gate with about 40-fold fewer tokens than Codex (GPT-6-Astra) agents and found a candidate with lower validation and held-out errors; only this candidate advanced to self-consistent evaluation. The resulting 13-parameter functional, O159, multiplies same-spin correlation by a smooth density window. Refitted controls favor a window that scales the entire same-spin factor, reducing it by 15--30\% at its peak, and that acts on reaction energies mainly in near-iso-orbital regions; against a refitted no-window control, it lowers heavy-atom total-energy errors on GSCDB137 by 29\%. With about 400 fits each, SyFES evolution did not improve on its GAS22 seed, whereas the agents found forms 0.10--0.13 \kcal\ lower in validation error by adding an explicit density scale. Self-consistent O159 lowers the held-out MGCDB84 test error of $ω$B97M-V by 11.7\%, and its mean normalized error ratio on 36 GSCDB137 datasets (1.139) is comparable to $ω$B97M-V (1.144) and below GAS22 (1.190). Frontier-LLM agents thus produced O159, a compact functional whose improvement over $ω$B97M-V survives self-consistent, physics-based validation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
