# Personalizing Large Language Model Agents with Small Policy Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.00215v1
- Published: 2026-07-31
- Updated: 2026-07-31
- Authors: Dian Jin, Zhi Zhang, Huichao Li, Yihe Pan, Rundong Huang, Doudou Zhou
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.00215v1

## One-Sentence Summary
Large language model (LLM) agents can retrieve memory, call tools, ask clarifying questions, and vary response style, yet adapting these execution decisions to an individual...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents can retrieve memory, call tools, ask clarifying questions, and vary response style, yet adapting these execution decisions to an individual user remains difficult.

进一步看，论文的核心做法或实验重点可以概括为：Fine-tuning a separate LLM is costly or impossible for proprietary systems, while prompts and memory primarily expose user information to the agent rather than adapt its execution decisions from feedback.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents can retrieve memory, call tools, ask clarifying questions, and vary response style, yet adapting these execution decisions to an individual user remains difficult. Fine-tuning a separate LLM is costly or impossible for proprietary systems, while prompts and memory primarily expose user information to the agent rather than adapt its execution decisions from feedback. We formulate personalization of a frozen agent as online learning of a per-user execution policy from scalar feedback observed only for the executed action. We propose FABLE (Factorized Adaptive Bandit Layer for Execution), a lightweight policy layer outside a potentially black-box host agent. FABLE factorizes memory, information-acquisition, and response decisions so feedback updates related choices; filters actions through an externally specified feasible set before exploration; and learns user-specific residual preferences relative to a fixed default-and-cost score via Bayesian contextual Thompson sampling. Under a linear residual-reward model, a calibrated variant inherits an expected-regret bound against the best feasible action. We also characterize preferences unidentifiable under persistent feasibility constraints and provide anytime-valid false-promotion control. Across personalized-reasoning, controlled-feedback, and executable tool-use evaluations, FABLE improves several preference-sensitive behaviors relative to rule-only control while remaining competitive on end-to-end task performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
