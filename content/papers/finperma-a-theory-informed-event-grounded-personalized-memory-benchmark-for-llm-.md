# FinPerMA: A Theory-Informed, Event-Grounded Personalized-Memory Benchmark for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.04095v1
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Ben Wang, Kang Zhou, Lifan Guo, Feng Chen, Chi Zhang
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.04095v1

## One-Sentence Summary
Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can maintain and update an individualized user...

进一步看，论文的核心做法或实验重点可以概括为：Existing personalized-memory benchmarks primarily test factual retention or rely on weakly constrained model-generated trajectories, leaving event-driven preference adaptation underexplored.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can maintain and update an individualized user model over long horizons. Existing personalized-memory benchmarks primarily test factual retention or rely on weakly constrained model-generated trajectories, leaving event-driven preference adaptation underexplored. We introduce FinPerMA, an event-grounded benchmark that evaluates personalized memory against frozen longitudinal investor trajectories. Its generation pipeline combines deterministic, theory-informed impact rules, controlled LLM narration, and automated quality screening; a Post-Shock checkpoint isolates whether an agent has integrated a material event into its persistent user model. On 2,994 questions from 276 personas, seven frontier LLMs and up to seven memory configurations remain far from saturated: no full-context configuration exceeds approximately 0.47 overall accuracy or approximately 39% on multiple-choice questions. Attribution analysis shows that summary-based memory often preserves factual details while losing the preference signals needed for personalization; simple retrieval can therefore outperform purpose-built memory systems, with the gap widening after shocks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
