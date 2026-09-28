# Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.28737v1
- Published: 2026-09-23
- Updated: 2026-09-23
- Authors: James Wu, Chris R. Sims
- Tags: agent, compression
- Categories: cs.LG, cs.AI, cs.IT
- URL: http://arxiv.org/abs/2609.28737v1

## One-Sentence Summary
Biological agents do not learn under conditions of unlimited computation.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Biological agents do not learn under conditions of unlimited computation.

进一步看，论文的核心做法或实验重点可以概括为：For humans, learning and choice are shaped by constraints on perception, attention, and working memory, which limit how much state information guides behavior and therefore bound policy complexity.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.AI, cs.IT

## Abstract Snapshot
Biological agents do not learn under conditions of unlimited computation. For humans, learning and choice are shaped by constraints on perception, attention, and working memory, which limit how much state information guides behavior and therefore bound policy complexity. Standard reinforcement learning models typically optimize reward without explicitly representing these internal costs, making them less suitable as models of biological intelligence. We derive MI-SARSA, an on-policy temporal-difference algorithm that incorporates mutual-information regularization through a learned marginal action prior and a penalty on state-specific deviations from that prior. This yields a sequential learning model in which state information is used selectively when its expected return benefit justifies the added informational cost. Critically, the same state-specific information cost that governs policy compression also generates trial-level predictions for reaction time, distinguishing MI-SARSA from most reinforcement learning models, which predict choices or returns but not latency. Empirically, MI-SARSA produces a reward-complexity tradeoff, and stronger information penalties produce simpler policies with lower control costs and faster reaction times. Under environment shift, increasing regularization reduces post-switch performance degradation but also lowers asymptotic return, revealing a robustness-capacity tradeoff. Together, these results position MI-SARSA as a model of bounded sequential learning under cognitive constraints.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
