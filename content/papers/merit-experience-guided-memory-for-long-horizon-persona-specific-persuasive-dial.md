# MERIT: Experience-Guided Memory for Long-Horizon Persona-Specific Persuasive Dialogue

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.29679v1
- Published: 2026-11-22
- Updated: 2026-11-22
- Authors: Rohan Kirti, Akash Ghosh, Pratik Amrit, Aryan Vats, Niladri Ghosh, Sriparna Saha
- Tags: memory-augmented
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.29679v1

## One-Sentence Summary
Effective long-horizon persuasion in recurring goal-oriented settings requires more than factual memory: it must track how a user's trust, negotiation behavior, and strategic...

## Introduction
这篇论文被纳入仓库，是因为它和 `memory-augmented` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Effective long-horizon persuasion in recurring goal-oriented settings requires more than factual memory: it must track how a user's trust, negotiation behavior, and strategic receptiveness evolve across interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing persuasive dialogue systems are largely single-session, static, and unimodal, while cross-session memory systems, though temporally aware, retain only factual content and overlook persuasion-specific dynamics.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：memory-augmented
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.CL

## Abstract Snapshot
Effective long-horizon persuasion in recurring goal-oriented settings requires more than factual memory: it must track how a user's trust, negotiation behavior, and strategic receptiveness evolve across interactions. Existing persuasive dialogue systems are largely single-session, static, and unimodal, while cross-session memory systems, though temporally aware, retain only factual content and overlook persuasion-specific dynamics. We propose MERIT (Memory-augmented Experience-Rationale for Iterative Temporal persuasion), which pairs a graph-based memory of four persuasion-specific memory types with a per-persona experience rationale library that records which strategies succeed for each user and why. Together they enable adaptive persuasion through prompt composition alone, with no parameter updates. To support this setting, we introduce PERSIST (PERSona-driven InSurance Interactions over Time), a dataset of 60 curated personas spanning 10+ years of motor insurance renewal interactions, with probabilistic life events that shift negotiation behavior and receptiveness across sessions, verified through strict human-in-the-loop annotation. MERIT surpasses memory and experience-based baselines on every metric across two policy backbones, reaching persuasive-appeal scores of 4.10 and 4.74 (out of 5).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
