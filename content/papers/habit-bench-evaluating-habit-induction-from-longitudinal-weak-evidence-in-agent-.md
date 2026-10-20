# HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.24520v1
- Published: 2026-10-17
- Updated: 2026-10-17
- Authors: Junming Zhang, Rubin Wei, Xu Cheng, Hao Sun, Ruoxi Cheng, Xiquan Wang, Peisong Wu, Mingsong Chen, Zhouhan Lin
- Tags: agent, conversation, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.24520v1

## One-Sentence Summary
In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions.

进一步看，论文的核心做法或实验重点可以概括为：These habits capture implicit user information that agents must infer across conversations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence about a habit or when it applies. Retaining past interactions alone does not ensure that agents can infer habits and apply them appropriately. We introduce HABIT-Bench to evaluate how well agent memory systems infer habits from weak evidence and apply them to later requests. We construct synthetic user histories from task-oriented dialogue data and controlled habit graphs. The histories span hundreds of sessions across food, finance, software, and travel. Four-choice tasks assess agents' ability to infer user habits and apply them appropriately. They include temporary exceptions, changes in habits, and suggestions that users have not accepted. Sampled tasks undergo independent human review. We evaluate eight memory methods with Qwen3-235B-A22B and GLM-5.3-Flash. The best-performing memory method achieves 33.61\% macro accuracy across the four domains. Performance remains limited even when annotated evidence is supplied directly. These results expose a persistent gap between access to past interactions and the ability to infer and appropriately use user habits.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
