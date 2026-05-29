# Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2602.01869v3
- Published: 2026-02-02
- Updated: 2026-05-28
- Authors: Qirui Mi, Zhijian Ma, Mengyue Yang, Haoxuan Li, Yisen Wang, Haifeng Zhang, Jun Wang
- Tags: agent, compression, episodic, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2602.01869v3

## One-Sentence Summary
LLM-driven agents excel at sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-driven agents excel at sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios.

进一步看，论文的核心做法或实验重点可以概括为：This insufficient experience reuse leads to computational redundancy and instability.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, episodic, long-term
- 检索关键词命中：memory compression
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM-driven agents excel at sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios. This insufficient experience reuse leads to computational redundancy and instability. To bridge this gap, we propose Skill-Pro, a framework enabling agents to autonomously learn reusable procedural skills from interaction experiences without parameter updates. By formalizing a Skill-MDP, Skill-Pro transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions to ensure executability. To achieve reliable reusability without capability degradation, we introduce Non-Parametric PPO, which leverages semantic gradients for high-quality candidate generation and a PPO Gate for robust Skill verification. Through score-based maintenance, Skill-Pro sustains compact, high-quality procedural memory. Experimental results across in-domain, cross-task, and cross-agent scenarios demonstrate that Skill-Pro achieves superior reuse rates and significant gains with extreme memory compression. Visualized evolutionary trajectories and Skill distributions further reveal how Skill-Pro transparently accumulates, refines, and reuses procedural knowledge to facilitate long-term autonomy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
