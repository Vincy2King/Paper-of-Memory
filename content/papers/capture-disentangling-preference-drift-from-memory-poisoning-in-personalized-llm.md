# CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.02265v1
- Published: 2026-09-02
- Updated: 2026-09-02
- Authors: S M Asif Hossain, Ruksat Khan Shayoni, Md Kishor Morol
- Tags: agent, benchmark, context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2609.02265v1

## One-Sentence Summary
Personalized language agents use persistent memory to adapt to users over time, but the same mechanism creates an attack surface.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized language agents use persistent memory to adapt to users over time, but the same mechanism creates an attack surface.

进一步看，论文的核心做法或实验重点可以概括为：When new information conflicts with stored preferences, an agent must distinguish genuine preference drift from temporary context shifts, ambiguity, or adversarial memory poisoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：memory augmented, memory-augmented, persistent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Personalized language agents use persistent memory to adapt to users over time, but the same mechanism creates an attack surface. When new information conflicts with stored preferences, an agent must distinguish genuine preference drift from temporary context shifts, ambiguity, or adversarial memory poisoning. We formulate this problem as a continuous-time partially observable decision process over a latent user state and show why rules based only on recency and provenance are insufficient. CAPTURE addresses this ambiguity with a neural differential-equation belief tracker, a multi-timescale memory ledger, uncertainty-triggered clarification, and counterfactual auditing of cited memories. On 480 held-out episodes from 96 users, CAPTURE achieves a 71.5% win rate, compared with 69.3% for an identically supervised baseline and 66.1% for the strongest heuristic baseline. It limits fixed-policy poisoning success to 11.5% while accepting 83.5% of genuine preference updates. Under an adaptive attacker with access to the released weights, attack success rises to 24.7%, exposing a real adaptation-security tradeoff. We further evaluate the frozen system zero-shot on an independently constructed benchmark and replay longitudinal interaction histories from 40 users collected over two to three weeks. These results suggest that modeling preference authenticity explicitly can improve both personalization and robustness in memory-augmented LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
