# Causal Episodic Memory for Feedback-Driven Agent Repair

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.05906v1
- Published: 2026-08-06
- Updated: 2026-08-06
- Authors: Khang Nhat Hoang Vo, Tam Minh Chu, Anh Trac Duc Dinh, Thuyen Vinh Ha Bui, Tho Quan
- Tags: agent, benchmark, episodic, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.05906v1

## One-Sentence Summary
LLM agents that repair failures often discard successful corrections, forcing later episodes to rediscover similar solutions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents that repair failures often discard successful corrections, forcing later episodes to rediscover similar solutions.

进一步看，论文的核心做法或实验重点可以概括为：We study whether finalized repair outcomes can improve subsequent Text-to-SQL episodes without parameter updates.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.CL

## Abstract Snapshot
LLM agents that repair failures often discard successful corrections, forcing later episodes to rediscover similar solutions. We study whether finalized repair outcomes can improve subsequent Text-to-SQL episodes without parameter updates. We introduce MERIT, a training-free agent that maintains an online dual-polarity memory of oracle-verified corrections and observed unsuccessful directions. Under oracle-assisted benchmark feedback, only memories from earlier finalized episodes are eligible for retrieval. A deterministic classifier assigns a coarse failure type, which conditions a hybrid lexical-dense retriever before the frozen model generates each revision. Using Qwen2.5-7B-Instruct with identical initial predictions and repair budgets, MERIT improves execution accuracy over stateless iterative repair from \(66.34\%\) to \(69.79\%\) on Spider and from \(47.35\%\) to \(48.44\%\) on BIRD. Paired analyses provide clear evidence for the Spider gain but weaker evidence on BIRD. MERIT is not reliably separated from untyped dynamic retrieval on either benchmark, while Reflexion-style memory reaches \(51.24\%\) on BIRD at substantially higher inference cost. Ablations show that negative memory contributes modestly, the value of type conditioning and lexical--dense ranking is dataset dependent, and schema-local experience provides the most consistent benefit. These results clarify when causal cross-query memory improves repair and when broader memory representations remain preferable.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
