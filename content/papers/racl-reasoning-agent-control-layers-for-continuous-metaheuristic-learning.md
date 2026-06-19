# RACL: Reasoning-Agent Control Layers for Continuous Metaheuristic Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.20142v1
- Published: 2026-06-18
- Updated: 2026-06-18
- Authors: Antón Asla Manzárraga
- Tags: agent
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2606.20142v1

## One-Sentence Summary
This paper introduces RACL, a Reasoning-Agent Control Layer for metaheuristics.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：This paper introduces RACL, a Reasoning-Agent Control Layer for metaheuristics.

进一步看，论文的核心做法或实验重点可以概括为：RACL places a reasoning agent above an existing optimizer.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
This paper introduces RACL, a Reasoning-Agent Control Layer for metaheuristics. RACL places a reasoning agent above an existing optimizer. The agent does not replace the optimizer and does not modify business constraints. Instead, it controls the optimizer's internal search behavior by observing operational memory, reasoning over past behavior, formulating bounded hypotheses, testing interventions, evaluating outcomes, applying guardrails, consolidating useful policies and explaining its decisions. The experiment uses vehicle routing as a testbed, but the contribution is not a new routing solver, a particular ALNS configuration or a specific set of routing rules. The contribution is the RACL method: a way for a reasoning agent to discover, validate, consolidate and explain algorithmic control rules for a metaheuristic. In the current experimental setting, RACL improves or ties the Operational Memory Policy in 21 of 21 feasible cases and improves or ties a non-reasoning Stagnation-Triggered Policy in 18 of 21 feasible cases, with an average RACL vs STP cost delta of -0.641%. In the Sevilla-9/10 runtime sample, RACL improves average cost by -8.337% versus Fixed and -1.605% versus STP without showing material computational overhead. During the proof-of-concept, Codex was used as an in-the-loop reasoning agent observing executions, interpreting logs and proposing live bounded interventions. The policy proxy was later used only to make quantitative evaluation reproducible.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
