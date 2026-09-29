# COUNTERMEM: World-Model Verified Counter-Factual Memory for Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.31874v1
- Published: 2026-09-25
- Updated: 2026-09-25
- Authors: Hongji Pu, Ruixiang Tang, Yongfeng Zhang
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.31874v1

## One-Sentence Summary
Existing agent memory frameworks mainly create memory through an agent's interaction with the factual world, e.g., remembering feedback from actions taken to improve performance...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Existing agent memory frameworks mainly create memory through an agent's interaction with the factual world, e.g., remembering feedback from actions taken to improve performance on future tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, these frameworks seldom ask the "what if" question during memory construction: what if a different action had been taken, would the feedback have changed, and how could this feedback become useful memory?

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Existing agent memory frameworks mainly create memory through an agent's interaction with the factual world, e.g., remembering feedback from actions taken to improve performance on future tasks. However, these frameworks seldom ask the "what if" question during memory construction: what if a different action had been taken, would the feedback have changed, and how could this feedback become useful memory? Obtaining such feedback directly in an active environment can be expensive and can alter the state needed for comparison. In this work, we introduce COUNTERMEM, a reinforcement-learning framework for constructing and using verified counterfactual memory across tasks. After a failed action, COUNTERMEM evaluates local alternatives from a copy or reset of the original state using executable world models, such as tests, proof checkers, and solvers. It stores improvements with the original and corrected actions, checked outcomes, and conditions for reuse. A learned memory-use policy selects a retrieved record or skips memory to balance task success and interaction cost, while the base LLM remains fixed. Both memory and policy are frozen during held-out evaluation. We evaluate COUNTERMEM on 12 benchmark settings across six domains. With gpt-oss-120b, COUNTERMEM improves both ReAct and Reflexion on all 12 benchmarks across six domains, averaging a gain of 12.6 percentage points over their unaugmented versions. In the four-domain comparison across two backbones, task-run tokens decrease by 7.7-42.0%, excluding offline selector-training costs. Further analyses show that removing verification or persistent storage weakens the gains, while applying verified corrections to unsuitable decisions can reverse them. Code will be released upon acceptance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
