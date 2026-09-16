# LSREP: A Longitudinal State-Replay Protocol for Evaluating Conversational Memory, with ICE v2 as an Audited Local-First Architecture

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.16730v1
- Published: 2026-09-15
- Updated: 2026-09-15
- Authors: Deepesh Sonar
- Tags: context, conversation, retrieval
- Categories: cs.AI, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2609.16730v1

## One-Sentence Summary
Conversational memory changes during use, so endpoint question answering alone cannot establish how a persistent state accumulates, ages, or incorporates revisions.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational memory changes during use, so endpoint question answering alone cannot establish how a persistent state accumulates, ages, or incorporates revisions.

进一步看，论文的核心做法或实验重点可以概括为：We introduce LSREP, a Longitudinal State-Replay Evaluation Protocol combining ordered replay, explicit lifecycle schedules, repeated probes, evolving reference answers, and mechanism-fidelity checks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Conversational memory changes during use, so endpoint question answering alone cannot establish how a persistent state accumulates, ages, or incorporates revisions. We introduce LSREP, a Longitudinal State-Replay Evaluation Protocol combining ordered replay, explicit lifecycle schedules, repeated probes, evolving reference answers, and mechanism-fidelity checks. Its architectural case study is ICE v2, a local-first memory middleware with typed stores, retrieval fusion, and dynamic context budgets. The private, single-user instantiation contains 1,985 turns, 219 distinct probes, and 1,211 probe-checkpoint observations across 52 checkpoints. On three ordinary-density datasets, ICE v2 has a near-zero mean quality difference from vector-RAG while selecting 32% fewer fragments but using 6.6% more estimated prompt tokens. A fourth, dense dataset exposes catastrophic failures of the unbudgeted baseline. The fidelity audit limits attribution: procedural retrieval is defective, several mechanisms are unexercised, and graph utility is not established. In a complementary matched public diagnostic, ICE v2 loses decisively to pure vector-RAG on LongMemEval: 50.8% versus 72.8% in the evidence-only oracle and 43.0% versus 69.5% in full-S. Paired differences are -22.0 points (95% CI [-26.6, -17.4]) and -26.5 ([-31.3, -21.8]). Conservative abstention accompanies severe multi-session and temporal failures. ICE uses less context in this diagnostic, establishing a quality-cost trade-off rather than superior efficiency. Together, replay, fidelity auditing, and public endpoint testing expose distinct failure modes that neither architectural descriptions nor aggregate scores identify alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
