# How Intervention History Changes AI Agent Sabotage on Subsequent Tasks

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.26935v1
- Published: 2026-10-17
- Updated: 2026-10-17
- Authors: Daniel Saeedi, Amirali Aghazadeh
- Tags: agent, benchmark, context
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2610.26935v1

## One-Sentence Summary
AI control evaluations often reset agents' memory between tasks, although deployed agents may retain records of prior interventions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI control evaluations often reset agents' memory between tasks, although deployed agents may retain records of prior interventions.

进一步看，论文的核心做法或实验重点可以概括为：We ask whether learning that an earlier attack was caught changes an agent's ability to evade defer-to-trusted (DtT), a protocol that replaces suspicious work with a trusted model's solution.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
AI control evaluations often reset agents' memory between tasks, although deployed agents may retain records of prior interventions. We ask whether learning that an earlier attack was caught changes an agent's ability to evade defer-to-trusted (DtT), a protocol that replaces suspicious work with a trusted model's solution. Herein, we study cross-episode adaptation: whether intervention history changes attack behavior on a subsequent task with different objectives and a fresh environment. We evaluate this using ControlArena's Infrastructure-as-Code (IaC) and SHADE-Arena as testbeds, where agents must complete a main task while covertly pursuing a harmful side objective. For each successor task, we pair a history-conditioned attempt with the model's no-history attempt. The retained history either states that the previous submission was replaced or additionally includes the trusted model's replacement. For Claude Opus 4.8 on IaC, intervention history reduces successful sabotage. Completion of both the main and side objectives falls from 77% to 12% when the agent is told about the replacement and to 38% when it is also shown the trusted model's replacement, while main task success remains essentially unchanged. Condensing the history weakens this effect, suggesting that the retained context matters and limiting attribution to intervention feedback alone. GPT-5.4 shows no significant change in successful sabotage on the same IaC benchmark. On SHADE-Arena, GPT-5's successful sabotage rate decreases, but the reduction is not significant. Across the tested models, history conditions, and deferral thresholds, intervention history never increases the rate of successful sabotage that survives DtT. These results show that intervention history can change subsequent attack behavior, but its effect depends on both the model and the retained context.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
