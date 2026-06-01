# Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.31354v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Yunpeng Zhou
- Tags: agent, benchmark, context
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.31354v1

## One-Sentence Summary
Modular visual reasoning systems increasingly rely on shared working memory for multi-step collaboration, yet the failure dynamics of intermediate state evolution in low-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modular visual reasoning systems increasingly rely on shared working memory for multi-step collaboration, yet the failure dynamics of intermediate state evolution in low-capacity regimes remain underexplored.

进一步看，论文的核心做法或实验重点可以概括为：We study failure modes of collaborative reasoning with weak learners (4B--8B models) through the lens of noise accumulation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Modular visual reasoning systems increasingly rely on shared working memory for multi-step collaboration, yet the failure dynamics of intermediate state evolution in low-capacity regimes remain underexplored. We study failure modes of collaborative reasoning with weak learners (4B--8B models) through the lens of noise accumulation. We introduce CoSee, an auditing framework that formalizes the read-write-verify loop to trace information flow in document visual question answering. Across multi-page, chart, and web-based benchmarks, we find a counter-intuitive degradation: naive shared workspaces often amplify hallucinations rather than resolve them. We identify two dominant failure modes: Noise Reinforcement, where ungrounded notes are reused as evidence, and Policy Collapse, where added context shifts the model toward under-specified, short-form answers. Using cost-accuracy Pareto frontiers, we show that increased compute can correlate negatively with performance without explicit verification. Our findings suggest that for resource-constrained agents, the bottleneck lies not in reasoning depth but in communication fidelity, providing trace-level diagnostics and a mechanistic baseline for reliable modular design.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
